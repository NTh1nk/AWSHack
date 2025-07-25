# TaskPilot AI

TaskPilot AI is a Slack delegation bot that understands natural language task requests, delegates them using a Temporal workflow, and logs all task data in Snowflake. It uses an LLM to parse and classify user intent.

## 🚀 Features

- **Natural Language Parsing**: Understands task requests like "Remind Sarah to send the draft next Monday and summarize her reply"
- **Temporal Workflow Simulation**: Orchestrates task delegation with scheduling and execution
- **Snowflake Integration**: Logs all tasks and results (simulated)
- **Interactive Dashboard**: View task statistics and manage tasks
- **Multiple Modes**: Single task, interactive, and demo modes
- **LLM Integration**: OpenAI API support with fallback to pattern matching

## 🏗️ Architecture

- **Slack/Console Interface**: Accepts user task requests
- **LLM Parser**: Extracts structured task data from natural language
- **Temporal Workflow**: Orchestrates task delegation and response
- **Snowflake Logger**: Stores and queries all task data
- **Dashboard**: Real-time task monitoring and management

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
   # Single task mode
   python main.py
   
   # Interactive mode
   python main.py interactive
   
   # Dashboard only
   python main.py dashboard
   
   # Demo mode
   python demo.py
   ```

## 📖 Usage Examples

### Single Task Mode
```bash
python main.py
# Enter: "Remind Sarah to send the draft next Monday and summarize her reply"
```

### Interactive Mode
```bash
python main.py interactive
# Available commands: dashboard, tasks, task <id>, help, quit
```

### Demo Mode
```bash
python demo.py
# Creates multiple sample tasks and shows full system functionality
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

## 📊 Dashboard Features

- **Task Statistics**: Total, completed, pending tasks with completion rate
- **Recent Tasks**: Last 5 tasks with status indicators
- **Task Details**: Full information for any specific task
- **Real-time Updates**: Live status tracking

## 🔧 Project Structure

```
TaskPilot AI/
├── main.py              # Entry point with multiple modes
├── llm_parser.py        # Natural language parsing (OpenAI + fallback)
├── workflow.py          # Temporal workflow simulation
├── snowflake_logger.py  # Database logging (simulated)
├── dashboard.py         # Task monitoring and management
├── slack_interface.py   # User input handling
├── demo.py             # Comprehensive demo script
├── requirements.txt    # Python dependencies
└── README.md          # This file
```

## 🎯 Current Status

✅ **Completed Features:**
- Natural language task parsing (stub + OpenAI)
- Temporal workflow simulation
- Snowflake database logging (simulated)
- Interactive dashboard
- Multiple execution modes
- Task scheduling and execution
- Response handling and summarization
- Comprehensive demo

🔄 **Ready for Production Integration:**
- Replace stubs with real Temporal workflows
- Connect to actual Snowflake database
- Integrate with Slack API
- Add authentication and user management

## 🚀 Next Steps

1. **Add OpenAI API Key** for enhanced LLM parsing
2. **Deploy Temporal Server** for real workflow orchestration
3. **Configure Snowflake** for production data storage
4. **Integrate Slack API** for real-time messaging
5. **Add Web UI** for better user experience

## 🧪 Testing

The system includes comprehensive testing through the demo script:

```bash
python demo.py
```

This creates multiple tasks with different scenarios and shows the full end-to-end workflow.

---

*Built for AWS Hackathon 2025 - TaskPilot AI Delegation Bot* 