"""
routes.py specifies all the endpoints for the api
"""

from flask import Blueprint
from app.entry.entry_service import HealthEntry

main = Blueprint("main", __name__)


@main.route("/health", methods=["GET"])
def health():
    return HealthEntry().get()
