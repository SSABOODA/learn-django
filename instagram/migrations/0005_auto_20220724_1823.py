# Generated by Django 3.0.14 on 2022-07-24 09:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0004_auto_20220724_1729'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name='instagrampostcomment',
            name='post',
            field=models.ForeignKey(limit_choices_to={'is_public': True}, on_delete=django.db.models.deletion.CASCADE, to='instagram.InstagramPost'),
        ),
        migrations.AddField(
            model_name='instagrampost',
            name='tag_set',
            field=models.ManyToManyField(blank=True, to='instagram.Tag'),
        ),
    ]
