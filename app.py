from flask import Flask, request, render_template, url_for
from data import assaults

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index2.html', assaults = assaults)

if __name__ == '__main__':
    app.run(debug=True)
