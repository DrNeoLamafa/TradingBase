# Generated by Django 3.0.8 on 2020-11-27 13:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authe', '0005_магазины_отделмагазин_товармагазинов'),
    ]

    operations = [
        migrations.AlterField(
            model_name='товармагазинов',
            name='номеротдела',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='authe.ОтделМагазин'),
        ),
    ]
