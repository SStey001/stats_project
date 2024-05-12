# Generated by Django 5.0.6 on 2024-05-10 17:12

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('passwords', '0007_rename_ggpassword_guesspasswordmodel'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='passwordguess',
            name='password',
        ),
        migrations.AddField(
            model_name='passwordguess',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='passwordguess',
            name='guess',
            field=models.TextField(default='0000', max_length=4, validators=[django.core.validators.MinLengthValidator(4, 'the field must be 4 characters')]),
        ),
    ]
