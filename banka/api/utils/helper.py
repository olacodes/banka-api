import re

class Helper:
    email_regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
    url_regex = 'https?:\/\/w{0,3}\w*?\.(\w*?\.)?\w{2,3}\S*|www\.(\w*?\.)?\w*?\.\w{2,3}\S*|(\w*?\.)?\w*?\.\w{2,3}[\/\?]\S*'

    @staticmethod
    def is_empty(value):
        return not (bool(value))
    
    @staticmethod
    def regex_validator(value, regex):
        return False if not value else  bool(re.search(regex, value))

    @classmethod
    def is_valid_email(cls, email):
        return cls.regex_validator(email, cls.email_regex)

    @staticmethod
    def min_length(value, num):
        return False if len(value) < num else True;
    
    @classmethod
    def is_valid_url(cls, url):
        return cls.regex_validator(url, cls.url_regex)

    @staticmethod
    def is_bool(value):
        return True if type(value) == bool else False;

    @staticmethod
    def get_field(data, value):
        try:
            return data[value]
        except:
            return "";

    @staticmethod
    def string_bool_to_bool(value):
        if value == True or value == "True" or value == "true":
            return True;
        elif value == "False" or value == False or value == "false":
            return True;
        else:
            return "";