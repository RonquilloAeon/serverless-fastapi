import nox


@nox.session(python="3.8", reuse_venv=True)
def dev(session):
    """For creating a development virtual environment. Handy for setting interpreter in
    IDE.
    """
    session.install("-r", "requirements.txt")


@nox.session(python="3.8", reuse_venv=True)
def format(session):
    session.install("black")
    session.run("black", "app.py")


@nox.session(python="3.8", reuse_venv=True)
def check(session):
    session.install("flake8")
    session.run("flake8", "app.py")
