# Generated by Django 5.0.7 on 2024-08-04 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['-created_at']},
        ),
        migrations.AlterModelOptions(
            name='transaction',
            options={'ordering': ['-created_at']},
        ),
        migrations.AlterField(
            model_name='category',
            name='is_default',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='category',
            name='type',
            field=models.IntegerField(choices=[(1, 'Thu nhập'), (2, 'Chi tiêu')]),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='type',
            field=models.IntegerField(choices=[(1, 'Thu nhập'), (2, 'Chi tiêu')]),
        ),
    ]