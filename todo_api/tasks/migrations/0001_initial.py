# Generated by Django 3.2.16 on 2023-02-08 10:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('projects', '0001_initial'),
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('beginning', models.DateTimeField()),
                ('completion', models.DateTimeField()),
                ('importance', models.CharField(choices=[('not_important', 'Not important'), ('moderately_important', 'Moderately important'), ('important', 'Important')], max_length=20)),
                ('current_status', models.CharField(choices=[('queue', 'Queue'), ('development', 'Development'), ('done', 'Done')], default='queue', max_length=11)),
                ('ptid', models.PositiveIntegerField()),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='projects.project')),
            ],
            options={
                'ordering': ['ptid'],
                'unique_together': {('project', 'ptid')},
            },
        ),
        migrations.CreateModel(
            name='AttachedFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tfid', models.PositiveIntegerField()),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
                ('info', models.TextField(blank=True, max_length=70, null=True)),
                ('attached_file', models.FileField(upload_to='attached_files/')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('object_id', models.PositiveIntegerField()),
                ('content_type', models.ForeignKey(limit_choices_to=models.Q(models.Q(('app_label', 'tasks'), ('model', 'task')), models.Q(('app_label', 'tasks'), ('model', 'subtask')), _connector='OR'), on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
            ],
            options={
                'ordering': ['tfid'],
            },
        ),
        migrations.CreateModel(
            name='SubTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('beginning', models.DateTimeField()),
                ('completion', models.DateTimeField()),
                ('importance', models.CharField(choices=[('not_important', 'Not important'), ('moderately_important', 'Moderately important'), ('important', 'Important')], max_length=20)),
                ('current_status', models.CharField(choices=[('queue', 'Queue'), ('development', 'Development'), ('done', 'Done')], default='queue', max_length=11)),
                ('tsid', models.PositiveIntegerField()),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subtasks', to='tasks.task')),
            ],
            options={
                'ordering': ['tsid'],
                'unique_together': {('task', 'tsid')},
            },
        ),
        migrations.AddIndex(
            model_name='attachedfile',
            index=models.Index(fields=['content_type', 'object_id'], name='tasks_attac_content_c5433e_idx'),
        ),
        migrations.AlterUniqueTogether(
            name='attachedfile',
            unique_together={('content_type', 'object_id', 'tfid')},
        ),
    ]