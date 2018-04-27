from flask import render_template, request, redirect, url_for, flash
from flask_security.decorators import roles_required, login_required, current_user

from application import app, db, user_datastore
from application.auth.models import User, Role, user_role
from application.auth.forms import LoginForm, CreateForm


@app.route("/admin_panel", methods=["GET"])
@roles_required('admin')
def admin_panel():
    return render_template("control/admin.html")


@app.route("/user/<user_id>", methods=["GET"])
@login_required
def user_panel(user_id):
    try:
        user_id = int(user_id)
    except ValueError:
        return redirect(url_for("category_index"))
    if not current_user.id == user_id:
        return redirect(url_for("category_index"))
    return render_template("control/user.html", user=user_datastore.get_user(user_id))
