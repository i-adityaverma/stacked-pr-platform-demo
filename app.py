from flask import Flask, jsonify


def create_app() -> Flask:
    app = Flask(__name__)

    @app.get("/")
    def index():
        return jsonify(service="stacked-pr-demo", status="running")

    @app.get("/health/live")
    def liveness():
        return jsonify(status="alive")

    @app.get("/health/ready")
    def readiness():
        return jsonify(status="ready")

    return app


if __name__ == "__main__":
    create_app().run(host="0.0.0.0", port=8080)
