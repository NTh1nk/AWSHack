from datetime import datetime
from workflow import get_all_tasks
from snowflake_logger import query_tasks_from_snowflake, get_task_statistics

def display_dashboard():
    """
    Display the TaskPilot AI dashboard
    """
    print("\n" + "="*60)
    print("🚀 TASKPILOT AI DASHBOARD")
    print("="*60)
    
    # Get statistics
    stats = get_task_statistics()
    
    # Display statistics
    print(f"\n📊 TASK STATISTICS:")
    print(f"   Total Tasks: {stats['total']}")
    print(f"   Completed: {stats['completed']}")
    print(f"   Pending: {stats['pending']}")
    print(f"   Completion Rate: {stats['completion_rate']:.1f}%")
    
    # Display recent tasks
    print(f"\n📋 RECENT TASKS:")
    tasks = query_tasks_from_snowflake()
    
    if not tasks:
        print("   No tasks found.")
    else:
        # Show last 5 tasks
        recent_tasks = tasks[-5:]
        for task in recent_tasks:
            status_emoji = {
                "scheduled": "⏰",
                "executing": "🔄", 
                "completed": "✅",
                "failed": "❌"
            }.get(task["status"], "❓")
            
            print(f"   {status_emoji} {task['recipient']}: {task['task'][:50]}...")
            print(f"      Status: {task['status']} | Due: {format_date(task['due_date'])}")
            if task.get('summary'):
                print(f"      Summary: {task['summary'][:60]}...")
            print()

def display_task_details(task_id):
    """
    Display detailed information about a specific task
    """
    tasks = query_tasks_from_snowflake()
    task = next((t for t in tasks if t["id"] == task_id), None)
    
    if not task:
        print(f"❌ Task {task_id} not found.")
        return
    
    print(f"\n📋 TASK DETAILS:")
    print(f"   ID: {task['id']}")
    print(f"   Creator: {task['creator']}")
    print(f"   Recipient: {task['recipient']}")
    print(f"   Task: {task['task']}")
    print(f"   Status: {task['status']}")
    print(f"   Due Date: {format_date(task['due_date'])}")
    print(f"   Created: {format_date(task['created_at'])}")
    if task.get('completed_at'):
        print(f"   Completed: {format_date(task['completed_at'])}")
    if task.get('summary'):
        print(f"   Summary: {task['summary']}")

def display_help():
    """
    Display help information
    """
    print("\n" + "="*60)
    print("❓ TASKPILOT AI HELP")
    print("="*60)
    print("\nAvailable commands:")
    print("  dashboard    - Show task statistics and recent tasks")
    print("  tasks        - List all tasks")
    print("  task <id>    - Show details for a specific task")
    print("  help         - Show this help message")
    print("  quit         - Exit the application")
    print("\nExample task inputs:")
    print("  'Remind Sarah to send the draft next Monday and summarize her reply'")
    print("  'Ask Alex to review Q3 numbers Friday'")
    print("  'Tell John to confirm the meeting tomorrow'")

def format_date(date_str):
    """
    Format date string for display
    """
    try:
        dt = datetime.fromisoformat(date_str.replace('Z', '+00:00'))
        return dt.strftime("%Y-%m-%d %H:%M")
    except:
        return date_str

def interactive_mode():
    """
    Run TaskPilot AI in interactive mode
    """
    print("Welcome to TaskPilot AI Interactive Mode!")
    print("Type 'help' for available commands.")
    
    while True:
        try:
            command = input("\nTaskPilot> ").strip().lower()
            
            if command == "quit" or command == "exit":
                print("Goodbye! 👋")
                break
            elif command == "help":
                display_help()
            elif command == "dashboard":
                display_dashboard()
            elif command == "tasks":
                tasks = query_tasks_from_snowflake()
                if tasks:
                    print(f"\n📋 ALL TASKS ({len(tasks)}):")
                    for task in tasks:
                        status_emoji = {
                            "scheduled": "⏰",
                            "executing": "🔄", 
                            "completed": "✅",
                            "failed": "❌"
                        }.get(task["status"], "❓")
                        print(f"   {status_emoji} {task['id'][:8]}... | {task['recipient']}: {task['task'][:40]}...")
                else:
                    print("No tasks found.")
            elif command.startswith("task "):
                task_id = command[5:].strip()
                display_task_details(task_id)
            elif command:
                print("Unknown command. Type 'help' for available commands.")
                
        except KeyboardInterrupt:
            print("\nGoodbye! 👋")
            break
        except Exception as e:
            print(f"Error: {e}") 