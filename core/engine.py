"""
胡希恕辨证推理引擎
抓主症 -> 辨六经 -> 定方证 -> 参体质
"""
from typing import List, Optional
from dataclasses import dataclass, field
from .knowledge import knowledge_base, Formula


@dataclass
class SymptomInfo:
    chief_complaint: str = ""
    fever: bool = False
    chills: bool = False
    fever_chills_alternate: bool = False
    fever_no_chills: bool = False
    no_sweat: bool = False
    sweating: bool = False
    cold_limbs: bool = False
    thirst: bool = False
    bitter_mouth: bool = False
    dry_throat: bool = False
    dizzy: bool = False
    headache: bool = False
    body_pain: bool = False
    stiff_neck: bool = False
    chest_fullness: bool = False
    hypochondriac_fullness: bool = False
    epigastric_palpit: bool = False
    epigastric_hard: bool = False
    abdominal_distention: bool = False
    abdominal_pain: bool = False
    nausea_vomit: bool = False
    diarrhea: bool = False
    constipation: bool = False
    dysuria: bool = False
    edema: bool = False
    poor_appetite: bool = False
    palpitation: bool = False
    insomnia: bool = False
    irritability: bool = False
    fatigue: bool = False
    fear_cold: bool = False
    other_symptoms: List[str] = field(default_factory=list)


@dataclass
class DiagnosisResult:
    meridian: str = ""
    meridian_reasoning: str = ""
    primary_formula: Optional[Formula] = None
    secondary_formulas: List[Formula] = field(default_factory=list)
    formula_reasoning: str = ""
    constitution: str = ""
    disease_mechanism: str = ""
    formula_meaning: str = ""
    treatment_advice: str = ""
    confidence: float = 0.0
    matched_symptoms: List[str] = field(default_factory=list)


class DiagnosisEngine:
    MERIDIAN_RULES = {
        "太阳": {"keywords": ["发热", "恶寒", "无汗", "汗出", "头痛", "项强", "身痛", "脉浮"]},
        "阳明": {"keywords": ["但热不寒", "大汗", "大渴", "便秘", "腹满", "潮热", "脉洪大", "脉沉实"]},
        "少阳": {"keywords": ["寒热往来", "胸胁苦满", "口苦", "咽干", "目眩", "心烦喜呕", "默默不欲食", "脉弦"]},
        "太阴": {"keywords": ["腹满", "吐利", "不欲食", "手足不温", "脉沉弱"]},
        "少阴": {"keywords": ["四肢厥冷", "但欲寐", "脉微细", "恶寒蜷卧", "脉沉微"]},
        "厥阴": {"keywords": ["消渴", "气上撞心", "饥不欲食", "寒热错杂", "手足厥寒"]}
    }

    def __init__(self):
        self.kb = knowledge_base

    def parse_symptoms(self, text):
        info = SymptomInfo()
        text = text.lower()
        info.chief_complaint = text

        if "寒热往来" in text: info.fever_chills_alternate = True
        if "发热" in text and "恶寒" in text:
            info.fever = True; info.chills = True
        elif "发热" in text: info.fever = True
        if "恶寒" in text or "怕冷" in text or "畏寒" in text: info.chills = True
        if "但热不寒" in text: info.fever_no_chills = True
        if "无汗" in text: info.no_sweat = True
        if "汗出" in text or "自汗" in text: info.sweating = True
        if "大汗" in text: info.sweating = True
        if "四肢厥冷" in text or "手足冷" in text or "肢冷" in text: info.cold_limbs = True
        if "手足不温" in text: info.cold_limbs = True
        if "口渴" in text or "渴" in text: info.thirst = True
        if "口苦" in text: info.bitter_mouth = True
        if "咽干" in text: info.dry_throat = True
        if "眩" in text or "头晕" in text or "头眩" in text: info.dizzy = True
        if "头痛" in text or "头疼" in text: info.headache = True
        if "项强" in text or "项背强" in text or "脖子硬" in text: info.stiff_neck = True
        if "身痛" in text or "身体痛" in text or "周身痛" in text: info.body_pain = True
        if "胸闷" in text or "胸满" in text: info.chest_fullness = True
        if ("胸胁" in text and ("满" in text or "胀" in text or "苦" in text)) or ("胁" in text and ("胀" in text or "满" in text)):
            info.hypochondriac_fullness = True
        if "心下悸" in text or "脐下悸" in text: info.epigastric_palpit = True
        if "心下痞" in text or "心下硬" in text or "心下满" in text: info.epigastric_hard = True
        if "腹满" in text or "腹胀" in text: info.abdominal_distention = True
        if "腹痛" in text or "肚子痛" in text: info.abdominal_pain = True
        if "呕" in text or "吐" in text or "恶心" in text: info.nausea_vomit = True
        if "下利" in text or "腹泻" in text or "拉肚子" in text: info.diarrhea = True
        if "便秘" in text or "大便干" in text or "大便不通" in text: info.constipation = True
        if "小便不利" in text or "尿少" in text: info.dysuria = True
        if "浮肿" in text or "水肿" in text: info.edema = True
        if "食欲不振" in text or "不欲食" in text or "纳差" in text: info.poor_appetite = True
        if "心悸" in text or "心慌" in text: info.palpitation = True
        if "失眠" in text or "不眠" in text or "睡不着" in text: info.insomnia = True
        if "烦躁" in text or "烦" in text: info.irritability = True
        if "乏力" in text or "疲倦" in text or "神疲" in text: info.fatigue = True

        return info

    def identify_meridian(self, info):
        scores = {}
        for meridian, rule in self.MERIDIAN_RULES.items():
            score = 0
            matched = []
            for kw in rule["keywords"]:
                if kw in info.chief_complaint:
                    score += 1
                    matched.append(kw)
            scores[meridian] = (score, matched)

        sorted_scores = sorted(scores.items(), key=lambda x: x[1][0], reverse=True)
        if sorted_scores[0][1][0] == 0:
            return "未明", "症状信息不足", 0.0

        meridian, (score, matched) = sorted_scores[0]
        confidence = min(score / 3.0, 1.0)
        reasoning = f"【{meridian}病】\n依据：{', '.join(matched)}\n"
        return meridian, reasoning, confidence

    def identify_formula(self, info, meridian, top_k=3):
        symptoms = []
        if info.fever: symptoms.append("发热")
        if info.chills: symptoms.append("恶寒")
        if info.fever_chills_alternate: symptoms.append("寒热往来")
        if info.no_sweat: symptoms.append("无汗")
        if info.sweating: symptoms.append("汗出")
        if info.thirst: symptoms.append("口渴")
        if info.bitter_mouth: symptoms.append("口苦")
        if info.headache: symptoms.append("头痛")
        if info.body_pain: symptoms.append("身痛")
        if info.stiff_neck: symptoms.append("项强")
        if info.hypochondriac_fullness: symptoms.append("胸胁苦满")
        if info.chest_fullness: symptoms.append("胸闷")
        if info.abdominal_distention: symptoms.append("腹满")
        if info.abdominal_pain: symptoms.append("腹痛")
        if info.nausea_vomit: symptoms.append("呕")
        if info.diarrhea: symptoms.append("下利")
        if info.constipation: symptoms.append("便秘")
        if info.dysuria: symptoms.append("小便不利")
        if info.edema: symptoms.append("浮肿")
        if info.palpitation: symptoms.append("心悸")
        if info.dizzy: symptoms.append("眩")
        if info.cold_limbs: symptoms.append("四肢厥冷")
        if info.insomnia: symptoms.append("不眠")
        if info.irritability: symptoms.append("烦")
        if info.fatigue: symptoms.append("乏力")
        if info.fear_cold: symptoms.append("畏寒")
        if info.poor_appetite: symptoms.append("不欲食")

        results = self.kb.search_by_symptoms(symptoms, top_k=top_k)
        if not results:
            return None, [], "未能匹配到合适方剂", 0.0

        primary, score = results[0]
        secondary = [f for f, s in results[1:]]
        confidence = min(score / 5.0, 1.0)

        reasoning = f"【方证】{primary.name}\n主症：{', '.join(primary.indications)}\n病机：{primary.disease_mechanism}\n"
        if secondary:
            reasoning += "备选：" + "、".join([f"{s.name}({s.six_meridian})" for s in secondary]) + "\n"

        return primary, secondary, reasoning, confidence

    def diagnose(self, text):
        info = self.parse_symptoms(text)
        meridian, meridian_reasoning, meridian_conf = self.identify_meridian(info)
        primary, secondary, formula_reasoning, formula_conf = self.identify_formula(info, meridian)

        if not primary:
            return DiagnosisResult(meridian=meridian, meridian_reasoning=meridian_reasoning,
                                   formula_reasoning=formula_reasoning, confidence=0.0)

        return DiagnosisResult(
            meridian=meridian,
            meridian_reasoning=meridian_reasoning,
            primary_formula=primary,
            secondary_formulas=secondary,
            formula_reasoning=formula_reasoning,
            constitution=primary.constitution,
            disease_mechanism=primary.disease_mechanism,
            formula_meaning=primary.formula_meaning,
            treatment_advice=f"水煎服，每日1剂，分2次温服。\n禁忌：{', '.join(primary.contraindications) if primary.contraindications else '忌生冷油腻'}\n",
            confidence=meridian_conf * 0.4 + formula_conf * 0.6
        )

    def consult_step(self, history, user_input):
        full_text = " ".join([h.get("content", "") for h in history if h.get("role") == "user"])
        full_text += " " + user_input
        result = self.diagnose(full_text)

        key_symptoms = ["发热", "恶寒", "汗", "口苦", "咽干", "胸", "胁", "腹", "大便", "下利", "便秘", "小便"]
        count = sum(1 for s in key_symptoms if s in full_text)
        enough = count >= 3

        if enough:
            return {"type": "diagnosis", "final_diagnosis": result}
        else:
            if "发热" not in full_text and "恶寒" not in full_text:
                q = "请问您有没有发热或怕冷的感觉？"
            elif "汗" not in full_text:
                q = "请问您出汗情况如何？无汗还是汗出？"
            elif "口苦" not in full_text and "口渴" not in full_text:
                q = "请问您口苦吗？口渴吗？"
            elif "胸" not in full_text and "胁" not in full_text and "腹" not in full_text:
                q = "请问您胸闷或胁肋胀吗？腹部感觉如何？"
            else:
                q = "请问还有其他不适吗？"
            return {"type": "question", "next_question": q, "result": result}


diagnosis_engine = DiagnosisEngine()
