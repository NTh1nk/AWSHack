# Environment Setup Guide for TaskPilot AI

This guide explains how to configure environment variables for TaskPilot AI to enable production features.

## 🔧 Environment Variables

### Required for Production

#### OpenAI API (for LLM parsing)
```bash
OPENAI_API_KEY=your_openai_api_key_here
```
- **Purpose**: Enables real LLM parsing instead of fallback pattern matching
- **How to get**: Sign up at [OpenAI Platform](https://platform.openai.com/api-keys)
- **Required for**: Enhanced natural language task parsing

#### Snowflake Database
```bash
SNOWFLAKE_ACCOUNT=your_account_identifier
SNOWFLAKE_USER=your_username
SNOWFLAKE_PASSWORD=your_password
SNOWFLAKE_DATABASE=your_database_name
SNOWFLAKE_SCHEMA=your_schema_name
SNOWFLAKE_WAREHOUSE=your_warehouse_name
```
- **Purpose**: Connect to real Snowflake database for task storage
- **How to get**: Configure in your Snowflake account
- **Required for**: Persistent task data storage

#### Slack Integration
```bash
SLACK_BOT_TOKEN=xoxb-your-bot-token
SLACK_APP_TOKEN=xapp-your-app-token
SLACK_SIGNING_SECRET=your_signing_secret
```
- **Purpose**: Enable real Slack bot functionality
- **How to get**: Create a Slack app at [api.slack.com](https://api.slack.com/apps)
- **Required for**: Real-time Slack messaging

#### Temporal Server
```bash
TEMPORAL_HOST=localhost:7233
TEMPORAL_NAMESPACE=default
```
- **Purpose**: Connect to Temporal server for workflow orchestration
- **How to get**: Deploy Temporal server or use Temporal Cloud
- **Required for**: Real workflow orchestration

### Optional Configuration

#### Application Settings
```bash
# Logging level
LOG_LEVEL=INFO

# Application port (for web interface)
PORT=8000

# Environment
ENVIRONMENT=development
```

## 📍 Where to Put Environment Variables

### Option 1: .env File (Recommended for Development)
Create a `.env` file in the project root:
```bash
# Create .env file
touch .env

# Add your variables
echo "OPENAI_API_KEY=your_key_here" >> .env
echo "SNOWFLAKE_ACCOUNT=your_account" >> .env
# ... add other variables
```

### Option 2: System Environment Variables
```bash
# macOS/Linux
export OPENAI_API_KEY="your_key_here"
export SNOWFLAKE_ACCOUNT="your_account"
# ... add other variables

# Windows (Command Prompt)
set OPENAI_API_KEY=your_key_here
set SNOWFLAKE_ACCOUNT=your_account

# Windows (PowerShell)
$env:OPENAI_API_KEY="your_key_here"
$env:SNOWFLAKE_ACCOUNT="your_account"
```

### Option 3: Docker Environment
```bash
# docker-compose.yml
environment:
  - OPENAI_API_KEY=your_key_here
  - SNOWFLAKE_ACCOUNT=your_account
```

## 🔒 Security Best Practices

1. **Never commit .env files to version control**
   ```bash
   # Add to .gitignore
   echo ".env" >> .gitignore
   echo "*.env" >> .gitignore
   ```

2. **Use different keys for development and production**

3. **Rotate keys regularly**

4. **Use environment-specific .env files**
   ```bash
   .env.development
   .env.production
   .env.testing
   ```

## 🚀 Quick Start

1. **Copy the example environment file:**
   ```bash
   cp example.env .env
   ```

2. **Edit .env with your actual values:**
   ```bash
   nano .env
   ```

3. **Test the configuration:**
   ```bash
   python main.py dashboard
   ```

## 🔍 Testing Environment Variables

Add this to your Python code to test:
```python
import os
from dotenv import load_dotenv

load_dotenv()

# Test if variables are loaded
print(f"OpenAI API Key: {'✅ Set' if os.getenv('OPENAI_API_KEY') else '❌ Missing'}")
print(f"Snowflake Account: {'✅ Set' if os.getenv('SNOWFLAKE_ACCOUNT') else '❌ Missing'}")
print(f"Slack Bot Token: {'✅ Set' if os.getenv('SLACK_BOT_TOKEN') else '❌ Missing'}")
```

## 📋 Environment Checklist

- [ ] OpenAI API key configured
- [ ] Snowflake credentials configured
- [ ] Slack app tokens configured
- [ ] Temporal server connection configured
- [ ] .env file added to .gitignore
- [ ] Environment variables tested
- [ ] Application runs without errors

---

*For production deployment, consider using a secrets management service like AWS Secrets Manager or HashiCorp Vault.* 