import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import sys

from utils.setup_available_funcs import setup_available_funcs
from utils.call_function import call_function
from utils.prompts import system_prompt

load_dotenv()
api_key = os.environ.get('GEMINI_API_KEY')
client = genai.Client(api_key=api_key)

available_functions = setup_available_funcs()



def main():
    arguments = sys.argv
    if len(arguments) == 1:
        raise Exception('not enough arguments')
    
    verbose = '--verbose' in arguments
    user_prompt = arguments[1]

    messages = [
    types.Content(role="user", parts=[types.Part(text=user_prompt)]),
]
    response = client.models.generate_content(
        model='gemini-2.0-flash',
        contents=messages,
        config=types.GenerateContentConfig(
            tools=[available_functions], system_instruction=system_prompt
        ))
    if verbose:
        print(f"User prompt: {user_prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
        
    if response.text:
        print(response.text)
    if response.function_calls:
        for function_call_part in response.function_calls:
            if verbose:
                print(f"Calling function: {function_call_part.name}({function_call_part.args})")
            else:
                print(f" - Calling function: {function_call_part.name}")
            results = call_function(function_call_part)
            print(results)

if __name__ == "__main__":
    main()
