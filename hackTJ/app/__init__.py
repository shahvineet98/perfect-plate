from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def form():
    return render_template('form_submit.html')


@app.route('/hello/',methods=['POST'])
def hello():
    name=request.form['yourname']
    email=request.form['youremail']
    return render_template('form_action.html', name=name, email=email)

if __name__ == "__main__":
    app.run()
