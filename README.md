# telegram login
A simple Python file to create a session string.

# installation
You must install telethon to use this script
```
$ sudo apt install python3-telethon
```
OR
```
$ python3 -m pip install telethon
```

# how to use
To use a script:

+ Go to: https://my.telegram.org  > [API development tools](https://my.telegram.org/apps) > creating a new app (if you don't have one).
+ Choose short app name (this is the name that will appear in the list of connected devices).
+ The data you need later is: App `api_id` & `api_hash`.
+ Download `telogin.py`
+ Run the script:
```
$ python3 telogin.py
```

The script will ask for:
+ Phone number (in international format, but it is not mandatory to put + at the beginning).
+ `api_id`
+ `api_hash`
+ The login code received
+ Two-step verification (if you have it)

The script creates a json file in the following format:
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

**Do not disconnect `SHORT_APP_NAME` from the list of connected devices, this will cause the user to no longer be able to connect with the created string, it will be necessary to create a new one.**
