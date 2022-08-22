# Generated by Django 4.0.6 on 2022-07-14 06:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blogwebsite', '0005_alter_writeenby_authorid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='blodid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blogid', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='writeenby',
        ),
    ]
