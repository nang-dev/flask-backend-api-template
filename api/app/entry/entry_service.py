"""
entry_service.py provides triages all requests from the endpoints
to the appropriate service.
"""

from flask_restful import Resource
from app.health.health_service import Health
from app.ai.shopping.product_search_bing import ProductSearchBing


class HealthEntry(Resource):
    def get(self):
        return Health().getHealth(), 200


class ProductSearchEntry(Resource):
    def get(self):
        return ProductSearchBing().search_product_by_img(None), 200