from .products import products_bp
from flask import jsonify


@products_bp.route("/api/products/", methods=["GET"])
@products_bp.route("/api/products", methods=["GET"])
def get_products_action():
    return jsonify({"message": "products module"})


@products_bp.route("/api/products/<product_id>", methods=["GET"])
def get_product_action(product_id):
    return jsonify({"message": f"product {product_id}"})


@products_bp.route("/api/products", methods=["POST"])
def create_product_action():
    return jsonify({"message": "create product"})


@products_bp.route("/api/products", methods=["PATCH"])
def update_product_action():
    return jsonify({"message": "update product"})


@products_bp.route("/api/products", methods=["DELETE"])
def delete_product_action():
    return jsonify({"message": "delete product"})
