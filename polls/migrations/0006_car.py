# Generated by Django 3.2.5 on 2021-07-14 07:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_auto_20210714_1449'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_brand', models.CharField(max_length=200)),
                ('choice_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.choice')),
                ('fruit_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.fruit')),
                ('question_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.question')),
            ],
        ),
    ]
