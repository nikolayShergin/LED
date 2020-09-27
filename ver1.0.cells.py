from flask import Flask, render_template, url_for
from markupsafe import escape
import datetime 
import board
import neopixel
 
pixel_pin = board.D18
num_pixels = 60


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
cells = {
  "C1":range(0, 3),
  "C2":range(3, 20),
  "C3":range(20, 27),
  "C4":range(27, 40),
  "C5":range(40, 50),
  "C6":range(50, 60)
}
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.2, auto_write=False)


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
      if ce in cells:
        for i in cells[ce]:
          pixels[i] = colors[c]
          pixels.show()
      else:
         return 'Cell not found' 
    else:
      return "Color not found"  
    return 'Current cell is %s' % escape(ce)


if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=True)
