from flask import Flask, render_template, redirect, request
from data.db_session import global_init, create_session
from data.jobs import Jobs
from data.users import User
from werkzeug.security import generate_password_hash

app = Flask(__name__)


@app.route("/jobs")
def jobs_list():
    session = create_session()
    jobs = session.query(Jobs).all()
    return render_template("jobs_list.html", jobs=jobs)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        if request.form["password"] != request.form["repeat_password"]:
            return render_template("register.html", message="Пароли не совпадают")

        session = create_session()
        if session.query(User).filter(User.email == request.form["email"]).first():
            return render_template(
                "register.html", message="Такой пользователь уже есть"
            )

        user = User(
            surname=request.form["surname"],
            name=request.form["name"],
            age=int(request.form["age"]),
            position=request.form["position"],
            speciality=request.form["speciality"],
            address=request.form["address"],
            email=request.form["email"],
            hashed_password=generate_password_hash(request.form["password"]),
        )
        session.add(user)
        session.commit()
        return redirect("/jobs")
    return render_template("register.html")


if __name__ == "__main__":
    global_init("db/mars.db")
    app.run()
