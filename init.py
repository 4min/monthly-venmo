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

  access_token, chat_id, bot_token, i_friend_id, j_friend_id, k_friend_id, l_friend_id, s_friend_id, y_friend_id, p_friend_id = actualVars

  month = get_month(now)
  venmo = Venmo(access_token)
  telegram = Telegram(bot_token, chat_id)

  friends =[
    {
      "name": "I",
      "id": i_friend_id,
      "amount": 50.00,
      "addons": "and YTP",
    },
    {
      "name": "J",
      "id": j_friend_id,
      "amount": 59.00,
      "addons": "and YTP + D++ + MX",
    },
    {
      "name": "K",
      "id": k_friend_id,
      "amount": 45.00,
      "addons": "",
    },
    {
      "name": "L",
      "id": l_friend_id,
      "amount": 35.00,
      "addons": "and YTP",
    },
    {
      "name": "S",
      "id": s_friend_id,
      "amount": 50.00,
      "addons": "and YTP",
    },
    {
      "name": "Y",
      "id": y_friend_id,
      "amount": 56.00,
      "addons": "and D++ + MX + PP",
    },
    {
      "name": "P",
      "id": p_friend_id,
      "amount": 85.00,
      "addons": "and D+ + PP",
    },
  ]

  successfulRequests = []
  expectedRequests = len(friends)

  for friend in friends:
    name = friend["name"]
    id = friend["id"]
    description = "TMO bill dated " + month + " " + friend["addons"]
    amount = friend["amount"]
    # print(venmo.get_user_id_by_username(id))
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
