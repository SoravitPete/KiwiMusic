# Generated by Django 3.2.7 on 2021-11-05 20:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BillBoard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('billboard', models.CharField(max_length=200)),
                ('place', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='BlogName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='SongType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('song_type', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='SongName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('song_name', models.CharField(max_length=200)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Home.songtype')),
            ],
        ),
        migrations.CreateModel(
            name='BlogRoom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=200)),
                ('room_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Home.blogname')),
            ],
        ),
    ]
