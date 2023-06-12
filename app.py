# Import dependencies
from flask import Flask, render_template, request, jsonify, g
import json

# Create Flask app
app = Flask(__name__)

# Home endpoint on Flask app.route /
@app.route('/')
def home():
    return render_template('home.html')

# Home endpoint on Flask app.route /python
@app.route('/python')
def python():
    return render_template('python.html')

# Map endpoint on Flask app.route /map
@app.route('/map')
def map():
    return render_template('map.html')

# JSON endpoint on Flask app.route /data_map
@app.route('/data_map')
def data_map():
    with open('data/map.geojson') as f:
        data_map = json.load(f)
        print(type(data_map))
    return jsonify(data_map)

# Run Flask app
if __name__ == "__main__":
    app.run(debug=True)
