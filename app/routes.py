from app import app

@app.route('/')
def hello():
    return "Hello, World2!"
@app.route('/index')
def index():
    return "Hello, World!"