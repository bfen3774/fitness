# Generated by Django 2.0 on 2018-02-16 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workouts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plan',
            name='calories',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='plan',
            name='goals',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='plan',
            name='macro_carb',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='plan',
            name='macro_fat',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='plan',
            name='macro_protein',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='plan',
            name='period',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='plan',
            name='user',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='plan',
            name='user_age',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='plan',
            name='user_body_type_end',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='plan',
            name='user_body_type_start',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='plan',
            name='user_ending_weight',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='plan',
            name='user_sex',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='plan',
            name='user_starting_weight',
            field=models.IntegerField(blank=True),
        ),
    ]
