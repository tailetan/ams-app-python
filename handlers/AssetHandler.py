from BaseHandler import *
from models.Asset.Asset import *
from forms.Asset.CreateAssetForm import *


class AssetHandler(BaseHandler):
    """

       Create an Asset

       """

    def post(self):
        asset = Asset()
        form = CreateAssetForm(self.request.POST, asset)
        if self.request.POST and form.validate():
            form.populate_obj(asset)
            # asset.create_prefix()
            # category.create_username()
            asset.save()
        self.return_json(self.request.POST.items())

