from flask import Flask, request, jsonify, abort
import json
from flask_cors import CORS

from .database.models import db_drop_and_create_all, setup_db, Drink
from auth.auth import AuthError, requires_auth

app = Flask(__name__)
setup_db(app)
CORS(app)


@app.before_first_request
def create_tables():
    db_drop_and_create_all()


@app.route("/drinks", methods=["GET"])
def get_drinks():
    drinks = Drink.get_all()

    if len(drinks) == 0:
        abort(404)

    return (
        jsonify(
            {"drinks": [drink.short() for drink in drinks], "success": True}
        ),
        200,
    )


# noinspection PyUnusedLocal
@app.route("/drinks-detail", methods=["GET"])
@requires_auth("get:drinks-detail")
def get_drinks_detail(payload):
    drinks = Drink.get_all()

    if len(drinks) == 0:
        abort(404)

    return (
        jsonify(
            {"drinks": [drink.long() for drink in drinks], "success": True}
        ),
        200,
    )


# noinspection PyUnusedLocal
@app.route("/drinks", methods=["POST"])
@requires_auth("post:drinks")
def create_drink(payload):
    data = request.get_json()
    drink = Drink(**data)
    result = drink.insert()

    if result["error"]:
        abort(500)

    _id = result["id"]

    return (
        jsonify({"drinks": [Drink.get_by_id(_id).long()], "success": True,}),
        200,
    )


# noinspection PyUnusedLocal
@app.route("/drinks/<int:drink_id>", methods=["PATCH"])
@requires_auth("patch:drinks")
def update_drink(payload, drink_id):
    drink = Drink.get_by_id(drink_id)

    if drink is None:
        abort(404)

    data = request.get_json()
    title = data.get("title", None)
    recipe = json.dumps(data.get("recipe", None))

    if title is None or recipe is None:
        abort(400)

    drink.title = title
    drink.recipe = recipe
    result = drink.insert()

    if result["error"]:
        abort(500)

    return (
        jsonify(
            {"drinks": [Drink.get_by_id(drink_id).long()], "success": True,}
        ),
        200,
    )


# noinspection PyUnusedLocal
@app.route("/drinks/<int:drink_id>", methods=["DELETE"])
@requires_auth("delete:drinks")
def delete_drink(payload, drink_id):
    drink = Drink.get_by_id(drink_id)

    if drink is None:
        abort(404)

    result = drink.delete()

    if result["error"]:
        abort(500)

    return jsonify({"delete": drink_id, "success": True,})


# noinspection PyUnusedLocal
@app.errorhandler(400)
def not_found(error):
    return (
        jsonify({"success": False, "error": 400, "message": "Bad request"}),
        400,
    )


# noinspection PyUnusedLocal
@app.errorhandler(404)
def not_found(error):
    return (
        jsonify({"success": False, "error": 404, "message": "Not found"}),
        404,
    )


# noinspection PyUnusedLocal
@app.errorhandler(422)
def unprocessable(error):  # pragma: no cover
    return (
        jsonify({"success": False, "error": 422, "message": "Unprocessable"}),
        422,
    )


# noinspection PyUnusedLocal
@app.errorhandler(500)
def unprocessable(error):
    return (
        jsonify(
            {
                "success": False,
                "error": 500,
                "message": "Internal server error",
            }
        ),
        500,
    )


@app.errorhandler(AuthError)
def auth_error(error):
    return (
        jsonify(
            {
                "success": False,
                "error": error.status_code,
                "message": error.error,
            }
        ),
        error.status_code,
    )
