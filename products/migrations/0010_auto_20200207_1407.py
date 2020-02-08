# Generated by Django 2.2.7 on 2020-02-07 09:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_auto_20200131_0434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='ingredients',
            field=models.ManyToManyField(to='products.Ingredient'),
        ),
        migrations.AlterField(
            model_name='product',
            name='manufacture',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='manuf', to='products.Manufacturer'),
        ),
    ]
