# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='created',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='updated',
            new_name='updated_at',
        ),
    ]
