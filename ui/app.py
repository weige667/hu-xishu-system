"""Streamlit 主界面"""
import sys
from pathlib import Path
ROOT = Path(__file__).parent.parent.resolve()
sys.path.insert(0, str(ROOT))

import streamlit as st
from core.engine import diagnosis_engine
from core.knowledge import knowledge_base
from core.config import settings, ensure_dirs

st.set_page_config(page_title="胡希恕经方辨证系统", page_icon="🌿", layout="wide")
ensure_dirs()

if "messages" not in st.session_state:
    st.session_state.messages = []
if "consultation_history" not in st.session_state:
    st.session_state.consultation_history = []
if "current_diagnosis" not in st.session_state:
    st.session_state.current_diagnosis = None

st.markdown("<h1 style='text-align:center;color:#2c5e3f;'>🌿 胡希恕经方辨证系统</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;color:#666;'>六经辨证 · 方证对应 · 模拟胡希恕先生辨证思路</p>", unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["🩺 辨证问诊", "📚 方剂库", "📖 辨证体系"])

with tab1:
    st.markdown("### 🩺 模拟胡希恕先生辨证问诊")
    mode = st.radio("选择问诊模式", ["💬 多轮问诊", "⚡ 快速辨证", "📝 完整病历"], horizontal=True)

    if mode == "💬 多轮问诊":
        st.info("模仿胡希恕先生问诊风格，逐步抓主症、辨六经、定方证")
        for msg in st.session_state.messages:
            with st.chat_message(msg["role"]):
                st.markdown(msg["content"])

        if prompt := st.chat_input("请描述您的主要不适..."):
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.spinner("胡希恕先生正在辨证..."):
                consultation = diagnosis_engine.consult_step(st.session_state.consultation_history, prompt)
                st.session_state.consultation_history.append({"role": "user", "content": prompt})
                if consultation["type"] == "diagnosis":
                    result = consultation["final_diagnosis"]
                    st.session_state.current_diagnosis = result
                    f = result.primary_formula
                    response = f"🩺 **辨证结论**\n\n【六经】{result.meridian}\n【方证】{f.name}\n\n【处方】\n"
                    for k, v in f.composition.items():
                        response += f"- {k}: {v}\n"
                    response += f"\n【病机】{f.disease_mechanism}\n【方义】{f.formula_meaning}"
                else:
                    response = f"🤔 **胡希恕先生**: {consultation['next_question']}"
                st.session_state.consultation_history.append({"role": "assistant", "content": response})
            st.rerun()

        if st.session_state.current_diagnosis:
            st.markdown("---")
            display_result(st.session_state.current_diagnosis)

    elif mode == "⚡ 快速辨证":
        templates = {
            "风寒感冒": "发热恶寒，无汗，头痛，身痛，脉浮紧",
            "风热感冒": "发热，微恶风，汗出，咽痛，口渴",
            "少阳感冒": "寒热往来，口苦咽干，胸胁苦满",
            "胃炎": "胃脘胀满，嗳气，反酸，食欲不振",
            "失眠": "失眠多梦，心烦易怒，口苦",
        }
        col1, col2 = st.columns([3, 1])
        with col1:
            symptoms_text = st.text_area("请详细描述症状", height=200,
                placeholder="例如：发热3天，体温38.5度，怕冷，无汗，头痛...")
        with col2:
            st.markdown("**快速模板**")
            for name, tpl in templates.items():
                if st.button(name, key=f"tpl_{name}"):
                    st.session_state.quick_text = tpl
            if "quick_text" in st.session_state:
                symptoms_text = st.session_state.quick_text

        if st.button("🎯 开始辨证", type="primary"):
            if symptoms_text:
                with st.spinner("辨证中..."):
                    result = diagnosis_engine.diagnose(symptoms_text)
                    st.session_state.current_diagnosis = result
                display_result(result)

    elif mode == "📝 完整病历":
        with st.form("complete_form"):
            col1, col2 = st.columns(2)
            with col1:
                chief = st.text_input("主诉", placeholder="如：胃脘胀痛3天")
                fever = st.text_input("寒热")
                sweat = st.text_input("汗出")
                head = st.text_input("头身")
                mouth = st.text_input("口咽")
            with col2:
                chest = st.text_input("胸腹")
                stool = st.text_input("大便")
                urine = st.text_input("小便")
                sleep = st.text_input("睡眠")
                tongue_pulse = st.text_input("舌脉")
            if st.form_submit_button("🎯 辨证"):
                full = " ".join([chief, fever, sweat, head, mouth, chest, stool, urine, sleep, tongue_pulse])
                if full.strip():
                    with st.spinner("辨证中..."):
                        result = diagnosis_engine.diagnose(full)
                    display_result(result)

    if st.button("🔄 重新开始"):
        st.session_state.messages = []
        st.session_state.consultation_history = []
        st.session_state.current_diagnosis = None
        st.rerun()

with tab2:
    st.markdown("### 📚 胡希恕常用方剂库")
    meridian_filter = st.multiselect("按六经筛选", ["太阳", "阳明", "少阳", "太阴", "少阴", "厥阴"], default=[])
    formulas = knowledge_base.get_all_formulas()
    if meridian_filter:
        formulas = [f for f in formulas if any(m in f.six_meridian for m in meridian_filter)]
    st.markdown(f"**共 {len(formulas)} 首方剂**")
    for f in formulas:
        with st.expander(f"🌿 {f.name}（{f.six_meridian}）"):
            col1, col2 = st.columns(2)
            with col1:
                st.markdown("**【组成】**")
                for k, v in f.composition.items():
                    st.markdown(f"- {k}: {v}")
                st.markdown(f"**【主症】** {'、'.join(f.indications)}")
            with col2:
                st.markdown(f"**【病机】** {f.disease_mechanism}")
                st.markdown(f"**【方义】** {f.formula_meaning}")
            if f.cases:
                st.markdown(f"**【适用】** {'、'.join(f.cases)}")

with tab3:
    st.markdown("### 📖 胡希恕辨证体系")
    st.markdown("""
**核心理念**：方证对应

**辨证步骤**：
1. **抓主症** - 找最突出症状
2. **辨六经** - 太阳/阳明/少阳/太阴/少阴/厥阴
3. **定方证** - 匹配方剂
4. **参体质** - 桂枝/麻黄/柴胡/附子体质

**学术特色**：
- 方证对应为核心
- 重视腹诊
- 痰、瘀、水三大病理产物
- 不拘病名，按方证用药
""")


def display_result(result):
    if not result.primary_formula:
        st.warning(f"⚠️ {result.formula_reasoning}")
        return
    f = result.primary_formula
    st.markdown(f"**辨证置信度**: {result.confidence*100:.1f}%")
    st.progress(min(result.confidence, 1.0))
    st.markdown(f"### 📋 处方：{f.name}")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**【组成】**")
        for k, v in f.composition.items():
            st.markdown(f"- **{k}**: {v}")
    with col2:
        st.markdown(f"**【出处】** {f.source}")
        st.markdown(f"**【体质】** {f.constitution}")
    with st.expander("🔍 详细辨证思路", expanded=True):
        st.markdown(result.meridian_reasoning)
        st.markdown("---")
        st.markdown(result.formula_reasoning)
    st.markdown(f"**病机**：{f.disease_mechanism}")
    st.markdown(f"**方义**：{f.formula_meaning}")
    if result.secondary_formulas:
        st.markdown("### 🔄 备选方剂")
        for s in result.secondary_formulas[:3]:
            st.markdown(f"- **{s.name}**（{s.six_meridian}）— {', '.join(s.indications[:3])}")
    st.info(result.treatment_advice)
