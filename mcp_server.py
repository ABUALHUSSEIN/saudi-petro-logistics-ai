from fastmcp import FastMCP
from agent import run_spla_analysis

# إنشاء سيرفر MCP
mcp = FastMCP("Saudi_Petro_Logistics_AI")

@mcp.tool()
def analyze_logistics(query: str) -> str:
    """أداة لتحليل لوجستيات النفط السعودي باستخدام وكيل ذكي"""
    return str(run_spla_analysis(query))

if __name__ == "__main__":
    mcp.run()