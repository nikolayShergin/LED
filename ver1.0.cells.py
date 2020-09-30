from flask import Flask, render_template, url_for
from markupsafe import escape
import datetime 
import board
import neopixel
 
#pixel_pin = board.D18
num_pixels = 160


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
c16 = {
  "C1.6.1":range(152, 160),
  "C1.6.2":range(142, 150),
  "C1.6.3":range(132, 140),
  "C1.6.4":range(122, 130),
  "C1.6.5":range(112, 120),
  "C1.6.6":range(102, 110),
  "C1.6.7":range(92, 100),
  "C1.6.8":range(82, 90),
  "C1.6.9":range(72, 80),
  "C1.6.10":range(62, 70),
  "C1.6.11":range(52, 60),
  "C1.6.12":range(42, 50),
  "C1.6.13":range(32, 40),
  "C1.6.14":range(22, 30),
  "C1.6.15":range(12, 20),
  "C1.6.16":range(2, 10) 
  }
#pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.2, auto_write=False)


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
      if ce in c16:
        pixel_pin = board.D18
        pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.2, auto_write=False)
        for i in c16[ce]:
          pixels[i] = colors[c]
          pixels.show()
      else:
         return 'Cell not found' 
    else:
      return "Color not found"  
    return 'Current cell is %s' % escape(ce)


if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=True)
