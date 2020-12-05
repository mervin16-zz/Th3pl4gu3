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


# Start the app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8082)
