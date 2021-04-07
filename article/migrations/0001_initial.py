# Generated by Django 3.1.8 on 2021-04-06 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='Title')),
                ('text', models.TextField(verbose_name='Content')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]