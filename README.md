# AI Agent (Gemini API/other)

A simple AI agent that uses the Google Gemini API to generate responses based on a terminal prompt.

## Installation & Setup


## 1. Clone the repo
```bash
git clone https://github.com/USER/REPO.git
cd <DIR>
```
## 2. Install dependencies
```bash
pip install -r requirements.txt
```
## 3. Generate API key
You can generate your gemini api key [here](https://aistudio.google.com/api-keys)

## 4. Create .env file and put your api key inside
```bash
echo "GEMINI_API_KEY='YOUR_API_KEY'" > .env

```
# How to use:

(In root directory of this repo)
```bash
python3 main.py "Prompt, Fix calculator/main.py, it's returning wrong values." [--verbose]
```
example
```bash
python main.py "Prompt, Fix calculator/main.py, it's returning wrong values." [--verbose]
```

## Additional information
Agent can use all functions in ``` functions/ ``` directory which are:
- Listing all files in directory with their size and type,
- Listing file content,
- Writing/Overwriting file content with creating its path,
- Execute python scripts (.py),
But it can only do it inside working directory.

Also make sure you tell in prompt exactly what you want because agent can just run functions in loop and get stuck.

# Example outputs

## List files
```bash
python3 main.py "hello, list files only names"
```
```bash
OUTPUT:
Function calls:  1
 - Calling function: get_files_info
 - Calling function: get_files_info
Final response: Okay, I see the following files and directories in the current working directory:

*   README.md
*   args.txt
*   tests.py
*   test\_calculator.py
*   lorem.txt
*   \_\_pycache\_\_ (directory)
*   temp\_runner.py
*   main.py
*   pkg (directory)
```



