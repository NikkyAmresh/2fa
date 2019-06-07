from flask import Flask, jsonify, render_template, request 
import pyotp
app = Flask(__name__)
text= ""
@app.route('/',methods = ['POST', 'GET'])
def index():
    return render_template('index.html', otp=text)
@app.route('/verify',methods=['POST', 'GET'])
def verify():
    if request.method == 'POST':
        key = request.form['key']
        try:
            return pyotp.TOTP(str(key)).now()
        except:
            return "0" 
if __name__ == '__main__':
   app.run(debug = True)