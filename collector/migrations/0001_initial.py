from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(verbose_name='date happened')),
                ('user_id', models.CharField(max_length=128)),
                ('content_id', models.IntegerField()),
                ('event', models.CharField(max_length=200)),
                ('session_inx', models.IntegerField()),
                ('visit_count', models.IntegerField()),
            ],
        ),
    ]

