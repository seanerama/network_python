from flask import Flask, render_template, request
import cmdrunner

app = Flask(__name__)

@app.route('/cmds')
def cmds():
    return render_template('form.html') 

@app.route('/')
def index():
    return 'hello world' 

@app.route('/submit', methods=['POST'])
def submit():
    email = request.form.get('email')
    commands = request.form.get('commands').splitlines()
    ips = request.form.get('ips').splitlines()

    result = cmdrunner.run_commands(commands,ips,email)
    
    return result

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9443, debug=True)

