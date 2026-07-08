from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "<h1>Mini SEIM Dashboard</h1><p>Phase 1 Setup Successful</p>"

if __name__ == '__main__':
    app.run(debug=True)

    