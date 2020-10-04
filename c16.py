from flask import Flask, render_template, url_for
from markupsafe import escape
<<<<<<< HEAD:c16.py
import datetime, board, neopixel, requests
pixel_pin = board.D18
num_pixels = 60
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.2, auto_write=False)
=======
from color import colors
import datetime, board, neopixel
 
#pixel_pin = board.D18
#num_pixels = 16
#pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.2, auto_write=False)
>>>>>>> origin/multiple-pins:ver1.0.cells.py

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
<<<<<<< HEAD:c16.py
=======

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


>>>>>>> origin/multiple-pins:ver1.0.cells.py

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
        for i in c16[ce]:
          pixels[i] = colors[c]
          pixels.show() 
      else:
<<<<<<< HEAD:c16.py
         #return 'Cell not found' 
         requests.get('http://localhost:5000/on/' + ce + '/' +c)
=======
        return 'Looking on another PIN'
        if ce in c17:
        pixel_pin = board.D21
        pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.2, auto_write=False)
        for i in c17[ce]:
          pixels[i] = colors[c]
          pixels.show()
         else:
           "No cell found"
          
>>>>>>> origin/multiple-pins:ver1.0.cells.py
    else:
      return "Color not found"  
    return 'Current cell is %s' % escape(ce)


if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=True)
