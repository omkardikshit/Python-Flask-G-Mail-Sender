from flask import Flask, render_template,request,url_for,redirect
from flask_mail import Mail, Message

app = Flask(__name__)
mail = Mail(app)

@app.route('/' , methods=['get','post'])
def index():
    try:
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']
            email = request.form['email']
            subject = request.form['subject']
            body = request.form['body']
            app.config['MAIL_SERVER'] = 'smtp.gmail.com'
            app.config['MAIL_PORT'] = 465
            app.config['MAIL_USERNAME'] = username
            app.config['MAIL_PASSWORD'] = password
            app.config['MAIL_USE_TLS'] = False
            app.config['MAIL_USE_SSL'] = True
            mail = Mail(app)
            msg = Message(
                subject,
                sender=username,
                recipients=
                [email])
            msg.body = body
            mail.send(msg)
            return render_template('sent.html')
    except Exception as e:
        return e
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)