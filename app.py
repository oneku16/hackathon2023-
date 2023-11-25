from flask import Flask, request, jsonify
from datetime import datetime
from face_recognition.camera import take_pic


class Hackathon:
    def __init__(self):
        self.seen = set()

    def face_recognition(self):
        take_pic()



app = Flask(__name__)
@app.route('/api/data', methods=['POST'])
def get_data():
    content = request.json
    customer_id = content['customer_id']
    in_queue_date = content['in_queue_date']
    in_queue_time = content['in_queue_time']
    service_type = content['service_type']
    queue_type = content['queue_type']
    branch = content['branch']
    city = content['city']
    pin = content['confirmationCode']
    # print(customer_id)

    # parse the datetime string into a datetime object
    # date_time_obj = datetime.strptime(date_time, '%Y-%m-%d %H:%M:%S')



    # return a response
    return jsonify({"message": "Data received and processed", "status": "success"}), 200


if __name__ == '__main__':
    app.run(debug=True)
