# Generated by Django 4.2.4 on 2023-08-31 08:26

from django.db import migrations

def populate_persons(apps, schema_editor):
    Person = apps.get_model('helloworld', 'Person')

    Person.objects.create(first_name='Abhishek', last_name='Anand')
    Person.objects.create(first_name='Shreyan', last_name='Shetty')

class Migration(migrations.Migration):

    dependencies = [
        ('helloworld', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(populate_persons),
    ]