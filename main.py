import os
from llm_parser import parse_task
from slack_interface import get_user_input

def main():
    """
    Simple TaskPilot AI - LLM parsing and Slack bot integration
    """
    print("🤖 TaskPilot AI - Simple LLM + Slack Bot")
    print("="*50)
    
    # Get task from user
    raw_input = get_user_input()
    print(f"\n📝 Received: {raw_input}")
    
    # Parse with LLM
    print("\n🧠 Parsing task with LLM...")
    parsed = parse_task(raw_input)
    print(f"✅ Parsed: {parsed}")
    
    # Simulate sending to Slack
    print("\n📱 Sending to Slack (simulated)...")
    send_to_slack(parsed)
    
    print("\n✅ Task processed successfully!")

def send_to_slack(parsed_task):
    """
    Simulate sending parsed task to Slack
    """
    recipient = parsed_task['recipient']
    task = parsed_task['task']
    due_date = parsed_task['due_date']
    
    print(f"📤 Message to {recipient}:")
    print(f"   Task: {task}")
    print(f"   Due: {due_date}")
    
    if parsed_task.get('response_required'):
        print(f"   Response required: Yes")
        print(f"   Output format: {parsed_task.get('output', 'confirmation')}")

if __name__ == "__main__":
    main() 