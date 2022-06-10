from BaseHandler import *
from factories.ObjectFactory import ObjectFactory
from models.Category.Category import *
from forms.Category.CreateCategoryForm import *


class CategoryHandler(BaseHandler):
    """

       Create a Category

       """
    invoker = ObjectFactory.create_invoker_object('CategoryInvoker')
    category_object = ObjectFactory.create_category_object('Category')

    def post(self):

        form_object = ObjectFactory.create_form_object(
            'CreateCategoryForm',
            self.request.POST,
            self.category_object
        )
        if self.request.POST and form_object.validate():
            form_object.populate_obj(self.category_object)
            command_create_object = ObjectFactory.create_command_object(
                'CrudCategoryCommand',
                category=self.category_object,
                form=form_object
            )
            self.invoker.register('create', command_create_object)
            self.invoker.execute('create')
        self.return_json(self.request.POST.items())


