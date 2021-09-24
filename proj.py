from flask import Flask, render_template
from scrape import elems, lanths, acts

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', elements=elems, lanthanides=lanths, actinides=acts)

if __name__=='__main__':
    app.run(debug=True)