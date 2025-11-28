import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import sys

from utils.generate_content import generate_content
from utils.config import MAX_ITERS

load_dotenv()
api_key = os.environ.get('GEMINI_API_KEY')
client = genai.Client(api_key=api_key)


def main():
    verbose = "--verbose" in sys.argv
    args = []
    for arg in sys.argv[1:]:
        if not arg.startswith("--"):
            args.append(arg)
    if not args:
        print("AI agent/assistant")
        print('Usage: python3 main.py "prompt" [--verbose]')
        print("No arguments, exiting...")
        sys.exit(1)

    user_prompt = " ".join(args)

    if verbose:
        print(f"User prompt: {user_prompt}")

    messages = [
    types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]
    
    iterations = 0
    while True:
        iterations += 1
        if iterations > MAX_ITERS:
            print(F"Maximum iterations {MAX_ITERS} reached. \nExiting...")
            sys.exit(1)
        try:
            response = generate_content(client, messages, verbose)
        except Exception as e:
            print(f"Error in generate_content: {e}")
            break
        if response:
            print(f"Final response: {response}")
            break
    

if __name__ == "__main__":
    main()
