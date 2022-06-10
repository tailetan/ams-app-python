# from BaseHandler import *
# from models.Location.Location import *
# from forms.Location.CreateCategoryForm import *
#
#
# class LocationHandler(BaseHandler):
#     """
#
#        Create a Category
#
#        """
#
#     def post(self):
#         location = Location()
#         form = CreateCategoryForm(self.request.POST, category)
#         if self.request.POST and form.validate():
#             form.populate_obj(category)
#             category.create_prefix()
#             # category.create_username()
#             category.save()
