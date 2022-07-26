# Generated by Django 3.0.8 on 2020-11-27 12:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authe', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AuthGroup',
        ),
        migrations.DeleteModel(
            name='AuthGroupPermissions',
        ),
        migrations.DeleteModel(
            name='AuthPermission',
        ),
        migrations.DeleteModel(
            name='AuthUser',
        ),
        migrations.DeleteModel(
            name='AuthUserGroups',
        ),
        migrations.DeleteModel(
            name='AuthUserUserPermissions',
        ),
        migrations.DeleteModel(
            name='DjangoAdminLog',
        ),
        migrations.DeleteModel(
            name='DjangoContentType',
        ),
        migrations.DeleteModel(
            name='DjangoMigrations',
        ),
        migrations.DeleteModel(
            name='DjangoSession',
        ),
        migrations.DeleteModel(
            name='БазаМагазин',
        ),
        migrations.DeleteModel(
            name='Магазины',
        ),
        migrations.DeleteModel(
            name='НазваниеМагазинов',
        ),
        migrations.RemoveField(
            model_name='отделтовары',
            name='артикул',
        ),
        migrations.DeleteModel(
            name='Отделы',
        ),
        migrations.DeleteModel(
            name='ТоварБазы',
        ),
        migrations.DeleteModel(
            name='ТоварБазыАртикул',
        ),
        migrations.DeleteModel(
            name='ТорговыеБазы',
        ),
        migrations.DeleteModel(
            name='ОтделТовары',
        ),
        migrations.DeleteModel(
            name='ТоварМагазин',
        ),
    ]
