# Generated by Django 2.0.2 on 2018-05-02 14:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('curriculo', '0002_curso_disciplina_disciplinaofertada'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mensagem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assunto', models.CharField(max_length=255, verbose_name='Assunto')),
                ('referencia', models.CharField(max_length=255, verbose_name='Referencia')),
                ('conteudo', models.CharField(max_length=255, verbose_name='Conteudo')),
                ('status', models.CharField(max_length=50, verbose_name='Status')),
                ('dtEnvio', models.DateTimeField(max_length=10, verbose_name='Data Envio')),
                ('dtResposta', models.DateField(max_length=10, verbose_name='Data Resposta')),
                ('resposta', models.CharField(max_length=255, verbose_name='Resposta')),
                ('Alunos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='curriculo.Alunos')),
                ('professor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='curriculo.Professor')),
            ],
        ),
    ]
