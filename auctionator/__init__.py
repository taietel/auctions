from flask import Blueprint

auctionator_bp = Blueprint("auctionator", __name__, url_prefix="/api/auctionator")

from . import routes
from .models import db, init_app


