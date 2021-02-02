# Generated by Django 3.1.5 on 2021-02-02 04:09

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('controlpannel', '0006_auto_20210201_1918'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 2, 2, 9, 39, 53, 26884)),
        ),
        migrations.CreateModel(
            name='Product_Side_Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('P_image', models.ImageField(upload_to='products/')),
                ('P_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='controlpannel.product')),
            ],
        ),
    ]
