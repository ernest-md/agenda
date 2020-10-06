from . import db
import os
import json

from flask import Flask, jsonify, request
from data.db import get_db


def create_app(test_config=None):
    # crea i configura la app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(__name__)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'agenda.sqlite'),
    )

    if test_config is None:
        # carreguem la configuració del 'instance' si hi ha
        app.config.from_pyfile('config.py', silent=True)
    else:
        # carreguem la configuració si hi ha
        app.config.from_mapping(test_config)

    # asegurar que existeix la carpeta 'instance'
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    app.config['JSON_AS_ASCII'] = False

    @app.route('/contactes/', methods=['GET', 'POST', 'DELETE', 'PUT'])
    def all_contacts():
        if request.method == 'GET':
            # agafem les dades de la base de dades fent una consulta
            db = get_db()

            data = db.execute(
                ' SELECT id, nom, cognoms, correu, telf, pais, address, poblacio, codipostal, provincia, NIF '
                ' FROM contacts '
            ).fetchall()

            # amb aquesta linea fem un bucle amb les dades trobades i les pasa a JSON
            cont = [{'id': contacts['id'], 'nom':contacts['nom'], 'cognoms':contacts['cognoms'], 'correu':contacts['correu'], 'telf':contacts['telf'], 'pais':contacts['pais'],
                     'address':contacts['address'], 'poblacio':contacts['poblacio'], 'codipostal':contacts['codipostal'], 'provincia':contacts['provincia'], 'NIF':contacts['NIF']} for contacts in data]

            return jsonify(cont)

        elif request.method == 'POST':
            # ens conectem a la base de dades, i recollim les dades que ens envia el POST
            db = get_db()
            post_data = request.get_json()

            # executem una transacció amb un INSERT amb les dades
            db.execute(' BEGIN TRANSACTION ')

            db.execute(
                'INSERT INTO contacts (nom, cognoms, correu, telf, pais, address, poblacio, codipostal, provincia, NIF) VALUES (?,?,?,?,?,?,?,?,?,?)',
                (post_data.get('nom'), post_data.get('cognoms'), post_data.get('correu'), post_data.get('telf'), post_data.get('pais'), post_data.get('address'), post_data.get('poblacio'),
                 post_data.get('codipostal'), post_data.get('provincia'),  post_data.get('NIF'))
            )

            db.execute(' COMMIT ')

            return("Contact added!")

        elif request.method == 'DELETE':
            # ens conectem a la base de dades, i recollim les dades que ens envia al DELETE
            db = get_db()
            id_contact = request.args.get("index")

            # executem una transacció amb un DELETE de les dades
            db.execute(' BEGIN TRANSACTION ')

            db.execute(
                'DELETE FROM contacts WHERE id = ?',
                (id_contact)
            )

            db.execute(' COMMIT ')

            return("Contact deleted!")

        elif request.method == 'PUT':
            # ens conectem a la base de dades
            db = get_db()
            post_data = request.get_json()

            # executem una transacció amb un UPDATE amb les dades
            db.execute(' BEGIN TRANSACTION ')

            db.execute(
                'UPDATE contacts SET nom = ?, cognoms = ?, correu = ?, telf = ?, pais = ?, address = ?, poblacio = ?, codipostal = ?, provincia = ?, NIF = ? WHERE id = ?',
                (post_data.get('nom'), post_data.get('cognoms'), post_data.get('correu'), post_data.get('telf'), post_data.get('pais'), post_data.get('address'), post_data.get('poblacio'),
                 post_data.get('codipostal'), post_data.get('provincia'),  post_data.get('NIF'), post_data.get('id'))
            )

            db.execute(' COMMIT ')

            return("Contact updated!")
        else:
            return("ok")

    db.init_app(app)

    return app
