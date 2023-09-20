from flask import Flask, json, request
import sqlite3
import pika
from settings import TABLE_NAME, DB_NAME

app = Flask(__name__)
connection = sqlite3.connect(DB_NAME, check_same_thread=False)
cursor = connection.cursor()


@app.route('/')
def index():
    statement = f"SELECT * FROM {TABLE_NAME}"
    cursor.execute(statement)
    result = cursor.fetchall()
    print(result)
    response = app.response_class(
        response=json.dumps(result),
        status=200,
        mimetype='application/json'
    )
    return response


@app.route('/sale/', methods=['POST'])
def sale():

    """
    The sale function is used to create a new sale record in the database.
    It takes two parameters: phone and price. The phone parameter is the
    phone number of the customer who made a purchase, while price is how much
    the customer paid for their purchase.

    :return: A response object that contains the status code and a json string
    """
    data = request.form
    phone = data['phone']
    price = data['price']
    is_sale = True
    status = 'DONE'
    statement = f"INSERT INTO {TABLE_NAME}(phone,price," \
        f"is_sale,status) values (?,?,?,?)"
    cursor.execute(statement, (phone, price, is_sale, status))
    response = app.response_class(
        response=json.dumps({'STATUS': 'OK'}),
        status=200,
        mimetype='application/json'
    )
    return response


@app.route('/repair/', methods=['POST'])
def repair():

    """
    The repair function is used to repair a phone.
        It takes the following parameters:
            - phone (string): The name of the phone to be repaired.
            - price (int): The price of repairing this particular model.

    :return: The status of the repair
    """
    data = request.form
    phone = data['phone']
    price = data['price']
    is_sale = False
    status = 'IN PROCESS'
    statement = f"INSERT INTO {TABLE_NAME}(phone,price," \
        f"is_sale,status) values (?,?,?,?)"
    cursor.execute(statement, (phone, price, is_sale, status))

    # Публикуем сообщение
    # connection = pika.BlockingConnection(pika.ConnectionParameters(
    #     'localhost'))
    connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
    channel = connection.channel()
    channel.queue_declare(queue='repair')
    channel.basic_publish(exchange='',
                          routing_key='repair',
                          body=phone)
    connection.close()

    response = app.response_class(
        response=json.dumps({'STATUS': 'OK'}),
        status=200,
        mimetype='application/json'
    )
    return response


@app.route('/change/', methods=['POST'])
def change_status():
    """
    The change_status function is used to change the status of a user in the database.
    It takes two parameters: phone and status. The phone parameter is used to identify
    which user's status should be changed, while the status parameter indicates what
    that new value should be.

    :return: A json object with the key status and value ok
    """
    data = request.form
    phone = data['phone']
    status = data['status']
    print(status)
    statement = f"UPDATE {TABLE_NAME} set status = ? where phone = ?"
    cursor.execute(statement, (status, phone))

    response = app.response_class(
        response=json.dumps({'STATUS': 'OK'}),
        status=200,
        mimetype='application/json'
    )
    return response


if __name__ == '__main__':
    app.run(debug=True)
