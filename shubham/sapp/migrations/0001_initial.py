# Generated by Django 2.2.3 on 2019-08-13 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='web2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('news_head', models.CharField(max_length=225)),
                ('news_web', models.CharField(max_length=225)),
                ('date', models.DateField()),
            ],
        ),
    ]
