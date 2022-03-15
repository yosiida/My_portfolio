from flask import Flask, render_template, redirect, url_for, Blueprint

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('top.html')


if __name__ == '__main__':
    app.run(debug=True)