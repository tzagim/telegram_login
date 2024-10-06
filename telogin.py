import os, json, asyncio
from telethon import TelegramClient
from telethon.sessions import StringSession

# Define the session file name
LOGIN_FILE = 'login.json'

# Load existing credentials or create a new one
if os.path.exists(LOGIN_FILE):
    with open(LOGIN_FILE, 'r') as f:
        login_data = json.load(f)
else:
    login_data = {
        "api_id": "",
        "api_hash": "",
        "session_string": ""
    }
    with open(LOGIN_FILE, 'w') as f:
        json.dump(login_data, f, indent=4)

# Get API credentials
api_id = login_data["api_id"]
api_hash = login_data["api_hash"]
phone_number = input("Please enter your phone number (with country code): ")

# Prompt for API credentials if they are empty
if not api_id:
    api_id = input("Please enter your API ID: ")
    login_data["api_id"] = api_id

if not api_hash:
    api_hash = input("Please enter your API Hash: ")
    login_data["api_hash"] = api_hash

# Write the updated API credentials back to the JSON file
with open(LOGIN_FILE, 'w') as f:
    json.dump(login_data, f, indent=4)

# Create a new Telegram client with the session name
client = TelegramClient(StringSession(), api_id, api_hash)

async def main():
    await client.start(phone=phone_number)

    # Generate the session string
    session_string = client.session.save()
    print(f"Session string: {session_string}")

    # Save session string to JSON
    login_data["session_string"] = session_string
    with open(LOGIN_FILE, 'w') as f:
        json.dump(login_data, f, indent=4)

# Run the client
if __name__ == '__main__':
    asyncio.run(main())
