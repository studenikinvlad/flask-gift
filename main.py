from flask import Flask, render_template, request
from flask_mail import Mail
from config import Configuration
import emails as em


app = Flask(__name__)
app.config.from_object(Configuration)


mail = Mail(app)

@app.route("/", methods=["POST", "GET"])
def contact():
    if request.method == "POST":
        print(request.form)
        subject = request.form["choiсe"]
        body = request.form["choiсe"]
        em.send_mail(subject, body)

    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)