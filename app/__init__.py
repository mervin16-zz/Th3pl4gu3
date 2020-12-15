from flask import Flask, render_template as HTML
import app.portfolio as portofolio_bprint

app = Flask(
    __name__,
    template_folder="templates",
    static_folder="static",
    instance_relative_config=True,
)

# Register Blueprints
app.register_blueprint(portofolio_bprint.portfolio)


@app.errorhandler(404)
def page_not_found(e):
    return HTML("404.html")
