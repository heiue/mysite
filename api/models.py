# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange basemodels' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the basemodels, but don't rename db_table values or field names.
from django.db import models


class SaasScPoster(models.Model):
    qrstyle = models.CharField(db_column='qrStyle', max_length=120)  # Field name made lowercase.
    posterid = models.IntegerField(db_column='posterId')  # Field name made lowercase.
    title = models.CharField(max_length=120)
    infoid = models.IntegerField(db_column='infoId')  # Field name made lowercase.
    posterimg = models.CharField(db_column='posterImg', max_length=120)  # Field name made lowercase.
    createtime = models.IntegerField(db_column='createTime')  # Field name made lowercase.
    status = models.IntegerField()
    shopcode = models.CharField(db_column='shopCode', max_length=20)  # Field name made lowercase.
    sellerid = models.IntegerField(db_column='sellerId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'saas_sc_poster'


class ChUser(models.Model):
    name = models.CharField(db_column='name', max_length=20)
    phone = models.CharField(db_column='phone', max_length=11)

    class Meta:
        db_table = 'ch_user'


