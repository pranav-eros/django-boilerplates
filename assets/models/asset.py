from django.db import models
from assets.query_sets.asset_query_set import AssetQuerySet


class Asset(models.Model):
    ASSET_TYPE_CHOICES = (
        ("Movie", "movie"),
        ("Shows", "show"),
    )
    title = models.CharField( max_length=50)
    asset_type = models.CharField(max_length=50)

    objects = AssetQuerySet.as_manager()

    class Meta:
        db_table = ""

    def __str__(self):
        return self.title
