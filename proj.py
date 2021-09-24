from flask import Flask, render_template
from scrape import elems

app = Flask(__name__)

arr =   [None,[],[],[],[],[]]
lanths = []
acts = []

for x in range(16):
    elems.insert(1, arr)
for x in range(10):
    elems.insert(20, arr)
for x in range(10):
    elems.insert(38, arr)
for x in range(15):
    lanths.append(elems.pop(92))
for x in range(2):
    lanths.insert(0, arr)
lanths.append(arr)
for x in range(15):
    acts.append(elems.pop(109))
for x in range(2):
    acts.insert(0, arr)
acts.append(arr)
elems.insert(92, arr)
elems.insert(110, arr)

@app.route('/')
def index():
    return render_template('index.html', elements=elems, lanthanides=lanths, actinides=acts)

if __name__=='__main__':
    app.run(debug=True)