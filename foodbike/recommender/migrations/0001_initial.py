from __future__ import unicode_literals

from django.db import migrations, models

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Similarity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateField()),
                ('source', models.IntegerField()),
                ('target', models.IntegerField()),
                ('similarity', models.DecimalField(max_digits=8, decimal_places=7)),
            ],
            options={
                'db_table': 'similarity',
            },
        ),
    ]
