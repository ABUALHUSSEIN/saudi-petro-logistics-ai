import streamlit as st
from agent import run_spla_analysis

st.set_page_config(page_title="SPLA AI Dashboard", layout="wide")

st.title("🚢 Saudi Petro-Logistics AI (SPLA)")
st.subheader("تحليل بيانات الشحن + بحث Tavily اللحظي")

query = st.text_input("اسأل عن تكاليف الشحن أو أسعار النفط اللحظية:", 
                     placeholder="مثال: قارن تكلفة ميناء جدة بأسعار النفط الحالية")

if st.button("بدء التحليل الاستراتيجي"):
    if query:
        with st.spinner("جاري قراءة البيانات والبحث في الإنترنت..."):
            result = run_spla_analysis(query)
            st.markdown("### 📋 التقرير النهائي:")
            st.success(result)
    else:
        st.warning("يرجى إدخال استفسار.")

st.sidebar.markdown("""
### الأدوات المستخدمة:
- **CSV Data**: بيانات شحن تاريخية.
- **Tavily Search**: أسعار النفط الحالية.
- **Gemini 1.5**: العقل المفكر.
""")