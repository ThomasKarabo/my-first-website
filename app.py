from flask import Flask, render_template

app = Flask(__name__)

ITEMS = [
  {'barcode': 123,
  'item': 'laptop',
  'available': True,
  'price': 'R5000.00'},
  {'barcode': 123,
  'item': 'laptop',
  'available': True,
  'price': 'R5000.00'},
  {'barcode': 123,
  'item': 'laptop',
  'available': True,
  'price': 'R5000.00'},
  {'barcode': 123,
  'item': 'laptop',
  'available': True,
  'price': 'R5000.00'},
]

@app.route("/")
def hello_world():
  return render_template("home.html",items = ITEMS)

if __name__ == "__main__":
  app.run(host = "0.0.0.0", debug = True)
  