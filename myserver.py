from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Server is running !"

def start():
    app.run(debug=True)

# ฟังก์ชันนี้ถูกเรียกในไฟล์ main.py
def server_on():
    start()
