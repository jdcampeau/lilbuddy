import sys
import os
from google import genai
from google.genai import types
from dotenv import load_dotenv

from system_prompt import system_prompt
from available_functions import available_functions, call_function
from config import MAXLOOPS

def main():
    load_dotenv()

    verbose = "--verbose" in sys.argv
    args = []
    for arg in sys.argv[1:]:
        if not arg.startswith("--"):
            args.append(arg)

    if not args:
        print("Lil' Buddy")
        print('\nUsage: uv run main.py "your prompt here" [--verbose]')
        print('Example: uv run main.py "How do I build a calculator app?"')
        sys.exit(1)

    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    user_prompt = " ".join(args)

    if verbose:
        print(f"User prompt: {user_prompt}\n")

    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    loops = 0
    while True:
        loops += 1
        if loops > MAXLOOPS:
            print("Maximum allowed iterations reached.")
            sys.exit(1)
        try:
            func_response = generate_content(client, messages, verbose)
            if func_response:
                print("Response")
                print(func_response)
                break
        except Exception as e:
            loops += 20
            print(f"An unexpected error has occurred: {e}")



def generate_content(client, messages, verbose):
    response = client.models.generate_content(
            model='gemini-2.0-flash-001', 
            contents = messages,
            config = types.GenerateContentConfig(
                tools=[available_functions], system_instruction=system_prompt
            )
    )

    
    for candidate in response.candidates:
        messages.append(candidate.content)
    


    if verbose:
        print("Prompt tokens:", response.usage_metadata.prompt_token_count)
        print("Response tokens:", response.usage_metadata.candidates_token_count)

    if response.candidates:
        for candidate in response.candidates:
            function_call_content = candidate.content
            messages.append(function_call_content)

    if not response.function_calls:
        return response.text

    function_responses = []
    for function_call_part in response.function_calls:
        function_call_result = call_function(function_call_part, verbose)
        if (
                not function_call_result.parts
                or not function_call_result.parts[0].function_response
        ):
            raise Exception("empty function call result")
        if verbose:
            print(f"->{function_call_result.parts[0].function_response.response}")
        function_responses.append(function_call_result.parts[0])

    if not function_responses:
        raise Exception("no function responses generated, exiting.")

    messages.append(types.Content(role="user", parts=function_responses))



if __name__ == "__main__":
    main()
