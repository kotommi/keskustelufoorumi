from application import app, db, user_datastore
from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user
from application.threads.forms import ThreadForm
from application.threads.models import Thread


@app.route("/c/<cat_id>/thread/new", methods=["POST", "GET"])
@login_required
def thread_new(cat_id):
    if request.method == "GET":
        return render_template("thread/new_thread.html", user_id=current_user.id, cat_id=cat_id, form=ThreadForm())
    form = ThreadForm(request.form)

    if not form.validate():
        return render_template("thread/new_thread.html", cat_id=cat_id, form=form)

    thread = Thread(title=form.title.data, content=form.content.data, category_id=cat_id,
                    user_id=current_user.id)
    db.session().add(thread)
    db.session().commit()
    return redirect(url_for("category_list", category_id=cat_id))


@app.route("/thread/<thread_id>/", methods=["GET"])
def thread_view(thread_id):
    thread = Thread.query.get(thread_id)
    posts = thread.posts

    return render_template("thread/view.html", thread=thread, posts=posts, user_datastore=user_datastore)
