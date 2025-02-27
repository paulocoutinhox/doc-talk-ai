
# CLOUD MODELS

This document explains how to configure API keys for cloud-based models like **OpenAI GPT** and **Gemini AI**.

## 🔑 **Supported API Providers**

- **OpenAI GPT**
- **Gemini AI**

## ⚙️ **How to Set API Keys**

Set the appropriate API keys for each provider as environment variables.

### 🔸 **OpenAI API Key**

#### Linux/macOS:
```bash
export OPENAI_API_KEY="your-openai-api-key"
```

#### Windows (Command Prompt):
```cmd
set OPENAI_API_KEY="your-openai-api-key"
```

#### Windows (PowerShell):
```powershell
$env:OPENAI_API_KEY="your-openai-api-key"
```

### 🔸 **Gemini API Key**

#### Linux/macOS:
```bash
export GOOGLE_API_KEY="your-gemini-api-key"
```

#### Windows (Command Prompt):
```cmd
set GOOGLE_API_KEY="your-gemini-api-key"
```

#### Windows (PowerShell):
```powershell
$env:GOOGLE_API_KEY="your-gemini-api-key"
```

## 📌 **Persistent Configuration**

To make these environment variables permanent:

- **Linux/macOS:** Add the export commands to your `~/.bashrc` or `~/.zshrc` file.
- **Windows:** Set environment variables via **System Properties** > **Advanced** > **Environment Variables**.

## ❓ **Troubleshooting**

- Ensure your API key is valid and active.
- Restart your terminal or development environment after setting the environment variables.
- Double-check the exact spelling of the environment variable names.
