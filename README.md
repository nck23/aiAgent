# AI Agent

A simple AI coding agent powered by Google Gemini that can read, write, and execute Python files.

## Requirements

- Python 3.13+
- Google Gemini API key

## Installation

1. Clone the repository:
```bash
git clone https://github.com/nck23/aiAgent.git
cd aiAgent
```

2. Install dependencies:
```bash
pip install google-genai python-dotenv
# or using uv
uv sync
```

3. Create a `.env` file and add your Gemini API key:
```
GEMINI_API_KEY=your_api_key_here
```

## Usage

```bash
python3 main.py "your prompt here"
```

For verbose output:
```bash
python3 main.py "your prompt here" --verbose
```

## Example

```bash
python3 main.py "list all files in the calculator folder"
```
