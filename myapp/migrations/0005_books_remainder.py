# Generated by Django 2.1.7 on 2019-07-07 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_auto_20190707_2140'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='remainder',
            field=models.CharField(default='3 days', max_length=255),
        ),
    ]
