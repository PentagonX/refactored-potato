import requests
import string
import random
import time

# ---------------- CONFIG ----------------
DISCORD_WEBHOOK = "YOUR_DISCORD_WEBHOOK_URL_HERE"
TARGET_URL = "https://discordapp.com/api/v9/entitlements/gift-codes/{}?with_application=false&with_subscription_plan=true"
# ----------------------------------------

def generate_code(length=18):
    """Generate a random alphanumeric string of given length."""
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))

def check_code(code):
    """Send GET request to Discord API to check the code."""
    url = TARGET_URL.format(code)
    response = requests.get(url)
    return response.status_code == 200

def send_to_webhook(code):
    """Send the valid code to a Discord webhook."""
    data = {"content": f"Valid code found: {code}"}
    requests.post(DISCORD_WEBHOOK, json=data)

def main():
    while True:
        code = generate_code()
        print(f"Checking code: {code}")
        if check_code(code):
            print(f"Valid code found! Sending to webhook: {code}")
            send_to_webhook(code)
        time.sleep(0.5)  # slight delay to avoid spamming too fast

if __name__ == "__main__":
    main()

