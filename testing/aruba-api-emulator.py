from flask_restful import Api
from aruba_api_endpoints import *

app = Flask(__name__)
api = Api(app)

api.add_resource(login, '/v1/api/login')
api.add_resource(logout, '/v1/api/logout')
api.add_resource(write_memory, '/v1/configuration/object/write_memory')


if __name__ == '__main__':
    app.run()