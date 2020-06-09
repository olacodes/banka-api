from ...utils.helper import Helper

class UserFieldValidation:
    @staticmethod
    def validate_email(data):
        email_field = Helper.get_field(data, 'email')
        return Helper.is_valid_email(email_field)

    @staticmethod
    def validate_firstname(data):
        # Todo: must not start start with number
        """
        This function validate firstname field must exist and not less than 2 character
        """
        firstname_field = Helper.get_field(data, 'firstname')
        return Helper.min_length(firstname_field, 2)

    @staticmethod
    def validate_lastname(data):
        # not empty and not less than 2 characters
        lastname_field = Helper.get_field(data, 'lastname')
        return Helper.min_length(lastname_field, 2)


    @staticmethod
    def validate_password(data):
        # not empty and not less than 5 characters
        password_field = Helper.get_field(data, 'password')
        return Helper.min_length(password_field, 5)


    @staticmethod
    def validate_user_type(data):
        # not empty and must be either client or staff
        user_type_field = Helper.get_field(data, 'user_type')
        if (user_type_field == 'client' or user_type_field == 'staff'):
            return True;
        return False

    @staticmethod
    def validate_is_admin(data):
        is_admin_field = Helper.get_field(data, 'is_admin')
        return Helper.string_bool_to_bool(is_admin_field)


  