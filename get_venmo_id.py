from datetime import datetime
from utils import get_env, verify_env_vars, env_vars, get_env_vars, Venmo
from dotenv import load_dotenv

def main():
  load_dotenv()
  print(f'This script retrieves a Venmo user''s ID by username\n')

  access_token, *tail = get_env_vars(env_vars)

  venmo = Venmo(access_token)

  while True:
    username = input("Enter a Venmo username (or 'exit' to quit): ")
    if username.lower() == 'exit':
        break

    user_id = venmo.get_user_id_by_username(username)
    if user_id:
        print(f"User ID for @{username}: {user_id}")
    else:
        print("User ID not found.")

main()
