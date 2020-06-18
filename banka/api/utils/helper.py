import re
import random
import string


class Helper:
    email_regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
    url_regex = 'https?:\/\/w{0,3}\w*?\.(\w*?\.)?\w{2,3}\S*|www\.(\w*?\.)?\w*?\.\w{2,3}\S*|(\w*?\.)?\w*?\.\w{2,3}[\/\?]\S*'
    decimal_regex = '^[-+]?[0-9]+\.[0-9]+$'

    @staticmethod
    def regex_validator(value, regex):
        return False if not value else bool(re.search(regex, value))

    @classmethod
    def is_valid_email(cls, email):
        return cls.regex_validator(email, cls.email_regex)

    @staticmethod
    def min_length(value, num):
        return False if len(str(value)) < num else True

    @classmethod
    def is_valid_url(cls, url):
        return cls.regex_validator(url, cls.url_regex)

    @staticmethod
    def is_bool(value):
        return True if type(value) == bool else False

    @staticmethod
    def get_field(data, value):
        try:
            return data[value]
        except:
            return ""

    @staticmethod
    def string_bool_to_bool(value):
        if value == True or value == "True" or value == "true":
            return True
        elif value == "False" or value == False or value == "false":
            return True
        else:
            return ""

    @staticmethod
    def create_random_num():
        return (random.randint(1000000000, 9999999999))

    @staticmethod
    def absolute_length(value, num):
        return True if len(str(value)) == num else False

    @staticmethod
    def max_length(value, num):
        return False if len(str(value)) > num else True

    @classmethod
    def is_decimal(cls, dec):
        return cls.regex_validator(str(float(dec)), cls.decimal_regex)

    @classmethod
    def create_account_num(cls, model):
        account_number = cls.create_random_num()
        unique = False

        while not unique:
            try:
                account_num = model.objects.get(account_number=account_number)
                if not account_num:
                    unique = True
                    return account_number
                else:
                    account_number = cls.create_random_num()
            except:
                unique = True
                return account_number

    @staticmethod
    def get_from_DB(model, field, value):
        try:
            result = model.objects.get(field=value)
            return result
        except:
            return False
