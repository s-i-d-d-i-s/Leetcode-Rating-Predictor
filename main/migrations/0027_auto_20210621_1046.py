# Generated by Django 3.2.3 on 2021-06-21 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0026_contest_manager'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='atcoder',
            field=models.CharField(default='null', max_length=255),
        ),
        migrations.AlterField(
            model_name='team',
            name='codeforces',
            field=models.CharField(default='null', max_length=255),
        ),
        migrations.AlterField(
            model_name='team',
            name='github',
            field=models.CharField(default='null', max_length=255),
        ),
        migrations.AlterField(
            model_name='team',
            name='leetcode',
            field=models.CharField(default='null', max_length=255),
        ),
        migrations.AlterField(
            model_name='team',
            name='work',
            field=models.CharField(default='null', max_length=255),
        ),
    ]
