from flask import Blueprint, render_template as HTML

# This is the Blueprint for the whole portoflio page
portfolio = Blueprint(
    "portfolio", __name__, static_folder="static", template_folder="templates"
)

################################################
################## Home Route ##################
################################################


@portfolio.route("/")
def index():
    return HTML("index.html")


#################################################
################ Porfolio Routes ################
#################################################


@portfolio.route("/ansible-automation")
def ansible_route():
    return HTML("ansible.html")


@portfolio.route("/checkpoint-automation")
def checkpoint_route():
    return HTML("checkpoint.html")


@portfolio.route("/fortweet")
def fortweet_route():
    return HTML("fortweet.html")


@portfolio.route("/locky")
def locky_route():
    return HTML("locky.html")


@portfolio.route("/mes")
def mes_route():
    return HTML("mes.html")


@portfolio.route("/mesg")
def mesg_route():
    return HTML("mesg.html")


@portfolio.route("/portfolio")
def portfolio_route():
    return HTML("portfolio.html")
