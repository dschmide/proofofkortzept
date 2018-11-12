# Generated by Django 2.0.5 on 2018-11-12 06:22

from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('restful_api', '0008_auto_20181111_1913'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlacedLandmark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', django.contrib.postgres.fields.ArrayField(base_field=models.DecimalField(decimal_places=15, max_digits=18), size=2)),
                ('label', models.CharField(max_length=99)),
                ('owner', models.CharField(max_length=99)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('creator',),
            },
        ),
    ]
