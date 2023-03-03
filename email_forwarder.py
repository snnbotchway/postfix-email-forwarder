#!/usr/bin/env python3
import email
import sys
import requests

message_bytes = sys.stdin.buffer.read()
message = email.message_from_bytes(message_bytes)

recipient = message.get("To").strip("<>")

subject = message.get("Subject")
body = ""
for part in message.walk():
    if part.get_content_type() == "text/plain":
        body = part.get_payload()

API_KEY = "qr!k1x4c@(!04s0a1_e7ia9patl38!qg_y7f_#ma2vt9r5pp6oa4o60ro!gnkdh#"

payload = {
    "key": API_KEY,
    "emailTo": [recipient],
    "emailFrom": f"solomonbotchway7@gmail.com",
    "emailBody": body,
    "senderName": "SOLOMON",
    "subject": subject,
    "callBackUrl": "",
}

response = requests.post(
    "https://email.nalosolutions.com/smsbackend/clientapi/Nal_resl/send-email/",
    json=payload,
)

if response.status_code != 200:
    print(
        f"Error calling email API: {response.status_code} {response.reason} {response.content}",
        file=sys.stderr,
    )
    sys.exit(1)
