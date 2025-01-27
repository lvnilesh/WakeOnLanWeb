from flask import Flask, render_template
import subprocess

SCRIPT = 'wake.py'
# Modify Mac Address below
MAC_ADDRESS = 'XX:XX:XX:XX:XX:XX'

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/run-script')
def run_script():
    subprocess.call(['python', SCRIPT, MAC_ADDRESS])
    return "Turned on PC"

if __name__ == '__main__':
    app.run(debug=True)
