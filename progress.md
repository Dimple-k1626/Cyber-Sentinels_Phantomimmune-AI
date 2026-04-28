# 🛡️ PhantomImmune AI - Progress.md

# TEAM NAME = Cyber Sentinels

# Team Members : Dikshit.P, G.Sanjeet, Dimple.K, Dimple.S

# Problem Statement: “Current cybersecurity systems are isolated and reactive. We propose a cyber immune network that connects multiple clients to a central                             intelligence system, traps attackers using a honeypot, learns their behavior, and generates shareable immunity using a blockchain-based                            approach".

## 📌 Project Objective: 🎯 PhantomImmune AI – Project Objective
The objective of PhantomImmune AI is to design and develop a self-adaptive cybersecurity defense system that can detect, analyze, and respond to cyber threats in real time using a combination of honeypot deception, automated immunity rules, and blockchain-based security logging.
🛡️ Core Objectives
1. Real-Time Threat Detection
To continuously monitor incoming network requests and identify suspicious or malicious activity in real time.
2. Intelligent Honeypot Mechanism
To mislead attackers by redirecting suspicious IPs into a controlled honeypot environment, allowing safe observation of attack behavior.
3. Automated Immunity System
To automatically generate defensive rules (such as IP blocking) when repeated malicious behavior is detected, ensuring proactive protection without human intervention.
4. Blockchain-Based Security Logging
To maintain an immutable and tamper-proof record of all security events (attacks, blocks, and system responses) using a lightweight blockchain system.
5. Live SOC Visualization
To provide a real-time Security Operations Center (SOC) dashboard that visualizes:
Attacks
Honeypot triggers
Immunity actions
Blockchain updates
6. Cybersecurity Awareness & Simulation
To simulate real-world cyberattack scenarios for educational, research, and hackathon purposes, helping demonstrate how modern SOC systems operate.
🚀 Final Goal
To build a self-evolving cyber defense prototype that mimics an intelligent security ecosystem capable of:
Detecting → Deceiving → Defending → Recording cyber threats in real time.


# Checkpoint 1 (Backend Core)
🎯 Objective

Build a working backend that detects attacks, tracks IPs, and responds in real time.

✅ Completed
🔐 Backend Setup
Flask + Socket.IO server created
APIs: /login, /status, /blockchain
🧠 Threat Detection
IP request tracking implemented
Rules:
Honeypot → > 3 requests
Block/IP immunity → > 6 requests
🪤 Honeypot System
Suspicious IPs diverted to honeypot
Fake admin response + full logging
🛡️ Immunity System
Auto-block malicious IPs
Rule generated and stored in memory
⛓️ Blockchain Logging
Each security action stored as a block
SHA-256 hashing used
Real-time updates via Socket.IO
📡 Real-Time Events
attack_detected
honeypot_triggered
immunity_generated
blockchain_updated
⚙️ Status

✔ Backend fully working
✔ Real-time system active
✔ Security logic implemented

🚀 Result

A working cyber defense backend prototype that:

Detects → Traps → Blocks → Logs → Streams events in real time

# Checkpoint 2 Frontend Progress (dashboard.html)

## 🎨 UI Design (SOC Dashboard)
- Cybersecurity-themed UI designed
- Dark mode SOC interface implemented
- Glass + neon style UI elements used
- Responsive layout for different screen sizes

---

## 📊 Live Statistics Panel
- Attacks Detected counter
- Honeypot Triggers counter
- Immunity Rules counter
- Blockchain Blocks counter

All counters update in real time.

---

## 📡 Real-Time Event Stream
- Live logs panel added
- Displays incoming events instantly:
  - Attack detected alerts
  - Honeypot activations
  - IP immunity generation
  - Blockchain updates
- Auto-scroll log system implemented
- Max log limit (50 entries) for performance

---

## 🔌 Socket.IO Integration
- Connected to Flask backend server
- Handles real-time events:
  - attack_detected
  - honeypot_triggered
  - immunity_generated
  - blockchain_updated
- Auto reconnect feature implemented

---

## 🧠 SOC Features
- Live connection status indicator
- Animated status pulse system
- Color-coded log system:
  - Red → Attack
  - Yellow → Honeypot
  - Green → Immunity
  - Purple → Blockchain
- System health monitoring UI

---

## 🧪 Frontend Status
✔ Real-time dashboard working  
✔ Socket connection stable  
✔ Logs updating live  
✔ UI fully responsive  
✔ SOC visualization complete  

# Checkpoint 3 Laptop Brute Force Attacker

# 🎯 Objective
Simulate a real-world brute-force attack from a laptop to test multi-IP detection, honeypot triggering, and automatic blocking.

✅ Implementation
💻 Attack Script


Python-based attacker using requests


Sends multiple login attempts to /login


Simulates brute-force password attacks



# 🔄 Attack Behavior


Configurable attempts (default: 8 attempts)


Sends payload:
{ "username": "admin", "password": "laptop_hack_i" }


Adds delay (0.6s) for realistic attack simulation



# 📊 Response Phases Observed


401 → ❌ Invalid credentials


200 → 🟢 Honeypot activated (fake admin access)


403 → 🚫 IP blocked (immunity triggered)



📡 System Validation


Confirms backend detects repeated attacks


Triggers:


Honeypot after threshold


Immunity (IP block) after higher threshold




Events visible on live SOC dashboard



# 🌐 Multi-Source Testing


Works alongside mobile (Termux) attacker


Demonstrates multi-IP attack simulation


Validates system handles multiple attackers simultaneously



# ⚙️ Status
✔ Brute-force simulation working
✔ Honeypot triggering verified
✔ Auto-blocking verified
✔ Real-time dashboard updates confirmed

# 🚀 Outcome
A successful simulation of a realistic attacker system that:

Sends attacks → Triggers defense → Gets trapped → Gets blocked → Logged in blockchain → Visualized live


# Checkpoint 4 (Real-Time Client System)

# 🎯 Objective

Enable continuous real-time monitoring clients (laptop/mobile) that stay connected to the server and receive live security events.

# ✅ Implementation
🔗 Socket.IO Client Setup
Python-based client using socketio
Connects to backend server (app.py)
Supports auto-reconnection with retry logic
# 💻 Continuous Client System
Persistent connection to server (runs indefinitely)
Heartbeat mechanism added:
Sends periodic ping every 15 seconds
Keeps connection alive
# 📡 Real-Time Event Listener

Client receives and displays:

⚠️ attack_detected → suspicious activity
🎭 honeypot_triggered → attacker trapped
🧬 immunity_generated → IP blocked
# 🖥️ Device Registration
Client identifies itself (laptop / mobile)
Sends registration event to server
Enables multi-device visibility on dashboard
# 🔄 Auto-Reconnection
Handles connection drops automatically
Retries connection with delay strategy
Ensures uninterrupted monitoring
# 🧪 Multi-Client Support
Works with:
Laptop client
Mobile (Termux) client
Enables distributed monitoring system
Simulates real SOC environment
# ⚙️ Status

✔ Continuous client working
✔ Real-time event streaming verified
✔ Multi-device connection supported
✔ Auto-reconnect + heartbeat stable

# 🚀 Outcome

A working real-time monitoring layer that:

Connects → Listens → Streams alerts → Maintains connection → Supports multiple devices

# 📌 Result

PhantomImmune AI now behaves like a distributed SOC system, where multiple clients can:

Monitor attacks live
Receive instant alerts
Stay connected continuously
