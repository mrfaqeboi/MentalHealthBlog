from flask import Blueprint, render_template, request
from app.models import Post

main = Blueprint('main', __name__)

@main.route("/")
@main.route("/home")
def home():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page = page, per_page=5)
    return render_template('home.html', posts=posts)


@main.route("/about")
def about():
    return render_template('about.html', title = 'ABOUT')

@main.route("/contact")
def contact():
    return render_template('contact_us.html', title = 'Contact_Us')

@main.route("/announcements")
def announcements():
    return render_template('announcements.html', title = 'Announcements')

@main.route("/info")
def info():
    return render_template('info.html', title = 'Info')


