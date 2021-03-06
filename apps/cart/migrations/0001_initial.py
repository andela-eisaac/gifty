# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gift', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cart_number', models.PositiveIntegerField()),
                ('is_paid_for', models.BooleanField(default=False)),
                ('gift_pack', models.ManyToManyField(related_name='carts', to='gift.GiftPack')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
