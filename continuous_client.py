import socketio
import sys
import time
import threading

# ⚙️ CONFIGURATION
# CHANGE THIS URL TO YOUR LAPTOP'S IP ADDRESS
SERVER_URL = "http://10.68.101.105:5000"

# CHANGE THIS TO "mobile" IF RUNNING ON TERMUX
DEVICE = "laptop" 

# Initialize Socket.IO client
sio = socketio.Client(
    reconnection=True,
    reconnection_attempts=999,
    reconnection_delay=1,
    reconnection_delay_max=5
)

@sio.event
def connect():
    print(f"✅ [{DEVICE.upper()}] CONNECTED to PhantomImmune AI")
    # Register with server so it shows on dashboard
    sio.emit('client_register', {'device': DEVICE, 'status': 'online'})

@sio.event
def disconnect():
    print(f"⚠️ [{DEVICE.upper()}] CONNECTION LOST. Auto-reconnecting...")

@sio.event
def attack_detected(data):
    print(f"⚠️ {data.get('ip', '?')} → {data.get('message', '')}")

@sio.event
def honeypot_triggered(data):
    print(f"🎭 {data.get('ip', '?')} → {data.get('message', '')}")

@sio.event
def immunity_generated(data):
    print(f"🧬 {data.get('ip', '?')} → {data.get('message', '')}")

def heartbeat_loop():
    """Sends periodic pings to keep WebSocket alive"""
    while True:
        if sio.connected:
            sio.emit('ping', {'device': DEVICE})
        time.sleep(15)

if __name__ == "__main__":
    print(f"🔗 Connecting to {SERVER_URL}...")
    print("🟢 Client will stay connected FOREVER. Press Ctrl+C to exit.\n")
    try:
        sio.connect(SERVER_URL)
        threading.Thread(target=heartbeat_loop, daemon=True).start()
        sio.wait()
    except KeyboardInterrupt:
        print("\n⛔ Disconnecting...")
        sys.exit(0)
    except Exception as e:
        print(f"❌ Error: {e}")