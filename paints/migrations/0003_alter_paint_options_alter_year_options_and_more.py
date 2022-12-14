# Generated by Django 4.1.1 on 2022-09-20 17:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('paints', '0002_collection_material_year_alter_paint_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='paint',
            options={'verbose_name': 'Картину', 'verbose_name_plural': 'Картины'},
        ),
        migrations.AlterModelOptions(
            name='year',
            options={'verbose_name': 'Год', 'verbose_name_plural': 'Год написания'},
        ),
        migrations.RemoveField(
            model_name='paint',
            name='materials',
        ),
        migrations.AddField(
            model_name='paint',
            name='materials',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='paints.material', verbose_name='Коллекция'),
        ),
    ]
