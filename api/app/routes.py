"""
routes.py specifies all the endpoints for the api
"""

from flask import Blueprint
from app.entry.entry_service import HealthEntry
from app.entry.entry_service import ProductSearchEntry

main = Blueprint("main", __name__)


@main.route("/health", methods=["GET"])
def health():
    return HealthEntry().get()


@main.route("/productSearch", methods=["GET"])
def productSearch():
    return ProductSearchEntry().get()
