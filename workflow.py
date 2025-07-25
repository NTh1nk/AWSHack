import uuid
from datetime import datetime, timedelta
import time
from snowflake_logger import log_task_to_snowflake

# In-memory task store (replace with Temporal in production)
task_store = {}

def start_task_workflow(parsed_task):
    """
    Start a task delegation workflow (simulating Temporal)
    """
    task_id = str(uuid.uuid4())
    
    print(f"[Workflow] Starting task delegation workflow: {task_id}")
    print(f"[Workflow] Scheduling task for {parsed_task['recipient']} on {parsed_task['due_date']}")
    print(f"[Workflow] Task: {parsed_task['task']}")
    
    # Create task record
    task_record = {
        "task_id": task_id,
        "creator": "CLI_User",  # In real app, this would be the Slack user
        "recipient": parsed_task['recipient'],
        "task": parsed_task['task'],
        "due_date": parsed_task['due_date'],
        "status": "scheduled",
        "response_required": parsed_task.get('response_required', False),
        "output_format": parsed_task.get('output', 'confirmation'),
        "created_at": datetime.now().isoformat(),
        "completed_at": None,
        "summary": None
    }
    
    # Store task
    task_store[task_id] = task_record
    
    # Log to Snowflake
    log_task_to_snowflake(task_record)
    
    # Simulate workflow execution
    if should_execute_now(parsed_task['due_date']):
        print("[Workflow] Executing task now (due date is in the past or near future)")
        result = execute_task(task_record)
    else:
        print(f"[Workflow] Task scheduled for future execution at {parsed_task['due_date']}")
        result = {"status": "scheduled", "task_id": task_id}
    
    return result

def should_execute_now(due_date_str):
    """
    Check if task should be executed now (for demo purposes)
    """
    try:
        due_date = datetime.fromisoformat(due_date_str.replace('Z', '+00:00'))
        # Execute if due date is in the past or within 1 minute
        return due_date <= datetime.now() + timedelta(minutes=1)
    except:
        return True  # Execute if date parsing fails

def execute_task(task_record):
    """
    Execute a scheduled task
    """
    task_id = task_record['task_id']
    
    print(f"[Workflow] Executing task {task_id}")
    print(f"[Workflow] Sending message to {task_record['recipient']}: '{task_record['task']}'")
    
    # Update status
    task_record['status'] = 'executing'
    task_store[task_id] = task_record
    
    # Simulate sending message and waiting for response
    if task_record['response_required']:
        print("[Workflow] Waiting for response (simulated)...")
        time.sleep(2)  # Simulate waiting
        
        # Generate mock response and summary
        mock_response = f"Mock response from {task_record['recipient']}: 'Task completed successfully'"
        summary = generate_summary(mock_response, task_record['output_format'])
        
        task_record['summary'] = summary
        task_record['status'] = 'completed'
        task_record['completed_at'] = datetime.now().isoformat()
        
        print(f"[Workflow] Response received: {mock_response}")
        print(f"[Workflow] Summary generated: {summary}")
    else:
        task_record['status'] = 'completed'
        task_record['completed_at'] = datetime.now().isoformat()
        print("[Workflow] Task completed (no response required)")
    
    # Update store and log
    task_store[task_id] = task_record
    log_task_to_snowflake(task_record)
    
    return {
        "status": "completed",
        "task_id": task_id,
        "summary": task_record.get('summary')
    }

def generate_summary(response, output_format):
    """
    Generate summary using LLM or simple template
    """
    if output_format == "summary":
        return f"Summary: {response} - Task was completed successfully and all requirements were met."
    elif output_format == "confirmation":
        return f"Confirmation: {response} - Task has been acknowledged and completed."
    else:
        return f"Response: {response}"

def get_all_tasks():
    """
    Get all tasks from the store
    """
    return list(task_store.values())

def get_task_by_id(task_id):
    """
    Get a specific task by ID
    """
    return task_store.get(task_id) 