# Generated by Django 5.1.4 on 2025-03-28 01:44

import django.db.models.deletion
import django_currentuser.db.models.fields
import django_currentuser.middleware
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_remove_plan_growth_rate'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='brokerage',
            options={'verbose_name': 'Brokerage ', 'verbose_name_plural': 'Brokerages '},
        ),
        migrations.AlterField(
            model_name='plan',
            name='iras',
            field=models.ManyToManyField(related_name='plans', to='main.ira', verbose_name='IRAs'),
        ),
        migrations.AlterField(
            model_name='plan',
            name='roth_iras',
            field=models.ManyToManyField(related_name='plans', to='main.rothira', verbose_name='Roth IRAs'),
        ),
        migrations.CreateModel(
            name='GlossaryTerm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('edited_at', models.DateTimeField(auto_now=True, verbose_name='Edited At')),
                ('term', models.CharField(max_length=255, verbose_name='Glossary Term')),
                ('slug', models.SlugField(unique=True, verbose_name='Slug')),
                ('definition', models.TextField(blank=True, verbose_name='Definition')),
                ('body', models.TextField(blank=True, null=True, verbose_name='Body')),
                ('creator', django_currentuser.db.models.fields.CurrentUserField(default=django_currentuser.middleware.get_current_authenticated_user, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='created_%(class)s', to=settings.AUTH_USER_MODEL, verbose_name='Creator')),
                ('editor', django_currentuser.db.models.fields.CurrentUserField(default=django_currentuser.middleware.get_current_authenticated_user, null=True, on_delete=django.db.models.deletion.CASCADE, on_update=True, related_name='edited_%(class)s', to=settings.AUTH_USER_MODEL, verbose_name='Editor')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='children', to='main.glossaryterm')),
                ('related_terms', models.ManyToManyField(related_name='related_to', to='main.glossaryterm', verbose_name='Related Terms')),
            ],
            options={
                'verbose_name': 'Glossary Term',
                'verbose_name_plural': 'Glossary Terms',
            },
        ),
        migrations.CreateModel(
            name='Hsa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('edited_at', models.DateTimeField(auto_now=True, verbose_name='Edited At')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('growth_rate', models.FloatField(help_text='Annual growth rate as a percentage', verbose_name='Growth Rate')),
                ('initial_balance', models.FloatField(help_text='Initial balance in the investment account', verbose_name='Initial Balance')),
                ('contribution_strategy', models.CharField(choices=[('fixed', 'Fixed')], default='fixed', max_length=50, verbose_name='Contribution Strategy')),
                ('contribution_fixed_amount', models.FloatField(blank=True, help_text='Fixed amount contributed annually', null=True, verbose_name='Contribution Fixed Amount')),
                ('creator', django_currentuser.db.models.fields.CurrentUserField(default=django_currentuser.middleware.get_current_authenticated_user, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='created_%(class)s', to=settings.AUTH_USER_MODEL, verbose_name='Creator')),
                ('editor', django_currentuser.db.models.fields.CurrentUserField(default=django_currentuser.middleware.get_current_authenticated_user, null=True, on_delete=django.db.models.deletion.CASCADE, on_update=True, related_name='edited_%(class)s', to=settings.AUTH_USER_MODEL, verbose_name='Editor')),
            ],
            options={
                'verbose_name': 'HSA ',
                'verbose_name_plural': 'HSAs ',
            },
        ),
        migrations.AddField(
            model_name='plan',
            name='hsas',
            field=models.ManyToManyField(related_name='plans', to='main.hsa', verbose_name='Hsas'),
        ),
    ]
