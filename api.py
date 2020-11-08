from tasks import clean
from flask import Flask, request, jsonify
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)
import os
app = Flask(__name__)

app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SEC')  
jwt = JWTManager(app)


@app.route('/token', methods=['POST'])
def login():
    if not request.is_json:
        return jsonify({"msg": "Missing JSON in request"}), 400

    username = request.json.get('username', None)
    password = request.json.get('password', None)
    if not username:
        return jsonify({"msg": "Missing username parameter"}), 400
    if not password:
        return jsonify({"msg": "Missing password parameter"}), 400

    if username != os.getenv('LEGEND')  or password != os.getenv('ARTIX_PASS'):
        return jsonify({"msg": "Bad username or password"}), 401

    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token), 200


@app.route('/prices', methods=['GET'])
@jwt_required
def protected():
    # Access the identity of the current user with get_jwt_identity
    current_user = get_jwt_identity()
    res = clean.delay()
    print(res)
    return res.get()

if __name__ == '__main__':
    app.run(debug=False, port=6969)
