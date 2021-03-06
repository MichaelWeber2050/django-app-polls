# Generated by Django 3.0.3 on 2022-02-20 20:51

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20220220_2030'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='choice_text',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='polls.Question'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='choice',
            name='votes',
            field=models.IntegerField(default=0),
        ),
    ]
