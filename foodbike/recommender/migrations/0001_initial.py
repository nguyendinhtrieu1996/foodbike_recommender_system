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
                ('source', models.CharField(db_index=True, max_length=16)),
                ('target', models.CharField(max_length=16)),
                ('similarity', models.FloatField()),
            ],
            options={
                'db_table': 'similarity',
            },
        ),
    ]
