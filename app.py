from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/', methods=['GET'])
def fun():
    return render_template('aks.html')


@app.route('/click', methods=['POST'])
def clc():
    return render_template('aks.html', message='Post Method')


# if __name__ == "__main__":
#     app.run(debug=True)
