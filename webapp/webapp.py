from flask import Flask, render_template
import os

app = Flask(__name__)

# File path of the alerts.txt in the parent directory
ALERTS_FILE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'alerts.txt')

def read_alerts():
    alerts = []
    if os.path.exists(ALERTS_FILE_PATH):
        with open(ALERTS_FILE_PATH, 'r') as file:
            raw_data = file.read().strip().split("\n\n")  # Split each alert block
            for block in raw_data:
                lines = block.split("\n")
                alert = {
                    'ticker': lines[0].split(": ")[1],
                    'data': lines[1:]  # All remaining rows
                }
                alerts.append(alert)
    return alerts

@app.route('/')
def index():
    alerts = read_alerts()
    return render_template('index.html', alerts=alerts)

if __name__ == '__main__':
    app.run(debug=True)

