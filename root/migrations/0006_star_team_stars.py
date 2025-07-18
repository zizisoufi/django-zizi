# Generated by Django 4.2 on 2025-07-05 19:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('root', '0005_skills_team'),
    ]

    operations = [
        migrations.CreateModel(
            name='Star',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.PositiveIntegerField(default=3)),
            ],
        ),
        migrations.AddField(
            model_name='team',
            name='stars',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.DO_NOTHING, to='root.star'),
            preserve_default=False,
        ),
    ]
