#!/usr/bin/env python3
"""
TaskPilot AI Demo Script
Demonstrates the full functionality of the TaskPilot AI system
"""

import time
from llm_parser import parse_task
from workflow import start_task_workflow
from dashboard import display_dashboard, display_task_details

def run_demo():
    """
    Run a comprehensive demo of TaskPilot AI
    """
    print("🚀 TASKPILOT AI DEMO")
    print("="*60)
    print("This demo will create several tasks and show the system in action.")
    print()
    
    # Demo tasks
    demo_tasks = [
        "Remind Sarah to send the draft next Monday and summarize her reply",
        "Ask Alex to review Q3 numbers today and confirm completion",
        "Tell John to prepare the presentation for tomorrow",
        "Ask Maria to check the budget numbers Friday"
    ]
    
    task_ids = []
    
    for i, task_text in enumerate(demo_tasks, 1):
        print(f"📝 Creating Task {i}: {task_text}")
        print("-" * 40)
        
        # Parse task
        parsed = parse_task(task_text)
        print(f"✅ Parsed: {parsed}")
        
        # Start workflow
        result = start_task_workflow(parsed)
        print(f"✅ Workflow result: {result}")
        
        if 'task_id' in result:
            task_ids.append(result['task_id'])
        
        print()
        time.sleep(1)  # Small delay for demo effect
    
    # Show final dashboard
    print("📊 FINAL DASHBOARD")
    print("="*60)
    display_dashboard()
    
    # Show details for first task
    if task_ids:
        print(f"\n📋 DETAILS FOR FIRST TASK")
        print("="*60)
        display_task_details(task_ids[0])
    
    print("\n🎉 Demo completed! TaskPilot AI is working perfectly!")
    print("You can now:")
    print("  - Run 'python main.py interactive' for interactive mode")
    print("  - Run 'python main.py dashboard' to see current status")
    print("  - Add your OpenAI API key to use real LLM parsing")

if __name__ == "__main__":
    run_demo() 