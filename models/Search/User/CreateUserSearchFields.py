from google.appengine.api import search


class CreateUserSearchFields():
    def __init__(self, **kwargs):
        self.attributes = kwargs

    def tokenize_autocomplete(self, phrase):
        a = []
        for word in phrase.split():
            j = 1
            while True:
                for i in range(len(word) - j + 1):
                    a.append(word[i:i + j])
                if j == len(word):
                    break
                j += 1
        return a

    def create_search_fields(self):
        staff_code = self.attributes['item'].staff_code
        first_name = self.attributes['item'].first_name
        last_name = self.attributes['item'].last_name
        full_name = self.attributes['item'].full_name
        location = self.attributes['item'].location
        username = self.attributes['item'].username
        password = self.attributes['item'].password
        role = self.attributes['item'].role
        date_of_birth = self.attributes['item'].date_of_birth
        joined_date = self.attributes['item'].joined_date

        staff_code_search = ','.join(self.tokenize_autocomplete(
            self.attributes['item'].staff_code))
        full_name_search = ','.join(self.tokenize_autocomplete(
            self.attributes['item'].full_name))
            
        document = search.Document(
            doc_id=self.attributes['item'].key.urlsafe(),
            fields=[
                search.TextField(name='staff_code', value=staff_code),
                search.TextField(name='first_name', value=first_name),
                search.TextField(name='last_name', value=last_name),
                search.TextField(name='full_name', value=full_name),
                search.TextField(name='location', value=location),
                search.TextField(name='username', value=username),
                search.TextField(name='password', value=password),
                search.TextField(name='role', value=role),
                search.TextField(name='date_of_birth', value=str(date_of_birth)),
                search.TextField(name='joined_date', value=str(joined_date)),
                search.TextField(name='staff_code_search',
                                 value=staff_code_search),
                search.TextField(name='full_name_search',
                                 value=full_name_search)
            ])
        return document
