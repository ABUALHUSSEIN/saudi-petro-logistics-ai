import pandas as pd
from crewai.tools import BaseTool

class ShippingDataTool(BaseTool):
    name: str = "Shipping_Data_Analyst"
    description: str = "تحليل بيانات شحن النفط من ملف CSV وتقديم إحصائيات حول الموانئ والكميات والتكاليف."

    def _run(self, query: str) -> str:
        try:
            # قراءة البيانات
            df = pd.read_csv("data/shipping_data.csv")
            
            # حساب ملخص سريع للبيانات
            summary = {
                "إجمالي البراميل المشحونة": int(df['Quantity_Barrels'].sum()),
                "متوسط تكلفة البرميل": round(float(df['Cost_Per_Barrel'].mean()), 2),
                "الموانئ المشمولة": df['Port'].unique().tolist(),
                "عدد العمليات المسجلة": len(df)
            }
            return f"ملخص البيانات المستخرج من الملف: {summary}"
        except Exception as e:
            return f"خطأ في قراءة الملف: {str(e)}"