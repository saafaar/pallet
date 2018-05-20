import sys, json, requests
from flask import Flask, request
from pallet.entities.match import Match
from pallet.entities.freight import Freight
from pallet.repository.repository import MemRepo

repository = MemRepo

access_token = 'l'

app = Flask(__name__)

PAT = 'l'

CLIENT_ACCESS_TOKEN = 'l'

VERIFY_TOKEN = 't'


@app.route('/', methods=['GET'])
def handle_verification():
    '''
    Verifies facebook webhook subscription
    Successful when verify_token is same as token sent by facebook app
    '''
    if (request.args.get('hub.verify_token', '') == VERIFY_TOKEN):
        print("succefully verified")
        return request.args.get('hub.challenge', '')
    else:
        print("Wrong verification token!")
        return "Wrong validation token"


@app.route('/', methods=['POST'])
def handle_message():
    '''
    Handle messages sent by facebook messenger to the applicaiton
    '''
    data = request.get_json()

    if data["object"] == "page":
        for entry in data["entry"]:
            print(entry)
            if "messaging" in entry:
                for messaging_event in entry["messaging"]:
                    sender_id = messaging_event["sender"]["id"]
                    recipient_id = messaging_event["recipient"]["id"]
                    print('Got an incoming message!')
                    if "message" in messaging_event and "text" in messaging_event["message"]:
                        message_text = messaging_event["message"]["text"]
                        send_message(sender_id, 'Heuréka! Ezt én is mondhattam volna: ' + message_text)
                    if "postback" in messaging_event:
                        postback_handler(sender_id, messaging_event["postback"]["payload"])

    return "ok"


def send_message(sender_id, message_text):
    '''
    Sending response back to the user using facebook graph API
    '''
    r = requests.post("https://graph.facebook.com/v2.6/me/messages",

                      params={"access_token": PAT},

                      headers={"Content-Type": "application/json"},

                      data=json.dumps({
                          "recipient": {"id": sender_id},
                          "message": {"text": message_text}
                      }))


# def send_message_response(sender_id, message_text):
#     sentenceDelimiter = ". "
#     messages = message_text.split(sentenceDelimiter)
#
#     for message in messages:
#         send_message(sender_id, message)


def postback_handler(sender_id, postback_message):
    if "dev_webpage" == postback_message:
        send_message(sender_id, "Kérlek látogass meg a https://saafaar.github.io/ weboldalon")
    if "new_cargo" == postback_message:
        pass

    # if "new_freight" == postback_message:
    # if "modify_existing" == postback_message:
    if "list_user_items" == postback_message:
        user_items = get_user_items(sender_id)
        send_carousel(sender_id, user_items)

    if "list_matches" in postback_message:
        matches = get_matches(postback_message['list_matches'])
        send_carousel()


def send_carousel(sender_id, generic_templates):
    r = requests.post("https://graph.facebook.com/v2.6/me/messages",

                      params={"access_token": PAT},

                      headers={"Content-Type": "application/json"},

                      data=json.dumps({
                          "recipient": {"id": sender_id},
                          "message": {
                              "attachment": {
                                  "type": "template",
                                  "payload": {
                                      "template_type": "generic",
                                      "elements": [",".join(generic_templates)]}}}
                      }))


def get_user_items(psid):
    item_list = []
    for item in repository.freight:
        if item[2] == psid:
            item_list.append(item)
    for item in repository.cargo:
        if item[2] == psid:
            item_list.append(item)

    return item_list


def get_matches():
    pass


if __name__ == '__main__':
    app.run()
