import os
from pathlib import Path
from flask import (Blueprint, render_template)
from if_dev.db import get_comments, connect, DB_PATH


main = Blueprint("main", __name__)
IMAGE_PATH = "assets/site_images/"

# routes
@main.route("/")
@main.route("/index")
def index():
    conn = connect(DB_PATH)
    comments = get_comments(conn)
    print(comments)
    return render_template("views/pricing.html", 
                            image=f"{IMAGE_PATH}2011.png", 
                            comments=comments, 
                            profile_image=f"{IMAGE_PATH}profile.png")


@main.route("/about")
def about():
    return render_template("views/about.html", title="About", image=f"{IMAGE_PATH}100.png")


@main.route("/team")
def team():
    return render_template("views/team.html", title="Team", image=f"{IMAGE_PATH}150.png")


@main.route("/services")
def services():
    return render_template("views/services.html", title="Services", image=f"{IMAGE_PATH}8590.png")


@main.route("/contact")
def contact():
    return  render_template("views/contact.html", title="Contact", image=f"{IMAGE_PATH}200.png")



# @main.route("/login", methods=["GET", "POST"])
# def login():
#     form = LoginEmpleado()
#     if(form.validate_on_submit()):
#         return redirect(url_for("main.index"))
#     return render_template("views/login.html", title="Employee Login", form=form)