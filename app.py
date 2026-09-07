from flask import Flask, Response, jsonify
from prometheus_client import CONTENT_TYPE_LATEST, Counter, generate_latest


REQUESTS = Counter(
    "stacked_pr_demo_http_requests_total",
    "Total requests served by endpoint",
    ["endpoint"],
)


def create_app() -> Flask:
    app = Flask(__name__)

    @app.get("/")
    def index():
        REQUESTS.labels(endpoint="index").inc()
        return jsonify(service="stacked-pr-demo", status="running")

    @app.get("/health/live")
    def liveness():
        REQUESTS.labels(endpoint="liveness").inc()
        return jsonify(status="alive")

    @app.get("/health/ready")
    def readiness():
        REQUESTS.labels(endpoint="readiness").inc()
        return jsonify(status="ready")

    @app.get("/metrics")
    def metrics():
        return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)

    return app


if __name__ == "__main__":
    create_app().run(host="0.0.0.0", port=8080)
