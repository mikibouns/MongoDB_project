# Generated by Django 2.1.5 on 2019-02-05 14:15

import catalog_app.models
from django.db import migrations, models
import djongo.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('description', models.TextField()),
                ('img', models.ImageField(upload_to='')),
                ('room', djongo.models.fields.EmbeddedModelField(model_container=catalog_app.models.Room, null=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
