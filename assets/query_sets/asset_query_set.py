from django.db import models


class AssetQuerySet(models.QuerySet):

    def movies(self):
        return self.filter(asset_type='movies')

    def shows(self):
        return self.filter(asset_type='shows')
