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
                            "type": "postback",
                            "title": "Új rakomány",
                            "payload": "new_freight"
                        },
                        {
                            "type": "postback",
                            "title": "Meglévők módosítása",
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
        },
        {
            "title": "Új/szerkesztés",
            "type": "nested",
            "call_to_actions": [
                {
                    "title": "Pay Bill",
                    "type": "postback",
                    "payload": "PAYBILL_PAYLOAD"
                },
                {
                    "type": "web_url",
                    "title": "Latest News",
                    "url": "https://www.messenger.com/",
                    "webview_height_ratio": "full"
                }
            ]
        }
    ]
}
