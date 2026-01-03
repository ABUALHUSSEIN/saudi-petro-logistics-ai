# 🚢 Saudi Petro-Logistics AI (SPLA)

SPLA is a sophisticated **Agentic AI** application built for the Saudi oil and gas market. It follows **Pattern 1** of the course requirements, integrating historical shipping data with real-time market insights.

## 🌟 Key Features
- **Intelligent Analysis:** Analyzes historical CSV shipping data for major Saudi ports (Jeddah, Yanbu, Jubail, Dammam).
- **Real-time Search:** Fetches live Brent crude oil prices and market news via **Tavily AI**.
- **Strategic Agent:** Uses a specialized **CrewAI** agent to synthesize data and provide cost-reduction recommendations.
- **Modern UI:** A creative dashboard built with **Streamlit**.

## 🏗️ Architecture (Pattern 1)
- **Brain:** Llama-3.3-70b (via Groq Cloud) - *Selected for high speed and stability.*
- **Orchestration:** CrewAI Framework.
- **Middleware:** FastMCP (wrapping logistical tools).
- **External API:** Tavily Search for live market data.

## 🚀 How to Run
1. **Clone the repository:**
   ```bash
   git clone [Your-Repo-Link]
   cd saudi-petro-logistics-ai
   
## 📂 Project Structure
app.py: The Streamlit dashboard interface.

agent.py: The CrewAI logic and agent configuration.

tools/: Custom tools for CSV analysis and web search.

data/: Sample historical shipping data.

SUBMISSION.md: Detailed project documentation for the course final.
   
   
