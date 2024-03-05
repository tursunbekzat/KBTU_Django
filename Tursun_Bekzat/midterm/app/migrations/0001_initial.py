# Generated by Django 3.2.12 on 2024-03-05 09:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Discipline',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('credits', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('relevant', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Speciality',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=10)),
                ('faculty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.faculty')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('id', models.CharField(max_length=9, primary_key=True, serialize=False)),
                ('gpa', models.DecimalField(decimal_places=2, max_digits=3)),
                ('login', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('disciplines', models.ManyToManyField(blank=True, to='app.Discipline')),
                ('speciality', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.speciality')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=30)),
                ('login', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('disciplines', models.ManyToManyField(to='app.Discipline')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='discipline',
            name='speciality',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.speciality'),
        ),
    ]
