from google.genai import types

from utils.config import WORKING_DIR
from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.run_python_file import run_python_file
from functions.write_file import write_file


def call_function(function_call_part, verbose=False):
    function_map = {
        "get_files_info": get_files_info,
        "get_file_content": get_file_content,
        "run_python_file": run_python_file,
        "write_file": write_file,
    }
    function_name = function_call_part.name
    function_args = function_call_part.args
    args = dict(function_args)

    args["working_directory"] = WORKING_DIR
    if verbose:
        print(f"Calling function: {function_name}({function_args})")
    else:
        print(f" - Calling function: {function_name}")
    if function_name not in function_map:
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_name,
                    response={"error": f"Unknown function: {function_name}"},
                )
            ],
        )
    # SETUP ARGS IN LIST
    if "args" in args:
        if isinstance(args["args"], str):
            args["args"] = [args["args"]]
    function_result = function_map[function_name](**args)
    return types.Content(
        role="tool", 
        parts=[
        types.Part.from_function_response(
            name=function_name, 
            response={"response": function_result},
        )
    ],
)
