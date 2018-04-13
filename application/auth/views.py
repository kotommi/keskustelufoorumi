from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user

from application import app, db
from application.auth.models import User
from application.auth.forms import LoginForm, CreateForm


@app.route("/auth/login", methods=["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/loginform.html", form=LoginForm())

    form = LoginForm(request.form)

    user = User.query.filter_by(username=form.username.data, password=form.password.data).first()
    if not user:
        return render_template("auth/loginform.html", form=form, error="No such username or password")

    login_user(user)
    return redirect(url_for("category_index"))


@app.route("/auth/create", methods=["GET", "POST"])
def auth_create():
    if request.method == "GET":
        return render_template("auth/createform.html", form=CreateForm())

    form = CreateForm(request.form)

    if not form.validate():
        return render_template("auth/createform.html", form=form)

    user = User(form.username.data, form.username.data, form.password.data)
    db.session().add(user)
    db.session().commit()
    flash("Registration complete!")
    return redirect(url_for("auth_login"))


@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("category_index"))
