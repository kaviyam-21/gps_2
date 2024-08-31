import serial
import flask
import threading

app = flask.Flask(__name__)

# Store the latest GPS data
latest_gps = {'lat': None, 'lng': None}

# Serial port configuration
ser = serial.Serial('COM3', 115200, timeout=1)  # Adjust COM port as necessary

def read_serial():
    while True:
        line = ser.readline().decode('utf-8').strip()
        if line:
            try:
                lat, lng = map(float, line.split(','))
                latest_gps['lat'] = lat
                latest_gps['lng'] = lng
            except ValueError:
                pass

@app.route('/get_gps', methods=['GET'])
def get_gps():
    return flask.jsonify(latest_gps)

if __name__ == '__main__':
    # Start serial reading in a separate thread
    serial_thread = threading.Thread(target=read_serial)
    serial_thread.daemon = True
    serial_thread.start()

    app.run(host='0.0.0.0', port=5000, debug=True)

