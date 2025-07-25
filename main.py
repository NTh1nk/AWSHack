import sys
from llm_parser import parse_task
from workflow import start_task_workflow
from slack_interface import get_user_input
from dashboard import interactive_mode, display_dashboard

def run_single_task():
    """
    Run TaskPilot AI in single task mode
    """
    print("Welcome to TaskPilot AI (Single Task Mode)")
    print("="*50)
    
    raw_input = get_user_input()
    print(f"\n📝 Received: {raw_input}")
    
    print("\n🧠 Parsing task with LLM...")
    parsed = parse_task(raw_input)
    print(f"✅ Parsed: {parsed}")
    
    print("\n⚡ Starting Temporal workflow...")
    result = start_task_workflow(parsed)
    print(f"✅ Workflow result: {result}")
    
    print("\n📊 Task completed! Here's the current dashboard:")
    display_dashboard()

def main():
    """
    Main entry point for TaskPilot AI
    """
    if len(sys.argv) > 1:
        if sys.argv[1] == "interactive" or sys.argv[1] == "-i":
            interactive_mode()
        elif sys.argv[1] == "dashboard" or sys.argv[1] == "-d":
            display_dashboard()
        elif sys.argv[1] == "help" or sys.argv[1] == "-h":
            print("TaskPilot AI - Slack Delegation Bot")
            print("\nUsage:")
            print("  python main.py              - Run single task mode")
            print("  python main.py interactive  - Run interactive mode")
            print("  python main.py dashboard    - Show dashboard only")
            print("  python main.py help         - Show this help")
        else:
            print(f"Unknown argument: {sys.argv[1]}")
            print("Use 'python main.py help' for usage information")
    else:
        run_single_task()

if __name__ == "__main__":
    main() 