import requests
import json

get_started = {
    "get_started": {
        "payload": "messaging_start"
    }
}

persistent_menu = {
    "persistent_menu": [
        {
            "locale": "default",
            "call_to_actions": [
                {
                    "title": "Új/szerkesztés",
                    "type": "nested",
                    "call_to_actions": [
                        {
                            "title": "Új raktér",
                            "type": "postback",
                            "payload": "new_cargo"
                        },
                        {
                            "title": "Új rakomány",
                            "type": "postback",
                            "payload": "new_freight"
                        },
                        {
                            "title": "Meglévők módosítása",
                            "type": "postback",
                            "payload": "modify_existing"
                        }
                    ]
                },
                {
                    "title": "Párok böngészése",
                    "type": "postback",
                    "payload": "browse_matches"
                },
                {
                    "type": "nested",
                    "title": "Segítség",
                    "call_to_actions": [
                        {
                            "title": "Használati útmutató",
                            "type": "postback",
                            "payload": "tutorial"
                        },
                        {
                            "title": "Fejlesztő weboldala",
                            "type": "postback",
                            "payload": "dev_webpage"
                        }
                    ]

                }
            ]
        }
    ]
}

greeting = {
    "greeting": [
        {
            "locale": "default",
            "text": "Üdvözlöm {{user_first_name}}!"
        }
    ]
}


def update_profile():
    url = "https://graph.facebook.com/v2.6/me/messenger_profile?access_token=EAAO096YLGpkBANk7IyOnF3vuhkTg56CZBFQSS3gTad43hnFBOXfI9pmUp3Xogs7uEj01ZBGEb2aXmd30ZA9BTM1XQcCghDSzycjf8X3rhM6pTufvkcC9Vh7hddxLIuMTfYundfeEcaaPJo1XajJgFxD6OKjr0NWUFXh8j4sDQZDZD"

    payload = {
        "get_started": get_started["get_started"],
        "greeting": greeting["greeting"],
        "persistent_menu": persistent_menu["persistent_menu"]
    }

    print(payload)

    payload = json.dumps(payload)

    headers = {
        'content-type': "application/json",
    }

    print(payload)

    response = requests.request("POST", url, data=payload.encode('utf-8'), headers=headers)

    print(response.text)


update_profile()
