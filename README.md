# TaskPilot AI

TaskPilot AI is a simple Slack bot that understands natural language task requests and parses them using LLM technology.

## 🚀 Features

- **Natural Language Parsing**: Understands task requests using OpenAI API
- **Slack Integration**: Sends parsed tasks to Slack (simulated)
- **Simple & Lightweight**: Focused on core functionality

## 🏗️ Architecture

- **LLM Parser**: Extracts structured task data from natural language
- **Slack Interface**: Handles user input and Slack integration

## 🛠️ Setup

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Optional: Configure OpenAI API** (for enhanced LLM parsing):
   ```bash
   export OPENAI_API_KEY="your_openai_api_key"
   ```

3. **Run the application:**
   ```bash
   python main.py
   ```

## 📖 Usage

```bash
python main.py
# Enter: "Remind Sarah to send the draft next Monday and summarize her reply"
```

## 🧠 Task Parsing

The system can parse various natural language formats:

- **"Remind [Name] to [task] [date] and [action]"**
- **"Ask [Name] to [task] [date]"**
- **"Tell [Name] to [task] [date]"**

**Example inputs:**
- "Remind Sarah to send the draft next Monday and summarize her reply"
- "Ask Alex to review Q3 numbers today and confirm completion"
- "Tell John to prepare the presentation for tomorrow"

## 🔧 Project Structure

```
TaskPilot AI/
├── main.py              # Entry point
├── llm_parser.py        # Natural language parsing (OpenAI + fallback)
├── slack_interface.py   # User input handling
├── requirements.txt    # Python dependencies
└── README.md          # This file
```

## 🎯 Current Status

✅ **Completed Features:**
- Natural language task parsing (OpenAI + fallback)
- Simple Slack integration simulation
- User input handling

🔄 **Ready for Enhancement:**
- Real Slack API integration
- Enhanced LLM parsing
- Task scheduling

## 🚀 Next Steps

1. **Add OpenAI API Key** for enhanced LLM parsing
2. **Integrate real Slack API** for actual messaging
3. **Add task scheduling** functionality

---

*Simple TaskPilot AI - LLM + Slack Bot* 