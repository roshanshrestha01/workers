# Generated by Django 2.2.3 on 2019-07-07 15:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('work_order', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='workorder',
            old_name='worker',
            new_name='workers',
        ),
    ]