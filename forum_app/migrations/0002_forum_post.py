# Generated by Django 2.2 on 2021-03-07 18:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forum_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Forum_Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=255)),
                ('username', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('forum', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='all_forum_posts', to='forum_app.Forum')),
            ],
        ),
    ]
