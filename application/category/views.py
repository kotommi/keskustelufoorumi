from application import app, db
from flask import redirect, render_template, request, url_for
from application.category.models import Category


@app.route("/index", methods=["GET"])
def category_index():
    return render_template("category/index.html", categories=db.Category.queryAll())


@app.route("/c/<category_id>/")
def category_list(category_id):
    return render_template()
