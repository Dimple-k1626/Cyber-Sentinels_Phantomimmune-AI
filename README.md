# Cyber-Sentinels_Phantomimmune-AI

# 🧬 PhantomImmune AI

### A Self-Evolving Cyber Immune System with Active Deception + Blockchain Security

---

## 🚀 Overview

**PhantomImmune AI** is an intelligent cybersecurity system inspired by the biological immune system, enhanced with **Blockchain-based threat logging**.

It not only detects and responds to cyber threats in real-time but also **stores every attack immutably**, ensuring transparency and tamper-proof security records.

---

## 🧠 Core Concept

> Detect → Classify → Respond → Record → Learn

* **Detect** → Identify suspicious activity
* **Classify** → Assign threat level
* **Respond** → Take automated action
* **Record** → Store event in blockchain
* **Learn** → (Future) Improve using AI

---

## ⚙️ Features

### 🔗 Real-Time Multi-Client System

* Socket.IO based communication
* Supports multiple devices (Laptop + Mobile)
* Auto-reconnection + heartbeat system

---

### 🧠 Threat Classification Engine

* Categorizes threats into:

  * LOW ⚪
  * MEDIUM 🟡
  * HIGH 🔴
* Based on attack behavior and frequency

---

### 🛡️ Automated Immune Response

* System reacts instantly:

  * LOW → Monitor
  * MEDIUM → Honeypot redirection
  * HIGH → Block attacker

---

### 🎭 Active Deception (Honeypots)

* Traps attackers in simulated environments
* Helps analyze malicious behavior

---

### 🔐 Blockchain-Based Security Logging ✅

All attack events are stored in a blockchain structure inside `app.py`.

#### 🔗 Block Structure:

```json
{
  "index": 1,
  "timestamp": "2026-04-28 10:30:00",
  "data": {
    "ip": "192.168.1.10",
    "event": "attack_detected",
    "level": "HIGH"
  },
  "previous_hash": "abc123",
  "hash": "def456"
}
```

#### ⚡ Features:

* Immutable attack logs
* Tamper-proof history
* Linked blocks using hashes
* Transparent event tracking

---

### 🌐 Multi-Device Awareness

* Tracks connected clients
* Maintains:

  * Device status
  * Last seen timestamps
* Enables distributed cyber defense

---

### 📊 Real-Time Dashboard

* Displays:

  * Active devices
  * Threat feed
  * Immune responses
* SOC-style monitoring

---

## 🏗️ Tech Stack

| Layer          | Technology                 |
| -------------- | -------------------------- |
| Backend        | Python (Flask + Socket.IO) |
| Frontend       | HTML, CSS, JavaScript      |
| Communication  | WebSockets                 |
| Security Layer | Custom Blockchain (Python) |

---

## 📁 Project Structure

```bash
PhantomImmune-AI/
│── backend/
│   ├── app.py              # Server + Blockchain logic
│
│── clients/
│   ├── client.py
│   ├── continuous_client.py
│
│── frontend/
│   ├── index.html
│
│── progress.md
│── README.md
```

---

## ⚡ Getting Started

### 1️⃣ Clone Repository

```bash
git clone https://github.com/Dimple-k1626/Cyber-Sentinels_Phantomimmune-AI.git
cd Phantomimmune-AI
```

---

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 3️⃣ Run Server

```bash
python app.py
```

---

### 4️⃣ Run Clients

```bash
python client.py
```

```bash
python continuous_client.py
```

---

## 🧪 Example Output

```bash
⚠️ [HIGH] 192.168.1.10 → Intrusion detected
🎭 Honeypot triggered
🛡️ BLOCKED attacker
⛓️ Block added to blockchain
```

---

## 🔗 How Blockchain Works in This Project

1. Attack is detected
2. Threat level is classified
3. Action is taken (block/honeypot/monitor)
4. Event is stored as a **new block**
5. Block is hashed and linked to previous block

---

## 🧭 Roadmap

### ✅ Completed

* Real-time communication
* Threat detection & classification
* Automated immune response
* Blockchain logging

### 🔄 Next

* AI-based anomaly detection
* Predictive threat intelligence

---

## 🏆 Hackathon Advantages

✅ Bio-inspired cyber defense
✅ Real-time distributed system
✅ Active deception (honeypots)
✅ Blockchain-based security logging 🔥
✅ Highly scalable architecture

---

## 🤝 Contributors

* Team Cyber Sentinels

---

## 📜 License

For educational and hackathon use

---

## ⭐ Final Note

PhantomImmune AI is not just a detection system —
it is a **self-evolving cyber defense organism**.

---

🔥 *Securing systems like an immune system — now with Blockchain trust.*
