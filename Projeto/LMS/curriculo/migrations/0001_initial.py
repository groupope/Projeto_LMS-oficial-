# Generated by Django 2.0.2 on 2018-05-02 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alunos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=50, verbose_name='Login')),
                ('senha', models.CharField(max_length=50, verbose_name='Senha')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('email', models.CharField(max_length=100, verbose_name='Email')),
                ('celular', models.CharField(max_length=20, verbose_name='Celular')),
                ('dt_expiracao', models.DateField(max_length=10, verbose_name='Data Expiracao')),
                ('ra', models.CharField(max_length=7, verbose_name='RA')),
                ('foto', models.CharField(blank=True, max_length=100, null=True, verbose_name='Foto')),
            ],
        ),
        migrations.CreateModel(
            name='Coordenador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=50, verbose_name='Login')),
                ('senha', models.CharField(max_length=50, verbose_name='Senha')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('email', models.CharField(max_length=100, verbose_name='Email')),
                ('celular', models.CharField(max_length=20, verbose_name='Celular')),
                ('dt_expiracao', models.DateField(max_length=10, verbose_name='Data Expiracao')),
            ],
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=50, verbose_name='Login')),
                ('senha', models.CharField(max_length=50, verbose_name='Senha')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('email', models.CharField(max_length=100, verbose_name='Email')),
                ('celular', models.CharField(max_length=20, verbose_name='Celular')),
                ('dt_expiracao', models.DateField(max_length=10, verbose_name='Data Expiracao')),
                ('apelido', models.CharField(max_length=25, verbose_name='Apelido')),
            ],
        ),
    ]
