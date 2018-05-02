from application import user_datastore, app, db
from flask import redirect, render_template, request, url_for, flash
from flask_security import roles_required
from application.category.models import Category
from application.category.forms import CategoryForm


@app.route("/", methods=["GET"])
def category_index():
    return render_template("category/index.html", categories=Category.query.all())


@app.route("/category/create", methods=["GET", "POST"])
@roles_required("admin")
def category_create():
    if request.method == "GET":
        return render_template("category/create.html", form=CategoryForm())

    form = CategoryForm(request.form)
    if not form.validate():
        flash("There were errors")
        return render_template("category/create.html", form=form, errors=form.errors)

    new_category = Category(form.title.data, form.description.data)
    db.session().add(new_category)
    db.session().commit()

    flash("Category created")
    return redirect(url_for("category_index"))


@app.route("/c/<category_id>/")
def category_list(category_id):
    category = Category.query.get(category_id)
    if not category:
        flash("No such category")
        return redirect(url_for("category_index"))

    return render_template("category/category.html", threads=category.threads, category_id=category_id,
                           category=category, user_datastore=user_datastore)
