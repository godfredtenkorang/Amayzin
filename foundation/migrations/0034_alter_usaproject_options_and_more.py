# Generated by Django 4.1 on 2024-03-26 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foundation', '0033_alter_ghanaproject_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='usaproject',
            options={'verbose_name_plural': 'USA projects'},
        ),
        migrations.RemoveField(
            model_name='usaproject',
            name='date_added',
        ),
        migrations.AlterField(
            model_name='ghanacategory',
            name='date_added',
            field=models.DateTimeField(verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='usacategory',
            name='date_added',
            field=models.DateTimeField(verbose_name='date published'),
        ),
    ]
