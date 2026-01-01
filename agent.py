
import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, Process
from langchain_google_genai import ChatGoogleGenerativeAI
from tools.logistics_tools import ShippingDataTool
from tools.search_tool import MarketSearchTool # استيراد الكلاس الجديد

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

os.environ["GOOGLE_API_KEY"] = api_key
os.environ["OPENAI_API_KEY"] = "NA"

llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=api_key)

def run_spla_analysis(user_query):
    # تهيئة الأدوات
    data_tool = ShippingDataTool()
    search_tool = MarketSearchTool() # استخدام الكلاس المستقر

    analyst_agent = Agent(
        role='محلل لوجستيات النفط السعودي',
        goal='دمج بيانات الشحن من الملف مع أسعار النفط الحالية من الإنترنت لتقديم نصيحة دقيقة.',
        backstory='أنت خبير لوجستي سعودي محترف، تستخدم الأرقام التاريخية والبحث الحي لتقديم تقارير استراتيجية.',
        tools=[data_tool, search_tool],
        llm=llm,
        verbose=True,
        allow_delegation=False
    )

    analysis_task = Task(
        description=f"أجب على سؤال المستخدم: {user_query}. ابحث في الإنترنت للحصول على أسعار النفط الحالية إذا لزم الأمر وقارنها بالبيانات.",
        agent=analyst_agent,
        expected_output="تقرير شامل يدمج الأرقام التاريخية مع حالة السوق الحالية باللغة العربية."
    )

    crew = Crew(
        agents=[analyst_agent],
        tasks=[analysis_task],
        process=Process.sequential,
        embedder={
            "provider": "google-generativeai",
            "config": {"model": "models/embedding-001", "api_key": api_key}
        }
    )

    try:
        return str(crew.kickoff())
    except Exception as e:
        # خطة بديلة لضمان ظهور إجابة دائماً
        response = llm.invoke(f"بصفتك خبير، أجب باختصار على: {user_query}")
        return f"{response.content}\n\n(ملاحظة: إجابة مباشرة من المحرك)"