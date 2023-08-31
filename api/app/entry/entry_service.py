"""
entry_service.py provides triages all requests from the endpoints
to the appropriate service.
"""

from flask_restful import Resource
from app.health.health_service import Health


class HealthEntry(Resource):
    def get(self):
        return Health().getHealth(), 200
