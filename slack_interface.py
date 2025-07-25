import os
from slack_sdk import WebClient
from slack_sdk.socket_mode import SocketModeClient
from slack_sdk.socket_mode.request import SocketModeRequest
from slack_sdk.socket_mode.response import SocketModeResponse
from slack_sdk.errors import SlackApiError
import asyncio
import json

def get_user_input():
    """Get task input from user"""
    return input("Enter a task (e.g., 'Remind Alex to review Q3 numbers Friday and summarize response'): ")

def send_to_slack(parsed_task):
    """
    Send parsed task to Slack using Socket Mode
    """
    try:
        # Get Slack tokens from environment
        bot_token = os.getenv('SLACK_BOT_TOKEN')
        app_token = os.getenv('SLACK_APP_TOKEN')
        
        if not bot_token or not app_token:
            print("❌ SLACK_BOT_TOKEN or SLACK_APP_TOKEN not found in environment variables")
            return simulate_slack_send(parsed_task)
        
        # Validate token formats
        if not bot_token.startswith('xoxb-'):
            print("❌ SLACK_BOT_TOKEN should start with 'xoxb-'")
            print("   Get this from: https://api.slack.com/apps > Your App > OAuth & Permissions")
            return simulate_slack_send(parsed_task)
            
        if not app_token.startswith('xapp-'):
            print("❌ SLACK_APP_TOKEN should start with 'xapp-'")
            print("   Get this from: https://api.slack.com/apps > Your App > Basic Information > App-Level Tokens")
            return simulate_slack_send(parsed_task)
        
        # Initialize WebClient for sending messages
        client = WebClient(token=bot_token)
        
        # Get default channel
        default_channel = os.getenv('SLACK_DEFAULT_CHANNEL', 'general')
        
        # Create message
        recipient = parsed_task['recipient']
        task = parsed_task['task']
        due_date = parsed_task['due_date']
        response_required = parsed_task.get('response_required', False)
        output_format = parsed_task.get('output', 'confirmation')
        
        # Format the message
        message = f"🤖 *TaskPilot AI Task*\n\n"
        message += f"*Recipient:* {recipient}\n"
        message += f"*Task:* {task}\n"
        message += f"*Due Date:* {due_date}\n"
        message += f"*Response Required:* {'Yes' if response_required else 'No'}\n"
        if response_required:
            message += f"*Output Format:* {output_format}\n"
        
        # Send message to Slack
        response = client.chat_postMessage(
            channel=default_channel,
            text=message,
            unfurl_links=False
        )
        
        print(f"✅ Message sent to Slack channel: {default_channel}")
        print(f"📤 Message ID: {response['ts']}")
        
        return True
        
    except SlackApiError as e:
        error_code = e.response.get('error', 'unknown_error')
        
        if error_code == 'not_allowed_token_type':
            print("❌ Token type not allowed for this operation")
            print("   Make sure you're using the correct token types:")
            print("   - SLACK_BOT_TOKEN: Should be 'xoxb-' (Bot User OAuth Token)")
            print("   - SLACK_APP_TOKEN: Should be 'xapp-' (App-Level Token)")
            print("   - Get tokens from: https://api.slack.com/apps")
        elif error_code == 'invalid_auth':
            print("❌ Invalid authentication token")
            print("   Check your SLACK_BOT_TOKEN and SLACK_APP_TOKEN")
        elif error_code == 'channel_not_found':
            print(f"❌ Channel '{default_channel}' not found")
            print("   Make sure the bot is added to the channel")
        else:
            print(f"❌ Slack API Error: {error_code}")
            print(f"   Details: {e.response.get('ok', False)}")
        
        print("Falling back to simulation...")
        return simulate_slack_send(parsed_task)
        
    except Exception as e:
        print(f"❌ Error sending to Slack: {e}")
        print("Falling back to simulation...")
        return simulate_slack_send(parsed_task)

def simulate_slack_send(parsed_task):
    """
    Simulate sending to Slack (fallback)
    """
    recipient = parsed_task['recipient']
    task = parsed_task['task']
    due_date = parsed_task['due_date']
    
    print(f"📤 [SIMULATED] Message to {recipient}:")
    print(f"   Task: {task}")
    print(f"   Due: {due_date}")
    
    if parsed_task.get('response_required'):
        print(f"   Response required: Yes")
        print(f"   Output format: {parsed_task.get('output', 'confirmation')}")
    
    return False

def test_slack_connection():
    """
    Test Slack API connection using Socket Mode
    """
    try:
        bot_token = os.getenv('SLACK_BOT_TOKEN')
        app_token = os.getenv('SLACK_APP_TOKEN')
        
        if not bot_token:
            print("❌ SLACK_BOT_TOKEN not found")
            print("   Get this from: https://api.slack.com/apps > Your App > OAuth & Permissions")
            return False
            
        if not app_token:
            print("❌ SLACK_APP_TOKEN not found")
            print("   Get this from: https://api.slack.com/apps > Your App > Basic Information > App-Level Tokens")
            return False
        
        # Validate token formats
        if not bot_token.startswith('xoxb-'):
            print("❌ SLACK_BOT_TOKEN should start with 'xoxb-'")
            print("   This should be your Bot User OAuth Token")
            return False
            
        if not app_token.startswith('xapp-'):
            print("❌ SLACK_APP_TOKEN should start with 'xapp-'")
            print("   This should be your App-Level Token")
            return False
            
        # Test WebClient connection
        client = WebClient(token=bot_token)
        response = client.auth_test()
        
        print(f"✅ Slack connection successful!")
        print(f"   Team: {response['team']}")
        print(f"   User: {response['user']}")
        print(f"   Bot ID: {response['bot_id']}")
        print(f"   App Token: {app_token[:10]}...")
        
        return True
        
    except SlackApiError as e:
        error_code = e.response.get('error', 'unknown_error')
        
        if error_code == 'not_allowed_token_type':
            print("❌ Token type not allowed for this operation")
            print("   Make sure you're using the correct token types:")
            print("   - SLACK_BOT_TOKEN: Should be 'xoxb-' (Bot User OAuth Token)")
            print("   - SLACK_APP_TOKEN: Should be 'xapp-' (App-Level Token)")
        elif error_code == 'invalid_auth':
            print("❌ Invalid authentication token")
            print("   Check your token values")
        else:
            print(f"❌ Slack connection failed: {error_code}")
        
        return False
    except Exception as e:
        print(f"❌ Error testing Slack connection: {e}")
        return False

def start_socket_mode_client():
    """
    Start Socket Mode client for real-time Slack events
    """
    try:
        bot_token = os.getenv('SLACK_BOT_TOKEN')
        app_token = os.getenv('SLACK_APP_TOKEN')
        
        if not bot_token or not app_token:
            print("❌ Missing Slack tokens for Socket Mode")
            return None
            
        # Validate token formats
        if not bot_token.startswith('xoxb-') or not app_token.startswith('xapp-'):
            print("❌ Invalid token format for Socket Mode")
            return None
            
        # Initialize Socket Mode client
        client = SocketModeClient(
            app_token=app_token,
            web_client=WebClient(token=bot_token)
        )
        
        print("🔌 Socket Mode client initialized")
        return client
        
    except Exception as e:
        print(f"❌ Error initializing Socket Mode client: {e}")
        return None

def handle_socket_mode_events(client):
    """
    Handle Socket Mode events (for future use)
    """
    def process_request(client, req: SocketModeRequest):
        # Handle different event types
        if req.type == "events_api":
            # Handle Events API events
            event_data = req.payload.get("event", {})
            event_type = event_data.get("type")
            
            if event_type == "message":
                # Handle incoming messages
                print(f"📨 Received message: {event_data.get('text', '')}")
                
        # Send acknowledgment
        client.send_socket_mode_response(SocketModeResponse(envelope_id=req.envelope_id))
    
    # Set up event handlers
    client.socket_mode_request_listeners.append(process_request)
    
    print("🎧 Socket Mode event handlers configured") 