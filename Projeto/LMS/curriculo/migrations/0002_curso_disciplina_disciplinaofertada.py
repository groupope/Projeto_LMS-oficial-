# Generated by Django 2.0.2 on 2018-05-02 14:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('curriculo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
            ],
        ),
        migrations.CreateModel(
            name='Disciplina',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('Nome', models.CharField(max_length=255, verbose_name='Nome')),
                ('Data', models.DateField(verbose_name='Data')),
                ('Status', models.CharField(max_length=255, verbose_name='Status')),
                ('PlanoDeEnsino', models.CharField(max_length=255, verbose_name='PlanoDeEnsino')),
                ('CargaHoraria', models.SmallIntegerField(verbose_name='CargaHoraria')),
                ('Competencias', models.CharField(max_length=255, verbose_name='Competencias')),
                ('Habilidades', models.CharField(max_length=255, verbose_name='Habilidades')),
                ('Ementa', models.CharField(max_length=255, verbose_name='Ementa')),
                ('ConteudoProgramatico', models.CharField(max_length=255, verbose_name='ConteudoProgramatico')),
                ('BibliografiaBasica', models.CharField(max_length=255, verbose_name='BibliografiaBasica')),
                ('BibliografiaComplementar', models.CharField(max_length=255, verbose_name='BibliografiaComplementar')),
                ('PercentualPratico', models.SmallIntegerField(verbose_name='PercentualPratico')),
                ('PercentualTeorico', models.SmallIntegerField(verbose_name='PercentualTeorico')),
                ('IdCoordenador', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='curriculo.Coordenador')),
            ],
        ),
        migrations.CreateModel(
            name='DisciplinaOfertada',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('DtInicioMatricula', models.DateField(null=True, verbose_name='DtInicioMatricula')),
                ('DtFimMatricula', models.DateField(null=True, verbose_name='DtFimMatricula')),
                ('Ano', models.SmallIntegerField(verbose_name='Ano')),
                ('Semestre', models.SmallIntegerField(verbose_name='Semestre')),
                ('Turma', models.CharField(max_length=255, verbose_name='Turma')),
                ('Metodologia', models.CharField(max_length=255, null=True, verbose_name='Metodologia')),
                ('Recursos', models.CharField(max_length=255, null=True, verbose_name='Recursos')),
                ('CriterioAvaliacao', models.CharField(max_length=255, null=True, verbose_name='CriterioAvaliacao')),
                ('PlanoDeAulas', models.CharField(max_length=255, null=True, verbose_name='PlanoDeAulas')),
                ('IdCoordenador', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='curriculo.Coordenador')),
                ('IdCurso', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='curriculo.Curso')),
                ('IdDisciplina', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='curriculo.Disciplina')),
                ('IdProfessor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='curriculo.Professor')),
            ],
        ),
    ]