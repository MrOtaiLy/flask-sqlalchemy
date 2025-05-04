import datetime
from data import db_session
from data.users import User
from data.jobs import Jobs

def main():
    db_session.global_init("db/mars.db")
    session = db_session.create_session()

    user = User()
    user.surname = "Scott"
    user.name = "Ridley"
    user.age = 21
    user.position = "captain"
    user.speciality = "research engineer"
    user.address = "module_1"
    user.email = "scott_chief@mars.org"
    session.add(user)

    user = User()
    user.surname = "Newman"
    user.name = "Joe"
    user.age = 25
    user.position = "engineer"
    user.speciality = "pilot"
    user.address = "module_2"
    user.email = "joe@mars.org"
    session.add(user)

    user = User()
    user.surname = "Doe"
    user.name = "John"
    user.age = 30
    user.position = "builder"
    user.speciality = "construction"
    user.address = "module_3"
    user.email = "john_doe@mars.org"
    session.add(user)

    user = User()
    user.surname = "Smith"
    user.name = "Jane"
    user.age = 22
    user.position = "navigator"
    user.speciality = "astronomy"
    user.address = "module_4"
    user.email = "jane_smith@mars.org"
    session.add(user)

    session.commit()

    job = Jobs()
    job.team_leader = 1
    job.job = "deployment of residential modules 1 and 2"
    job.work_size = 15
    job.collaborators = "2, 3"
    job.start_date = datetime.datetime.now()
    job.is_finished = False
    session.add(job)

    session.commit()

if __name__ == "__main__":
    main()
