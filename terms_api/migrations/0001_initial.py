# Generated by Django 4.1.1 on 2022-09-24 09:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Term',
            fields=[
                ('label', models.CharField(max_length=180)),
                ('has_children', models.BooleanField(default=False)),
                ('is_obsolete', models.BooleanField(default=False)),
                ('is_defining_ontology', models.BooleanField(default=False)),
                ('obo_id', models.CharField(default='', max_length=200, primary_key=True, serialize=False)),
                ('description', models.CharField(default='', max_length=2000)),
                ('lang', models.CharField(default='en', max_length=2)),
                ('ontology_name', models.CharField(default='', max_length=200)),
                ('ontology_prefix', models.CharField(default='', max_length=200)),
                ('short_form', models.CharField(default='', max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Synonyms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=180)),
                ('scope', models.CharField(blank=True, default='', max_length=150, null=True)),
                ('type', models.CharField(blank=True, default='', max_length=150, null=True)),
                ('term', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='synonyms', to='terms_api.term')),
            ],
        ),
    ]