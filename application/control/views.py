from flask import render_template, request, redirect, url_for, flash
from flask_security.decorators import roles_required, login_required, current_user

from application import app, user_datastore
from application.auth.models import User
from application.category.models import Category


@app.route("/admin_panel", methods=["GET"])
@roles_required('admin')
def admin_panel():
    users = User.query.all()
    categories = Category.query.all()
    return render_template("control/admin.html", users=users, categories=categories)


@app.route("/user/<user_id>", methods=["GET"])
@login_required
def user_panel(user_id):
    try:
        user_id = int(user_id)
    except ValueError:
        flash("No such user")
        return redirect(url_for("category_index"))
    if not current_user.id == user_id or not current_user.has_role("admin"):
        flash("Authentication error")
        return redirect(url_for("category_index"))
    return render_template("control/user.html", user=user_datastore.get_user(user_id))
