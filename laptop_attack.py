#!/usr/bin/env python3
"""
💻 PhantomImmune AI - Laptop Brute-Force Attacker
Run this alongside your mobile (Termux) attack to test multi-IP detection.
"""
import requests, time, sys

# ⚠️ UPDATE THIS IF YOUR SERVER IP CHANGED
TARGET = "http://10.30.136.65:5000/login"
ATTEMPTS = 8

print("\n" + "="*55)
print("💻 PHANTOMIMMUNE AI - LAPTOP ATTACKER")
print("="*55)
print(f"🎯 Target   : {TARGET}")
print(f"🔄 Attempts : {ATTEMPTS}")
print(f"🌐 Source   : Laptop (Windows)")
print("-"*55 + "\n")

for i in range(1, ATTEMPTS + 1):
    try:
        payload = {"username": "admin", "password": f"laptop_hack_{i}"}
        res = requests.post(TARGET, json=payload, timeout=5)
        
        if res.status_code == 401:
            phase = "❌ CREDENTIALS REJECTED"
        elif res.status_code == 200 and "Welcome Admin" in res.text:
            phase = "🟢 HONEYPOT TRAPPED"
        elif res.status_code == 403:
            phase = "🚫 IMMUNITY BLOCKED"
        else:
            phase = "⚠️ UNKNOWN"
            
        print(f"Attempt {i:2d}/{ATTEMPTS} | HTTP {res.status_code} | {phase}")
        print(f"   📤 {res.text.strip()}\n")
        
    except Exception as e:
        print(f"Attempt {i:2d}/{ATTEMPTS} | 🔌 ERROR: {e}\n")
        
    time.sleep(0.6)  # Realistic pacing

print("✅ Laptop attack complete. Check dashboard for dual-IP tracking.\n")