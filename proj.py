from scrape import elems
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', elements=elems)

if __name__=='__main__':
    app.run(debug=True)
