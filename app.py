__author__ = 'Dieferson'
from flask import Flask ,render_template ,redirect ,url_for ,request ,session ,flash
app = Flask(__name__)


@app.route('/' ,methods=['GET', 'POST'])
def index():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Por favor, preencha os campos e tente novamente.'
        else:
            return redirect(url_for('home'))
    return render_template("index.html", error=error)

@app.route('/home')
def home():
    return render_template("home.html")














if __name__ == '__main__':
    app.run(debug=True)
