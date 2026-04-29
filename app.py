from flask import Flask, request, jsonify
from flask_socketio import SocketIO, emit
from datetime import datetime
import hashlib, json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'phantomimmune-pro'
# CORS enabled for dashboard communication
socketio = SocketIO(app, cors_allowed_origins="*", async_mode='threading')

# ================= GLOBAL STATE =================
connected_clients = {}    # Tracks live socket connections
request_counts = {}       # Tracks attack attempts per IP
blocked_ips = set()       # IPs permanently banned
blockchain = []           # Immutable log of immunity rules

HONEYPOT_THRESHOLD = 3
IMMUNITY_THRESHOLD = 6

# ================= BLOCKCHAIN MODULE =================
def create_block(data):
    prev_hash = blockchain[-1]["hash"] if blockchain else "0"
    block = {
        "index": len(blockchain),
        "timestamp": datetime.now().isoformat(),
        "data": data,
        "previous_hash": prev_hash
    }
    # Generate Hash
    block["hash"] = hashlib.sha256(json.dumps(block, sort_keys=True).encode()).hexdigest()
    blockchain.append(block)
    
    # Emit to Dashboard
    socketio.emit('blockchain_updated', {
        "ip": "system",
        "message": f"Block {block['index']} added - IP {data.get('ip', 'unknown')} blocked"
    })

# ================= CLIENT TRACKING (SOCKET.IO) =================
@socketio.on('connect')
def on_connect():
    ip = request.remote_addr
    if ip not in connected_clients:
        connected_clients[ip] = {"ip": ip, "name": "New Device", "status": "Online"}
        # Broadcast updated list to ALL dashboards
        socketio.emit('clients_update', list(connected_clients.values()))
        print(f"🔌 Client Connected: {ip}")

@socketio.on('disconnect')
def on_disconnect():
    ip = request.remote_addr
    if ip in connected_clients:
        del connected_clients[ip]
        socketio.emit('clients_update', list(connected_clients.values()))
        print(f"🔌 Client Disconnected: {ip}")

@socketio.on('register_device')
def on_register(data):
    ip = request.remote_addr
    if ip in connected_clients:
        connected_clients[ip]['name'] = data.get('name', 'Unknown Device')
        socketio.emit('clients_update', list(connected_clients.values()))
        print(f"📱 Device Registered: {connected_clients[ip]['name']}")

# ================= MAIN SECURITY GATEWAY =================
@app.route('/login', methods=['POST'])
@app.route('/api/data', methods=['POST'])
def security_gateway():
    ip = request.remote_addr
    request_counts[ip] = request_counts.get(ip, 0) + 1
    attempts = request_counts[ip]

    # 1. 🔒 IMMUNITY TRIGGER (Attempts > 6)
    if attempts > IMMUNITY_THRESHOLD:
        if ip not in blocked_ips:
            blocked_ips.add(ip)
            create_block({"action": "block_ip", "ip": ip})
            socketio.emit('immunity_generated', {
                "ip": ip,
                "message": f"🛡️ IMMUNITY ACTIVATED: {ip} is permanently blocked."
            })
        return jsonify({"error": "Access Denied by PhantomImmune AI"}), 403

    # 2. 🎭 HONEYPOT TRAP (Attempts 4, 5, 6)
    if attempts > HONEYPOT_THRESHOLD:
        socketio.emit('honeypot_triggered', {
            "ip": ip,
            "message": f"🕸️ HONEYPOT TRIGGERED: {ip} is trapped in a fake system."
        })
        return jsonify({"status": "success", "msg": "Welcome Admin (Fake Response)"}), 200

    # 3. ⚠️ NORMAL ATTACK (Attempts 1, 2, 3)
    socketio.emit('attack_detected', {
        "ip": ip,
        "message": f"🚨 Attack Detected: Failed login attempt #{attempts}"
    })
    
    return jsonify({"status": "failed", "msg": "Invalid Credentials"}), 401

# ================= RUN SERVER =================
if __name__ == '__main__':
    print("\n" + "="*60)
    print("🛡️  PHANTOMIMMUNE AI - CYBER IMMUNE SYSTEM")
    print("="*60)
    print("✅ Server running on http://0.0.0.0:5000")
    print("✅ Dashboard: Open dashboard.html")
    print("✅ Client: Run client.py to see devices connect")
    print("="*60 + "\n")
    
    socketio.run(app, host='0.0.0.0', port=5000, debug=False)