from flask import Flask, render_template, url_for
from markupsafe import escape
import datetime, board, neopixel
pixel_pin = board.D21
num_pixels = 60
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.2, auto_write=False)

#COLORS
colors = {
  "BLACK":(0, 0, 0),
  "RED":(255, 0, 0), 
  "YELLOW": (255, 150, 0),
  "GREEN":(0, 255, 0),
  "CYAN":(0, 255, 255),
  "BLUE":(0, 0, 255),
  "PURPLE":(180, 0, 255)
}
#CELLS
c17 = {
  "C1.7.1":range(152, 160),
  "C1.7.2":range(142, 150),
  "C1.7.3":range(132, 140),
  "C1.7.4":range(122, 130),
  "C1.7.5":range(112, 120),
  "C1.7.6":range(102, 110),
  "C1.7.7":range(92, 100),
  "C1.7.8":range(82, 90),
  "C1.7.9":range(72, 80),
  "C1.7.10":range(62, 70),
  "C1.7.11":range(52, 60),
  "C1.7.12":range(42, 50),
  "C1.7.13":range(32, 40),
  "C1.7.14":range(22, 30),
  "C1.7.15":range(12, 20),
  "C1.7.16":range(2, 10) 
  }

app = Flask(__name__)
@app.route("/")
def hello():
   now = datetime.datetime.now()
   timeString = now.strftime("%Y-%m-%d %H:%M")
   templateData = {
      'title' : 'LED CONTROL CENTER IN KAZANEXPERSS',
      'time': timeString
      }
   return render_template('index.html', **templateData)

@app.route('/off/')
def poweroff():
   pixels.fill((0, 0, 0))
   pixels.show()
   return 'PowerOFF'

@app.route('/on/<string:cell>/<string:color>')
def test(cell, color):
    c = color.upper()
    ce = cell.upper()
    print(ce, c)
    if c in colors:
      if ce in c17:
        for i in c17[ce]:
          pixels[i] = colors[c]
          pixels.show()
      else:
         return 'Cell not found' 
    else:
      return "Color not found"  
    return 'Current cell is %s' % escape(ce)


if __name__ == "__main__":
   app.run(host='0.0.0.0', port=5000, debug=True)
