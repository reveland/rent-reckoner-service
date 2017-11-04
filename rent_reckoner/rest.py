import json
from reckoner import RentReckoner
from provider_trello import DataProvider
import flask
from flask import request

APP = flask.Flask(__name__)

DATA_PATH = "./rent_reckoner/data/"

DATA_PROVIDER = DataProvider(DATA_PATH)
RENT_RECKONER = RentReckoner(DATA_PROVIDER)


@APP.route("/habitations/<int:habitant_id>/residents/<int:resident_id>/dept")
def get_dept(habitant_id, resident_id):
    dept = "# %d #" % RENT_RECKONER.get_debt(
        habitant_id, DATA_PROVIDER.get_resident_by_id(habitant_id, resident_id))
    resp = flask.Response(dept)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp


@APP.route("/habitations/<int:habitant_id>/bills")
def get_bills(habitant_id):
    bills = json.dumps(RENT_RECKONER.get_bills_to_ui(
        habitant_id), default=lambda o: o.__dict__)
    resp = flask.Response(bills)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp


@APP.route("/habitations/<int:habitant_id>/residents")
def get_residents(habitant_id):
    residents = json.dumps(RENT_RECKONER.get_residents_to_ui(
        habitant_id), default=lambda o: o.__dict__)
    resp = flask.Response(residents)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp


@APP.route("/habitations/<int:habitant_id>/update_depts")
def update_depts(habitant_id):
    RENT_RECKONER.update_debts(habitant_id)
    return "updated"


@APP.route("/habitations/<int:habitant_id>/residents", methods=['POST'])
def add_resident(habitant_id):
    start = request.args.get('start')
    end = request.args.get('end')
    name = request.args.get('name')

    added_resident = DATA_PROVIDER.add_resident(habitant_id, start, end, name)
    resp = flask.Response(added_resident)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp


@APP.route("/habitations/<int:habitant_id>/bills", methods=['POST'])
def add_bill(habitant_id):
    start = request.args.get('start')
    end = request.args.get('end')
    type = request.args.get('type')
    amount = request.args.get('amount')

    added_bill = DATA_PROVIDER.add_bill(habitant_id, start, end, type, amount)
    resp = flask.Response(added_bill)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp


if __name__ == "__main__":
    APP.run()
