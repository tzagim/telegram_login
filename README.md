# Telogin - Telegram login
A simple Python file to create and save a Telegram session string.

## Installation
You must install `telethon` to use this script:
```
$ sudo apt install python3-telethon
```
OR
```
$ python3 -m pip install telethon
```

## How to use
### Step 1
+ Go to: [my.telegram.org](https://my.telegram.org)  > [API development tools](https://my.telegram.org/apps) > creating a new app (if you don't have one).
+ Choose short app name (NOTE: this is the name that will appear in the list of connected devices).
+ The data you need later is: App `api_id` & `api_hash`.

### Step 2
+ Download the file [`telogin.py`](https://github.com/tzagim/telogin/blob/main/telogin.py "Click here") from this repository
+ Run the script:
```
$ python3 telogin.py
```

The script will ask for:
+ Phone number (in international format, but it is not mandatory to put + at the beginning).
+ `api_id` (from [step 1](#step-1))
+ `api_hash` (from [step 1](#step-1))
+ The login code received
+ Two-step verification (If you have enabled it)

The script creates a json file called `login.json`, in the following format:
```json
{
    "api_id": "123456789",
    "api_hash": "1234567890abcdefg",
    "session_string": "abcdefghig-klmnopqr="
}
```
Please note, session_string contains about 350 characters and usually ends with =

You can also see in the terminal
```js
Signed in successfully as YOUR_NAME; remember to not break the ToS or you will risk an account ban!
Session string: abcdefghig-klmnopqr=
```
<img src=".github/images/Icons8_flat_high_priority.svg" align="left" width="42" height="42"> **Do not disconnect `SHORT_APP_NAME` from the list of connected devices, this will cause the user to no longer be able to connect with the created string, it will be necessary to create a new one.**