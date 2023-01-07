import requests
import os

# Replace YOUR_API_TOKEN with the API token for your bot, which you can obtain from the BotFather
TOKEN = ""

# Replace YOUR_CHAT_ID with the chat ID of the chat where you want to receive the IP address updates.
# You can obtain your chat ID by sending a message to your bot and then calling the following API method:
# https://api.telegram.org/botYOUR_API_TOKEN/getUpdates
CHAT_ID = ""

def send_message(text):
    """Sends a message to the chat specified by CHAT_ID using the Telegram API."""
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": text}
    requests.post(url, json=payload)

def get_current_ip():
    """Returns the current public IP address of the server."""
    return requests.get("https://api.ipify.org").text.strip()

def main():
    # Get the current IP address
    current_ip = get_current_ip()

    # Load the previously saved IP address from a file (if it exists)
    prev_ip_file = "prev_ip.txt"
    if os.path.exists(prev_ip_file):
        with open(prev_ip_file, "r") as f:
            prev_ip = f.read().strip()
    else:
        prev_ip = None

    # If the IP address has changed, send a message to the Telegram chat
    if current_ip != prev_ip:
        send_message(f"The IP address of the server has changed to {current_ip}")

    # Save the current IP address to the file
    with open(prev_ip_file, "w") as f:
        f.write(current_ip)

if __name__ == "__main__":
    main()
