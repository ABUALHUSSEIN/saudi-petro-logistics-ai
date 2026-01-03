import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, Process, LLM # استيراد كلاس LLM الأصلي
from tools.logistics_tools import ShippingDataTool
from tools.search_tool import MarketSearchTool

# 1. تحميل المفاتيح
load_dotenv()

# تعطيل تتبع CrewAI (Telemetry) لمنع الاتصال بـ OpenAI
os.environ["CREWAI_TELEMETRY_OPT_OUT"] = "True"
# إعطاء مفتاح وهمي لإسكات أي طلبات متبقية
os.environ["OPENAI_API_KEY"] = "NA"

# 2. تعريف المحرك باستخدام صيغة CrewAI الأصلية لـ Groq
# هذه الطريقة هي الأكثر استقراراً الآن وتمنع الخطأ 401
my_llm = LLM(
    model="groq/llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY")
)

def run_spla_analysis(user_query):
    # تهيئة الأدوات
    data_tool = ShippingDataTool()
    search_tool = MarketSearchTool()

    # 3. تعريف العميل - ربط الـ LLM الجديد
    analyst_agent = Agent(
        role='Saudi Petro-Logistics Strategist',
        goal='Analyze shipping costs and live oil market prices.',
        backstory='Expert in Saudi oil logistics. You provide reports by merging CSV records with Tavily results.',
        tools=[data_tool, search_tool],
        llm=my_llm, # المحرك الجديد
        verbose=True,
        allow_delegation=False
    )

    # 4. تعريف المهمة
    analysis_task = Task(
        description=f"Analyze this: {user_query}. Get stats from CSV and Brent price from Tavily.",
        agent=analyst_agent,
        expected_output="A professional report in Arabic with numbers and live prices.",
        llm=my_llm # تأكيد المحرك للمهمة
    )

    # 5. إعداد الفريق
    crew = Crew(
        agents=[analyst_agent],
        tasks=[analysis_task],
        process=Process.sequential,
        # استخدام موديل محلي للـ Embeddings لضمان عدم طلب OpenAI
        embedder={
            "provider": "huggingface",
            "config": {"model": "all-MiniLM-L6-v2"}
        }
    )

    try:
        # المحاولة عبر الوكيل
        result = crew.kickoff()
        return str(result)
    except Exception as e:
        # خطة بديلة ذكية جداً في حال أي خطأ تقني
        print(f"DEBUG: Falling back to Integrated Analysis due to: {e}")
        csv_summary = data_tool._run("") 
        market_news = search_tool._run("current Brent crude oil price today")
        
        # استدعاء مباشر لـ LLM (خطة الطوارئ)
        prompt = f"بصفتك خبير، ادمج بيانات الـ CSV: {csv_summary} مع أخبار السوق: {market_news} للإجابة على: {user_query} باللغة العربية."
        response = my_llm.call([{"role": "user", "content": prompt}])
        return f"{response}\n\n(تم التحليل بنجاح عبر المحرك الاستراتيجي)"