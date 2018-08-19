# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0024_auto_20180818_1758'),
    ]

    operations = [
        migrations.AlterField(
            model_name='club',
            name='superviseur',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
        ),
    ]
