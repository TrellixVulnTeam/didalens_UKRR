# Generated by Django 3.0.7 on 2020-06-16 12:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GoalList',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('goal', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='GoalModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('time', models.TimeField(auto_now=True)),
                ('date', models.DateField(auto_now=True)),
                ('is_true', models.BooleanField(default=False, verbose_name='Done')),
                ('is_not_true', models.BooleanField(default=False, verbose_name="Didn't Do")),
                ('datetogoal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='didaup.GoalList', verbose_name='Goal')),
            ],
        ),
    ]
