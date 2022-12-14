# Generated by Django 3.1 on 2022-10-02 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='about',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='isSelected',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='certifications',
            name='certificationId',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='education',
            name='endYear',
            field=models.DecimalField(decimal_places=0, max_digits=4, null=True),
        ),
        migrations.AlterField(
            model_name='experience',
            name='endDate',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='projects',
            name='endDate',
            field=models.DateField(null=True),
        ),
    ]
