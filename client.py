import socketio

# Connect to the PhantomImmune Server
sio = socketio.Client()

@sio.event
def connect():
    print("✅ Connected to PhantomImmune AI Server")
    # Register this device so it shows on the dashboard
    sio.emit('register_device', {'name': 'Laptop Client'})

@sio.event
def disconnect():
    print("❌ Disconnected from Server")

@sio.event
def attack_detected(data):
    print(f"⚠️ ALERT: {data['message']}")

@sio.event
def honeypot_triggered(data):
    print(f"🎭 TRAP: {data['message']}")

@sio.event
def immunity_generated(data):
    print(f"🛡️ IMMUNITY: {data['message']}")

if __name__ == '__main__':
    print("🚀 Starting Laptop Client...")
    try:
        sio.connect('http://10.68.101.105:5000')
        sio.wait()
    except KeyboardInterrupt:
        sio.disconnect()