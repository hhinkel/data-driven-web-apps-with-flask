import flask

from infrastructure.view_modifiers import response

app = flask.Flask(__name__)


def get_latest_packages():
    return [
        {'name': 'flask', 'version': '1.2.3'},
        {'name': 'sqlalchemy', 'version': '2.2.0'},
        {'name': 'passlib', 'version': '3.0.0'}
    ]


@app.route('/')
@response(template_file='Home/index.html')
def index():
    return {'packages': get_latest_packages()}
    # return flask.render_template('Home/index.html', packages=get_latest_packages())


@app.route('/about')
@response(template_file='Home/about.html')
def about():
    return {}
    # return flask.render_template('Home/about.html')


if __name__ == '__main__':
    app.run(debug=True)
