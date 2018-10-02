from django.db import models


class Bu(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False, unique=True)
    description = models.TextField()
    owner = models.CharField(max_length=50, blank=False, null=False)
    created = models.DateTimeField(auto_now_add=True)

class Product(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False, unique=True)
    description = models.TextField()
    owner = models.CharField(max_length=50, blank=False, null=False)
    created = models.DateTimeField(auto_now_add=True)
    bu = models.ForeignKey(Bu, to_field='name', on_delete='PROTECT', default='')




    # class Meta:
    #     ordering = ('created',)

class Application(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, blank=False, null=False, unique=True, db_index=True)
    description = models.TextField()
    is_production = models.BooleanField(default=False)
    owner = models.CharField(max_length=50, blank=False, null=False)
    product = models.ForeignKey(Product, to_field='name', on_delete='PROTECT', default='')




class Host(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False, unique=True, db_index=True)
    ip = models.CharField(max_length=100, blank=False, null=False,db_index=True)
    description = models.TextField()
    application = models.ForeignKey(Application, to_field='name', on_delete='PROTECT')
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
