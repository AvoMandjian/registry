import requests
import json

API_URL = "https://registry.modelcontextprotocol.io/v0/servers"
OUTPUT_FILE = "registry.json"

def fetch_and_save_registry():
    """
    Fetches the complete MCP server registry from the production API
    and saves it to a local JSON file.
    """
    print(f"Fetching registry data from {API_URL}...")
    try:
        response = requests.get(API_URL, timeout=30)
        response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)

        print("Successfully fetched registry data.")
        data = response.json()

        with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

        print(f"Complete registry saved to {OUTPUT_FILE}")
        print(f"Total servers found: {len(data)}")

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.ConnectionError as conn_err:
        print(f"Connection error occurred: {conn_err}")
    except requests.exceptions.Timeout as timeout_err:
        print(f"Timeout error occurred: {timeout_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"An unexpected error occurred: {req_err}")
    except json.JSONDecodeError:
        print("Failed to parse JSON from the response.")

if __name__ == "__main__":
    fetch_and_save_registry()
