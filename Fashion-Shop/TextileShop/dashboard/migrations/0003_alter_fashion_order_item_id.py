# Generated by Django 4.1.1 on 2022-11-02 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_alter_fashion_order_item_id_delete_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fashion_order',
            name='item_Id',
            field=models.CharField(max_length=20, null=True),
        ),
    ]