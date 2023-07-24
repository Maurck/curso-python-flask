from flask import jsonify

def response(msg, res, code=200):
    return jsonify({
        "msg": msg,
        "res": res
    }), code