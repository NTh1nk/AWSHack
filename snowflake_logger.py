import os
from datetime import datetime

# In-memory database simulation (replace with real Snowflake in production)
snowflake_data = []

def log_task_to_snowflake(task_data):
    """
    Log task data to Snowflake (simulated)
    """
    try:
        # Simulate database connection
        print(f"[Snowflake] Connecting to database...")
        
        # Create database record
        record = {
            "id": task_data.get("task_id", "unknown"),
            "creator": task_data.get("creator", "unknown"),
            "recipient": task_data.get("recipient", "unknown"),
            "task": task_data.get("task", "unknown"),
            "due_date": task_data.get("due_date", datetime.now().isoformat()),
            "status": task_data.get("status", "unknown"),
            "response": task_data.get("summary", ""),
            "summary": task_data.get("summary", ""),
            "created_at": task_data.get("created_at", datetime.now().isoformat()),
            "completed_at": task_data.get("completed_at", "")
        }
        
        # Add to in-memory database
        snowflake_data.append(record)
        
        print(f"[Snowflake] Successfully logged task {record['id']}")
        print(f"[Snowflake] Status: {record['status']}")
        
        return {"status": "logged", "task_id": record['id']}
        
    except Exception as e:
        print(f"[Snowflake] Error logging task: {e}")
        return {"status": "error", "error": str(e)}

def query_tasks_from_snowflake(filters=None):
    """
    Query tasks from Snowflake (simulated)
    """
    try:
        print("[Snowflake] Querying tasks from database...")
        
        # Apply filters if provided
        results = snowflake_data.copy()
        
        if filters:
            if filters.get("status"):
                results = [r for r in results if r["status"] == filters["status"]]
            if filters.get("recipient"):
                results = [r for r in results if r["recipient"] == filters["recipient"]]
            if filters.get("creator"):
                results = [r for r in results if r["creator"] == filters["creator"]]
        
        print(f"[Snowflake] Found {len(results)} tasks")
        return results
        
    except Exception as e:
        print(f"[Snowflake] Error querying tasks: {e}")
        return []

def get_task_statistics():
    """
    Get task statistics from Snowflake
    """
    try:
        total_tasks = len(snowflake_data)
        completed_tasks = len([t for t in snowflake_data if t["status"] == "completed"])
        pending_tasks = len([t for t in snowflake_data if t["status"] in ["scheduled", "executing"]])
        
        return {
            "total": total_tasks,
            "completed": completed_tasks,
            "pending": pending_tasks,
            "completion_rate": (completed_tasks / total_tasks * 100) if total_tasks > 0 else 0
        }
        
    except Exception as e:
        print(f"[Snowflake] Error getting statistics: {e}")
        return {"total": 0, "completed": 0, "pending": 0, "completion_rate": 0} 