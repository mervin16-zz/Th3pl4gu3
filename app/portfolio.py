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


@portfolio.route("/portfolio")
def portfolio_route():
    return HTML("portfolio.html")
