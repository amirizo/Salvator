# Generated by Django 5.0.6 on 2024-06-04 23:12

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salva', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='question',
            options={'verbose_name_plural': 'Question'},
        ),
        migrations.AlterModelOptions(
            name='questioncategory',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.CreateModel(
            name='UserSubmittedAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('right_answer', models.CharField(max_length=200)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='salva.question')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'User Submitted Answers',
            },
        ),
    ]
