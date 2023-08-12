from flask import jsonify


class Health:
    def getHealth(self):
        return jsonify({"message": "I am healthy!"})
