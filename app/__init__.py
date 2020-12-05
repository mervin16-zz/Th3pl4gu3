from flask import Flask, render_template as HTML

app = Flask(
    __name__,
    template_folder="templates",
    static_folder="static",
    instance_relative_config=True,
)


@app.route("/")
def index():
    return HTML("index.html")


@app.errorhandler(404)
def page_not_found(e):
    return HTML("404.html")
