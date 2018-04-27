from flask import render_template, request, redirect, url_for, flash
from flask_security.utils import hash_password, verify_and_update_password, login_user, logout_user

from application import app, db, user_datastore
from application.auth.models import User, Role, user_role
from application.auth.forms import LoginForm, CreateForm


@app.route("/auth/login", methods=["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/loginform.html", form=LoginForm())

    form = LoginForm(request.form)
    user = User.query.filter_by(username=form.username.data).first()
    password = form.password.data
    if not user or not verify_and_update_password(password, user):
        return render_template("auth/loginform.html", form=form, error="No such username or password")
    login_user(user)
    return redirect(url_for("category_index"))


@app.route("/auth/create", methods=["GET", "POST"])
def auth_create():
    """

    Users are created with the Normal role only
    """
    if request.method == "GET":
        return render_template("auth/createform.html", form=CreateForm())

    form = CreateForm(request.form)

    existing_user = User.query.filter_by(username=form.username.data).first()

    if not form.validate() or existing_user:
        if existing_user:
            form.username.errors.append("Username already exists!")
        return render_template("auth/createform.html", form=form)

    hashed_pw = hash_password(form.password.data)
    new_user = User(form.username.data, form.username.data, hashed_pw)
    db.session().add(new_user)
    db.session().commit()
    default_role = user_datastore.find_or_create_role("normal")
    # Add roles here if needed
    user_datastore.add_role_to_user(new_user, role=default_role)
    user_datastore.activate_user(new_user)
    user_datastore.commit()
    flash("Registration complete!")
    return redirect(url_for("auth_login"))


@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("category_index"))
