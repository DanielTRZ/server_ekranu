









import socket
import threading
import tkinter as tk
from tkinter import messagebox
import cv2
from flask import Flask, Response, render_template_string
import numpy as np
from mss import mss

app = Flask(__name__)


def get_local_ip():
  s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  try:
    s.connect(('10.255.255.255', 1))
    IP = s.getsockname()[0]
  except Exception:
    IP = '127.0.0.1'
  finally:
    s.close()
  return IP


HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>Stream Ekranu na Zywo</title>
    <style>
        body { background: #111; color: #fff; text-align: center; font-family: sans-serif; margin: 0; padding: 20px; }
        h2 { color: #00ffcc; }
        img { max-width: 100%; height: auto; border: 2px solid #333; border-radius: 8px; box-shadow: 0 0 20px rgba(0,255,204,0.2); }
    </style>
</head>
<body>
    <h2>Transmisja Pulpitu (Sieć LAN)</h2>
    <img src="/video_feed" />
</body>
</html>
"""


def generate_frames():
  with mss() as sct:
    monitor = sct.monitors[1]
    while True:
      img = np.array(sct.grab(monitor))
      frame = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)

      _, buffer = cv2.imencode('.jpg', frame, [cv2.IMWRITE_JPEG_QUALITY, 75])
      frame_bytes = buffer.tobytes()

      yield (
          b'--frame\r\n'
          b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n'
      )


@app.route('/')
def index():
  return render_template_string(HTML_PAGE)


@app.route('/video_feed')
def video_feed():
  return Response(
      generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame'
  )


def run_server():
  # Uruchamiamy serwer w tle (wyciszamy też logi flask żeby nie śmieciły)
  import logging

  log = logging.getLogger('werkzeug')
  log.setLevel(logging.ERROR)
  app.run(host='0.0.0.0', port=5000, threaded=True)


if __name__ == '__main__':
  # Odpalamy serwer w osobnym wątku
  server_thread = threading.Thread(target=run_server, daemon=True)
  server_thread.start()

  local_ip = get_local_ip()

  # Tworzymy ładne okienko sterowania z przyciskiem do wyłączenia
  root = tk.Tk()
  root.title('Panel Sterowania Streamem')
  root.geometry('380x220')
  root.configure(bg='#1e1e1e')

  label_title = tk.Label(
      root,
      text='TRANSMISJA AKTYWNA',
      font=('Arial', 12, 'bold'),
      fg='#00ffcc',
      bg='#1e1e1e',
  )
  label_title.pack(pady=15)

  label_info = tk.Label(
      root,
      text=(
          'Wpisz ten adres na innych'
          f' monitorach:\nhttp://{local_ip}:5000\n\n(Nie zamykaj tego okna, dopóki'
          ' chcesz streamować)'
      ),
      font=('Arial', 10),
      fg='#ffffff',
      bg='#1e1e1e',
      justify='center',
  )
  label_info.pack(pady=5)


  def stop_app():
    root.destroy()
    import os

    os._exit(0)


  btn_exit = tk.Button(
      root,
      text='WYŁĄCZ STREAM',
      command=stop_app,
      font=('Arial', 11, 'bold'),
      bg='#ff4d4d',
      fg='white',
      padx=10,
      pady=5,
  )
  btn_exit.pack(pady=15)

  root.protocol('WM_DELETE_WINDOW', stop_app)
  root.mainloop()
