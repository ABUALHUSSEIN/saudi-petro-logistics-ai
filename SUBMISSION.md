# Final Project Submission: Saudi Petro-Logistics AI (SPLA)
## Project Overview
This document outlines the development, architecture, and business value of the SPLA application as part of the Agentic AI course final project.
...
## 1. Name and Description
**Project Name:** Saudi Petro-Logistics AI (SPLA)  
**Description:** SPLA is an "Agentic AI" application designed to revolutionize logistics in the Saudi oil sector. It follows **Pattern 1** by placing an intelligent Agent (Logistics Strategist) in front of a RAG system (CSV data) and a real-time Search engine (Tavily). The app helps users analyze historical shipping costs while staying updated with global oil market trends.

## 2. Benefits to the End User
- **Natural Language Analysis:** Users can ask questions in Arabic or English to get deep insights without knowing data science.
- **Unified Insights:** Combines internal shipping records with live Brent crude prices automatically.
- **Efficiency:** Provides strategic reports in seconds that would otherwise take hours to compile manually.

## 3. Business Benefits
- **Cost Optimization:** Identifies expensive routes and suggests better shipping timings based on market fluctuations.
- **Operational Agility:** Enables logistics companies to react instantly to market changes (e.g., oil price drops/hikes).
- **Resource Allocation:** Frees up human analysts to focus on high-level strategy rather than data entry.

## 4. Technical Details & Architecture
- **Architecture (Pattern 1):**
  - **Frontend:** Streamlit Dashboard (Port 8501).
  - **Orchestrator:** **CrewAI** (Managing a specialized Logistics Strategist agent).
  - **LLM:** **Llama-3.3-70b (via Groq Cloud)** for high-speed, 70-billion parameter reasoning.
  - **Tools:**
    - `ShippingDataTool`: Custom Python tool for CSV data processing.
    - `MarketSearchTool`: Tavily-powered live search tool.

- **Tools/Techniques Tried but Discarded:**
  - **Google Gemini 1.5 Flash:** We initially implemented Gemini, but due to regional **API 404 NOT_FOUND errors** in the Codespaces environment, we successfully pivoted to **Groq/Llama 3.3**. This demonstrates our ability to adapt to infrastructure challenges and select the most stable LLM provider.
  - **LangChain Standard Agents:** Discarded in favor of **CrewAI** for better multi-tasking and role-playing capabilities.

## 5. Current Limitations and Drawbacks
- **Telemetry Errors:** Minor signal warnings in the terminal due to Streamlit’s multi-threaded environment (doesn't affect core logic).
- **Data Dependency:** The quality of insights depends directly on the historical CSV data provided.
- **API Limits:** Performance is subject to Groq and Tavily free-tier rate limits.

## 6. References and Citations
- CrewAI Framework: [https://docs.crewai.com/](https://docs.crewai.com/)
- Groq Cloud API: [https://console.groq.com/](https://console.groq.com/)
- Tavily AI Search: [https://tavily.com/](https://tavily.com/)
- Streamlit Documentation: [https://docs.streamlit.io/](https://docs.streamlit.io/)
