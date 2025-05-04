from flask import Flask, render_template
from data.db_session import global_init, create_session
from data.jobs import Jobs

app = Flask(__name__)


@app.route("/jobs")
def jobs_list():
    session = create_session()
    jobs = session.query(Jobs).all()
    return render_template("jobs_list.html", jobs=jobs)


if __name__ == "__main__":
    global_init("db/mars.db")
    app.run()
