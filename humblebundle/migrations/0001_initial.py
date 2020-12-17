# Generated by Django 3.1.4 on 2020-12-17 06:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('application_name', models.TextField()),
                ('application_url', models.URLField()),
                ('release_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Bundle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bundle_name', models.TextField()),
                ('bundle_url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Developer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('developer', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publisher', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='HumbleItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('claimed', models.BooleanField(default=False)),
                ('claimed_by', models.TextField()),
                ('date_claimed', models.DateField()),
                ('application', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='humblebundle.application')),
                ('bundle_name', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='humblebundle.bundle')),
                ('developer', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='humblebundle.developer')),
                ('publisher', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='humblebundle.publisher')),
            ],
        ),
    ]
