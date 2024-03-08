"""
routes.py specifies all the endpoints for the api
"""

from flask import Blueprint
from app.health.health_service import Health

main = Blueprint("main", __name__)


@main.route("/health", methods=["GET"])
def health():
    return Health().getHealth(), 200
