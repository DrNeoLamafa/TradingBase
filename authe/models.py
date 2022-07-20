from django.db import models


class Base(models.Model):
    номер = models.AutoField(primary_key=True)
    название = models.CharField(max_length=100)
    заведующий = models.CharField(max_length=100)
    город = models.CharField(max_length=100)

class Item_base(models.Model):
    база = models.ForeignKey(Base, on_delete=models.CASCADE, null=False)
    артикул = models.AutoField(primary_key=True)
    название = models.CharField(max_length=70, null = True)
    тип = models.CharField(max_length=70)
    количество = models.IntegerField()
    цена = models.IntegerField()    



class Shops(models.Model):
    номер = models.IntegerField(primary_key = True)
    торговаябаза = models.ForeignKey(Base, null = True, on_delete=models.SET_NULL)
    класс = models.CharField(max_length=50)
    заведующий = models.CharField(max_length=100)
    название = models.CharField(max_length=70)

class Section_shop(models.Model):

    номермагазина = models.ForeignKey(Shops, on_delete = models.CASCADE)
    номеротдела = models.AutoField(primary_key=True)
    тип = models.CharField(max_length=70)
    заведующий = models.CharField(max_length=70)
    def __str__(self):
        return self.тип

class Type_item_shop(models.Model):
    номер = models.AutoField(primary_key=True)
    тип = models.CharField(max_length=50)
    def __str__(self):
        return self.тип

class Item_shop(models.Model):
    артикул = models.AutoField(primary_key=True)
    номермагазина = models.ForeignKey(Shops, on_delete=models.CASCADE, null=False)
    номеротдела = models.ForeignKey(Section_shop, on_delete = models.SET_NULL, null=True, blank=True )
    название = models.CharField(max_length=100)
    тип = models.ForeignKey(Type_item_shop, null=True, on_delete = models.SET_NULL)
    количество = models.IntegerField()
    цена = models.IntegerField()








