from flask import Flask, jsonify, request
from flask_mail import Mail, Message

app = Flask(__name__)
mail= Mail(app)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'hcifall2020@gmail.com'
app.config['MAIL_PASSWORD'] = '*****' # password for the sender email
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['AUTHENTICATION'] = "plain"
mail = Mail(app)

@app.route("/send", methods=["GET"])
def index():
   msg = Message('Hello', sender = 'hcifall2020@gmail.com', recipients = ['examplemail@gmail.com'])
   msg.body = "Hello Flask message sent from Flask-Mail"
   mail.send(msg)
   return "Sent"


'''
example request
curl -X POST -H "Content-Type: application/json" -d '{"recipient": "examplemail@virginia.edu", "title": "Reading Response 9 based on Topic Presentation List T9 or T10", "content": "Reading response for Nov 9 topic presentations Choose one from the following four papers"}' http://0.0.0.0:5050/send-mail

'''
@app.route("/send-mail", methods=["POST"])
def sendAlert():
    data = request.get_json()
    mail_title = data['title']
    mail_content = data['content']
    sendTo = data['recipient']
    msg = Message('Due: ' + str(mail_title), sender = 'hcifall2020@gmail.com', recipients = [sendTo])
    msg.body = mail_content
    mail.send(msg)
    return "Sent"

if __name__ == '__main__':
   app.run(port=5050, host="0.0.0.0", debug = True)