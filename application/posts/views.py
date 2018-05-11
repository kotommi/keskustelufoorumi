from application import app, db
from flask import redirect, render_template, request, url_for, flash
from flask_login import login_required, current_user
from application.posts.models import Post
from application.posts.forms import PostForm
from html import escape


@app.route("/posts/")
def post_index():
    return render_template("post/list.html", posts=Post.query.all())


@app.route("/post/new/<thread_id>")
@login_required
def post_new(thread_id):
    return render_template("post/new.html", form=PostForm(), thread_id=thread_id)


@app.route("/post/edit/<post_id>/", methods=["GET", "POST"])
@login_required
def post_edit(post_id):
    post = Post.query.get(post_id)
    if request.method == "POST":
        form = PostForm(request.form)
        form.content.data = escape(form.content.data)

        if form.validate() and (current_user.id == post.account_id or current_user.has_role("admin")):
            Post.query.filter(Post.id == post.id).update({'name': 'reply', 'content': form.content.data})
            db.session().commit()
            flash("Post successful!")
            return redirect(url_for("thread_view", thread_id=post.thread_id))
        else:
            return render_template("post/edit.html", form=form, post=post)

    form = PostForm()
    form.content.data = post.content
    return render_template("post/edit.html", form=form, post=post)


@app.route("/post/delete/<post_id>", methods=["GET"])
@login_required
def post_delete(post_id):
    post = Post.query.get(post_id)
    if post.account_id != current_user.id and not current_user.has_role("admin"):
        flash("Authentication error")
        return redirect(url_for("category_index"))
    db.session().delete(post)
    db.session().commit()
    return redirect(url_for("thread_view", thread_id=post.thread_id))


@app.route("/post/<thread_id>", methods=["POST"])
@login_required
def post_create(thread_id):
    form = PostForm(request.form)
    form.content.data = escape(form.content.data)

    if not form.validate():
        return render_template("post/new.html", form=form, thread_id=thread_id)
    if not current_user.is_authenticated:
        flash("Authentication error")
        return redirect(url_for("category_index"))
    p = Post(form.content.data)
    p.account_id = current_user.id
    p.thread_id = thread_id
    db.session().add(p)
    db.session().commit()
    return redirect(url_for("thread_view", thread_id=thread_id))
