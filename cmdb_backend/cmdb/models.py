from django.db import models


class Bu(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False, unique=True)
    description = models.TextField()
    owner = models.ForeignKey('auth.User', related_name='bu', on_delete='PROTECT', default=1)
    created = models.DateTimeField(auto_now_add=True)

class Product(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False, unique=True)
    description = models.TextField()
    owner = models.ForeignKey('auth.User', related_name='product', on_delete='PROTECT', default=1)
    created = models.DateTimeField(auto_now_add=True)
    bu = models.ForeignKey(Bu, to_field='name', related_name='product', on_delete='PROTECT', default='')

class Application(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, blank=False, null=False, unique=True, db_index=True)
    description = models.TextField()
    is_production = models.BooleanField(default=False)
    owner = models.ForeignKey('auth.User', related_name='application', on_delete='PROTECT', default=1)
    product = models.ForeignKey(Product, to_field='name', related_name='application', on_delete='PROTECT', default='')


class Host(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False, unique=True, db_index=True)
    ip = models.CharField(max_length=100, blank=False, null=False,db_index=True)
    description = models.TextField()
    owner = models.ForeignKey('auth.User', related_name='host', on_delete='PROTECT', default=1)
    application = models.ForeignKey(Application, related_name='host', to_field='name', on_delete='PROTECT')
    status_choice = (
        ('INUSE', 'INUSE'),
        ('SPARE', 'SPARE'),
        ('LEGACY', 'LEGACY'),
        ('SHUTDOWN', 'SHUTDOWN'),
    )
    status = models.CharField(
        max_length=10,
        choices=status_choice,
        default='SPARE',
    )
    created = models.DateTimeField(auto_now_add=True)
