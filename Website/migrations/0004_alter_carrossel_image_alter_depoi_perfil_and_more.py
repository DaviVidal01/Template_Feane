# Generated by Django 4.2.4 on 2023-09-05 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Website', '0003_products'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carrossel',
            name='image',
            field=models.ImageField(upload_to='./carrossel'),
        ),
        migrations.AlterField(
            model_name='depoi',
            name='perfil',
            field=models.ImageField(upload_to='./users'),
        ),
        migrations.AlterField(
            model_name='infor',
            name='image',
            field=models.ImageField(upload_to='./images'),
        ),
        migrations.AlterField(
            model_name='offer',
            name='imagem',
            field=models.ImageField(upload_to='./offers'),
        ),
        migrations.AlterField(
            model_name='products',
            name='imagem',
            field=models.ImageField(upload_to='./produtos'),
        ),
    ]