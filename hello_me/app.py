import flask
import sys
import pathlib

verbose = True

# set app routes and route functions
def createAppRoutes():
    if verbose:
        print("createAppRoutes()")

    @app.route("/")
    def index():
        return flask.render_template("index.html")


# configure app folder paths
app = flask.Flask(__name__, static_folder="./dist/assets", template_folder="./dist")
createAppRoutes()


# run the app
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port="5000")
