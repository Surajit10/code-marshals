# Generated by Django 3.1.7 on 2021-05-30 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0004_alter_blogs_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]