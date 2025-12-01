import firebase_admin
from firebase_admin import credentials, db
import time
import random
import os
from dotenv import load_dotenv  # Import this

# 1. LOAD ENV VARIABLES
load_dotenv() # This reads the .env file

# Get the values
key_path = os.getenv("FIREBASE_CRED_PATH")
db_url = os.getenv("FIREBASE_DB_URL")

# Check if they exist (Good for debugging)
if not key_path or not db_url:
    raise ValueError("Error: Missing keys in .env file!")

# 2. CONNECT TO FIREBASE
cred = credentials.Certificate(key_path) # Use the variable

firebase_admin.initialize_app(cred, {
    'databaseURL': db_url # Use the variable
})

print("Connected to Firebase using .env!")

# ... rest of your code remains the same ...