from venmo_api import Client
from dotenv import load_dotenv
from notifiers import get_notifier
from datetime import datetime

from utils import get_env, env_vars, get_month, Venmo, Telegram

def main(now):
  """
  The main function which initiates the script.
  """

  load_dotenv()  # take environment variables from .env.
  actualVars = []
  for var in env_vars:
    actualVars.append(get_env(var))

  access_token, chat_id, bot_token, k_friend_id, c_friend_id, w_friend_id, j_friend_id = actualVars

  month = get_month(now)
  venmo = Venmo(access_token)
  telegram = Telegram(bot_token, chat_id)

  friends =[
    {
      "name": "Z",
      "id": z_friend_id,
      "amount": 45.00,
    },
#     {
#       "name": "J",
#       "id": u_friend_id,
#       "amount":"40",
#     },
#     {
#       "name": "I",
#       "id": i_friend_id,
#       "amount":"40"
#     },
  ]

  successfulRequests = []
  expectedRequests = len(friends)

  for friend in friends:
    name = friend["name"]
    id = friend["id"]
    description = "T-Mobile bill dated " + month + " — Sent by Ilya's assistant iHustler"
    amount = friend["amount"]
    message = f"""✅ Good news everyone!

I have successfully requested money from {name}.

— iHustler 🤵🏻‍♂️
    """
    
    message_fail = f"""❌ Bad news everyone!

Something went wrong when I requested money from {name}.

— iHustler 🤵🏻‍♂️
    """
    success = venmo.request_money(id, amount, description, telegram.send_message(message))
    if success:
      successfulRequests.append(success)
    else:
      telegram.send_message(message)

  if len(successfulRequests) == expectedRequests:
    print("✅ Ran script successfully and sent " + str(expectedRequests) + " Venmo requests.")
  else:
    print("❌ Something went wrong. Only sent " + str(len(successfulRequests)) + "/" + str(expectedRequests) + " venmo requests.")

now = datetime.now()
main(now)
