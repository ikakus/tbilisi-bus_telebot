import json
import requests
import time
import urllib
from subprocess import call

TOKEN = "453908741:AAHbiAayPq5cQPEitEw5SHIoAWyxmVD48BM"
URL = "https://api.telegram.org/bot{}/".format(TOKEN)


def get_url(url):
    response = requests.get(url)
    content = response.content.decode("utf8")
    return content


def get_json_from_url(url):
    content = get_url(url)
    js = json.loads(content)
    return js


def get_updates(offset=None):
    url = URL + "getUpdates?timeout=100"
    if offset:
        url += "&offset={}".format(offset)
    js = get_json_from_url(url)
    return js


def get_last_chat_id_and_text(updates):
    num_updates = len(updates["result"])
    last_update = num_updates - 1
    text = updates["result"][last_update]["message"]["text"]
    chat_id = updates["result"][last_update]["message"]["chat"]["id"]
    return (text, chat_id)


def get_last_update_id(updates):
    update_ids = []
    for update in updates["result"]:
        update_ids.append(int(update["update_id"]))
    return max(update_ids)


def send_message(text, chat_id):
    text = urllib.parse.quote_plus(text)
    url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
    get_url(url)


def echo_all(updates):
    for update in updates["result"]:
        try:
            text = update["message"]["text"]
            chat = update["message"]["chat"]["id"]
            text = handle_command(text)
            send_message(text, chat)
        except Exception as e:
            print(e)


def handle_command(text):
    parts = text.split(" ")
    if text[0] == '/':
        if len(parts) != 2:
            return "Invalid Command format"
        else:
            command = text[1:]
            if command.split(" ")[0] == "setVolume":
                value, result = int_try_parse(command.split(" ")[1])
                if result:
                    set_volume(value)
                else:
                    return "Wrong value. Should be 0 - 100"
                return "Volume set to {}".format(value)
            else:
                return "Unknown Command {}".format(command.split(" ")[0])
    else:
        return text


def int_try_parse(value):
    try:
        return int(value), True
    except ValueError:
        return value, False


def set_volume(value):
    call(["amixer", "-D", "pulse", "sset", "Master", str(value) + "%"])


def main():
    last_update_id = None
    while True:
        updates = get_updates(last_update_id)
        if len(updates["result"]) > 0:
            last_update_id = get_last_update_id(updates) + 1
            echo_all(updates)
        time.sleep(0.5)


if __name__ == '__main__':
    main()
