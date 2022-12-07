# Generated by Django 4.1.3 on 2022-12-07 00:03

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_rename_spendinglimit_user_spendable'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=512, validators=[django.core.validators.MinLengthValidator(8)]),
        ),
    ]
