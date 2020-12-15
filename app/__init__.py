from flask import Flask, render_template as HTML, request
from flask_mail import Mail, Message
import app.helpers.utils as Utils
import app.portfolio as portofolio_bprint
import os

app = Flask(
    __name__,
    template_folder="templates",
    static_folder="static",
    instance_relative_config=True,
)

# Register Blueprints
app.register_blueprint(portofolio_bprint.portfolio)

# SMTP Settings
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 587
app.config["MAIL_USERNAME"] = os.environ["MAIL_USERNAME"]
app.config["MAIL_PASSWORD"] = os.environ["MAIL_PASSWORD"]
app.config["MAIL_USE_TLS"] = True
app.config["MAIL_USE_SSL"] = False

# Create a mail object
mail = Mail(app)


@app.errorhandler(404)
def page_not_found(e):
    return HTML("404.html")


# Send mail from contact form
@app.route("/send-email", methods=["POST"])
def send_email():

    try:
        sender_email = request.form["email"]

        # Email validity check
        if not Utils.validate_email(sender_email):
            return (
                "Please enter a valid email",
                200,
            )

        msg = Message(
            request.form["message"],
            sender=sender_email,
            recipients=os.environ["MAIL_RECIPIENTS"].split(","),
        )
        msg.body = request.form["message"]
        msg.subject = f"{request.form['name']} :: {request.form['subject']}"
        mail.send(msg)
    except Exception as e:
        return (
            'Unfortunately, your message couldn\'t be submitted right now. Please contact me directly on <a href="mailto:th3pl4gu33@gmail.com">th3pl4gu33@gmail.com</a>.',
            200,
        )

    # Returns a no content status code
    # because the user doesn't need to get away
    # from current page
    return "OK", 200
