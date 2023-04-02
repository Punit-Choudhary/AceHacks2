from flask import Blueprint, request


import models.student as student_db



auth = Blueprint('auth', __name__, template_folder="template")


@auth.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        roll_num = request.json['roll']
        passwd = request.json['passwd']

        user_data = student_db.get_user(roll_num)

        if passwd == user_data['passwd']:
            return {
                "roll": roll_num
            }, "200"
        else:
            return {
                "err": "Wrong Username/Password!"
            }, "403"


@auth.route('/register', methods=['POST'])
def register():
    if request.method == 'POST':
        roll = request.json['roll']
        user_data = {
            "_id": roll,
            "aadhar": request.json['aadhar'],
            "passwd": request.json['passwd'],
            "college": {
                "college_id": request.json['college_id'],
                "branch": request.json['branch'],
                "yoj": request.json['yoj']
            },
            "interest": [],
            "clubs": [],
            "societies": [],
            "report": [],
            "certs": [],
            "hackathons": []
        }

        student_db.register(user_data)
        return {"roll": roll}
