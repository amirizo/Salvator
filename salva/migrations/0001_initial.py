# Generated by Django 5.0.6 on 2024-06-04 00:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=244)),
                ('opt_1', models.CharField(max_length=224)),
                ('opt_2', models.CharField(max_length=224)),
                ('opt_3', models.CharField(max_length=224)),
                ('opt_4', models.CharField(max_length=224)),
                ('question_type', models.CharField(choices=[('MC', 'Multiple Choice'), ('FB', 'Fill in the Blank')], max_length=2)),
                ('right_opt', models.CharField(max_length=224)),
            ],
        ),
        migrations.CreateModel(
            name='QuestionCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=224)),
                ('detail', models.CharField(max_length=224)),
            ],
        ),
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='salva.question')),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='salva.questioncategory'),
        ),
    ]
