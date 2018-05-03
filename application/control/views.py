from flask import render_template, request, redirect, url_for, flash
from flask_security.decorators import roles_required, login_required, current_user

from application import app, user_datastore
from application.auth.models import User
from application.category.models import Category
from application.posts.models import Post
from application.threads.models import Thread
from application.control.forms import AdminForm


@app.route("/admin_panel", methods=["GET"])
@login_required
@roles_required('admin')
def admin_panel():
    users = User.query.all()
    categories = Category.query.all()
    return render_template("control/admin.html", users=users, categories=categories)


@app.route("/admin/users")
@login_required
@roles_required("admin")
def user_list():
    users = User.query.all()
    return render_template("control/users.html", users=users)


@app.route("/admin/add", methods=["GET", "POST"])
@login_required
@roles_required("admin")
def admin_promote():
    if request.method == "GET":
        return render_template("control/add.html", form=AdminForm())
    form = AdminForm(request.form)
    new_admin = user_datastore.find_user(username=form.username.data)
    if not new_admin:
        flash("No such user")
        return render_template("control/add.html", form=form)
    user_datastore.add_role_to_user(new_admin, role="admin")
    user_datastore.commit()
    flash("Added new admin " + new_admin.username)
    return redirect(url_for("admin_panel"))


@app.route("/user/<user_id>", methods=["GET"])
@login_required
def user_panel(user_id):
    try:
        user_id = int(user_id)
    except ValueError:
        flash("No such user")
        return redirect(url_for("category_index"))
    if not current_user.id == user_id and not current_user.has_role("admin"):
        flash("Authentication error")
        return redirect(url_for("category_index"))
    return render_template("control/user.html", user=user_datastore.get_user(user_id),
                           recent_posts=Post.find_latest_posts(user_id), recent_threads=Thread.find_latest_threads(user_id))
