# Cyber-Sentinels_Phantomimmune-AI

# 🛡️ PhantomImmune AI — Cyber Immune Network

## 🚀 Overview

PhantomImmune AI is a **real-time cybersecurity prototype** that mimics a biological immune system.
It detects cyber attacks, traps attackers using a honeypot, learns from their behavior, generates immunity, and visualizes everything through a live dashboard.

---

## 🧠 Key Idea

Instead of simply blocking attackers, the system:

* Detects suspicious activity
* Engages attackers in a honeypot
* Learns from their behavior
* Generates **digital immunity (defense rules)**
* Records actions using a **blockchain-inspired system**

---

## 🎯 Features

* ⚠️ **Attack Detection**
  Tracks request patterns and identifies suspicious activity

* 🎭 **Honeypot Engine**
  Traps attackers by simulating a fake admin system

* 🧬 **Immunity Generator**
  Converts attack behavior into protection rules

* 🔗 **Blockchain Logging**
  Stores immunity rules in a tamper-resistant chain

* 📊 **Real-Time Dashboard**
  Visualizes system activity live

---

## 📊 Dashboard Highlights

The dashboard provides real-time insights:

* ⚠️ Attacks Detected
* 🎭 Honeypot Triggers
* 🧬 Immunity Rules Generated
* 🔗 Blockchain Blocks Created

### 🔌 Connected Clients

Displays active devices connected to the system
(Currently shows local admin dashboard)

### 📡 Real-Time Event Stream

Live logs including:

* System connection events
* Attack detection
* Honeypot activation
* Immunity generation
* Blockchain updates

---

## 🧱 System Architecture

```text
Attacker → Server (Detection)
                 ↓
            Honeypot
                 ↓
        Immunity Generator
                 ↓
          Blockchain Log
                 ↓
            Dashboard
```

---

## ⚙️ How It Works

### 1. Detection

* Tracks number of requests per IP
* Flags suspicious behavior after threshold

---

### 2. Honeypot Activation

* Suspicious users are not blocked immediately
* They are redirected to a fake admin system

---

### 3. Behavior Logging

System records:

* IP address
* Request payload
* Attempt count
* Timestamp

---

### 4. Immunity Generation

* Creates rule:

  * Block malicious IP
* Updates system protection

---

### 5. Blockchain Logging

* Stores immunity rule in a block
* Ensures traceability and integrity

---

### 6. Dashboard Visualization

* Displays all actions in real time
* Provides system transparency

---

## 🧪 Example Flow

```text
Attack → Detected → Honeypot Triggered
       → Immunity Generated → Blockchain Updated
       → Displayed on Dashboard
```

---

## 🛠️ Tech Stack

* Python (Flask) 🐍
* Flask-SocketIO ⚡
* HTML/CSS/JS Dashboard 💻
* Blockchain (Lightweight Simulation) 🔗

---

## ▶️ How to Run

```bash
pip install flask flask-socketio
python server.py
```

Open:

```
http://127.0.0.1:5000
```

---

## 📡 API Endpoint

### POST `/login`

#### Request:

```json
{
  "username": "admin",
  "password": "hack"
}
```

#### Response:

* Normal:

```json
{"status": "failed"}
```

* Honeypot:

```json
{"status": "success", "msg": "Welcome Admin"}
```

---

## 💡 Innovation

This system transforms cybersecurity from:

❌ Reactive blocking
➡️
✅ Proactive learning + adaptive defense

---

## 🔮 Future Enhancements

* 🌐 Multi-client protection network
* 🤖 AI-based attack classification
* 📍 Attacker geolocation tracking
* 🔐 Distributed blockchain network

---

## 🏆 Hackathon Value

* Real-time working system
* Unique concept: **Cyber Immune Network**
* Combines:

  * Detection
  * Deception
  * Learning
  * Visualization

---

## 🎤 One-Line Pitch

> “We don’t just block hackers — we trap them, learn from them, and turn their attacks into protection.”

---

