# Generated by Django 4.0.4 on 2022-05-28 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Paragraph',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paragraphId', models.IntegerField()),
                ('paragraphBody', models.TextField(max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('questionId', models.IntegerField()),
                ('paragraph', models.IntegerField()),
                ('questionTitle', models.TextField(max_length=100)),
                ('answer', models.TextField(max_length=100)),
                ('distractor1', models.TextField(max_length=100)),
                ('distractor2', models.TextField(max_length=100)),
                ('distractor3', models.TextField(max_length=100)),
                ('distractor4', models.TextField(max_length=100)),
            ],
        ),
    ]