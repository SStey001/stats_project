# Generated by Django 5.0.6 on 2024-05-09 09:53

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('passwords', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='GGPassword',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pw', models.TextField(max_length=4, validators=[django.core.validators.MinLengthValidator(4, 'the field must be 4 characters')])),
                ('user', models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='passwordguess',
            name='password',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='passwords.ggpassword'),
        ),
        migrations.DeleteModel(
            name='Password',
        ),
    ]