# Generated by Django 4.1.1 on 2022-11-03 04:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stockapp', '0002_alter_item_item_code'),
        ('dashboard', '0005_alter_fashion_order_item_id'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='fashion_order',
            new_name='Order',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='item_Id',
            new_name='item_code',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='quantity_order',
            new_name='quantity',
        ),
    ]
