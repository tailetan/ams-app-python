

class CreatePrefix:

    def __init__(self):
        pass

    @classmethod
    def get_prefix(self, category_name):
        # prefix = ''
        prefix = category_name[:2]
        # for category_name_word in category_name_words:
        #     prefix += category_name_word[0]+category_name_word[1]
        return prefix.upper()
