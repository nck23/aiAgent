from google import genai
from google.genai import types

from utils.setup_available_funcs import setup_available_funcs
from utils.prompts import system_prompt
from utils.call_function import call_function

def generate_content(client, messages, verbose):
    available_functions = setup_available_funcs()

    response = client.models.generate_content(
        model='gemini-2.0-flash',
        contents=messages,
        config=types.GenerateContentConfig(
            tools=[available_functions], system_instruction=system_prompt
        ))
    if verbose:
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    if response.candidates:
        for candidate in response.candidates:
            messages.append(candidate.content) 
    
    if not response.function_calls:
        if response.text:
            return response.text
        return None

    function_responses = []
    print("Function calls: ", len(response.function_calls))
    for function_call_part in response.function_calls:
        if verbose:
            print(f"Calling function: {function_call_part.name}({function_call_part.args})")
        else:
            print(f" - Calling function: {function_call_part.name}")

        function_call_result = call_function(function_call_part, verbose)

        if not (function_call_result.parts) or not (function_call_result.parts[0].function_response):
            raise Exception("empty function call result")
        if verbose:
            print(f"-> {function_call_result.parts[0].function_response.response}")
        function_responses.append(function_call_result.parts[0])


    if not function_responses:
        raise Exception("no function responses generated")
    messages.append(types.Content(role="user", parts=function_responses))
    return generate_content(client, messages, verbose)