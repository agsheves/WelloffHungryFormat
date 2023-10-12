# Test bed for the main AI ERM components
from utilities import Spinner
import time

print('Welcome to the ERM Sandbox')
with Spinner('Loading'):
  time.sleep(3)
print("\nReady Player 1.")

user_name = input("Please enter your name so we can get started ")
print(f"Hi {user_name}, what can I help you with today?")

