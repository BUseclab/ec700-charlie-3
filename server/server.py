import os
from flask import Flask, request, redirect, url_for, send_from_directory
from flask_restful import Resource, Api, reqparse
from sqlalchemy import create_engine
from werkzeug import secure_filename
from werkzeug.datastructures import FileStorage

app = Flask(__name__)
api = Api(app)

# Configs
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///malware.db'
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['DOWNLOAD_FOLDER'] = 'samples'
app.config['ALLOWED_EXTENSIONS'] = set(['zip'])

# SQLite engine, db assumed to be in same directory
e = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
ALLOWED_EXTENSIONS = set(['zip'])


###############################################################################
####### DB Functions
###############################################################################

def get_current_sample_id(machine_id):
    malware_id = None
    conn = e.connect()
    sql = 'SELECT malware_id FROM machine WHERE machine = :name'
    result = conn.execute(sql, name=machine_id).fetchone()
    if result is not None:
        malware_id = result[0]
    conn.close()
    return malware_id


def change_sample(machine_id):
    malware_id = get_current_sample_id(machine_id)
    conn = e.connect()
    sql = 'UPDATE machine SET malware_id=:new_id WHERE machine = :name'
    conn.execute(sql, name=machine_id, new_id=malware_id + 1)
    conn.close()

###############################################################################
####### I/O Related Functions
###############################################################################


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']


def upload_file(machine_id, results):
    malware_id = get_current_sample_id(machine_id)
    filename = secure_filename(results.filename)
    path = os.path.join(app.config['UPLOAD_FOLDER'], machine_id)

    # Create machine folder if it doesn't exist
    if not os.path.exists(path):
        os.makedirs(path)

    path = os.path.join(path, filename)
    results.save(path)

    change_sample(machine_id)

    return '', 200

###############################################################################
####### API Endpoints
###############################################################################


class Machine(Resource):
    def put(self, machine_id):
        return self.add_machine(machine_id)

    def get(self, machine_id):
        return self.add_machine(machine_id)

    def add_machine(self, machine_id):
        # Connect to databse
        conn = e.connect()
        # Perform query
        sql = 'INSERT INTO machine (machine, malware_id) VALUES (:name, 1)'
        conn.execute(sql, name=machine_id)
        conn.close()
        return '', 201


class Malware(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('result', type=FileStorage, location='files')

    def get(self, machine_id):
        malware_id = get_current_sample_id(machine_id)
        return send_from_directory(app.config['DOWNLOAD_FOLDER'],
                                   str(malware_id) + '.zip')

    def put(self, machine_id):
        args = self.parser.parse_args()
        results = args['result']
        if results and allowed_file(results.filename):
            return upload_file(machine_id, results)
        else:
            return 'File extension is not supported', 400

    def post(self, machine_id):
        args = self.parser.parse_args()
        results = args['result']
        if results and allowed_file(results.filename):
            return upload_file(machine_id, results)
        else:
            return 'File extension is not supported', 400

###############################################################################
####### API Endpoints
###############################################################################

# Register endpoints
api.add_resource(Malware, '/<string:machine_id>')
api.add_resource(Machine, '/create/<string:machine_id>')

if __name__ == '__main__':
    app.run(debug=True)
