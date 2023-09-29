from flask import Flask

#Creates a new Flask web application 'app'
app = Flask(__name__)

#Defines a route for the root URL of the web application.
@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/test')
def test():
    return 'this is a test'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9443, debug=True)

