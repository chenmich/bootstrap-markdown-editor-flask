from editor import app
from flask import render_template
from .forms import BlogEditor

@app.route('/', methods=['GET', 'POST'], defaults={"post_id": None})
def index(post_id):
    form = BlogEditor()
    
    return render_template("markdown_editor.html", form=form)
