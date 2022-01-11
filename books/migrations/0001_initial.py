# Generated by Django 4.0.1 on 2022-01-10 12:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bookstore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('vol', models.IntegerField()),
                ('copies', models.IntegerField()),
                ('store', models.CharField(max_length=100)),
                ('gid', models.CharField(max_length=100, null=True)),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='books', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
