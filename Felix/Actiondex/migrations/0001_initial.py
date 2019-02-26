# Generated by Django 2.1.7 on 2019-02-26 21:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Drug',
            fields=[
                ('name', models.CharField(max_length=200, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('disease', models.CharField(max_length=200)),
                ('occupation', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Trial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result', models.CharField(max_length=200)),
                ('lesson', models.CharField(max_length=200)),
                ('time', models.DateField(verbose_name='trial date')),
                ('drug', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Actiondex.Drug')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Actiondex.Subject')),
            ],
        ),
    ]
