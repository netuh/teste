# save this as app.py
from flask import Flask, request, render_template
from markupsafe import escape

app = Flask(__name__)

stateis = "00deg"


@app.route('/')
def hello(name=None):
    return render_template('index.html', message=stateis)


@app.route('/test')
def test(name=None):
    return f'Test com {stateis}'


@app.route('/send')
def send_data():
    ax = int(request.args.get('ax'))
    ay = int(request.args.get('ay'))
    az = int(request.args.get('az'))
    global stateis
    if ax == 0 and ay == 0 and az == 1:
        stateis = "0deg"
    elif ax == 0 and az == 0 and (ay == 1 or ay == -1):
        stateis = "90deg"
    elif ax == 0 and ay == 0 and az == -1:
        stateis = "180deg"
    else:
        stateis = "270deg"
    return f'alterado para, {escape(stateis)}!'


if __name__ == '__main__':
    print("test")
    app.run(debug=True, host='0.0.0.0', port=80)
