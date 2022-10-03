# Generated by Django 4.1.1 on 2022-09-20 17:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('paints', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Коллекция')),
            ],
            options={
                'verbose_name': 'Коллекции',
                'verbose_name_plural': 'Коллекция',
            },
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Материал')),
            ],
            options={
                'verbose_name': 'Материал',
                'verbose_name_plural': 'Материал',
            },
        ),
        migrations.CreateModel(
            name='Year',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Год')),
            ],
            options={
                'verbose_name': 'Год',
                'verbose_name_plural': 'Год',
            },
        ),
        migrations.AlterModelOptions(
            name='paint',
            options={'verbose_name': 'Картина', 'verbose_name_plural': 'Картину'},
        ),
        migrations.AddField(
            model_name='paint',
            name='in_stock',
            field=models.BooleanField(default=True, verbose_name='В наличии '),
        ),
        migrations.RemoveField(
            model_name='paint',
            name='materials',
        ),
        migrations.AlterField(
            model_name='paint',
            name='price',
            field=models.FloatField(blank=True, verbose_name='Цена'),
        ),
        migrations.AddField(
            model_name='paint',
            name='collection',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='paints.collection', verbose_name='Коллекция'),
        ),
        migrations.AddField(
            model_name='paint',
            name='materials',
            field=models.ManyToManyField(to='paints.material'),
        ),
        migrations.AlterField(
            model_name='paint',
            name='year',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='paints.year', verbose_name='Год'),
        ),
    ]