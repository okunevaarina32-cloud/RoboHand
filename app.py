from flask import Flask, render_template, redirect
import serial
import threading

app = Flask(__name__)

ser = serial.Serial('COM3', 9600, timeout=1)

state = "0"

def read_serial():
    global state
    while True:
        if ser.in_waiting:
            state = ser.readline().decode().strip()

threading.Thread(target=read_serial, daemon=True).start()

@app.route("/")
def index():
    if state == "0":
        text = "Рука разжата"
    elif state == "1":
        text = "Сжата без предмета"
    elif state == "2":
        text = "Сжата С ПРЕДМЕТОМ"
    else:
        text = "Нет данных"

    return render_template("index.html", status=text)

@app.route("/close")
def close():
    ser.write(b'c')
    return redirect("/")

@app.route("/open")
def open_hand():
    ser.write(b'o')
    return redirect("/")

app.run(debug=True)