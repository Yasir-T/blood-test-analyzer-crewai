
# Blood Test Report Analyzer - CrewAI Debug Challenge ✅

## 🚀 Project Overview:
This is a FastAPI-based blood test analysis system built using CrewAI and Langchain.  
It processes PDF blood reports and generates fun, over-the-top medical, nutrition, and fitness recommendations.

## ✅ Bugs Found and Fixes Applied:

 Bug Fix 
| ❌ LLM was not initialized (llm = llm error)   | 	✅ Properly initialized `llm` using `ChatOpenAI()` |
| ❌ `PDFLoader` import missing in `tools.py`  | 	✅ Added: `from langchain_community.document_loaders import PDFLoader` |
| ❌ Used `tool=` instead of `tools=` in Agent definitions | ✅ Corrected to `tools=[...]` |
| ❌ Class methods in `tools.py` missing `self` | ✅ Added `self` and made methods non-async |
| ❌ Duplicate `ExerciseTool` class | ✅ Removed duplicate definition |
| ❌ Wrong requirement filename in README (`requirement.txt`) | ✅ Corrected to `requirements.txt` |
| ❌ crew.kickoff inputs missing file path | ✅ Passed both `query` and `file_path` in `kickoff(inputs={...})` |
| ❌ Minor code cleanup | ✅ Fixed indentation, improved error handling |

## ✅ How to Set Up and Run Locally:

 1. Clone the Repository:
```bash
git clone <https://github.com/Yasir-T/blood-test-analyzer-crewai>
cd <blood-test-analyzer-crewai>
```

### 2. Create Virtual Environment (Optional but Recommended):
```bash
python -m venv venv
source venv/bin/activate  # (Linux/macOS)
# OR
venv\Scripts\activate  # (Windows)
```

### 3. Install Required Packages:
```bash
pip install -r requirements.txt
```

### 4. Setup OpenAI API Key (Environment Variable):
Create a `.env` file in project root:

```
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxx
```

### 5. Run the FastAPI Application:
```bash
uvicorn main:app --reload
```

Visit Swagger UI:  
http://127.0.0.1:8000/docs




## ✅ Features:
- Reads blood test PDF  
- Generates fictional, humorous, medical, nutrition, and fitness suggestions  
- Uses CrewAI agents and tasks  
- Can extend with database or queue worker (Bonus if time allows)  

## ✅ Bonus Ideas (Optional Extensions):
- Add Redis Queue + Celery for async request handling  
- Integrate SQLite/PostgreSQL for storing user analysis history  
- Implement real nutrition and exercise logic  
- Add more agents (Mental Health Advisor, Lifestyle Coach)

## ✅ Project Directory Structure:

```
├── agents.py
├── tools.py
├── task.py
├── main.py
├── requirements.txt
 |----Readme.txt
├── .env
└── data/
```

## ✅ Contact:
YASIR TIMBROO
Email: yasirtimbroo@example.com
LinkedIn: https://www.linkedin.com/in/yasir-timbroo-b4b176238/
GitHub: https://github.com/Yasir-T
