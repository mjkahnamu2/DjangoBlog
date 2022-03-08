# Generated by Django 4.0.3 on 2022-03-08 18:34

from django.db import migrations, models
import django_quill.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('content', django_quill.fields.QuillField()),
                ('image', models.ImageField(upload_to='media/images')),
                ('slug', models.SlugField(unique=True)),
                ('publish_date', models.DateTimeField()),
                ('status', models.BooleanField(default=0)),
            ],
            options={
                'ordering': ['-publish_date'],
            },
        ),
    ]
