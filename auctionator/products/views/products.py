from flask import Blueprint, jsonify, request, current_app

products_bp = Blueprint("products", __name__)


@products_bp.route("/products", methods=["GET"])
def index():
    return 'get products'


@products_bp.route("/products/<product_id>", methods=["GET"])
def get_product(product_id):
    return f"this will display a product {product_id}"


@products_bp.route("/", methods=["POST"])
def create_product():
    return 'create product'


@products_bp.route("/", methods=["PATCH"])
def update_product():
    return 'update product'


@products_bp.route("/", methods=["DELETE"])
def delete_product():
    return 'delete product'
