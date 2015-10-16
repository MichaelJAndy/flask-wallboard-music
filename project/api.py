from project import api_manager
from project.models import SongRequest, SongFile

api_blueprint = api_manager.create_api_blueprint(SongRequest, methods=['GET', 'POST'])
api_blueprint = api_manager.create_api_blueprint(SongFile, methods=['GET', 'POST'])
