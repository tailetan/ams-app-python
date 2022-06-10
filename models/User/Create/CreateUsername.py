from models.User.User import User


class CreateUsername:
    def __init__(self, **kwargs):
        self.attributes = kwargs

    def get_first_letter_of_last_name(self, last_name):
        result = ''
        last_name_words = last_name.split()
        for last_name_word in last_name_words:
            result += last_name_word[0]
        return result

    def count_username(self):
        results = self.attributes['user_model'].query().filter(
            User.first_name == self.attributes['user_model'].first_name)
        count = 0
        for p in results:
            if(
                self.get_first_letter_of_last_name(self.attributes['user_model'].last_name) ==
                self.get_first_letter_of_last_name(p.last_name)
            ):
                count += 1
        return count

    def generate_username(self):
        if self.count_username() == 0:
            result = self.attributes['user_model'].first_name + \
                self.get_first_letter_of_last_name(
                    self.attributes['user_model'].last_name)
        else:
            result = self.attributes['user_model'].first_name + \
                self.get_first_letter_of_last_name(
                    self.attributes['user_model'].last_name) + \
                str(self.count_username())
        return result.lower()
