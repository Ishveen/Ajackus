# Generated by Django 3.1.2 on 2020-10-22 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0002_auto_20201022_2340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='category',
            field=models.CharField(choices=[('null', '--'), ('Mystery', 'Mystery'), ('Fiction', 'Fiction'), ('Fantasy', 'Fantasy')], default='--', max_length=50),
        ),
    ]