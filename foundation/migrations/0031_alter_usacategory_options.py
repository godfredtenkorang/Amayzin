# Generated by Django 4.1 on 2024-03-26 03:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foundation', '0030_ghanacategory_usacategory_usaproject_ghanaproject'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='usacategory',
            options={'ordering': ['-date_added'], 'verbose_name_plural': 'USA category'},
        ),
    ]
