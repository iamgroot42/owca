import os

from flask import Flask


def create_app(test_config=None):
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        # a default secret that should be overridden by instance config
        SECRET_KEY="dev"
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile("config.py", silent=True)
    else:
        # load the test config if passed in
        app.config.update(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # A platypus?
    @app.route("/platypus")
    def platypus():
        return '<img src="https://thumbs.gfycat.com/AdorableFailingJackal-size_restricted.gif">'

    # Perry the Platypus?!
    @app.route("/perry")
    def perry():
        return '<img src="https://i.pinimg.com/originals/67/78/4b/67784bf35a65ecd7c80843cc2cd5e6cd.gif">'

    # register the database commands
    from backend import db

    db.init_app(app)

    # apply the blueprints to the app
    from backend import course, auth, home

    app.register_blueprint(course.bp)
    app.register_blueprint(auth.bp)
    app.register_blueprint(home.bp)

    # make url_for('index') == url_for('blog.index')
    # in another app, you might define a separate main index here with
    # app.route, while giving the blog blueprint a url_prefix, but for
    # the tutorial the blog will be the main index
    app.add_url_rule("/", endpoint="index")

    return app