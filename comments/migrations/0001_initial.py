# Generated by Django 3.2.16 on 2023-01-01 14:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tcid', models.PositiveIntegerField()),
                ('text', models.TextField(max_length=255)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('object_id', models.PositiveIntegerField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('content_type', models.ForeignKey(limit_choices_to=models.Q(models.Q(('app_label', 'tasks'), ('model', 'task')), models.Q(('app_label', 'tasks'), ('model', 'subtask')), _connector='OR'), on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='comments.comment')),
            ],
            options={
                'ordering': ('created',),
            },
        ),
    ]
