import flask
import pypi_org.services.package_service as package_service
from pypi_org.infrastructure.view_modifiers import response

blueprint = flask.Blueprint('packages', __name__, template_folder='templates')


@blueprint.route('/project/<package_name>')
# @response(template_file='packages/details.html')
def package_details(package_name: str):
    return "Package details for {}".format(package_name)


@blueprint.route('/<int:rank>')
# @response(template_file='packages/details.html')
def popular(rank: int):
    return "Package details for {}th most popular package".format(rank)
