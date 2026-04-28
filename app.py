from flask import Flask, request, jsonify
from flask_socketio import SocketIO, emit
from datetime import datetime
import hashlib, json, sys

app = Flask(__name__)
app.config['SECRET_KEY'] = 'phantomimmune-secret'
socketio = SocketIO(app, cors_allowed_origins="*", async_mode='threading')

# ================= BLOCKCHAIN MODULE =================
blockchain = []

def create_block(index, timestamp, data, previous_hash):
    block = {
        "index": index,
        "timestamp": timestamp,
        "data": data,
        "previous_hash": previous_hash
    }
    block_hash = hashlib.sha256(json.dumps(block, sort_keys=True).encode()).hexdigest()
    block["hash"] = block_hash
    return block

def add_block(data):
    previous_hash = blockchain[-1]["hash"] if blockchain else "0"
    index = len(blockchain)
    timestamp = datetime.now().isoformat()
    new_block = create_block(index, timestamp, data, previous_hash)
    blockchain.append(new_block)
    print("[BLOCKCHAIN] New block added", flush=True)
    socketio.emit('blockchain_updated', {
        "ip": "system",
        "message": f"Block {index} added to PhantomImmune AI blockchain",
        "block": new_block
    })
    return new_block
# =====================================================

# State tracking
request_count = {}
honeypot_ips = set()
blocked_ips = set()

HONEYPOT_THRESHOLD = 3
IMMUNITY_THRESHOLD = 6

def log_honeypot(ip, payload, attempts):
    entry = {
        "ip": ip,
        "payload": payload,
        "attempts": attempts,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    print("\n🪤 HONEYPOT LOG", flush=True)
    print(f"📍 Attacker IP   : {ip}", flush=True)
    print(f"🔢 Attempt Count : {attempts}", flush=True)
    print(f"📦 Payload       : {payload}", flush=True)
    print(f"🕒 Timestamp     : {entry['timestamp']}", flush=True)
    print(f"🟢 Status        : Serving fake admin response", flush=True)
    print("="*40 + "\n", flush=True)

def generate_immunity(ip):
    rule = {"action": "block_ip", "ip": ip}
    blocked_ips.add(ip)
    print(f"\n[IMMUNITY] Generated for IP: {ip}", flush=True)
    print(f"📜 Rule Applied  : {rule}", flush=True)
    add_block(rule)
    socketio.emit('immunity_generated', {
        "ip": ip,
        "message": f"PhantomImmune AI rule generated and IP blocked",
        "rule": rule
    })
    print("="*40 + "\n", flush=True)
    return rule

@app.route('/login', methods=['POST'])
def login():
    ip = request.remote_addr
    payload = request.get_json(silent=True) or request.form.to_dict() or request.get_data(as_text=True)
    
    request_count[ip] = request_count.get(ip, 0) + 1
    attempts = request_count[ip]
    
    if ip in blocked_ips:
        print(f"🚫 BLOCKED: {ip} attempted access but immunity is active", flush=True)
        socketio.emit('attack_detected', {
            "ip": ip,
            "message": f"Blocked IP attempted access (attempt #{attempts})"
        })
        return jsonify({"status": "error", "msg": "IP blocked by PhantomImmune AI"}), 403
    
    if attempts > IMMUNITY_THRESHOLD:
        if ip not in blocked_ips:
            generate_immunity(ip)
        return jsonify({"status": "error", "msg": "IP blocked by PhantomImmune AI"}), 403
    
    if attempts > HONEYPOT_THRESHOLD:
        if ip not in honeypot_ips:
            honeypot_ips.add(ip)
            print(f"👁️  IP {ip} crossed threshold ({HONEYPOT_THRESHOLD}). Entering honeypot mode...", flush=True)
            socketio.emit('honeypot_triggered', {
                "ip": ip,
                "message": f"IP entered PhantomImmune AI honeypot after {attempts} requests",
                "payload": payload
            })
        log_honeypot(ip, payload, attempts)
        return jsonify({"status": "success", "msg": "Welcome Admin"}), 200
    
    print(f"📝 Normal request from {ip} (Attempt {attempts}/{HONEYPOT_THRESHOLD})", flush=True)
    socketio.emit('attack_detected', {
        "ip": ip,
        "message": f"Suspicious request detected (attempt {attempts}/{HONEYPOT_THRESHOLD})"
    })
    return jsonify({"status": "failed", "msg": "Invalid credentials"}), 401

@app.route('/blockchain', methods=['GET'])
def get_blockchain():
    return jsonify({"chain": blockchain, "length": len(blockchain)}), 200

@app.route('/status', methods=['GET'])
def status():
    return jsonify({
        "total_ips_tracked": len(request_count),
        "active_honeypot_ips": len(honeypot_ips),
        "blocked_ips": list(blocked_ips),
        "blockchain_blocks": len(blockchain)
    }), 200

@socketio.on('connect')
def handle_connect():
    print("🔌 Client connected to PhantomImmune AI SocketIO", flush=True)
    emit('connected', {"message": "Connected to PhantomImmune AI"})

@socketio.on('disconnect')
def handle_disconnect():
    print("🔌 Client disconnected from PhantomImmune AI SocketIO", flush=True)

if __name__ == '__main__':
    print("\n" + "="*50, flush=True)
    print("🛡️  PHANTOMIMMUNE AI - REAL-TIME HONEYPOT", flush=True)
    print("="*50, flush=True)
    print("📡 SocketIO enabled on port 5000", flush=True)
    print("="*50 + "\n", flush=True)
    socketio.run(app, host='0.0.0.0', port=5000, debug=False)