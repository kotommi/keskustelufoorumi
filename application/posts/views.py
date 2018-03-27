from application import app, db
from flask import redirect, render_template, request, url_for
from application.posts.models import Post
from application.posts.forms import PostForm


@app.route("/posts/")
def post_index():
    return render_template("post/list.html", posts=Post.query.all())


@app.route("/post/new")
def post_form():
    return render_template("post/new.html", form=PostForm())


@app.route("/post/edit/<post_id>/", methods=["GET"])
def post_edit(post_id):
    p = Post.query.get(post_id)
    return render_template("post/edit.html", post=p)


@app.route("/post/edit/<post_id>/", methods=["POST"])
def post_update(post_id):
    p = Post.query.get(post_id)
    p.name = request.form.get("name")
    p.content = request.form.get("content")
    db.session().add(p)
    db.session().commit()
    return redirect(url_for("post_index"))


@app.route("/post/", methods=["POST"])
def post_create():
    form = PostForm(request.form)

    if not form.validate():
        return render_template("post/new.html", form=form)
    p = Post(form.name.data, form.content.data)
    db.session().add(p)
    db.session().commit()
    return redirect(url_for("post_index"))
