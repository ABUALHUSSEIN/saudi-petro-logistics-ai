import os
from crewai.tools import BaseTool
from tavily import TavilyClient

class MarketSearchTool(BaseTool):
    name: str = "Market_Search_Tool"
    description: str = "البحث في الإنترنت عن أسعار النفط الحالية وأخبار السوق اللوجستي السعودي."

    def _run(self, query: str) -> str:
        try:
            # استخدام مكتبة tavily مباشرة لضمان الاستقرار
            tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))
            response = tavily.search(query=query, search_depth="basic")
            return str(response)
        except Exception as e:
            return f"خطأ أثناء البحث: {str(e)}"