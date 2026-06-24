"""Vercel Serverless API"""
import sys
import json
from pathlib import Path
ROOT = Path(__file__).parent.parent.resolve()
sys.path.insert(0, str(ROOT))

from core.engine import diagnosis_engine
from core.knowledge import knowledge_base


class handler:
    def do_GET(self):
        if self.path in ["/", "/api"]:
            return self._json({
                "name": "胡希恕经方辨证系统",
                "version": "1.0.0",
                "endpoints": ["POST /api/diagnose", "GET /api/formulas"]
            })
        if self.path == "/api/formulas":
            formulas = [{"name": f.name, "meridian": f.six_meridian, "indications": f.indications}
                       for f in knowledge_base.get_all_formulas()]
            return self._json({"formulas": formulas, "count": len(formulas)})
        return self._json({"error": "Not Found"}, 404)

    def do_POST(self):
        if self.path == "/api/diagnose":
            data = json.loads(self.rfile.read(int(self.headers.get("Content-Length", 0))).decode("utf-8"))
            symptoms = data.get("symptoms", "")
            if not symptoms:
                return self._json({"error": "Missing symptoms"}, 400)

            result = diagnosis_engine.diagnose(symptoms)
            response = {
                "meridian": result.meridian,
                "meridian_reasoning": result.meridian_reasoning,
                "confidence": result.confidence,
            }

            if result.primary_formula:
                f = result.primary_formula
                response["primary_formula"] = {
                    "name": f.name, "meridian": f.six_meridian,
                    "composition": f.composition, "indications": f.indications,
                    "disease_mechanism": f.disease_mechanism,
                    "formula_meaning": f.formula_meaning,
                    "constitution": f.constitution, "cases": f.cases,
                }
                response["formula_reasoning"] = result.formula_reasoning
                response["treatment_advice"] = result.treatment_advice

            return self._json(response)
        return self._json({"error": "Not Found"}, 404)

    def _json(self, data, status=200):
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(json.dumps(data, ensure_ascii=False).encode("utf-8"))
