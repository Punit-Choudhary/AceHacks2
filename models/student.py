from models import mongo_client


user_dbs = mongo_client['STUDENTS']

user_collection = user_dbs['user']
cert_collection = user_dbs['cert']


def get_user(roll):
    return user_collection.find_one({"_id": roll})


def register(user_data):
    try:
        user_collection.insert_one(user_data)
    except Exception as e:
        print("Error/register: {e}")


def add_club(roll, club):
    try:
        user_collection.update_one(
            {"_id": roll},
            {"$inc": {"clubs": club}}
        )
    except Exception as e:
        print("Error/add_club: {e}")


def add_society(roll, society):
    try:
        user_collection.update_one(
            {"_id": roll},
            {"$inc": {"societies": society}}
        )
    except Exception as e:
        print("Error/add_club: {e}")


def get_cert(roll):
    try:
        cert_data = cert_collection.find_one({"_id": roll})
        return cert_data
    except Exception as e:
        print("Error/get_cert: {e}")
        return False


def add_cert(roll, cert_data):
    try:
        cert_collection.update_one(
            {"_id": roll},
            {"$push": {"certs": cert_data}}
        )
    except Exception as e:
        print(f"Error/add_cert: {e}")

