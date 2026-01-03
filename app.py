import streamlit as st
from agent import run_spla_analysis

# إعدادات الصفحة الاحترافية
st.set_page_config(page_title="SPLA Dashboard", page_icon="🚢", layout="wide")

# تصميم CSS مخصص لتحسين المظهر
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stButton>button { width: 100%; border-radius: 20px; background-color: #004b87; color: white; }
    .report-box { padding: 20px; border-radius: 15px; background-color: #ffffff; border-left: 5px solid #004b87; box-shadow: 2px 2px 10px rgba(0,0,0,0.1); }
    </style>
    """, unsafe_allow_html=True)

# الشريط الجانبي - معلومات الموديل والتقنيات
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/995/995260.png", width=100)
    st.title("System Info")
    st.success("✅ Model: Llama-3.3-70b (Groq)")
    st.info("✅ Tools: CSV Analyst + Tavily Search")
    st.warning("✅ Framework: CrewAI (Agentic)")
    st.write("---")
    st.markdown("### عن المشروع\nمشروع SPLA يهدف لربط بيانات الموانئ السعودية بحالة السوق العالمية لحظياً.")

# العنوان الرئيسي
st.markdown("<h1 style='text-align: center; color: #004b87;'>🚢 Saudi Petro-Logistics AI (SPLA)</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>الجيل القادم من التحليل اللوجستي المدعوم بالذكاء الاصطناعي الوكيل</p>", unsafe_allow_html=True)

# تقسيم الصفحة لأعمدة
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("📝 طلب تحليل جديد")
    query = st.text_area("ما هو سؤالك اللوجستي؟", placeholder="مثال: قارن تكاليفنا الحالية بأسعار برنت اليوم وكيف يمكننا التحسين؟", height=100)
    btn = st.button("إرسال للوكيل الذكي")

with col2:
    st.subheader("💡 اقتراحات")
    st.caption("• تحليل متوسط تكلفة برميل النفط في ميناء جدة")
    st.caption("• مقارنة إجمالي الشحنات بأسعار السوق الحالية")
    st.caption("• توصية لتقليل تكاليف الشحن في ميناء ينبع")

st.write("---")

# عرض النتائج
if btn:
    if query:
        with st.status("🎯 الوكيل الذكي يعمل...", expanded=True) as status:
            st.write("🔍 فحص بيانات الـ CSV الداخلية...")
            st.write("🌐 البحث عبر Tavily عن أسعار السوق...")
            st.write("🧠 صياغة التقرير الاستراتيجي عبر Llama 3.3...")
            response = run_spla_analysis(query)
            status.update(label="✅ تم اكتمال التحليل!", state="complete", expanded=False)
        
        st.markdown("### 📊 التقرير الاستراتيجي النهائي")
        st.markdown(f"<div class='report-box'>{response}</div>", unsafe_allow_html=True)
    else:
        st.warning("يرجى إدخال سؤال للبدء.")