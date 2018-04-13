from application import app, db
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
        return render_template("thread/new_thread.html", form=form)

    thread = Thread(title=form.title.data, content=form.content.data, category_id=form.cat_id.data,
                    user_id=current_user.id)


