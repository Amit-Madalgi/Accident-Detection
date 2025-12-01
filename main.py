import firebase_admin
from firebase_admin import credentials, db
import time
import random
import os
from dotenv import load_dotenv

# 1. LOAD ENV VARIABLES
load_dotenv()
key_path = os.getenv("FIREBASE_CRED_PATH")
db_url = os.getenv("FIREBASE_DB_URL")

# 2. CONNECT TO FIREBASE
if not firebase_admin._apps: # Avoid initializing twice
    cred = credentials.Certificate(key_path)
    firebase_admin.initialize_app(cred, {'databaseURL': db_url})

print("✅ Connected to Firebase using .env!")

# 3. THE CRASH FUNCTION
def simulate_crash():
    print("\n🚗 Simulating Car Driving...")
    time.sleep(2)
    print("💥 BOOM! Crash Detected!")
    
    # Generate random vitals
    heart_rate = random.randint(110, 150) # High BPM (Stress)
    spo2 = random.randint(85, 95)         # Low Oxygen
    
    alert_data = {
        "status": "ACTIVE",
        "timestamp": int(time.time()),
        "severity": "CRITICAL",
        "patient_vitals": {
            "bpm": heart_rate,
            "spo2": spo2
        },
        "location": {
            "lat": 12.9716, 
            "lng": 77.5946
        },
        "assigned_hospital": {
            "name": "City Care Hospital",
            "lat": 12.9352,
            "lng": 77.6200
        }
    }
    
    # Write to Firebase
    ref = db.reference('alerts/crash_001')
    ref.set(alert_data)
    
    print(f"🚀 Alert Sent! BPM: {heart_rate}, SpO2: {spo2}%")

# --- MAIN EXECUTION (THIS IS WHAT RUNS IT) ---
if __name__ == "__main__":
    simulate_crash()  # <--- Make sure this line exists!