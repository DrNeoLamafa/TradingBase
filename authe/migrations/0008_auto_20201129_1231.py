# Generated by Django 3.0.8 on 2020-11-29 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authe', '0007_товармагазинов_номермагазина'),
    ]

    operations = [
        migrations.AlterField(
            model_name='отделмагазин',
            name='номеротдела',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
