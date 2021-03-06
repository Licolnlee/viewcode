# Generated by Django 3.0.5 on 2020-04-26 07:27

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import re
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UserUUID', models.UUIDField(default=uuid.UUID('0224e9bd-2695-3a17-92e4-a3018ad3238a'), editable=False)),
                ('username', models.EmailField(max_length=254, unique=True)),
                ('password', models.TextField(max_length=128)),
                ('createTime', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=40)),
                ('gender', models.CharField(choices=[('dansei', '男'), ('josei', '女'), ('mainoriti', '其它'), ('empty', '')], default='', max_length=10)),
                ('occupation', models.CharField(max_length=40)),
                ('organization', models.CharField(max_length=40)),
                ('telephone', models.CharField(max_length=40)),
                ('introduction', models.CharField(max_length=100)),
                ('isDeleted', models.BooleanField(default=False)),
                ('favourites', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Docs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DocUUID', models.UUIDField(default=uuid.UUID('2bae2eb4-bd56-3a4e-bb49-f55f42de9b8e'), editable=False)),
                ('title', models.CharField(max_length=100)),
                ('uploadTime', models.DateTimeField(auto_now_add=True)),
                ('summary', models.CharField(max_length=100, validators=[django.core.validators.RegexValidator(re.compile('^\\d+(?:\\,\\d+)*\\Z'), code='invalid', message='Enter only digits separated by commas.')])),
                ('context', models.TextField()),
                ('isPublic', models.BooleanField(default=True)),
                ('isDeleted', models.BooleanField(default=False)),
                ('uploader', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jextractor.Users')),
            ],
        ),
    ]
