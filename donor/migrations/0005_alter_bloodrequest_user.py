# Generated by Django 4.0.4 on 2022-04-22 08:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('donor', '0004_bloodrequest_tel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bloodrequest',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
