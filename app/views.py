from app import app

@app.route("/")
def hello():
    return render_template('index.html')
