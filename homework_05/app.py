from flask import Flask
from werkzeug.exceptions import InternalServerError

from views.others import others_app

app = Flask(__name__)
app.register_blueprint(others_app)


@app.errorhandler(KeyError)
def handle_key_error(exc):
    return InternalServerError(f"oops, could not find that by key {exc}!")


@app.errorhandler(ZeroDivisionError)
def handle_zero_division_error(exc):
    print("exc", exc)
    return InternalServerError("oops, could divide that!")


@app.errorhandler(Exception)
def handle_all_exception(exc):
    print("exc", exc)
    return InternalServerError("oops, unexpected exception!")


if __name__ == "__main__":
    app.run(debug=True)
