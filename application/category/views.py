from flask import redirect, render_template, request, url_for

from application import app, db
from application.category.models import Category


@app.route("/", methods=["GET"])
def category_index():
    return render_template("category/index.html", categories=Category.query.all())


@app.route("/c/<category_id>/")
def category_list(category_id):
    return render_template()
