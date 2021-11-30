from flask import request, redirect, render_template, url_for, flash
from flask_login import login_required
from models.models import Posts
from app import app, db


@app.route('/create-post', methods=["GET", "POST"])
@login_required
def create_post():
    post_id = request.form.get('post_id')
    categor = request.form.get('categor')
    topic = request.form.get('topic')
    text = request.form.get('text')
    date_add = request.form.get('date_add')

    if request.method == 'POST':
        if len(categor) <= 5:
            flash("Категорія має містити мінімум 6 символів", category='error')
            return redirect(url_for('create_post'))
        if len(topic) <= 6:
            flash("Тема має містити мінімум 7 символів", category='error')
            return redirect(url_for('create_post'))
        if len(text) <= 4:
            flash("Введіть текст поста мінімум 5 символів)", category='error')
            return redirect(url_for('create_post'))
        else:
            post = Posts(
                post_id=post_id,
                categor=categor,
                topic=topic,
                text=text,
                date_add=date_add
            )
            try:
                db.session.add(post)
                db.session.commit()
                flash("Пост добавлено успішно", category='success')
                return redirect("/")
            except:
                flash("Невідома помилка при добавлянні поста", category='error')
                return redirect(url_for('create_post'))

    else:
        return render_template('create-post.html')


