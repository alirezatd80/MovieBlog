from movie import app

@app.route('/')
def mainpage():
    return "hello"