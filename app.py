from flask import Flask, request, render_template, url_for,jsonify
from data import assaults, crash_coordinates

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('testing.html', assaults=assaults, crashes=crash_coordinates )

if __name__ == '__main__':
    app.run(debug=True)
