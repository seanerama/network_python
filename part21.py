from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html')  

@app.route('/submit', methods=['POST'])
def submit():
    email = request.form.get('email')
    commands = request.form.get('commands').splitlines()
    ips = request.form.get('ips').splitlines()
    
    # You can now process the received data as needed
    print(email, commands, ips)
    
    return 'Form submitted successfully!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9443, debug=True)

