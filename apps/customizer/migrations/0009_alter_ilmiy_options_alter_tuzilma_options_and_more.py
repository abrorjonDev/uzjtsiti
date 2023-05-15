# Generated by Django 4.2.1 on 2023-05-15 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customizer', '0008_ilmiy_tuzilma'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ilmiy',
            options={'verbose_name_plural': 'Ilmiy'},
        ),
        migrations.AlterModelOptions(
            name='tuzilma',
            options={'verbose_name_plural': 'Tuzilma'},
        ),
        migrations.RemoveField(
            model_name='tuzilma',
            name='type',
        ),
        migrations.AddField(
            model_name='tuzilma',
            name='slug',
            field=models.CharField(choices=[('director', 'Direktor'), ('ilmiy-kengash', 'Ilmiy kengash'), ('institut-kengashi', 'Institut kengashi')], default='', max_length=50),
        ),
        migrations.AddField(
            model_name='tuzilma',
            name='title',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]
