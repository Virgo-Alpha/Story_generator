# TODO: Get a free LLM API
# TODO: Test the API using a simple prompt

import requests
import os

def save_response_to_file(url, output_folder="response_data"):
    # Ensure the output folder exists
    os.makedirs(output_folder, exist_ok=True)

    try:
        # Send a GET request to the specified URL
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Create a file path to save the response data
            file_path = os.path.join(output_folder, "response_data.txt")

            # Save the response content to a text file
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(response.text)

            print(f"Response saved to: {file_path}")
        else:
            print(f"Error: Unable to fetch data. Status code: {response.status_code}")

    except requests.RequestException as e:
        print(f"Error: {e}")

# Example usage
url_to_request = "https://www.example.com"
save_response_to_file(url_to_request)
