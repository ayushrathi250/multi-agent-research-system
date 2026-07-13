# ResearchMind 🔬 - Multi-Agent AI Research System

ResearchMind is an advanced, automated multi-agent AI system built with [LangChain](https://python.langchain.com/) and [Streamlit](https://streamlit.io/). It coordinates four specialized AI agents to autonomously search the web, scrape content, write comprehensive research reports, and critique its own work.

## 🚀 Features

The system operates through a sequential pipeline of four components:

1. **🔍 Search Agent:** Uses [Tavily API](https://tavily.com/) to gather recent, reliable, and detailed web information on the specified topic.
2. **📄 Reader Agent:** Selects the most relevant URL from the search results and scrapes deep content, filtering out noise like navbars and scripts.
3. **✍️ Writer Chain:** Synthesizes the gathered research and scraped content into a well-structured Markdown report, complete with Introduction, Key Findings, Conclusion, and Sources.
4. **🧐 Critic Chain:** Reviews the final report, providing a strict score out of 10, outlining strengths, identifying areas for improvement, and giving a concise final verdict.

ResearchMind provides both a **beautiful Streamlit Dashboard** for an interactive visual experience and a **CLI tool** for running research directly from your terminal.

## 🛠️ Tech Stack

- **LLM Engine:** Google Gemini (via `langchain-google-genai` using `gemini-2.5-flash`)
- **Orchestration:** LangChain
- **Web Search Tool:** Tavily Search API
- **Web Scraping:** BeautifulSoup & Requests
- **Frontend UI:** Streamlit

## 📦 Installation

1. **Clone the repository and navigate to the project directory** (if you haven't already):
   ```bash
   cd Multi-agent-research-system
   ```

2. **Create and activate a virtual environment (optional but recommended):**
   ```bash
   python -m venv .venv
   # On Windows
   .venv\Scripts\activate
   # On macOS/Linux
   source .venv/bin/activate
   ```

3. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up Environment Variables:**
   Create a `.env` file in the root directory and add your API keys:
   ```env
   GOOGLE_API_KEY=your_google_gemini_api_key_here
   TAVILY_API_KEY=your_tavily_api_key_here
   ```

## 🎮 Usage

### 1. Streamlit Web UI
Run the interactive dashboard with a beautiful dark mode and responsive components.
```bash
streamlit run app.py
```
*Wait for the server to start, and your browser will open to the ResearchMind application where you can enter any topic to begin research.*

### 2. Command Line Interface
Run the exact same pipeline directly in your terminal and view the logs in real-time.
```bash
python pipeline.py
```

## 📁 Project Structure

- `app.py`: The Streamlit web application frontend and interactive pipeline runner.
- `pipeline.py`: The standalone CLI script to run the agent sequence.
- `agents.py`: Contains the LangChain agent configurations for the Search, Reader, Writer, and Critic components.
- `tools.py`: Custom LangChain tool definitions, including the Tavily web search and BeautifulSoup URL scraper.
- `requirements.txt`: Project Python dependencies.
