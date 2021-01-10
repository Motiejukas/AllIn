from flask import Flask, render_template, request
from funkcijos import get_currencies, gauti_data

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    res = ''
    if request.method == 'POST':
        from_ = request.form['add']
        to_ = request.form['to']
        amount = request.form['amount']
        res = gauti_data(amount, from_, to_)
    return render_template('labas.html', res=res, currencies=get_currencies())


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8081, debug=True)
