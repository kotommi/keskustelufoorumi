from application import app, db
from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user
from application.posts.models import Post
from application.posts.forms import PostForm


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
        if form.validate() and current_user.id == post.account_id:
            post.name = form.name.data
            post.content = form.name.data
            Post.query.filter(Post.id == post.id).update({'name': form.name.data, 'content': form.content.data})
            db.session().commit()
            return redirect(url_for("thread_view", thread_id=post.thread_id))
        else:
            return render_template("post/edit.html", form=form, post=post)

    form = PostForm()
    form.name.data = post.name
    form.content.data = post.content
    return render_template("post/edit.html", form=form, post=post)


@app.route("/post/delete/<post_id>", methods=["GET"])
@login_required
def post_delete(post_id):
    post = Post.query.get(post_id)
    if post.account_id != current_user.id:
        return "Authentication error"
    db.session().delete(post)
    db.session().commit()
    return redirect(url_for("thread_view", thread_id=post.thread_id))


@app.route("/post/<thread_id>", methods=["POST"])
@login_required
def post_create(thread_id):
    form = PostForm(request.form)

    if not form.validate():
        return render_template("post/new.html", form=form, thread_id=thread_id)
    p = Post(form.name.data, form.content.data)
    p.account_id = current_user.id
    p.thread_id = thread_id
    db.session().add(p)
    db.session().commit()
    return redirect(url_for("thread_view", thread_id=thread_id))
