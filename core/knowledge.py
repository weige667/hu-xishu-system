"""
胡希恕方证知识库
胡希恕常用方剂 100+ 首
"""
from typing import List, Dict, Optional
from pydantic import BaseModel


class Formula(BaseModel):
    name: str
    six_meridian: str
    composition: Dict[str, str]
    decoction: str = ""
    indications: List[str] = []
    symptoms: List[str] = []
    tongue: str = ""
    pulse: str = ""
    abdomen: str = ""
    constitution: str = ""
    disease_mechanism: str = ""
    formula_meaning: str = ""
    contraindications: List[str] = []
    cases: List[str] = []
    keywords: List[str] = []
    source: str = ""


F = []
F.append(Formula(
    name="桂枝汤", six_meridian="太阳",
    composition={"桂枝": "9g", "白芍": "9g", "甘草": "6g", "生姜": "9g", "大枣": "4枚"},
    indications=["发热", "汗出", "恶风", "头痛"],
    symptoms=["发热汗出", "恶风寒", "头痛", "脉浮缓"],
    constitution="桂枝体质：肤白体瘦易汗",
    disease_mechanism="营卫不和",
    formula_meaning="桂枝解肌，芍药和营",
    contraindications=["表实无汗"],
    cases=["外感风寒", "自汗", "妊娠呕吐"],
    keywords=["发热", "汗出", "恶风", "脉缓", "头痛"],
    source="《伤寒论》"
))
F.append(Formula(
    name="麻黄汤", six_meridian="太阳",
    composition={"麻黄": "9g", "桂枝": "6g", "杏仁": "9g", "甘草": "3g"},
    indications=["发热", "恶寒", "无汗", "身痛"],
    symptoms=["发热恶寒", "无汗", "身痛", "气喘", "脉浮紧"],
    constitution="麻黄体质：体壮无汗",
    disease_mechanism="风寒束表",
    formula_meaning="麻黄发汗，桂枝助汗，杏仁平喘",
    contraindications=["表虚自汗"],
    cases=["感冒重症", "急性支气管炎"],
    keywords=["发热", "恶寒", "无汗", "身痛", "气喘", "脉紧"],
    source="《伤寒论》"
))
F.append(Formula(
    name="葛根汤", six_meridian="太阳",
    composition={"葛根": "12g", "麻黄": "9g", "桂枝": "6g", "白芍": "6g", "甘草": "6g", "生姜": "9g", "大枣": "4枚"},
    indications=["项背强几几", "无汗", "恶风"],
    symptoms=["项背强紧", "无汗恶风", "发热", "下利"],
    disease_mechanism="风寒束表经输不利",
    formula_meaning="葛根解肌升津",
    cases=["颈椎病", "肩周炎"],
    keywords=["项强", "无汗", "恶风", "肩背痛", "下利"],
    source="《伤寒论》"
))
F.append(Formula(
    name="大青龙汤", six_meridian="太阳",
    composition={"麻黄": "12g", "桂枝": "6g", "杏仁": "6g", "甘草": "6g", "生姜": "9g", "大枣": "4枚", "石膏": "30g"},
    indications=["发热", "恶寒", "身痛", "烦躁"],
    symptoms=["发热恶寒", "不汗出而烦躁"],
    disease_mechanism="风寒束表里郁热",
    formula_meaning="麻黄汤加石膏",
    keywords=["发热", "无汗", "烦躁", "身痛"],
    source="《伤寒论》"
))
F.append(Formula(
    name="小青龙汤", six_meridian="太阳",
    composition={"麻黄": "9g", "白芍": "9g", "细辛": "3g", "干姜": "6g", "甘草": "6g", "桂枝": "9g", "半夏": "9g", "五味子": "9g"},
    indications=["喘咳", "痰稀白", "恶寒"],
    symptoms=["恶寒发热", "无汗", "咳喘", "痰稀白"],
    disease_mechanism="外寒内饮",
    formula_meaning="麻桂解表姜辛夏温化水饮",
    cases=["哮喘", "慢性支气管炎"],
    keywords=["咳喘", "痰稀", "恶寒", "无汗", "水饮"],
    source="《伤寒论》"
))
F.append(Formula(
    name="白虎汤", six_meridian="阳明",
    composition={"石膏": "30-60g", "知母": "12g", "甘草": "6g", "粳米": "15g"},
    indications=["大热", "大汗", "大渴", "脉洪大"],
    symptoms=["壮热", "不恶寒反恶热", "大汗", "大渴", "面赤"],
    disease_mechanism="阳明气分热盛",
    formula_meaning="石膏清气分热知母滋阴",
    cases=["高热", "乙脑", "糖尿病"],
    keywords=["大热", "大汗", "大渴", "脉洪大", "面赤"],
    source="《伤寒论》"
))
F.append(Formula(
    name="调胃承气汤", six_meridian="阳明",
    composition={"大黄": "12g", "甘草": "6g", "芒硝": "12g"},
    indications=["便秘", "蒸蒸发热"],
    symptoms=["大便不通", "蒸蒸发热"],
    disease_mechanism="燥屎内结",
    formula_meaning="大黄攻下芒硝软坚",
    keywords=["便秘", "发热", "腹满"],
    source="《伤寒论》"
))
F.append(Formula(
    name="小承气汤", six_meridian="阳明",
    composition={"大黄": "12g", "厚朴": "6g", "枳实": "9g"},
    indications=["便秘", "潮热", "腹满"],
    symptoms=["大便不通", "潮热", "腹满", "谵语"],
    disease_mechanism="热实内结",
    keywords=["便秘", "潮热", "腹满", "脉沉"],
    source="《伤寒论》"
))
F.append(Formula(
    name="大承气汤", six_meridian="阳明",
    composition={"大黄": "12g", "厚朴": "15g", "枳实": "12g", "芒硝": "9g"},
    indications=["痞满燥实", "潮热", "谵语"],
    symptoms=["大便不通", "腹满硬痛", "潮热", "谵语"],
    disease_mechanism="燥屎内结",
    cases=["肠梗阻", "急性阑尾炎"],
    keywords=["便秘", "腹满硬痛", "潮热", "谵语"],
    source="《伤寒论》"
))
F.append(Formula(
    name="小柴胡汤", six_meridian="少阳",
    composition={"柴胡": "24g", "黄芩": "9g", "人参": "9g", "半夏": "9g", "甘草": "9g", "生姜": "9g", "大枣": "4枚"},
    indications=["寒热往来", "胸胁苦满", "口苦", "咽干", "目眩"],
    symptoms=["寒热往来", "胸胁苦满", "心烦喜呕", "口苦", "咽干", "目眩"],
    constitution="柴胡体质：体瘦情志抑郁",
    disease_mechanism="少阳枢机不利",
    formula_meaning="柴胡黄芩解少阳郁热参草姜枣扶正",
    cases=["感冒", "肝炎", "胃炎", "更年期"],
    keywords=["寒热往来", "胸胁苦满", "口苦", "咽干", "目眩", "心烦", "喜呕"],
    source="《伤寒论》"
))
F.append(Formula(
    name="大柴胡汤", six_meridian="少阳",
    composition={"柴胡": "24g", "黄芩": "9g", "白芍": "9g", "半夏": "9g", "生姜": "15g", "枳实": "12g", "大黄": "6g", "大枣": "4枚"},
    indications=["胸胁苦满", "心下痞硬", "便秘"],
    symptoms=["胸胁苦满", "心下痞硬", "便秘"],
    disease_mechanism="少阳兼阳明里实",
    cases=["胆囊炎", "高血压"],
    keywords=["胸胁苦满", "心下痞硬", "便秘", "腹满", "呕"],
    source="《伤寒论》"
))
F.append(Formula(
    name="柴胡桂枝汤", six_meridian="太阳少阳",
    composition={"柴胡": "12g", "黄芩": "4.5g", "人参": "4.5g", "半夏": "4.5g", "甘草": "3g", "生姜": "4.5g", "大枣": "4枚", "桂枝": "4.5g", "白芍": "4.5g"},
    indications=["发热恶寒", "胸胁苦满"],
    symptoms=["太阳少阳合病"],
    disease_mechanism="太少合病",
    keywords=["发热", "恶寒", "胸胁苦满", "肢节烦疼"],
    source="《伤寒论》"
))
F.append(Formula(
    name="柴胡加龙骨牡蛎汤", six_meridian="少阳",
    composition={"柴胡": "12g", "龙骨": "4.5g", "黄芩": "4.5g", "生姜": "4.5g", "人参": "4.5g", "桂枝": "4.5g", "茯苓": "4.5g", "半夏": "4.5g", "大黄": "6g", "牡蛎": "4.5g", "大枣": "4枚", "铅丹": "4.5g"},
    indications=["胸满烦惊", "谵语"],
    symptoms=["胸满", "烦惊", "谵语"],
    disease_mechanism="少阳枢机不利痰热扰心",
    cases=["精神分裂症", "癫痫"],
    keywords=["胸满", "烦惊", "谵语", "失眠"],
    source="《伤寒论》"
))
F.append(Formula(
    name="理中汤", six_meridian="太阴",
    composition={"人参": "9g", "干姜": "9g", "甘草": "9g", "白术": "9g"},
    indications=["腹满", "吐利", "不欲食"],
    symptoms=["腹满", "吐利", "不欲食", "手足不温"],
    disease_mechanism="中焦虚寒",
    formula_meaning="人参益气干姜温中",
    cases=["慢性胃炎", "腹泻"],
    keywords=["腹满", "吐利", "不欲食", "手足不温"],
    source="《伤寒论》"
))
F.append(Formula(
    name="附子理中汤", six_meridian="太阴",
    composition={"人参": "9g", "干姜": "9g", "甘草": "9g", "白术": "9g", "附子": "9g"},
    indications=["理中汤证", "畏寒肢冷"],
    symptoms=["腹满", "吐利", "畏寒肢冷"],
    disease_mechanism="中焦虚寒阳气虚衰",
    cases=["慢性腹泻", "阳虚体质"],
    keywords=["腹满", "吐利", "畏寒", "肢冷"],
    source="《伤寒论》"
))
F.append(Formula(
    name="麻黄附子细辛汤", six_meridian="少阴",
    composition={"麻黄": "6g", "附子": "9g", "细辛": "6g"},
    indications=["发热", "脉沉"],
    symptoms=["发热恶寒", "脉沉"],
    disease_mechanism="少阴阳虚外感",
    formula_meaning="麻黄解表附子温阳",
    cases=["感冒阳虚", "病态窦房结"],
    keywords=["发热", "脉沉", "恶寒", "少阴"],
    source="《伤寒论》"
))
F.append(Formula(
    name="真武汤", six_meridian="少阴",
    composition={"附子": "9g", "茯苓": "9g", "白术": "6g", "白芍": "9g", "生姜": "9g"},
    indications=["肢冷", "浮肿", "心悸", "眩晕"],
    symptoms=["四肢沉重", "浮肿", "心下悸", "头眩"],
    disease_mechanism="肾阳虚衰水湿内停",
    cases=["慢性肾炎", "心衰", "甲减"],
    keywords=["肢冷", "浮肿", "心悸", "眩", "小便不利"],
    source="《伤寒论》"
))
F.append(Formula(
    name="四逆汤", six_meridian="少阴",
    composition={"附子": "15g", "干姜": "9g", "甘草": "9g"},
    indications=["四肢厥冷", "脉微欲绝"],
    symptoms=["四肢厥冷", "恶寒蜷卧", "下利"],
    disease_mechanism="阳气衰微",
    cases=["心衰", "休克"],
    keywords=["四肢厥冷", "脉微", "恶寒", "下利"],
    source="《伤寒论》"
))
F.append(Formula(
    name="乌梅丸", six_meridian="厥阴",
    composition={"乌梅": "30g", "细辛": "3g", "干姜": "9g", "黄连": "6g", "当归": "6g", "附子": "6g", "蜀椒": "3g", "桂枝": "6g", "人参": "6g", "黄柏": "6g"},
    indications=["消渴", "气上撞心", "饥不欲食"],
    symptoms=["消渴", "气上撞心", "饥不欲食"],
    disease_mechanism="上热下寒",
    cases=["胆道蛔虫", "神经性呕吐"],
    keywords=["消渴", "气上撞心", "饥不欲食", "寒热错杂"],
    source="《伤寒论》"
))
F.append(Formula(
    name="当归四逆汤", six_meridian="厥阴",
    composition={"当归": "9g", "桂枝": "9g", "白芍": "9g", "细辛": "6g", "甘草": "6g", "通草": "6g", "大枣": "8枚"},
    indications=["手足厥寒", "脉细欲绝"],
    symptoms=["手足厥寒", "脉细欲绝"],
    disease_mechanism="血虚寒凝",
    cases=["雷诺病", "冻疮"],
    keywords=["手足厥寒", "脉细", "寒凝"],
    source="《伤寒论》"
))
F.append(Formula(
    name="吴茱萸汤", six_meridian="厥阴",
    composition={"吴茱萸": "9g", "人参": "9g", "生姜": "18g", "大枣": "4枚"},
    indications=["干呕", "吐涎沫", "头痛"],
    symptoms=["干呕", "吐涎沫", "巅顶头痛"],
    disease_mechanism="肝寒犯胃",
    cases=["神经性头痛", "梅尼埃病"],
    keywords=["干呕", "吐涎沫", "头痛", "厥冷"],
    source="《伤寒论》"
))
F.append(Formula(
    name="五苓散", six_meridian="太阳",
    composition={"猪苓": "9g", "泽泻": "15g", "白术": "9g", "茯苓": "9g", "桂枝": "6g"},
    indications=["小便不利", "口渴", "水入即吐"],
    symptoms=["小便不利", "微热", "消渴"],
    disease_mechanism="膀胱气化不利",
    cases=["水肿", "尿潴留", "美尼尔"],
    keywords=["小便不利", "口渴", "水入即吐", "眩"],
    source="《伤寒论》"
))
F.append(Formula(
    name="苓桂术甘汤", six_meridian="太阳",
    composition={"茯苓": "12g", "桂枝": "9g", "白术": "6g", "甘草": "6g"},
    indications=["心下逆满", "气上冲胸", "眩"],
    symptoms=["心下逆满", "气上冲胸", "起则头眩"],
    disease_mechanism="脾虚水停水气上冲",
    cases=["眩晕", "心悸"],
    keywords=["心下逆满", "气上冲", "眩", "心悸"],
    source="《伤寒论》"
))
F.append(Formula(
    name="炙甘草汤", six_meridian="太阳",
    composition={"炙甘草": "12g", "生姜": "9g", "桂枝": "9g", "人参": "6g", "生地黄": "30g", "阿胶": "6g", "麦门冬": "9g", "麻仁": "9g", "大枣": "10枚"},
    indications=["心动悸", "脉结代"],
    symptoms=["心动悸", "脉结代"],
    disease_mechanism="心之气血不足",
    cases=["心律不齐", "甲亢"],
    keywords=["心动悸", "脉结代", "虚"],
    source="《伤寒论》"
))
F.append(Formula(
    name="半夏泻心汤", six_meridian="少阳",
    composition={"半夏": "12g", "黄芩": "9g", "干姜": "9g", "人参": "9g", "甘草": "9g", "黄连": "3g", "大枣": "4枚"},
    indications=["心下痞", "呕", "肠鸣"],
    symptoms=["心下痞满", "干呕", "肠鸣下利"],
    disease_mechanism="脾胃升降失常",
    cases=["慢性胃炎", "胃溃疡"],
    keywords=["心下痞", "呕", "肠鸣", "下利"],
    source="《伤寒论》"
))
F.append(Formula(
    name="半夏厚朴汤", six_meridian="少阳",
    composition={"半夏": "12g", "厚朴": "9g", "茯苓": "12g", "生姜": "15g", "苏叶": "6g"},
    indications=["咽中如有炙脔", "胸闷"],
    symptoms=["咽中如有物阻", "胸胁满闷"],
    disease_mechanism="痰气互结咽喉",
    cases=["梅核气", "咽炎"],
    keywords=["咽堵", "梅核气", "胸闷", "痰气"],
    source="《金匮要略》"
))
F.append(Formula(
    name="栀子豉汤", six_meridian="太阳",
    composition={"栀子": "9g", "淡豆豉": "9g"},
    indications=["虚烦", "不得眠", "心中懊恼"],
    symptoms=["虚烦", "不得眠", "心中懊恼"],
    disease_mechanism="热扰胸膈",
    cases=["神经衰弱", "失眠", "抑郁"],
    keywords=["虚烦", "失眠", "懊恼"],
    source="《伤寒论》"
))
F.append(Formula(
    name="茵陈蒿汤", six_meridian="阳明",
    composition={"茵陈": "18g", "栀子": "9g", "大黄": "6g"},
    indications=["身黄", "尿黄", "腹满"],
    symptoms=["身目俱黄", "黄色鲜明", "腹满", "小便不利"],
    disease_mechanism="湿热郁蒸",
    cases=["黄疸型肝炎"],
    keywords=["黄疸", "身黄", "尿黄"],
    source="《伤寒论》"
))
F.append(Formula(
    name="猪苓汤", six_meridian="阳明",
    composition={"猪苓": "9g", "茯苓": "9g", "泽泻": "9g", "滑石": "9g", "阿胶": "9g"},
    indications=["小便不利", "口渴", "心烦", "失眠"],
    symptoms=["小便不利", "发热", "口渴", "心烦不眠"],
    disease_mechanism="水热互结兼阴虚",
    cases=["泌尿系感染"],
    keywords=["小便不利", "口渴", "心烦"],
    source="《伤寒论》"
))
F.append(Formula(
    name="苓桂甘枣汤", six_meridian="太阳",
    composition={"茯苓": "12g", "桂枝": "9g", "甘草": "6g", "大枣": "4枚"},
    indications=["脐下悸", "欲作奔豚"],
    symptoms=["脐下悸动", "欲作奔豚"],
    disease_mechanism="心阳不足水气上冲",
    keywords=["脐下悸", "奔豚", "气上冲"],
    source="《伤寒论》"
))
F.append(Formula(
    name="桂枝加桂汤", six_meridian="太阳",
    composition={"桂枝": "15g", "白芍": "9g", "甘草": "6g", "生姜": "9g", "大枣": "4枚"},
    indications=["气从少腹上冲心"],
    symptoms=["奔豚", "气从少腹上冲", "心悸"],
    disease_mechanism="心阳虚水气上冲",
    keywords=["气上冲", "奔豚", "心悸"],
    source="《伤寒论》"
))
F.append(Formula(
    name="附子汤", six_meridian="少阴",
    composition={"附子": "12g", "茯苓": "9g", "人参": "6g", "白术": "12g", "白芍": "9g"},
    indications=["身痛", "手足寒", "脉沉"],
    symptoms=["身体痛", "手足寒", "骨节痛"],
    disease_mechanism="阳虚寒湿身痛",
    cases=["风湿性关节炎"],
    keywords=["身痛", "肢寒", "脉沉", "寒湿"],
    source="《伤寒论》"
))
F.append(Formula(
    name="桂枝加葛根汤", six_meridian="太阳",
    composition={"桂枝": "6g", "白芍": "6g", "甘草": "6g", "生姜": "9g", "大枣": "4枚", "葛根": "12g"},
    indications=["项背强几几", "汗出", "恶风"],
    symptoms=["项背强几几", "汗出", "恶风"],
    disease_mechanism="桂枝汤加葛根",
    formula_meaning="桂枝汤加葛根，解肌升津",
    keywords=["项强", "汗出", "恶风", "肩背痛"],
    source="《伤寒论》"
))
F.append(Formula(
    name="桂枝加厚朴杏子汤", six_meridian="太阳",
    composition={"桂枝": "9g", "白芍": "9g", "甘草": "6g", "生姜": "9g", "大枣": "4枚", "厚朴": "6g", "杏仁": "9g"},
    indications=["汗出", "恶风", "喘"],
    symptoms=["汗出", "恶风", "喘"],
    disease_mechanism="桂枝汤加厚朴杏子",
    formula_meaning="桂枝汤加厚朴杏子，解表降气平喘",
    keywords=["汗出", "恶风", "气喘", "咳嗽"],
    source="《伤寒论》"
))
F.append(Formula(
    name="桂枝加附子汤", six_meridian="太阳",
    composition={"桂枝": "9g", "白芍": "9g", "甘草": "6g", "生姜": "9g", "大枣": "4枚", "附子": "9g"},
    indications=["汗出", "恶风", "肢冷"],
    symptoms=["汗出", "恶风", "肢冷"],
    disease_mechanism="桂枝汤加附子",
    formula_meaning="桂枝汤加附子，温阳固表",
    keywords=["汗出", "恶风", "肢冷", "小便难"],
    source="《伤寒论》"
))
F.append(Formula(
    name="桂枝去芍药汤", six_meridian="太阳",
    composition={"桂枝": "9g", "甘草": "6g", "生姜": "9g", "大枣": "4枚"},
    indications=["胸满", "脉促"],
    symptoms=["胸满", "脉促"],
    disease_mechanism="桂枝汤去芍药",
    formula_meaning="桂枝汤去芍药，专于解表通阳",
    keywords=["胸满", "脉促", "恶寒"],
    source="《伤寒论》"
))
F.append(Formula(
    name="桂枝去芍药加附子汤", six_meridian="太阳",
    composition={"桂枝": "9g", "甘草": "6g", "生姜": "9g", "大枣": "4枚", "附子": "9g"},
    indications=["胸满", "肢冷", "脉微"],
    symptoms=["胸满", "肢冷", "脉微"],
    disease_mechanism="桂枝去芍药汤加附子",
    formula_meaning="桂枝去芍药汤加附子，温阳通经",
    keywords=["胸满", "肢冷", "脉微", "恶寒"],
    source="《伤寒论》"
))
F.append(Formula(
    name="小建中汤", six_meridian="太阳",
    composition={"桂枝": "9g", "白芍": "18g", "甘草": "6g", "生姜": "9g", "大枣": "4枚", "饴糖": "30g"},
    indications=["腹痛", "心悸", "虚劳"],
    symptoms=["腹痛", "心悸", "虚劳"],
    disease_mechanism="桂枝汤倍芍药加饴糖",
    formula_meaning="桂枝汤倍芍药加饴糖，建中补虚",
    keywords=["腹痛", "心悸", "虚劳", "面色无华"],
    source="《伤寒论》"
))
F.append(Formula(
    name="桂枝新加汤", six_meridian="太阳",
    composition={"桂枝": "9g", "白芍": "12g", "甘草": "6g", "生姜": "12g", "大枣": "4枚", "人参": "9g"},
    indications=["身痛", "汗出", "脉沉迟"],
    symptoms=["身痛", "汗出", "脉沉迟"],
    disease_mechanism="桂枝汤加重芍姜加人参",
    formula_meaning="桂枝汤加重芍姜加人参，益气养血",
    keywords=["身痛", "汗出", "脉沉迟", "气短"],
    source="《伤寒论》"
))
F.append(Formula(
    name="桂枝麻黄各半汤", six_meridian="太阳",
    composition={"桂枝": "5g", "白芍": "3g", "甘草": "3g", "生姜": "3g", "大枣": "2枚", "麻黄": "3g", "杏仁": "3g"},
    indications=["发热恶寒", "面热", "身痒"],
    symptoms=["发热恶寒", "面热", "身痒"],
    disease_mechanism="桂枝汤麻黄汤各半合方",
    formula_meaning="桂枝汤麻黄汤各半合方",
    keywords=["发热恶寒", "面热", "身痒", "无汗"],
    source="《伤寒论》"
))
F.append(Formula(
    name="桂枝二麻黄一汤", six_meridian="太阳",
    composition={"桂枝": "6g", "白芍": "3g", "甘草": "3g", "生姜": "3g", "大枣": "2枚", "麻黄": "2g", "杏仁": "2g"},
    indications=["发热", "汗出", "形似疟"],
    symptoms=["发热", "汗出", "形似疟"],
    disease_mechanism="桂枝汤二分麻黄汤一分解表",
    formula_meaning="桂枝汤二分麻黄汤一分解表",
    keywords=["发热", "汗出", "形似疟", "一日再发"],
    source="《伤寒论》"
))
F.append(Formula(
    name="桂枝二越婢一汤", six_meridian="太阳",
    composition={"桂枝": "3g", "白芍": "3g", "甘草": "3g", "生姜": "3g", "大枣": "2枚", "麻黄": "3g", "石膏": "9g"},
    indications=["发热恶寒", "口渴", "烦躁"],
    symptoms=["发热恶寒", "口渴", "烦躁"],
    disease_mechanism="桂枝汤合越婢汤轻剂",
    formula_meaning="桂枝汤合越婢汤轻剂",
    keywords=["发热恶寒", "口渴", "烦躁", "脉浮大"],
    source="《伤寒论》"
))
F.append(Formula(
    name="麻黄杏仁甘草石膏汤", six_meridian="太阳",
    composition={"麻黄": "9g", "杏仁": "9g", "甘草": "6g", "石膏": "24g"},
    indications=["汗出", "喘", "口渴"],
    symptoms=["汗出", "喘", "口渴"],
    disease_mechanism="麻黄汤去桂枝加石膏",
    formula_meaning="麻黄汤去桂枝加石膏，清肺平喘",
    keywords=["汗出", "气喘", "口渴", "咳嗽"],
    source="《伤寒论》"
))
F.append(Formula(
    name="麻黄附子甘草汤", six_meridian="太阳",
    composition={"麻黄": "6g", "附子": "9g", "甘草": "6g"},
    indications=["发热", "脉沉", "无汗"],
    symptoms=["发热", "脉沉", "无汗"],
    disease_mechanism="麻黄附子细辛汤去细辛加甘草",
    formula_meaning="麻黄附子细辛汤去细辛加甘草",
    keywords=["发热", "脉沉", "无汗", "微恶寒"],
    source="《伤寒论》"
))
F.append(Formula(
    name="麻黄连翘赤小豆汤", six_meridian="太阳",
    composition={"麻黄": "6g", "连翘": "9g", "杏仁": "9g", "赤小豆": "30g", "大枣": "4枚", "生姜": "6g", "甘草": "6g"},
    indications=["身黄", "小便不利", "浮肿"],
    symptoms=["身黄", "小便不利", "浮肿"],
    disease_mechanism="麻黄汤去桂枝加连翘赤小豆",
    formula_meaning="麻黄汤去桂枝加连翘赤小豆，解表利湿退黄",
    keywords=["身黄", "小便不利", "浮肿", "发热"],
    source="《伤寒论》"
))
F.append(Formula(
    name="栀子甘草豉汤", six_meridian="阳明",
    composition={"栀子": "9g", "甘草": "6g", "淡豆豉": "9g"},
    indications=["虚烦", "少气"],
    symptoms=["虚烦", "少气"],
    disease_mechanism="栀子豉汤加甘草",
    formula_meaning="栀子豉汤加甘草，益气除烦",
    keywords=["虚烦", "少气", "心烦"],
    source="《伤寒论》"
))
F.append(Formula(
    name="栀子生姜豉汤", six_meridian="阳明",
    composition={"栀子": "9g", "生姜": "9g", "淡豆豉": "9g"},
    indications=["虚烦", "呕吐"],
    symptoms=["虚烦", "呕吐"],
    disease_mechanism="栀子豉汤加生姜止呕",
    formula_meaning="栀子豉汤加生姜止呕",
    keywords=["虚烦", "呕吐", "心烦"],
    source="《伤寒论》"
))
F.append(Formula(
    name="栀子厚朴汤", six_meridian="阳明",
    composition={"栀子": "9g", "厚朴": "12g", "枳实": "9g"},
    indications=["心烦", "腹满", "卧不安"],
    symptoms=["心烦", "腹满", "卧不安"],
    disease_mechanism="栀子豉汤去豆豉加厚朴枳实",
    formula_meaning="栀子豉汤去豆豉加厚朴枳实",
    keywords=["心烦", "腹满", "卧不安"],
    source="《伤寒论》"
))
F.append(Formula(
    name="栀子干姜汤", six_meridian="阳明",
    composition={"栀子": "9g", "干姜": "9g"},
    indications=["身热", "微烦", "腹泻"],
    symptoms=["身热", "微烦", "腹泻"],
    disease_mechanism="栀子清上热干姜温中寒",
    formula_meaning="栀子清上热干姜温中寒",
    keywords=["身热", "微烦", "腹泻"],
    source="《伤寒论》"
))
F.append(Formula(
    name="白虎加人参汤", six_meridian="阳明",
    composition={"石膏": "30-60g", "知母": "12g", "甘草": "6g", "粳米": "15g", "人参": "9g"},
    indications=["大热", "大汗", "大渴", "脉虚大"],
    symptoms=["大热", "大汗", "大渴", "脉虚大"],
    disease_mechanism="白虎汤加人参",
    formula_meaning="白虎汤加人参，益气生津",
    keywords=["大热", "大汗", "大渴", "脉虚", "口渴"],
    source="《伤寒论》"
))
F.append(Formula(
    name="白虎加桂枝汤", six_meridian="阳明",
    composition={"石膏": "30g", "知母": "9g", "甘草": "6g", "粳米": "15g", "桂枝": "9g"},
    indications=["身热", "骨节疼", "微呕"],
    symptoms=["身热", "骨节疼", "微呕"],
    disease_mechanism="白虎汤加桂枝",
    formula_meaning="白虎汤加桂枝，清热通络",
    keywords=["身热", "骨节疼", "微呕"],
    source="《金匮要略》"
))
F.append(Formula(
    name="麻子仁丸", six_meridian="阳明",
    composition={"麻子仁": "30g", "白芍": "15g", "枳实": "15g", "大黄": "15g", "厚朴": "15g", "杏仁": "15g"},
    indications=["便秘", "小便频", "脾约"],
    symptoms=["便秘", "小便频", "脾约"],
    disease_mechanism="小承气加麻仁杏仁润肠通便",
    formula_meaning="小承气加麻仁杏仁润肠通便",
    keywords=["便秘", "小便频", "脾约"],
    source="《伤寒论》"
))
F.append(Formula(
    name="黄芩汤", six_meridian="少阳",
    composition={"黄芩": "9g", "白芍": "9g", "甘草": "6g", "大枣": "4枚"},
    indications=["下利", "腹痛", "口苦"],
    symptoms=["下利", "腹痛", "口苦"],
    disease_mechanism="清热止利",
    formula_meaning="清热止利",
    keywords=["下利", "腹痛", "口苦", "肛门灼热"],
    source="《伤寒论》"
))
F.append(Formula(
    name="黄芩加半夏生姜汤", six_meridian="少阳",
    composition={"黄芩": "9g", "白芍": "9g", "甘草": "6g", "大枣": "4枚", "半夏": "9g", "生姜": "9g"},
    indications=["下利", "呕吐", "口苦"],
    symptoms=["下利", "呕吐", "口苦"],
    disease_mechanism="黄芩汤加半夏生姜和胃止呕",
    formula_meaning="黄芩汤加半夏生姜和胃止呕",
    keywords=["下利", "呕吐", "口苦"],
    source="《伤寒论》"
))
F.append(Formula(
    name="四逆散", six_meridian="少阳",
    composition={"柴胡": "9g", "白芍": "9g", "枳实": "9g", "甘草": "9g"},
    indications=["手足不温", "胸胁满", "脉弦"],
    symptoms=["手足不温", "胸胁满", "脉弦"],
    disease_mechanism="透邪解郁",
    formula_meaning="透邪解郁，疏肝理脾",
    keywords=["手足不温", "胸胁满", "脉弦", "腹痛"],
    source="《伤寒论》"
))
F.append(Formula(
    name="柴胡加芒硝汤", six_meridian="少阳",
    composition={"柴胡": "12g", "黄芩": "4.5g", "人参": "4.5g", "半夏": "4.5g", "甘草": "3g", "生姜": "4.5g", "大枣": "4枚", "芒硝": "6g"},
    indications=["胸胁满", "潮热", "下利"],
    symptoms=["胸胁满", "潮热", "下利"],
    disease_mechanism="小柴胡汤加芒硝",
    formula_meaning="小柴胡汤加芒硝，和解攻下",
    keywords=["胸胁满", "潮热", "下利"],
    source="《伤寒论》"
))
F.append(Formula(
    name="厚朴生姜半夏甘草人参汤", six_meridian="太阴",
    composition={"厚朴": "24g", "生姜": "24g", "半夏": "15g", "甘草": "6g", "人参": "3g"},
    indications=["腹胀满", "食不下"],
    symptoms=["腹胀满", "食不下"],
    disease_mechanism="温中行气除满",
    formula_meaning="温中行气除满",
    keywords=["腹胀满", "食不下", "时腹自痛"],
    source="《伤寒论》"
))
F.append(Formula(
    name="桂枝加芍药汤", six_meridian="太阴",
    composition={"桂枝": "9g", "白芍": "18g", "甘草": "6g", "生姜": "9g", "大枣": "4枚"},
    indications=["腹满时痛", "下利"],
    symptoms=["腹满时痛", "下利"],
    disease_mechanism="桂枝汤倍芍药和脾缓急",
    formula_meaning="桂枝汤倍芍药和脾缓急",
    keywords=["腹满时痛", "下利"],
    source="《伤寒论》"
))
F.append(Formula(
    name="桂枝加大黄汤", six_meridian="太阴",
    composition={"桂枝": "9g", "白芍": "18g", "甘草": "6g", "生姜": "9g", "大枣": "4枚", "大黄": "6g"},
    indications=["腹满痛", "便秘"],
    symptoms=["腹满痛", "便秘"],
    disease_mechanism="桂枝加芍药汤加大黄",
    formula_meaning="桂枝加芍药汤加大黄，导滞通腑",
    keywords=["腹满痛", "便秘", "拒按"],
    source="《伤寒论》"
))
F.append(Formula(
    name="甘草干姜汤", six_meridian="太阴",
    composition={"甘草": "12g", "干姜": "6g"},
    indications=["吐逆", "肢冷", "烦躁"],
    symptoms=["吐逆", "肢冷", "烦躁"],
    disease_mechanism="温中复阳",
    formula_meaning="温中复阳",
    keywords=["吐逆", "肢冷", "烦躁"],
    source="《伤寒论》"
))
F.append(Formula(
    name="通脉四逆汤", six_meridian="少阴",
    composition={"附子": "15g", "干姜": "12g", "甘草": "6g"},
    indications=["四肢厥冷", "脉微欲绝", "面色赤"],
    symptoms=["四肢厥冷", "脉微欲绝", "面色赤"],
    disease_mechanism="四逆汤重用姜附",
    formula_meaning="四逆汤重用姜附，回阳通脉",
    keywords=["四肢厥冷", "脉微欲绝", "面色赤"],
    source="《伤寒论》"
))
F.append(Formula(
    name="通脉四逆加猪胆汁汤", six_meridian="少阴",
    composition={"附子": "15g", "干姜": "12g", "甘草": "6g", "猪胆汁": "10ml"},
    indications=["四肢厥冷", "脉微", "吐利止而烦"],
    symptoms=["四肢厥冷", "脉微", "吐利止而烦"],
    disease_mechanism="通脉四逆汤加猪胆汁",
    formula_meaning="通脉四逆汤加猪胆汁，益阴和阳",
    keywords=["四肢厥冷", "脉微", "吐利止而烦"],
    source="《伤寒论》"
))
F.append(Formula(
    name="白通汤", six_meridian="少阴",
    composition={"附子": "9g", "干姜": "6g", "葱白": "4茎"},
    indications=["下利", "脉微", "面赤"],
    symptoms=["下利", "脉微", "面赤"],
    disease_mechanism="通阳破阴",
    formula_meaning="通阳破阴",
    keywords=["下利", "脉微", "面赤"],
    source="《伤寒论》"
))
F.append(Formula(
    name="白通加猪胆汁汤", six_meridian="少阴",
    composition={"附子": "9g", "干姜": "6g", "葱白": "4茎", "猪胆汁": "10ml", "人尿": "50ml"},
    indications=["下利不止", "厥逆无脉", "干呕"],
    symptoms=["下利不止", "厥逆无脉", "干呕"],
    disease_mechanism="白通汤加猪胆汁人尿",
    formula_meaning="白通汤加猪胆汁人尿，引阳入阴",
    keywords=["下利不止", "厥逆无脉", "干呕"],
    source="《伤寒论》"
))
F.append(Formula(
    name="桃花汤", six_meridian="少阴",
    composition={"赤石脂": "30g", "干姜": "9g", "粳米": "15g"},
    indications=["下利", "便脓血", "腹痛"],
    symptoms=["下利", "便脓血", "腹痛"],
    disease_mechanism="温中涩肠止利",
    formula_meaning="温中涩肠止利",
    keywords=["下利", "便脓血", "腹痛", "滑脱不禁"],
    source="《伤寒论》"
))
F.append(Formula(
    name="猪肤汤", six_meridian="少阴",
    composition={"猪肤": "30g", "白蜜": "15g", "米粉": "10g"},
    indications=["咽痛", "下利", "心烦"],
    symptoms=["咽痛", "下利", "心烦"],
    disease_mechanism="滋阴润燥",
    formula_meaning="滋阴润燥",
    keywords=["咽痛", "下利", "心烦"],
    source="《伤寒论》"
))
F.append(Formula(
    name="甘草汤", six_meridian="少阴",
    composition={"甘草": "12g"},
    indications=["咽痛"],
    symptoms=["咽痛"],
    disease_mechanism="清热解毒利咽",
    formula_meaning="清热解毒利咽",
    keywords=["咽痛", "轻症"],
    source="《伤寒论》"
))
F.append(Formula(
    name="桔梗汤", six_meridian="少阴",
    composition={"甘草": "12g", "桔梗": "6g"},
    indications=["咽痛", "咳吐脓血"],
    symptoms=["咽痛", "咳吐脓血"],
    disease_mechanism="甘草汤加桔梗",
    formula_meaning="甘草汤加桔梗，宣肺利咽",
    keywords=["咽痛", "咳吐脓血"],
    source="《伤寒论》"
))
F.append(Formula(
    name="苦酒汤", six_meridian="少阴",
    composition={"半夏": "10g", "鸡子清": "1枚", "苦酒": "适量"},
    indications=["咽痛", "声嘶", "咽烂"],
    symptoms=["咽痛", "声嘶", "咽烂"],
    disease_mechanism="清热涤痰",
    formula_meaning="清热涤痰，敛疮消肿",
    keywords=["咽痛", "声嘶", "咽烂"],
    source="《伤寒论》"
))
F.append(Formula(
    name="半夏散及汤", six_meridian="少阴",
    composition={"半夏": "9g", "桂枝": "9g", "甘草": "6g"},
    indications=["咽痛", "恶寒"],
    symptoms=["咽痛", "恶寒"],
    disease_mechanism="散寒通阳",
    formula_meaning="散寒通阳，利咽止痛",
    keywords=["咽痛", "恶寒"],
    source="《伤寒论》"
))
F.append(Formula(
    name="白头翁汤", six_meridian="厥阴",
    composition={"白头翁": "15g", "黄柏": "12g", "黄连": "6g", "秦皮": "12g"},
    indications=["下利", "肛门灼热", "渴欲饮水"],
    symptoms=["下利", "肛门灼热", "渴欲饮水"],
    disease_mechanism="清热燥湿",
    formula_meaning="清热燥湿，凉肝止利",
    keywords=["下利", "肛门灼热", "渴欲饮水", "腹痛"],
    source="《伤寒论》"
))
F.append(Formula(
    name="干姜黄芩黄连人参汤", six_meridian="厥阴",
    composition={"干姜": "9g", "黄芩": "9g", "黄连": "9g", "人参": "9g"},
    indications=["下利", "食入口即吐"],
    symptoms=["下利", "食入口即吐"],
    disease_mechanism="清上温下",
    formula_meaning="清上温下，辛开苦降",
    keywords=["下利", "食入口即吐"],
    source="《伤寒论》"
))
F.append(Formula(
    name="麻黄升麻汤", six_meridian="厥阴",
    composition={"麻黄": "9g", "升麻": "3g", "当归": "3g", "知母": "3g", "黄芩": "3g", "玉竹": "3g", "白芍": "3g", "天冬": "3g", "桂枝": "3g", "茯苓": "3g", "甘草": "3g", "石膏": "3g", "白术": "3g", "干姜": "3g"},
    indications=["手足厥冷", "下利", "咽喉不利", "唾脓血"],
    symptoms=["手足厥冷", "下利", "咽喉不利", "唾脓血"],
    disease_mechanism="发越郁阳",
    formula_meaning="发越郁阳，清上温下",
    keywords=["手足厥冷", "下利", "咽喉不利", "唾脓血"],
    source="《伤寒论》"
))
F.append(Formula(
    name="百合地黄汤", six_meridian="杂病",
    composition={"百合": "30g", "生地黄": "30g"},
    indications=["精神恍惚", "欲卧不能卧", "欲行不能行"],
    symptoms=["精神恍惚", "欲卧不能卧", "欲行不能行"],
    disease_mechanism="润肺清心",
    formula_meaning="润肺清心，凉血养阴",
    keywords=["精神恍惚", "欲卧不能卧", "欲行不能行", "口苦"],
    source="《金匮要略》"
))
F.append(Formula(
    name="百合知母汤", six_meridian="杂病",
    composition={"百合": "30g", "知母": "9g"},
    indications=["百合病", "口渴"],
    symptoms=["百合病", "口渴"],
    disease_mechanism="润肺清心",
    formula_meaning="润肺清心",
    keywords=["百合病", "口渴"],
    source="《金匮要略》"
))
F.append(Formula(
    name="百合滑石散", six_meridian="杂病",
    composition={"百合": "30g", "滑石": "30g"},
    indications=["百合病", "小便赤涩", "发热"],
    symptoms=["百合病", "小便赤涩", "发热"],
    disease_mechanism="清热利尿",
    formula_meaning="清热利尿",
    keywords=["百合病", "小便赤涩", "发热"],
    source="《金匮要略》"
))
F.append(Formula(
    name="甘草干姜汤", six_meridian="杂病",
    composition={"甘草": "12g", "干姜": "6g"},
    indications=["肺痿", "吐涎沫", "遗尿"],
    symptoms=["肺痿", "吐涎沫", "遗尿"],
    disease_mechanism="温肺复气",
    formula_meaning="温肺复气",
    keywords=["肺痿", "吐涎沫", "遗尿", "不渴"],
    source="《金匮要略》"
))
F.append(Formula(
    name="射干麻黄汤", six_meridian="杂病",
    composition={"射干": "9g", "麻黄": "9g", "生姜": "9g", "细辛": "3g", "紫菀": "9g", "款冬花": "9g", "五味子": "9g", "半夏": "9g", "大枣": "3枚"},
    indications=["咳而上气", "喉中水鸡声"],
    symptoms=["咳而上气", "喉中水鸡声"],
    disease_mechanism="温肺化饮",
    formula_meaning="温肺化饮，止咳平喘",
    keywords=["咳而上气", "喉中水鸡声", "喘息"],
    source="《金匮要略》"
))
F.append(Formula(
    name="皂荚丸", six_meridian="杂病",
    composition={"皂荚": "适量"},
    indications=["咳逆", "上气", "时时吐浊"],
    symptoms=["咳逆", "上气", "时时吐浊"],
    disease_mechanism="涤痰开窍",
    formula_meaning="涤痰开窍",
    keywords=["咳逆", "上气", "时时吐浊"],
    source="《金匮要略》"
))
F.append(Formula(
    name="厚朴大黄汤", six_meridian="杂病",
    composition={"厚朴": "15g", "大黄": "12g", "枳实": "9g"},
    indications=["支饮", "胸满", "腹胀"],
    symptoms=["支饮", "胸满", "腹胀"],
    disease_mechanism="疏导肠胃",
    formula_meaning="疏导肠胃，荡涤实邪",
    keywords=["支饮", "胸满", "腹胀", "便秘"],
    source="《金匮要略》"
))
F.append(Formula(
    name="葶苈大枣泻肺汤", six_meridian="杂病",
    composition={"葶苈子": "15g", "大枣": "4枚"},
    indications=["肺痈", "喘不得卧"],
    symptoms=["肺痈", "喘不得卧"],
    disease_mechanism="泻肺逐饮",
    formula_meaning="泻肺逐饮",
    keywords=["肺痈", "喘不得卧", "胸满"],
    source="《金匮要略》"
))
F.append(Formula(
    name="越婢汤", six_meridian="杂病",
    composition={"麻黄": "9g", "石膏": "18g", "生姜": "9g", "甘草": "6g", "大枣": "4枚"},
    indications=["风水", "一身悉肿", "脉浮"],
    symptoms=["风水", "一身悉肿", "脉浮"],
    disease_mechanism="发汗利水",
    formula_meaning="发汗利水",
    keywords=["风水", "一身悉肿", "脉浮", "不渴"],
    source="《金匮要略》"
))
F.append(Formula(
    name="防己黄芪汤", six_meridian="杂病",
    composition={"防己": "12g", "黄芪": "15g", "白术": "9g", "甘草": "6g", "生姜": "3片", "大枣": "1枚"},
    indications=["风水", "身重", "汗出恶风"],
    symptoms=["风水", "身重", "汗出恶风"],
    disease_mechanism="益气利水",
    formula_meaning="益气利水",
    keywords=["风水", "身重", "汗出恶风", "浮肿"],
    source="《金匮要略》"
))
F.append(Formula(
    name="黄芪桂枝五物汤", six_meridian="杂病",
    composition={"黄芪": "15g", "桂枝": "9g", "白芍": "9g", "生姜": "18g", "大枣": "4枚"},
    indications=["血痹", "肌肤麻木", "脉微涩"],
    symptoms=["血痹", "肌肤麻木", "脉微涩"],
    disease_mechanism="益气温经",
    formula_meaning="益气温经，和血通痹",
    keywords=["血痹", "肌肤麻木", "脉微涩", "身不仁"],
    source="《金匮要略》"
))
F.append(Formula(
    name="桂枝芍药知母汤", six_meridian="杂病",
    composition={"桂枝": "12g", "白芍": "9g", "甘草": "6g", "麻黄": "6g", "生姜": "15g", "白术": "15g", "知母": "12g", "防风": "12g", "附子": "6g"},
    indications=["历节", "肢节疼痛", "脚肿"],
    symptoms=["历节", "肢节疼痛", "脚肿"],
    disease_mechanism="祛风除湿",
    formula_meaning="祛风除湿，温经散寒",
    keywords=["历节", "肢节疼痛", "脚肿", "头眩"],
    source="《金匮要略》"
))
F.append(Formula(
    name="乌头汤", six_meridian="杂病",
    composition={"麻黄": "9g", "白芍": "9g", "黄芪": "9g", "甘草": "9g", "川乌": "12g"},
    indications=["历节", "疼痛剧烈", "不可屈伸"],
    symptoms=["历节", "疼痛剧烈", "不可屈伸"],
    disease_mechanism="温经散寒",
    formula_meaning="温经散寒，除湿止痛",
    keywords=["历节", "疼痛剧烈", "不可屈伸"],
    source="《金匮要略》"
))
F.append(Formula(
    name="黄芪建中汤", six_meridian="杂病",
    composition={"黄芪": "9g", "白芍": "18g", "桂枝": "9g", "甘草": "6g", "生姜": "9g", "大枣": "4枚", "饴糖": "30g"},
    indications=["虚劳", "里急", "诸不足"],
    symptoms=["虚劳", "里急", "诸不足"],
    disease_mechanism="温中补气",
    formula_meaning="温中补气，和里缓急",
    keywords=["虚劳", "里急", "诸不足"],
    source="《金匮要略》"
))
F.append(Formula(
    name="肾气丸", six_meridian="杂病",
    composition={"干地黄": "24g", "山药": "12g", "山茱萸": "12g", "泽泻": "9g", "茯苓": "9g", "牡丹皮": "9g", "桂枝": "3g", "附子": "3g"},
    indications=["肾阳虚", "腰痛", "小便不利"],
    symptoms=["肾阳虚", "腰痛", "小便不利"],
    disease_mechanism="温补肾阳",
    formula_meaning="温补肾阳",
    keywords=["肾阳虚", "腰痛", "小便不利", "畏寒"],
    source="《金匮要略》"
))
F.append(Formula(
    name="酸枣仁汤", six_meridian="杂病",
    composition={"酸枣仁": "30g", "甘草": "3g", "知母": "9g", "茯苓": "9g", "川芎": "6g"},
    indications=["虚劳", "虚烦失眠", "头目眩晕"],
    symptoms=["虚劳", "虚烦失眠", "头目眩晕"],
    disease_mechanism="养血安神",
    formula_meaning="养血安神，清热除烦",
    keywords=["虚劳", "虚烦失眠", "头目眩晕"],
    source="《金匮要略》"
))
F.append(Formula(
    name="温经汤", six_meridian="杂病",
    composition={"吴茱萸": "9g", "当归": "9g", "川芎": "6g", "白芍": "9g", "人参": "6g", "桂枝": "6g", "阿胶": "9g", "牡丹皮": "6g", "生姜": "6g", "甘草": "6g", "半夏": "9g", "麦冬": "9g"},
    indications=["崩漏", "月经不调", "少腹寒"],
    symptoms=["崩漏", "月经不调", "少腹寒"],
    disease_mechanism="温经散寒",
    formula_meaning="温经散寒，养血祛瘀",
    keywords=["崩漏", "月经不调", "少腹寒", "唇口干燥"],
    source="《金匮要略》"
))
F.append(Formula(
    name="当归芍药散", six_meridian="杂病",
    composition={"当归": "9g", "白芍": "30g", "川芎": "9g", "白术": "12g", "茯苓": "12g", "泽泻": "15g"},
    indications=["妇人腹痛", "腹中拘急"],
    symptoms=["妇人腹痛", "腹中拘急"],
    disease_mechanism="养血调肝",
    formula_meaning="养血调肝，健脾利湿",
    keywords=["妇人腹痛", "腹中拘急", "小便不利"],
    source="《金匮要略》"
))
F.append(Formula(
    name="当归生姜羊肉汤", six_meridian="杂病",
    composition={"当归": "15g", "生姜": "30g", "羊肉": "30g"},
    indications=["虚寒", "腹痛", "胁痛"],
    symptoms=["虚寒", "腹痛", "胁痛"],
    disease_mechanism="温中补虚",
    formula_meaning="温中补虚，祛寒止痛",
    keywords=["虚寒", "腹痛", "胁痛", "产后"],
    source="《金匮要略》"
))
F.append(Formula(
    name="胶艾汤", six_meridian="杂病",
    composition={"阿胶": "6g", "艾叶": "9g", "当归": "9g", "川芎": "6g", "白芍": "12g", "甘草": "6g", "干地黄": "12g"},
    indications=["崩漏", "月经过多", "妊娠下血"],
    symptoms=["崩漏", "月经过多", "妊娠下血"],
    disease_mechanism="养血止血",
    formula_meaning="养血止血，调经安胎",
    keywords=["崩漏", "月经过多", "妊娠下血"],
    source="《金匮要略》"
))
F.append(Formula(
    name="苓桂五味甘草汤", six_meridian="杂病",
    composition={"茯苓": "12g", "桂枝": "9g", "五味子": "9g", "甘草": "6g"},
    indications=["咳嗽", "手足厥冷", "小便难"],
    symptoms=["咳嗽", "手足厥冷", "小便难"],
    disease_mechanism="温肺化饮",
    formula_meaning="温肺化饮",
    keywords=["咳嗽", "手足厥冷", "小便难"],
    source="《金匮要略》"
))
F.append(Formula(
    name="苓甘五味姜辛汤", six_meridian="杂病",
    composition={"茯苓": "12g", "甘草": "6g", "五味子": "9g", "干姜": "9g", "细辛": "3g"},
    indications=["咳嗽", "胸满"],
    symptoms=["咳嗽", "胸满"],
    disease_mechanism="温肺化饮",
    formula_meaning="温肺化饮",
    keywords=["咳嗽", "胸满"],
    source="《金匮要略》"
))
F.append(Formula(
    name="苓甘五味加姜辛半夏杏仁汤", six_meridian="杂病",
    composition={"茯苓": "12g", "甘草": "6g", "五味子": "9g", "干姜": "9g", "细辛": "3g", "半夏": "9g", "杏仁": "9g"},
    indications=["咳嗽", "肢体浮肿"],
    symptoms=["咳嗽", "肢体浮肿"],
    disease_mechanism="温肺化饮",
    formula_meaning="温肺化饮，宣肺利水",
    keywords=["咳嗽", "肢体浮肿"],
    source="《金匮要略》"
))
F.append(Formula(
    name="苓甘五味加姜辛半杏大黄汤", six_meridian="杂病",
    composition={"茯苓": "12g", "甘草": "6g", "五味子": "9g", "干姜": "9g", "细辛": "3g", "半夏": "9g", "杏仁": "9g", "大黄": "6g"},
    indications=["咳嗽", "面热如醉"],
    symptoms=["咳嗽", "面热如醉"],
    disease_mechanism="温肺化饮",
    formula_meaning="温肺化饮，兼清胃热",
    keywords=["咳嗽", "面热如醉"],
    source="《金匮要略》"
))
F.append(Formula(
    name="旋覆代赭汤", six_meridian="杂病",
    composition={"旋覆花": "9g", "代赭石": "3g", "人参": "6g", "生姜": "15g", "半夏": "9g", "甘草": "9g", "大枣": "4枚"},
    indications=["心下痞硬", "噫气", "呕逆"],
    symptoms=["心下痞硬", "噫气", "呕逆"],
    disease_mechanism="降逆化痰",
    formula_meaning="降逆化痰，益气和胃",
    keywords=["心下痞硬", "噫气", "呕逆"],
    source="《伤寒论》"
))
F.append(Formula(
    name="生姜泻心汤", six_meridian="杂病",
    composition={"生姜": "12g", "甘草": "9g", "人参": "9g", "干姜": "3g", "黄芩": "9g", "半夏": "9g", "黄连": "3g", "大枣": "4枚"},
    indications=["心下痞硬", "干噫食臭", "腹中雷鸣"],
    symptoms=["心下痞硬", "干噫食臭", "腹中雷鸣"],
    disease_mechanism="和胃消痞",
    formula_meaning="和胃消痞，散结除水",
    keywords=["心下痞硬", "干噫食臭", "腹中雷鸣"],
    source="《伤寒论》"
))
F.append(Formula(
    name="甘草泻心汤", six_meridian="杂病",
    composition={"甘草": "12g", "黄芩": "9g", "干姜": "9g", "半夏": "9g", "黄连": "3g", "大枣": "4枚", "人参": "9g"},
    indications=["心下痞硬", "下利", "狐惑"],
    symptoms=["心下痞硬", "下利", "狐惑"],
    disease_mechanism="补中降逆",
    formula_meaning="补中降逆，消痞除烦",
    keywords=["心下痞硬", "下利", "狐惑"],
    source="《伤寒论》"
))
F.append(Formula(
    name="大黄黄连泻心汤", six_meridian="杂病",
    composition={"大黄": "6g", "黄连": "3g"},
    indications=["心下痞", "按之濡", "脉关上浮"],
    symptoms=["心下痞", "按之濡", "脉关上浮"],
    disease_mechanism="泻热消痞",
    formula_meaning="泻热消痞",
    keywords=["心下痞", "按之濡", "脉关上浮", "心烦"],
    source="《伤寒论》"
))
F.append(Formula(
    name="附子泻心汤", six_meridian="杂病",
    composition={"大黄": "6g", "黄连": "3g", "黄芩": "3g", "附子": "9g"},
    indications=["心下痞", "恶寒", "汗出"],
    symptoms=["心下痞", "恶寒", "汗出"],
    disease_mechanism="泻热消痞",
    formula_meaning="泻热消痞，扶阳固表",
    keywords=["心下痞", "恶寒", "汗出"],
    source="《伤寒论》"
))
F.append(Formula(
    name="黄连汤", six_meridian="杂病",
    composition={"黄连": "9g", "甘草": "9g", "干姜": "9g", "桂枝": "9g", "人参": "6g", "半夏": "9g", "大枣": "4枚"},
    indications=["胸中有热", "胃中有邪气", "腹痛欲呕"],
    symptoms=["胸中有热", "胃中有邪气", "腹痛欲呕"],
    disease_mechanism="清上温下",
    formula_meaning="清上温下，和胃降逆",
    keywords=["胸中有热", "胃中有邪气", "腹痛欲呕"],
    source="《伤寒论》"
))
F.append(Formula(
    name="黄连阿胶汤", six_meridian="少阴",
    composition={"黄连": "12g", "黄芩": "6g", "白芍": "6g", "鸡子黄": "2枚", "阿胶": "9g"},
    indications=["心中烦", "不得卧"],
    symptoms=["心中烦", "不得卧"],
    disease_mechanism="滋阴清热",
    formula_meaning="滋阴清热",
    keywords=["心中烦", "不得卧", "失眠", "口干"],
    source="《伤寒论》"
))
F.append(Formula(
    name="桂枝加龙骨牡蛎汤", six_meridian="杂病",
    composition={"桂枝": "9g", "白芍": "9g", "甘草": "6g", "生姜": "9g", "大枣": "4枚", "龙骨": "9g", "牡蛎": "9g"},
    indications=["虚劳", "失精", "梦交"],
    symptoms=["虚劳", "失精", "梦交"],
    disease_mechanism="调和阴阳",
    formula_meaning="调和阴阳，潜镇固涩",
    keywords=["虚劳", "失精", "梦交", "少腹弦急"],
    source="《金匮要略》"
))

F.append(Formula(
    name="百合滑石代赭汤", six_meridian="杂病",
    composition={"百合": "30g", "滑石": "30g", "代赭石": "15g"},
    indications=["百合病", "下利"],
    symptoms=["百合病", "下利"],
    disease_mechanism="清热利尿重镇降逆",
    formula_meaning="清热利尿重镇降逆",
    keywords=["百合病", "下利", "小便赤涩"],
    source="《金匮要略》"
))
F.append(Formula(
    name="百合洗方", six_meridian="杂病",
    composition={"百合": "100g"},
    indications=["百合病", "一月不解"],
    symptoms=["百合病", "一月不解"],
    disease_mechanism="外洗润肺",
    formula_meaning="外洗润肺",
    keywords=["百合病", "一月不解", "变成渴"],
    source="《金匮要略》"
))
F.append(Formula(
    name="瓜蒌牡蛎散", six_meridian="杂病",
    composition={"瓜蒌根": "30g", "牡蛎": "30g"},
    indications=["百合病", "口渴"],
    symptoms=["百合病", "口渴"],
    disease_mechanism="生津止渴",
    formula_meaning="生津止渴",
    keywords=["百合病", "口渴"],
    source="《金匮要略》"
))
F.append(Formula(
    name="百合鸡子汤", six_meridian="杂病",
    composition={"百合": "30g", "鸡子黄": "1枚"},
    indications=["百合病", "吐之后"],
    symptoms=["百合病", "吐之后"],
    disease_mechanism="养阴润燥",
    formula_meaning="养阴润燥",
    keywords=["百合病", "吐之后"],
    source="《金匮要略》"
))
F.append(Formula(
    name="百合紫菀汤", six_meridian="杂病",
    composition={"百合": "21g", "紫菀": "9g", "桔梗": "6g", "贝母": "9g", "天冬": "9g", "茯苓": "9g", "甘草": "6g", "生姜": "3片"},
    indications=["肺痈", "咳吐脓血"],
    symptoms=["肺痈", "咳吐脓血"],
    disease_mechanism="清热排脓",
    formula_meaning="清热排脓",
    keywords=["肺痈", "咳吐脓血"],
    source="《金匮要略》"
))
F.append(Formula(
    name="桂枝茯苓丸", six_meridian="杂病",
    composition={"桂枝": "9g", "茯苓": "9g", "牡丹皮": "9g", "白芍": "9g", "桃仁": "9g"},
    indications=["癥病", "妇人小腹肿块"],
    symptoms=["癥病", "妇人小腹肿块"],
    disease_mechanism="活血化瘀消癥",
    formula_meaning="活血化瘀消癥",
    keywords=["癥病", "妇人小腹肿块", "月经不调", "痛经"],
    source="《金匮要略》"
))
F.append(Formula(
    name="胶艾汤", six_meridian="杂病",
    composition={"阿胶": "6g", "艾叶": "9g", "当归": "9g", "川芎": "6g", "白芍": "12g", "甘草": "6g", "干地黄": "12g"},
    indications=["崩漏", "妊娠下血"],
    symptoms=["崩漏", "妊娠下血"],
    disease_mechanism="养血止血安胎",
    formula_meaning="养血止血安胎",
    keywords=["崩漏", "妊娠下血", "腹中痛"],
    source="《金匮要略》"
))
F.append(Formula(
    name="当归散", six_meridian="杂病",
    composition={"当归": "30g", "黄芩": "30g", "白芍": "30g", "川芎": "30g", "白术": "15g"},
    indications=["妊娠", "养胎"],
    symptoms=["妊娠", "养胎"],
    disease_mechanism="养血健脾清热安胎",
    formula_meaning="养血健脾清热安胎",
    keywords=["妊娠", "养胎", "胎动不安"],
    source="《金匮要略》"
))
F.append(Formula(
    name="白术散", six_meridian="杂病",
    composition={"白术": "30g", "川芎": "30g", "蜀椒": "9g", "牡蛎": "9g"},
    indications=["妊娠", "胎动不安"],
    symptoms=["妊娠", "胎动不安"],
    disease_mechanism="健脾温中安胎",
    formula_meaning="健脾温中安胎",
    keywords=["妊娠", "胎动不安", "寒湿"],
    source="《金匮要略》"
))
F.append(Formula(
    name="当归贝母苦参丸", six_meridian="杂病",
    composition={"当归": "12g", "贝母": "12g", "苦参": "12g"},
    indications=["妊娠", "小便难"],
    symptoms=["妊娠", "小便难"],
    disease_mechanism="养血清热利尿",
    formula_meaning="养血清热利尿",
    keywords=["妊娠", "小便难", "饮食如故"],
    source="《金匮要略》"
))
F.append(Formula(
    name="葵子茯苓散", six_meridian="杂病",
    composition={"葵子": "30g", "茯苓": "9g"},
    indications=["妊娠", "头眩", "小便难"],
    symptoms=["妊娠", "头眩", "小便难"],
    disease_mechanism="利水通阳",
    formula_meaning="利水通阳",
    keywords=["妊娠", "头眩", "小便难", "身重"],
    source="《金匮要略》"
))
F.append(Formula(
    name="当归散加味", six_meridian="杂病",
    composition={"当归": "9g", "白芍": "9g", "川芎": "6g", "黄芩": "9g", "白术": "12g"},
    indications=["妊娠", "胎动不安"],
    symptoms=["妊娠", "胎动不安"],
    disease_mechanism="养血安胎",
    formula_meaning="养血安胎",
    keywords=["妊娠", "胎动不安", "血虚"],
    source="《金匮要略》"
))
F.append(Formula(
    name="白术散加味", six_meridian="杂病",
    composition={"白术": "12g", "川芎": "6g", "蜀椒": "3g", "牡蛎": "9g"},
    indications=["妊娠", "胎动不安", "腹痛"],
    symptoms=["妊娠", "胎动不安", "腹痛"],
    disease_mechanism="温中安胎",
    formula_meaning="温中安胎",
    keywords=["妊娠", "胎动不安", "腹痛", "寒证"],
    source="《金匮要略》"
))
F.append(Formula(
    name="小柴胡汤", six_meridian="少阳",
    composition={"柴胡": "24g", "黄芩": "9g", "人参": "9g", "半夏": "9g", "甘草": "9g", "生姜": "9g", "大枣": "4枚"},
    indications=["产后", "郁冒", "大便难"],
    symptoms=["产后", "郁冒", "大便难"],
    disease_mechanism="和解少阳",
    formula_meaning="和解少阳",
    keywords=["产后", "郁冒", "大便难", "呕不能食"],
    source="《金匮要略》"
))
F.append(Formula(
    name="大承气汤", six_meridian="阳明",
    composition={"大黄": "12g", "厚朴": "15g", "枳实": "12g", "芒硝": "9g"},
    indications=["产后", "胃实"],
    symptoms=["产后", "胃实"],
    disease_mechanism="攻下热结",
    formula_meaning="攻下热结",
    keywords=["产后", "胃实", "烦躁", "发热"],
    source="《金匮要略》"
))
F.append(Formula(
    name="当归生姜羊肉汤", six_meridian="杂病",
    composition={"当归": "15g", "生姜": "30g", "羊肉": "30g"},
    indications=["产后", "腹痛"],
    symptoms=["产后", "腹痛"],
    disease_mechanism="温中补虚止痛",
    formula_meaning="温中补虚止痛",
    keywords=["产后", "腹痛", "虚寒"],
    source="《金匮要略》"
))
F.append(Formula(
    name="枳实芍药散", six_meridian="杂病",
    composition={"枳实": "9g", "白芍": "9g"},
    indications=["产后", "腹痛", "烦满"],
    symptoms=["产后", "腹痛", "烦满"],
    disease_mechanism="行气活血",
    formula_meaning="行气活血",
    keywords=["产后", "腹痛", "烦满", "不得卧"],
    source="《金匮要略》"
))
F.append(Formula(
    name="下瘀血汤", six_meridian="杂病",
    composition={"大黄": "9g", "桃仁": "9g", "䗪虫": "9g"},
    indications=["产后", "腹痛", "瘀血"],
    symptoms=["产后", "腹痛", "瘀血"],
    disease_mechanism="破血下瘀",
    formula_meaning="破血下瘀",
    keywords=["产后", "腹痛", "瘀血", "经水不利"],
    source="《金匮要略》"
))
F.append(Formula(
    name="阳旦汤", six_meridian="太阳",
    composition={"桂枝": "9g", "白芍": "9g", "甘草": "6g", "生姜": "9g", "大枣": "4枚", "黄芩": "9g"},
    indications=["产后", "发热", "头痛"],
    symptoms=["产后", "发热", "头痛"],
    disease_mechanism="解表清热",
    formula_meaning="解表清热",
    keywords=["产后", "发热", "头痛", "汗出"],
    source="《金匮要略》"
))
F.append(Formula(
    name="竹叶汤", six_meridian="太阳",
    composition={"竹叶": "9g", "葛根": "9g", "防风": "9g", "桔梗": "6g", "桂枝": "6g", "人参": "6g", "甘草": "6g", "附子": "6g", "大枣": "4枚", "生姜": "9g"},
    indications=["产后", "发热", "面赤"],
    symptoms=["产后", "发热", "面赤"],
    disease_mechanism="解表扶阳",
    formula_meaning="解表扶阳",
    keywords=["产后", "发热", "面赤", "喘而头痛"],
    source="《金匮要略》"
))
F.append(Formula(
    name="竹皮大丸", six_meridian="杂病",
    composition={"竹茹": "9g", "石膏": "9g", "桂枝": "6g", "甘草": "9g", "白薇": "9g"},
    indications=["产后", "烦呕"],
    symptoms=["产后", "烦呕"],
    disease_mechanism="清热除烦",
    formula_meaning="清热除烦",
    keywords=["产后", "烦呕", "发热"],
    source="《金匮要略》"
))
F.append(Formula(
    name="白头翁加甘草阿胶汤", six_meridian="杂病",
    composition={"白头翁": "15g", "黄柏": "12g", "黄连": "6g", "秦皮": "12g", "甘草": "6g", "阿胶": "9g"},
    indications=["产后", "下利"],
    symptoms=["产后", "下利"],
    disease_mechanism="清热止利养血",
    formula_meaning="清热止利养血",
    keywords=["产后", "下利", "虚极"],
    source="《金匮要略》"
))
F.append(Formula(
    name="半夏厚朴汤", six_meridian="少阳",
    composition={"半夏": "12g", "厚朴": "9g", "茯苓": "12g", "生姜": "15g", "苏叶": "6g"},
    indications=["妇人", "咽中如有炙脔"],
    symptoms=["妇人", "咽中如有炙脔"],
    disease_mechanism="行气散结",
    formula_meaning="行气散结",
    keywords=["妇人", "咽中如有炙脔", "梅核气"],
    source="《金匮要略》"
))
F.append(Formula(
    name="甘麦大枣汤", six_meridian="杂病",
    composition={"甘草": "9g", "小麦": "30g", "大枣": "10枚"},
    indications=["妇人", "脏躁", "喜悲伤"],
    symptoms=["妇人", "脏躁", "喜悲伤"],
    disease_mechanism="养心安神",
    formula_meaning="养心安神",
    keywords=["妇人", "脏躁", "喜悲伤欲哭", "数欠伸"],
    source="《金匮要略》"
))
F.append(Formula(
    name="温经汤", six_meridian="杂病",
    composition={"吴茱萸": "9g", "当归": "9g", "川芎": "6g", "白芍": "9g", "人参": "6g", "桂枝": "6g", "阿胶": "9g", "牡丹皮": "6g", "生姜": "6g", "甘草": "6g", "半夏": "9g", "麦冬": "9g"},
    indications=["崩漏", "月经不调"],
    symptoms=["崩漏", "月经不调"],
    disease_mechanism="温经散寒养血",
    formula_meaning="温经散寒养血",
    keywords=["崩漏", "月经不调", "少腹寒", "唇口干燥"],
    source="《金匮要略》"
))
F.append(Formula(
    name="土瓜根散", six_meridian="杂病",
    composition={"土瓜根": "9g", "白芍": "9g", "桂枝": "9g", "䗪虫": "9g"},
    indications=["月经不调", "带下"],
    symptoms=["月经不调", "带下"],
    disease_mechanism="活血通经",
    formula_meaning="活血通经",
    keywords=["月经不调", "带下", "少腹满痛"],
    source="《金匮要略》"
))
F.append(Formula(
    name="旋覆花汤", six_meridian="杂病",
    composition={"旋覆花": "9g", "葱": "14茎", "新绛": "少许"},
    indications=["半产漏下", "胁痛"],
    symptoms=["半产漏下", "胁痛"],
    disease_mechanism="行气活血通络",
    formula_meaning="行气活血通络",
    keywords=["半产漏下", "胁痛"],
    source="《金匮要略》"
))
F.append(Formula(
    name="胶姜汤", six_meridian="杂病",
    composition={"阿胶": "9g", "干姜": "9g"},
    indications=["妇人", "陷经漏下"],
    symptoms=["妇人", "陷经漏下"],
    disease_mechanism="温经止血",
    formula_meaning="温经止血",
    keywords=["妇人", "陷经漏下", "色黑"],
    source="《金匮要略》"
))
F.append(Formula(
    name="大黄甘遂汤", six_meridian="杂病",
    composition={"大黄": "12g", "甘遂": "6g", "阿胶": "9g"},
    indications=["妇人", "少腹满如敦状"],
    symptoms=["妇人", "少腹满如敦状"],
    disease_mechanism="破血逐水",
    formula_meaning="破血逐水",
    keywords=["妇人", "少腹满如敦状", "小便微难"],
    source="《金匮要略》"
))
F.append(Formula(
    name="抵当汤", six_meridian="杂病",
    composition={"水蛭": "30个", "虻虫": "30个", "桃仁": "20个", "大黄": "9g"},
    indications=["妇人", "经水不利", "瘀血"],
    symptoms=["妇人", "经水不利", "瘀血"],
    disease_mechanism="破血逐瘀",
    formula_meaning="破血逐瘀",
    keywords=["妇人", "经水不利", "瘀血", "少腹硬满"],
    source="《金匮要略》"
))
F.append(Formula(
    name="矾石丸", six_meridian="杂病",
    composition={"矾石": "9g", "杏仁": "3g"},
    indications=["妇人", "带下"],
    symptoms=["妇人", "带下"],
    disease_mechanism="清热燥湿止带",
    formula_meaning="清热燥湿止带",
    keywords=["妇人", "带下", "经水闭"],
    source="《金匮要略》"
))
F.append(Formula(
    name="红蓝花酒", six_meridian="杂病",
    composition={"红蓝花": "9g"},
    indications=["妇人", "腹痛", "风血"],
    symptoms=["妇人", "腹痛", "风血"],
    disease_mechanism="活血止痛",
    formula_meaning="活血止痛",
    keywords=["妇人", "腹痛", "风血相搏"],
    source="《金匮要略》"
))
F.append(Formula(
    name="蛇床子散", six_meridian="杂病",
    composition={"蛇床子": "适量"},
    indications=["妇人", "阴寒"],
    symptoms=["妇人", "阴寒"],
    disease_mechanism="温阴散寒",
    formula_meaning="温阴散寒",
    keywords=["妇人", "阴寒", "带下"],
    source="《金匮要略》"
))
F.append(Formula(
    name="狼牙汤", six_meridian="杂病",
    composition={"狼牙": "适量"},
    indications=["妇人", "阴中蚀疮"],
    symptoms=["妇人", "阴中蚀疮"],
    disease_mechanism="清热燥湿解毒",
    formula_meaning="清热燥湿解毒",
    keywords=["妇人", "阴中蚀疮"],
    source="《金匮要略》"
))
F.append(Formula(
    name="小儿疳虫蚀齿方", six_meridian="杂病",
    composition={"雄黄": "适量", "葶苈": "适量"},
    indications=["小儿", "疳虫蚀齿"],
    symptoms=["小儿", "疳虫蚀齿"],
    disease_mechanism="杀虫解毒",
    formula_meaning="杀虫解毒",
    keywords=["小儿", "疳虫蚀齿"],
    source="《金匮要略》"
))
F.append(Formula(
    name="麻仁丸", six_meridian="杂病",
    composition={"麻仁": "30g", "白芍": "15g", "枳实": "15g", "大黄": "15g", "厚朴": "15g", "杏仁": "15g"},
    indications=["脾约", "便秘"],
    symptoms=["脾约", "便秘"],
    disease_mechanism="润肠通便",
    formula_meaning="润肠通便",
    keywords=["脾约", "便秘", "小便数"],
    source="《金匮要略》"
))
F.append(Formula(
    name="甘草干姜茯苓白术汤", six_meridian="杂病",
    composition={"甘草": "6g", "干姜": "12g", "茯苓": "12g", "白术": "6g"},
    indications=["肾着", "身重", "腰冷"],
    symptoms=["肾着", "身重", "腰冷"],
    disease_mechanism="温中祛湿",
    formula_meaning="温中祛湿",
    keywords=["肾着", "身重", "腰冷", "如坐水中"],
    source="《金匮要略》"
))
F.append(Formula(
    name="甘遂半夏汤", six_meridian="杂病",
    composition={"甘遂": "3g", "半夏": "12g", "白芍": "9g", "甘草": "6g"},
    indications=["留饮", "脉伏"],
    symptoms=["留饮", "脉伏"],
    disease_mechanism="攻破利水",
    formula_meaning="攻破利水",
    keywords=["留饮", "脉伏", "利后反快"],
    source="《金匮要略》"
))
F.append(Formula(
    name="木防己汤", six_meridian="杂病",
    composition={"木防己": "9g", "石膏": "30g", "桂枝": "9g", "人参": "12g"},
    indications=["支饮", "心下痞坚"],
    symptoms=["支饮", "心下痞坚"],
    disease_mechanism="行水散结",
    formula_meaning="行水散结",
    keywords=["支饮", "心下痞坚", "面色黧黑"],
    source="《金匮要略》"
))
F.append(Formula(
    name="木防己去石膏加茯苓芒硝汤", six_meridian="杂病",
    composition={"木防己": "9g", "桂枝": "9g", "人参": "12g", "茯苓": "12g", "芒硝": "9g"},
    indications=["支饮", "心下痞坚", "复发"],
    symptoms=["支饮", "心下痞坚", "复发"],
    disease_mechanism="软坚散结",
    formula_meaning="软坚散结",
    keywords=["支饮", "心下痞坚", "复发"],
    source="《金匮要略》"
))
F.append(Formula(
    name="泽泻汤", six_meridian="杂病",
    composition={"泽泻": "15g", "白术": "6g"},
    indications=["支饮", "眩"],
    symptoms=["支饮", "眩"],
    disease_mechanism="利水健脾",
    formula_meaning="利水健脾",
    keywords=["支饮", "眩", "苦冒眩"],
    source="《金匮要略》"
))
F.append(Formula(
    name="小半夏汤", six_meridian="杂病",
    composition={"半夏": "15g", "生姜": "15g"},
    indications=["呕吐", "谷不得下"],
    symptoms=["呕吐", "谷不得下"],
    disease_mechanism="和胃止呕",
    formula_meaning="和胃止呕",
    keywords=["呕吐", "谷不得下", "心下有支饮"],
    source="《金匮要略》"
))
F.append(Formula(
    name="小半夏加茯苓汤", six_meridian="杂病",
    composition={"半夏": "15g", "生姜": "15g", "茯苓": "9g"},
    indications=["眩", "呕吐", "心下痞"],
    symptoms=["眩", "呕吐", "心下痞"],
    disease_mechanism="和胃止呕利水",
    formula_meaning="和胃止呕利水",
    keywords=["眩", "呕吐", "心下痞", "膈间有水"],
    source="《金匮要略》"
))
F.append(Formula(
    name="己椒苈黄丸", six_meridian="杂病",
    composition={"防己": "9g", "椒目": "9g", "葶苈子": "9g", "大黄": "9g"},
    indications=["腹满", "口燥"],
    symptoms=["腹满", "口燥"],
    disease_mechanism="攻逐水饮",
    formula_meaning="攻逐水饮",
    keywords=["腹满", "口燥", "肠间有水气"],
    source="《金匮要略》"
))
F.append(Formula(
    name="五苓散加味", six_meridian="杂病",
    composition={"茯苓": "9g", "猪苓": "9g", "泽泻": "15g", "白术": "9g", "桂枝": "6g"},
    indications=["脐下悸", "吐涎沫"],
    symptoms=["脐下悸", "吐涎沫"],
    disease_mechanism="化气利水",
    formula_meaning="化气利水",
    keywords=["脐下悸", "吐涎沫", "癫眩"],
    source="《金匮要略》"
))
F.append(Formula(
    name="茯苓饮", six_meridian="杂病",
    composition={"茯苓": "9g", "人参": "9g", "白术": "9g", "枳实": "9g", "橘皮": "9g", "生姜": "9g"},
    indications=["心胸间虚", "气满不能食"],
    symptoms=["心胸间虚", "气满不能食"],
    disease_mechanism="健脾行气",
    formula_meaning="健脾行气",
    keywords=["心胸间虚", "气满不能食"],
    source="《金匮要略》"
))
F.append(Formula(
    name="文蛤散", six_meridian="杂病",
    composition={"文蛤": "15g"},
    indications=["消渴", "欲饮水"],
    symptoms=["消渴", "欲饮水"],
    disease_mechanism="清热生津",
    formula_meaning="清热生津",
    keywords=["消渴", "欲饮水", "小便不利"],
    source="《金匮要略》"
))
F.append(Formula(
    name="瓜蒌瞿麦丸", six_meridian="杂病",
    composition={"瓜蒌根": "6g", "茯苓": "9g", "薯蓣": "9g", "附子": "6g", "瞿麦": "3g"},
    indications=["小便不利", "苦渴"],
    symptoms=["小便不利", "苦渴"],
    disease_mechanism="温阳利水生津",
    formula_meaning="温阳利水生津",
    keywords=["小便不利", "苦渴", "腹中冷"],
    source="《金匮要略》"
))
F.append(Formula(
    name="蒲灰散", six_meridian="杂病",
    composition={"蒲灰": "15g", "滑石": "15g"},
    indications=["小便不利"],
    symptoms=["小便不利"],
    disease_mechanism="清热利尿",
    formula_meaning="清热利尿",
    keywords=["小便不利", "皮水"],
    source="《金匮要略》"
))
F.append(Formula(
    name="滑石白鱼散", six_meridian="杂病",
    composition={"滑石": "15g", "白鱼": "15g", "乱发": "15g"},
    indications=["小便不利", "血淋"],
    symptoms=["小便不利", "血淋"],
    disease_mechanism="化瘀利尿",
    formula_meaning="化瘀利尿",
    keywords=["小便不利", "血淋"],
    source="《金匮要略》"
))
F.append(Formula(
    name="茯苓戎盐汤", six_meridian="杂病",
    composition={"茯苓": "15g", "白术": "9g", "戎盐": "3g"},
    indications=["小便不利"],
    symptoms=["小便不利"],
    disease_mechanism="健脾利尿",
    formula_meaning="健脾利尿",
    keywords=["小便不利", "劳淋"],
    source="《金匮要略》"
))
F.append(Formula(
    name="越婢加术汤", six_meridian="杂病",
    composition={"麻黄": "9g", "石膏": "18g", "生姜": "9g", "甘草": "6g", "大枣": "4枚", "白术": "12g"},
    indications=["皮水", "一身面目黄肿"],
    symptoms=["皮水", "一身面目黄肿"],
    disease_mechanism="发汗利水健脾",
    formula_meaning="发汗利水健脾",
    keywords=["皮水", "一身面目黄肿", "小便不利"],
    source="《金匮要略》"
))
F.append(Formula(
    name="越婢加半夏汤", six_meridian="杂病",
    composition={"麻黄": "9g", "石膏": "18g", "生姜": "9g", "甘草": "6g", "大枣": "4枚", "半夏": "9g"},
    indications=["咳喘", "目如脱状"],
    symptoms=["咳喘", "目如脱状"],
    disease_mechanism="宣肺泄热",
    formula_meaning="宣肺泄热",
    keywords=["咳喘", "目如脱状", "脉浮大"],
    source="《金匮要略》"
))
F.append(Formula(
    name="甘草麻黄汤", six_meridian="杂病",
    composition={"甘草": "6g", "麻黄": "12g"},
    indications=["皮水", "一身面目黄肿"],
    symptoms=["皮水", "一身面目黄肿"],
    disease_mechanism="发汗利水",
    formula_meaning="发汗利水",
    keywords=["皮水", "一身面目黄肿", "无汗"],
    source="《金匮要略》"
))
F.append(Formula(
    name="麻黄附子汤", six_meridian="杂病",
    composition={"麻黄": "9g", "甘草": "6g", "附子": "9g"},
    indications=["水气", "脉沉"],
    symptoms=["水气", "脉沉"],
    disease_mechanism="温阳发汗",
    formula_meaning="温阳发汗",
    keywords=["水气", "脉沉", "小便不利"],
    source="《金匮要略》"
))
F.append(Formula(
    name="杏子汤", six_meridian="杂病",
    composition={"麻黄": "9g", "杏仁": "9g", "甘草": "6g"},
    indications=["水气", "面目浮肿"],
    symptoms=["水气", "面目浮肿"],
    disease_mechanism="宣肺利水",
    formula_meaning="宣肺利水",
    keywords=["水气", "面目浮肿", "咳嗽"],
    source="《金匮要略》"
))
F.append(Formula(
    name="防己茯苓汤", six_meridian="杂病",
    composition={"防己": "9g", "黄芪": "9g", "桂枝": "9g", "茯苓": "18g", "甘草": "6g"},
    indications=["皮水", "四肢肿"],
    symptoms=["皮水", "四肢肿"],
    disease_mechanism="益气利水",
    formula_meaning="益气利水",
    keywords=["皮水", "四肢肿", "聂聂动"],
    source="《金匮要略》"
))
F.append(Formula(
    name="黄芪芍药桂枝苦酒汤", six_meridian="杂病",
    composition={"黄芪": "15g", "白芍": "9g", "桂枝": "9g", "苦酒": "适量"},
    indications=["黄汗", "身肿"],
    symptoms=["黄汗", "身肿"],
    disease_mechanism="益气调和营卫",
    formula_meaning="益气调和营卫",
    keywords=["黄汗", "身肿", "汗出沾衣"],
    source="《金匮要略》"
))
F.append(Formula(
    name="桂枝加黄芪汤", six_meridian="杂病",
    composition={"桂枝": "9g", "白芍": "9g", "甘草": "6g", "生姜": "9g", "大枣": "4枚", "黄芪": "6g"},
    indications=["黄汗", "身重"],
    symptoms=["黄汗", "身重"],
    disease_mechanism="调和营卫益气",
    formula_meaning="调和营卫益气",
    keywords=["黄汗", "身重", "汗出"],
    source="《金匮要略》"
))
F.append(Formula(
    name="茵陈五苓散", six_meridian="杂病",
    composition={"茵陈": "30g", "五苓散": "15g"},
    indications=["黄疸"],
    symptoms=["黄疸"],
    disease_mechanism="利湿退黄",
    formula_meaning="利湿退黄",
    keywords=["黄疸", "小便不利"],
    source="《金匮要略》"
))
F.append(Formula(
    name="大黄硝石汤", six_meridian="杂病",
    composition={"大黄": "12g", "黄柏": "12g", "芒硝": "12g", "栀子": "9g"},
    indications=["黄疸", "腹满"],
    symptoms=["黄疸", "腹满"],
    disease_mechanism="攻下清热退黄",
    formula_meaning="攻下清热退黄",
    keywords=["黄疸", "腹满", "小便不利"],
    source="《金匮要略》"
))
F.append(Formula(
    name="栀子大黄汤", six_meridian="杂病",
    composition={"栀子": "9g", "大黄": "3g", "枳实": "9g", "淡豆豉": "9g"},
    indications=["酒疸", "心中懊恼"],
    symptoms=["酒疸", "心中懊恼"],
    disease_mechanism="清心除烦",
    formula_meaning="清心除烦",
    keywords=["酒疸", "心中懊恼", "热痛"],
    source="《金匮要略》"
))
F.append(Formula(
    name="硝石矾石散", six_meridian="杂病",
    composition={"硝石": "等分", "矾石": "等分"},
    indications=["女劳疸"],
    symptoms=["女劳疸"],
    disease_mechanism="清热化湿",
    formula_meaning="清热化湿",
    keywords=["女劳疸", "额上黑", "微汗出"],
    source="《金匮要略》"
))
F.append(Formula(
    name="猪膏发煎", six_meridian="杂病",
    composition={"猪膏": "15g", "乱发": "9g"},
    indications=["黄疸", "便秘"],
    symptoms=["黄疸", "便秘"],
    disease_mechanism="润燥通便退黄",
    formula_meaning="润燥通便退黄",
    keywords=["黄疸", "便秘", "少腹急"],
    source="《金匮要略》"
))
F.append(Formula(
    name="桂枝去芍药加蜀漆牡蛎龙骨救逆汤", six_meridian="杂病",
    composition={"桂枝": "9g", "甘草": "6g", "生姜": "9g", "大枣": "4枚", "蜀漆": "9g", "牡蛎": "15g", "龙骨": "12g"},
    indications=["惊狂", "起卧不安"],
    symptoms=["惊狂", "起卧不安"],
    disease_mechanism="温阳镇惊安神",
    formula_meaning="温阳镇惊安神",
    keywords=["惊狂", "起卧不安", "火逆"],
    source="《金匮要略》"
))
F.append(Formula(
    name="半夏麻黄丸", six_meridian="杂病",
    composition={"半夏": "9g", "麻黄": "9g"},
    indications=["心下悸"],
    symptoms=["心下悸"],
    disease_mechanism="蠲饮降逆",
    formula_meaning="蠲饮降逆",
    keywords=["心下悸", "水饮内停"],
    source="《金匮要略》"
))
F.append(Formula(
    name="柏叶汤", six_meridian="杂病",
    composition={"侧柏叶": "15g", "干姜": "9g", "艾叶": "9g"},
    indications=["吐血", "虚寒"],
    symptoms=["吐血", "虚寒"],
    disease_mechanism="温中止血",
    formula_meaning="温中止血",
    keywords=["吐血", "虚寒", "面色苍白"],
    source="《金匮要略》"
))
F.append(Formula(
    name="黄土汤", six_meridian="杂病",
    composition={"甘草": "9g", "干地黄": "9g", "白术": "9g", "附子": "9g", "阿胶": "9g", "黄芩": "9g", "灶心黄土": "30g"},
    indications=["脾虚", "出血"],
    symptoms=["脾虚", "出血"],
    disease_mechanism="温阳健脾止血",
    formula_meaning="温阳健脾止血",
    keywords=["脾虚", "出血", "便血", "崩漏"],
    source="《金匮要略》"
))
F.append(Formula(
    name="泻心汤", six_meridian="杂病",
    composition={"大黄": "6g", "黄连": "3g", "黄芩": "3g"},
    indications=["吐血", "衄血", "热盛"],
    symptoms=["吐血", "衄血", "热盛"],
    disease_mechanism="泻火解毒",
    formula_meaning="泻火解毒",
    keywords=["吐血", "衄血", "热盛"],
    source="《金匮要略》"
))
F.append(Formula(
    name="补中益气汤", six_meridian="时方",
    composition={"黄芪": "15g", "甘草": "6g", "人参": "9g", "当归": "6g", "橘皮": "6g", "升麻": "3g", "柴胡": "3g", "白术": "9g"},
    indications=["脾胃气虚", "中气下陷"],
    symptoms=["脾胃气虚", "中气下陷"],
    disease_mechanism="补中益气升阳举陷",
    formula_meaning="补中益气升阳举陷",
    keywords=["脾胃气虚", "中气下陷", "气短", "乏力", "发热"],
    source="《脾胃论》"
))
F.append(Formula(
    name="归脾汤", six_meridian="时方",
    composition={"白术": "9g", "茯神": "9g", "黄芪": "12g", "龙眼肉": "12g", "酸枣仁": "12g", "人参": "6g", "木香": "3g", "甘草": "3g", "当归": "9g", "远志": "6g", "生姜": "3片", "大枣": "3枚"},
    indications=["心脾两虚", "失眠"],
    symptoms=["心脾两虚", "失眠"],
    disease_mechanism="益气补血健脾养心",
    formula_meaning="益气补血健脾养心",
    keywords=["心脾两虚", "失眠", "健忘", "心悸"],
    source="《济生方》"
))
F.append(Formula(
    name="六味地黄丸", six_meridian="时方",
    composition={"熟地黄": "24g", "山茱萸": "12g", "山药": "12g", "泽泻": "9g", "茯苓": "9g", "牡丹皮": "9g"},
    indications=["肾阴虚"],
    symptoms=["肾阴虚"],
    disease_mechanism="滋阴补肾",
    formula_meaning="滋阴补肾",
    keywords=["肾阴虚", "腰膝酸软", "头晕耳鸣"],
    source="《小儿药证直诀》"
))
F.append(Formula(
    name="天王补心丹", six_meridian="时方",
    composition={"生地黄": "30g", "人参": "6g", "丹参": "6g", "玄参": "6g", "茯苓": "6g", "五味子": "6g", "远志": "6g", "桔梗": "6g", "当归身": "9g", "天冬": "9g", "麦冬": "9g", "柏子仁": "9g", "酸枣仁": "9g"},
    indications=["心阴虚", "失眠"],
    symptoms=["心阴虚", "失眠"],
    disease_mechanism="滋阴养血补心安神",
    formula_meaning="滋阴养血补心安神",
    keywords=["心阴虚", "失眠", "心悸", "健忘"],
    source="《摄生秘剖》"
))
F.append(Formula(
    name="逍遥散", six_meridian="时方",
    composition={"柴胡": "9g", "当归": "9g", "白芍": "9g", "白术": "9g", "茯苓": "9g", "甘草": "3g", "薄荷": "3g", "生姜": "3片"},
    indications=["肝郁脾虚"],
    symptoms=["肝郁脾虚"],
    disease_mechanism="疏肝解郁健脾养血",
    formula_meaning="疏肝解郁健脾养血",
    keywords=["肝郁脾虚", "胁胀", "月经不调", "情志抑郁"],
    source="《太平惠民和剂局方》"
))
F.append(Formula(
    name="龙胆泻肝汤", six_meridian="时方",
    composition={"龙胆草": "6g", "黄芩": "9g", "栀子": "9g", "泽泻": "9g", "木通": "6g", "车前子": "9g", "当归": "3g", "生地黄": "9g", "柴胡": "6g", "甘草": "6g"},
    indications=["肝胆湿热"],
    symptoms=["肝胆湿热"],
    disease_mechanism="清肝胆实火利湿热",
    formula_meaning="清肝胆实火利湿热",
    keywords=["肝胆湿热", "口苦", "胁痛", "阴肿", "耳聋"],
    source="《医方集解》"
))
F.append(Formula(
    name="血府逐瘀汤", six_meridian="时方",
    composition={"桃仁": "12g", "红花": "9g", "当归": "9g", "生地黄": "9g", "川芎": "5g", "赤芍": "6g", "牛膝": "9g", "桔梗": "5g", "柴胡": "3g", "枳壳": "6g", "甘草": "3g"},
    indications=["胸中血瘀"],
    symptoms=["胸中血瘀"],
    disease_mechanism="活血化瘀行气止痛",
    formula_meaning="活血化瘀行气止痛",
    keywords=["胸中血瘀", "胸痛", "头痛", "日久不愈"],
    source="《医林改错》"
))
F.append(Formula(
    name="补阳还五汤", six_meridian="时方",
    composition={"黄芪": "120g", "当归尾": "6g", "赤芍": "5g", "地龙": "3g", "川芎": "3g", "红花": "3g", "桃仁": "3g"},
    indications=["中风", "半身不遂"],
    symptoms=["中风", "半身不遂"],
    disease_mechanism="补气活血通络",
    formula_meaning="补气活血通络",
    keywords=["中风", "半身不遂", "口眼歪斜"],
    source="《医林改错》"
))
F.append(Formula(
    name="温胆汤", six_meridian="时方",
    composition={"半夏": "9g", "竹茹": "9g", "枳实": "9g", "橘皮": "9g", "茯苓": "9g", "甘草": "3g", "生姜": "3片", "大枣": "3枚"},
    indications=["胆郁痰扰"],
    symptoms=["胆郁痰扰"],
    disease_mechanism="理气化痰清胆和胃",
    formula_meaning="理气化痰清胆和胃",
    keywords=["胆郁痰扰", "心烦不眠", "眩晕", "呕吐"],
    source="《三因极一病证方论》"
))
F.append(Formula(
    name="藿香正气散", six_meridian="时方",
    composition={"藿香": "9g", "紫苏": "3g", "白芷": "3g", "大腹皮": "3g", "茯苓": "3g", "白术": "6g", "半夏曲": "6g", "陈皮": "6g", "厚朴": "6g", "桔梗": "6g", "甘草": "6g", "生姜": "3片", "大枣": "1枚"},
    indications=["外感风寒", "内伤湿滞"],
    symptoms=["外感风寒", "内伤湿滞"],
    disease_mechanism="解表化湿理气和中",
    formula_meaning="解表化湿理气和中",
    keywords=["外感风寒", "内伤湿滞", "呕吐", "腹泻"],
    source="《太平惠民和剂局方》"
))
F.append(Formula(
    name="银翘散", six_meridian="时方",
    composition={"金银花": "9g", "连翘": "9g", "桔梗": "6g", "薄荷": "6g", "竹叶": "4g", "生甘草": "5g", "荆芥穗": "5g", "淡豆豉": "5g", "牛蒡子": "9g"},
    indications=["风热感冒"],
    symptoms=["风热感冒"],
    disease_mechanism="辛凉透表清热解毒",
    formula_meaning="辛凉透表清热解毒",
    keywords=["风热感冒", "发热", "咽痛"],
    source="《温病条辨》"
))
F.append(Formula(
    name="桑菊饮", six_meridian="时方",
    composition={"桑叶": "9g", "菊花": "9g", "杏仁": "6g", "连翘": "6g", "薄荷": "3g", "桔梗": "6g", "甘草": "3g", "芦根": "6g"},
    indications=["风温初起", "咳嗽"],
    symptoms=["风温初起", "咳嗽"],
    disease_mechanism="疏风清热宣肺止咳",
    formula_meaning="疏风清热宣肺止咳",
    keywords=["风温初起", "咳嗽", "身热不甚"],
    source="《温病条辨》"
))
F.append(Formula(
    name="二陈汤", six_meridian="时方",
    composition={"半夏": "9g", "橘红": "9g", "茯苓": "9g", "甘草": "3g", "生姜": "3片", "乌梅": "1个"},
    indications=["痰湿咳嗽"],
    symptoms=["痰湿咳嗽"],
    disease_mechanism="燥湿化痰理气和中",
    formula_meaning="燥湿化痰理气和中",
    keywords=["痰湿咳嗽", "痰多色白", "胸膈痞闷"],
    source="《太平惠民和剂局方》"
))
F.append(Formula(
    name="平胃散", six_meridian="时方",
    composition={"苍术": "9g", "厚朴": "6g", "陈皮": "6g", "甘草": "3g", "生姜": "2片", "大枣": "2枚"},
    indications=["湿滞脾胃"],
    symptoms=["湿滞脾胃"],
    disease_mechanism="燥湿运脾行气和胃",
    formula_meaning="燥湿运脾行气和胃",
    keywords=["湿滞脾胃", "脘腹胀满", "食少"],
    source="《太平惠民和剂局方》"
))
F.append(Formula(
    name="四物汤", six_meridian="时方",
    composition={"当归": "9g", "川芎": "6g", "白芍": "9g", "熟地黄": "12g"},
    indications=["血虚", "月经不调"],
    symptoms=["血虚", "月经不调"],
    disease_mechanism="补血调血",
    formula_meaning="补血调血",
    keywords=["血虚", "月经不调", "头晕心悸"],
    source="《仙授理伤续断秘方》"
))
F.append(Formula(
    name="四君子汤", six_meridian="时方",
    composition={"人参": "9g", "白术": "9g", "茯苓": "9g", "甘草": "6g"},
    indications=["脾胃气虚"],
    symptoms=["脾胃气虚"],
    disease_mechanism="益气健脾",
    formula_meaning="益气健脾",
    keywords=["脾胃气虚", "食少", "乏力", "面色萎白"],
    source="《太平惠民和剂局方》"
))
F.append(Formula(
    name="八珍汤", six_meridian="时方",
    composition={"人参": "9g", "白术": "9g", "茯苓": "9g", "甘草": "6g", "当归": "9g", "川芎": "6g", "白芍": "9g", "熟地黄": "12g", "生姜": "3片", "大枣": "3枚"},
    indications=["气血两虚"],
    symptoms=["气血两虚"],
    disease_mechanism="益气补血",
    formula_meaning="益气补血",
    keywords=["气血两虚", "面色苍白", "头晕心悸"],
    source="《正体类要》"
))
F.append(Formula(
    name="十全大补汤", six_meridian="时方",
    composition={"八珍汤": "原方", "黄芪": "12g", "肉桂": "3g"},
    indications=["气血两虚重证"],
    symptoms=["气血两虚重证"],
    disease_mechanism="温补气血",
    formula_meaning="温补气血",
    keywords=["气血两虚重证", "虚劳", "遗精"],
    source="《太平惠民和剂局方》"
))
F.append(Formula(
    name="六君子汤", six_meridian="时方",
    composition={"人参": "9g", "白术": "9g", "茯苓": "9g", "甘草": "6g", "半夏": "9g", "陈皮": "9g"},
    indications=["脾胃气虚", "痰湿"],
    symptoms=["脾胃气虚", "痰湿"],
    disease_mechanism="益气健脾燥湿化痰",
    formula_meaning="益气健脾燥湿化痰",
    keywords=["脾胃气虚", "痰湿", "食少", "咳嗽"],
    source="《医学正传》"
))
F.append(Formula(
    name="香砂六君子汤", six_meridian="时方",
    composition={"六君子汤": "原方", "木香": "6g", "砂仁": "6g"},
    indications=["脾胃气虚", "气滞"],
    symptoms=["脾胃气虚", "气滞"],
    disease_mechanism="益气健脾理气化痰",
    formula_meaning="益气健脾理气化痰",
    keywords=["脾胃气虚", "气滞", "脘腹胀痛"],
    source="《古今名医方论》"
))
F.append(Formula(
    name="生化汤", six_meridian="时方",
    composition={"当归": "24g", "川芎": "9g", "桃仁": "6g", "干姜": "2g", "甘草": "2g"},
    indications=["产后", "血虚寒凝"],
    symptoms=["产后", "血虚寒凝"],
    disease_mechanism="养血化瘀温经止痛",
    formula_meaning="养血化瘀温经止痛",
    keywords=["产后", "血虚寒凝", "恶露不行", "腹痛"],
    source="《傅青主女科》"
))
F.append(Formula(
    name="保和丸", six_meridian="时方",
    composition={"山楂": "18g", "神曲": "6g", "半夏": "9g", "茯苓": "9g", "陈皮": "3g", "连翘": "3g", "莱菔子": "3g"},
    indications=["食积"],
    symptoms=["食积"],
    disease_mechanism="消食和胃",
    formula_meaning="消食和胃",
    keywords=["食积", "脘腹胀满", "嗳腐吞酸"],
    source="《丹溪心法》"
))
F.append(Formula(
    name="越鞠丸", six_meridian="时方",
    composition={"香附": "9g", "川芎": "9g", "苍术": "9g", "栀子": "9g", "神曲": "9g"},
    indications=["郁证"],
    symptoms=["郁证"],
    disease_mechanism="行气解郁",
    formula_meaning="行气解郁",
    keywords=["郁证", "气郁", "血郁", "痰郁", "食郁", "湿郁", "火郁"],
    source="《丹溪心法》"
))
F.append(Formula(
    name="桃红四物汤", six_meridian="时方",
    composition={"四物汤": "原方", "桃仁": "9g", "红花": "6g"},
    indications=["血瘀", "月经不调"],
    symptoms=["血瘀", "月经不调"],
    disease_mechanism="养血活血",
    formula_meaning="养血活血",
    keywords=["血瘀", "月经不调", "痛经", "经色紫暗"],
    source="《医宗金鉴》"
))
F.append(Formula(
    name="柴胡疏肝散", six_meridian="时方",
    composition={"柴胡": "6g", "白芍": "9g", "枳壳": "6g", "香附": "6g", "川芎": "6g", "甘草": "3g"},
    indications=["肝气郁结"],
    symptoms=["肝气郁结"],
    disease_mechanism="疏肝理气活血止痛",
    formula_meaning="疏肝理气活血止痛",
    keywords=["肝气郁结", "胁肋疼痛", "善太息"],
    source="《景岳全书》"
))
F.append(Formula(
    name="天台乌药散", six_meridian="时方",
    composition={"天台乌药": "12g", "木香": "6g", "小茴香": "6g", "青皮": "6g", "高良姜": "9g", "槟榔": "9g", "川楝子": "12g", "巴豆": "适量"},
    indications=["寒凝肝脉", "疝痛"],
    symptoms=["寒凝肝脉", "疝痛"],
    disease_mechanism="行气疏肝散寒止痛",
    formula_meaning="行气疏肝散寒止痛",
    keywords=["寒凝肝脉", "疝痛", "少腹引控睾丸而痛"],
    source="《医学发明》"
))
F.append(Formula(
    name="暖肝煎", six_meridian="时方",
    composition={"当归": "6g", "枸杞子": "9g", "小茴香": "6g", "肉桂": "3g", "乌药": "6g", "沉香": "3g", "茯苓": "6g"},
    indications=["肝肾虚寒", "少腹冷痛"],
    symptoms=["肝肾虚寒", "少腹冷痛"],
    disease_mechanism="温补肝肾行气止痛",
    formula_meaning="温补肝肾行气止痛",
    keywords=["肝肾虚寒", "少腹冷痛", "疝气"],
    source="《景岳全书》"
))
F.append(Formula(
    name="苏子降气汤", six_meridian="时方",
    composition={"紫苏子": "9g", "半夏": "9g", "当归": "6g", "甘草": "6g", "前胡": "6g", "厚朴": "6g", "肉桂": "3g"},
    indications=["上实下虚", "喘咳"],
    symptoms=["上实下虚", "喘咳"],
    disease_mechanism="降气平喘祛痰止咳",
    formula_meaning="降气平喘祛痰止咳",
    keywords=["上实下虚", "喘咳", "痰涎壅盛"],
    source="《太平惠民和剂局方》"
))
F.append(Formula(
    name="定喘汤", six_meridian="时方",
    composition={"麻黄": "9g", "白果": "9g", "苏子": "6g", "甘草": "3g", "款冬花": "9g", "杏仁": "5g", "桑白皮": "9g", "黄芩": "5g", "半夏": "9g"},
    indications=["风寒外束", "痰热内蕴"],
    symptoms=["风寒外束", "痰热内蕴"],
    disease_mechanism="宣肺降气清热化痰",
    formula_meaning="宣肺降气清热化痰",
    keywords=["风寒外束", "痰热内蕴", "哮喘"],
    source="《摄生众妙方》"
))
F.append(Formula(
    name="葶苈大枣泻肺汤", six_meridian="杂病",
    composition={"葶苈子": "15g", "大枣": "4枚"},
    indications=["肺痈", "喘不得卧"],
    symptoms=["肺痈", "喘不得卧"],
    disease_mechanism="泻肺逐饮",
    formula_meaning="泻肺逐饮",
    keywords=["肺痈", "喘不得卧", "胸满"],
    source="《金匮要略》"
))
F.append(Formula(
    name="桔梗汤", six_meridian="少阴",
    composition={"甘草": "12g", "桔梗": "6g"},
    indications=["肺痈", "咳吐脓血"],
    symptoms=["肺痈", "咳吐脓血"],
    disease_mechanism="清热排脓",
    formula_meaning="清热排脓",
    keywords=["肺痈", "咳吐脓血"],
    source="《金匮要略》"
))
F.append(Formula(
    name="苇茎汤", six_meridian="杂病",
    composition={"苇茎": "30g", "薏苡仁": "30g", "桃仁": "9g", "冬瓜子": "15g"},
    indications=["肺痈", "咳吐脓血"],
    symptoms=["肺痈", "咳吐脓血"],
    disease_mechanism="清肺化痰逐瘀排脓",
    formula_meaning="清肺化痰逐瘀排脓",
    keywords=["肺痈", "咳吐脓血", "胸中甲错"],
    source="《备急千金要方》"
))
F.append(Formula(
    name="大黄牡丹皮汤", six_meridian="杂病",
    composition={"大黄": "12g", "牡丹皮": "9g", "桃仁": "12g", "冬瓜子": "30g", "芒硝": "9g"},
    indications=["肠痈", "少腹肿痞"],
    symptoms=["肠痈", "少腹肿痞"],
    disease_mechanism="泻热破瘀散结消肿",
    formula_meaning="泻热破瘀散结消肿",
    keywords=["肠痈", "少腹肿痞", "发热"],
    source="《金匮要略》"
))
F.append(Formula(
    name="薏苡附子败酱散", six_meridian="杂病",
    composition={"薏苡仁": "30g", "附子": "6g", "败酱草": "15g"},
    indications=["肠痈", "脓成"],
    symptoms=["肠痈", "脓成"],
    disease_mechanism="排脓消肿",
    formula_meaning="排脓消肿",
    keywords=["肠痈", "脓成", "身甲错"],
    source="《金匮要略》"
))
F.append(Formula(
    name="排脓散", six_meridian="杂病",
    composition={"枳实": "9g", "白芍": "9g", "桔梗": "3g"},
    indications=["肠痈", "排脓"],
    symptoms=["肠痈", "排脓"],
    disease_mechanism="排脓和血",
    formula_meaning="排脓和血",
    keywords=["肠痈", "排脓", "腹痛"],
    source="《金匮要略》"
))
F.append(Formula(
    name="排脓汤", six_meridian="杂病",
    composition={"甘草": "6g", "桔梗": "9g", "生姜": "3片", "大枣": "3枚"},
    indications=["肠痈", "排脓"],
    symptoms=["肠痈", "排脓"],
    disease_mechanism="排脓解毒",
    formula_meaning="排脓解毒",
    keywords=["肠痈", "排脓"],
    source="《金匮要略》"
))
F.append(Formula(
    name="乌梅丸", six_meridian="厥阴",
    composition={"乌梅": "30g", "细辛": "3g", "干姜": "9g", "黄连": "6g", "当归": "6g", "附子": "6g", "蜀椒": "3g", "桂枝": "6g", "人参": "6g", "黄柏": "6g"},
    indications=["蛔厥"],
    symptoms=["蛔厥"],
    disease_mechanism="安蛔止痛",
    formula_meaning="安蛔止痛",
    keywords=["蛔厥", "得食而呕", "时发时止"],
    source="《伤寒论》"
))
F.append(Formula(
    name="蜘蛛散", six_meridian="杂病",
    composition={"蜘蛛": "14枚", "桂枝": "3g"},
    indications=["阴狐疝"],
    symptoms=["阴狐疝"],
    disease_mechanism="辛温通利",
    formula_meaning="辛温通利",
    keywords=["阴狐疝", "偏有大小", "时时上下"],
    source="《金匮要略》"
))
F.append(Formula(
    name="藜芦甘草汤", six_meridian="杂病",
    composition={"藜芦": "9g", "甘草": "9g"},
    indications=["手指臂肿动"],
    symptoms=["手指臂肿动"],
    disease_mechanism="涌吐导痰",
    formula_meaning="涌吐导痰",
    keywords=["手指臂肿动", "身体瞤动"],
    source="《金匮要略》"
))
F.append(Formula(
    name="鸡屎白散", six_meridian="杂病",
    composition={"鸡屎白": "适量"},
    indications=["转筋"],
    symptoms=["转筋"],
    disease_mechanism="清热祛风",
    formula_meaning="清热祛风",
    keywords=["转筋", "臂脚直", "脉上下行"],
    source="《金匮要略》"
))
F.append(Formula(
    name="三物备急丸", six_meridian="杂病",
    composition={"大黄": "30g", "干姜": "30g", "巴豆": "30g"},
    indications=["心腹胀满", "猝痛"],
    symptoms=["心腹胀满", "猝痛"],
    disease_mechanism="攻下寒积",
    formula_meaning="攻下寒积",
    keywords=["心腹胀满", "猝痛", "面青口噤"],
    source="《金匮要略》"
))
F.append(Formula(
    name="九痛丸", six_meridian="杂病",
    composition={"附子": "9g", "巴豆": "3g", "干姜": "9g", "吴茱萸": "9g", "人参": "9g", "狼毒": "9g"},
    indications=["心痛", "积聚"],
    symptoms=["心痛", "积聚"],
    disease_mechanism="温通止痛",
    formula_meaning="温通止痛",
    keywords=["心痛", "积聚", "痰饮", "虫注"],
    source="《金匮要略》"
))
F.append(Formula(
    name="紫参汤", six_meridian="杂病",
    composition={"紫参": "15g", "甘草": "9g"},
    indications=["下利", "肺痛"],
    symptoms=["下利", "肺痛"],
    disease_mechanism="清热止利",
    formula_meaning="清热止利",
    keywords=["下利", "肺痛"],
    source="《金匮要略》"
))
F.append(Formula(
    name="诃梨勒散", six_meridian="杂病",
    composition={"诃子": "10枚"},
    indications=["气利"],
    symptoms=["气利"],
    disease_mechanism="涩肠止利",
    formula_meaning="涩肠止利",
    keywords=["气利", "下利滑脱"],
    source="《金匮要略》"
))

FORMULA_LIBRARY = F


class KnowledgeBase:
    def __init__(self):
        self.formulas = {f.name: f for f in FORMULA_LIBRARY}
        self.all_formulas = FORMULA_LIBRARY

    def get_all_formulas(self):
        return self.all_formulas

    def get_by_meridian(self, meridian):
        return [f for f in self.all_formulas if meridian in f.six_meridian]

    def search_by_symptoms(self, symptoms, top_k=5):
        results = []
        symptom_str = " ".join(symptoms).lower()
        for formula in self.all_formulas:
            score = 0
            for kw in formula.keywords:
                if kw.lower() in symptom_str:
                    score += 2
            for ind in formula.indications:
                if ind.lower() in symptom_str:
                    score += 1.5
            for sym in formula.symptoms:
                if sym.lower() in symptom_str:
                    score += 1
            if score > 0:
                results.append((formula, score))
        results.sort(key=lambda x: x[1], reverse=True)
        return results[:top_k]

    def get_count(self):
        return len(self.all_formulas)


knowledge_base = KnowledgeBase()
