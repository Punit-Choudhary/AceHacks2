from flask import Blueprint, request


import models.student as student_db
import tools.image as image


stdnt = Blueprint('stdnt', __name__)


@stdnt.route("/add/clubs", methods=['POST'])
def add_clubs():
    # Add club
    if request.method == 'POST':
        roll = request.json['roll']
        club_id = request.json['club_id']

        student_db.add_club(roll, club_id)
        
        return "OK", "200"


@stdnt.route("/add/society", methods=['POST'])
def add_society():
    # Add society
    if request.method == 'POST':
        roll = request.json['roll']
        socity_id = request.json['society_id']

        student_db.add_society(roll, socity_id)
        
        return "OK", "200"


@stdnt.route('/cert', method=['GET', 'POST'])
def certificates():
    roll = request.json['roll']
    if request.method == 'GET':
        cert_data = student_db.get_cert(roll)

        if cert_data:
            return cert_data, "200"
        else:
            return {"err": "Not Found"}, "404"
    elif request.method == 'POST':
        cert_img = request.files['img']
        cert_name = request.json['name']
        cert_img_url = image.upload(cert_img, ''.join([x for x in cert_name if x.isalnum()]), "Certificates")

        cert_data = {
            "name": request.json['name'],
            "img": cert_img_url,
            "url": request.json['url']
        }

        student_db.add_cert(roll, cert_data)

        return "OK", "200"

