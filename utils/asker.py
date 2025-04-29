import requests 
import json 
import logging 

def get_gemini_response(prompt: str, api_key: str, model: str = 'gemini-pro') -> str: 
    endpoint = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent"
    headers = {
        'Content-Type': 'application/json',
    }

    payload = {
        'contents': [
            {
                'parts': [
                    {
                        'text': prompt,
                    },
                ],
            },
        ],
    }

    params = {
        'key': api_key,
    }

    try:
        response = requests.post(endpoint, headers=headers, params=params, json=payload)
        response.raise_for_status()  # Will raise an HTTPError if the response status code is not 2xx

        result = response.json()

        # Check for errors in the API response.
        if 'error' in result:
            logging.error(f"Gemini API Error: {result['error']['message']}")
            return None

        # Extract the generated text. Handles cases where there might be multiple candidates.
        if 'candidates' in result and isinstance(result['candidates'], list) and len(result['candidates']) > 0:
            for candidate in result['candidates']:
                if 'content' in candidate and isinstance(candidate['content'], dict):
                    if 'parts' in candidate['content'] and isinstance(candidate['content']['parts'], list):
                        for part in candidate['content']['parts']:
                            if 'text' in part:
                                return part['text']  # Return the first text part found.

        logging.error("Gemini API: No text found in response.")
        return None  # Or an empty string, depending on desired behavior

    except requests.exceptions.RequestException as e:
        # Handle HTTP errors (e.g., 400, 500)
        logging.error(f"HTTP Request Error: {e}")
        return None
    except Exception as e:
        # Handle other exceptions (e.g., network errors, JSON decoding errors)
        logging.error(f"Error: {e}")
        return None

def Resources(role):
    # Replace with your actual API key and prompt. DO NOT HARDCODE IN PRODUCTION
    api_key = 'AIzaSyCU9mAQIM_YO6uYgQ_LjpXAQ8B6WSyZy6M'  # DO NOT COMMIT YOUR API KEY TO VERSION CONTROL
    prompt = "give me the md formate of a skills required for " + role +" and each has its sub array of the concepts and its learning free resource just give only md do not give any text in the response"
    model = 'gemini-2.0-flash'  # Or 'gemini-pro-vision', 'gemini-2.0-flash', etc.

    # Get the response from Gemini
    response = get_gemini_response(prompt, api_key, model)

    if response is not None:
        print("Gemini Response:")
        print(response)
    else:
        print("Failed to get a response from the Gemini API.")


Resources('Automation Testing')