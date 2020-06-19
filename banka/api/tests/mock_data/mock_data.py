

class UserData:
    @staticmethod
    def user_signup_data():
        return {
            "firstname": "test",
            "lastname": "testing",
            "password": "testsecret",
            "email": "test@gmail.com",
            "user_type": "staff",
            "is_admin": "true"
        }


def sign_up_data():
    return {
        "firstname": "test",
        "lastname": "testing",
        "password": "testsecret",
        "email": "testing@gmail.com",
        "user_type": "staff",
        "is_admin": True
    }


def create_account(user_id):
    return {
        "user_id": user_id,
        "account_type": "savings",
        "account_status": "draft",
        "balance": 0,
    }


def update_account():
    return {
        "account_status": "active",
        "account_type": "savings"
    }
