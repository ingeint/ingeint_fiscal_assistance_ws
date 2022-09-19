from flask import Flask, request, jsonify
from dbfread import DBF
from utils import fiscal

app = Flask(__name__)


@app.route('/create_invoice', methods=['POST'])
def create_invoice():
    file = request.get_json()
    fiscal.create_invoice(file)
    return "Created"


@app.route('/get_invoice_number', methods=['GET'])
def get_invoice_number():
    number = request.args['number']
    table = DBF('C:\PRINTSPOOL\DATOS3.DBF', load=True)
    records = table.records
    loop = len(records) - 1
    while loop > 0:
        if records[loop]['REFINT'] == number:
            return records[loop]['NUMDOC']
        loop -= 1
    return "Not Processed"


if __name__ == '__main__':
    app.run()
