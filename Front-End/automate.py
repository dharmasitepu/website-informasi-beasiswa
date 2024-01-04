import requests
import json
import time

def get_data_from_url(url):
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")
        return None

def save_data_to_file(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=2)
        print(f"Data saved to {filename}")

def main():
    url = "http://139.255.41.66/Back-End/kominfo/data_with_id.json"
    filename = "./Front-End/data_with_id.json"

    while True:
        data = get_data_from_url(url)

        if data:
            save_data_to_file(data, filename)

        time.sleep(60)  # Delay for 1 minute (60 seconds)

if __name__ == "__main__":
    main()
