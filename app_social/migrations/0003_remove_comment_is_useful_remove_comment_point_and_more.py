# Generated by Django 5.1.1 on 2024-10-04 13:52

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_market', '0007_blog_detail'),
        ('app_social', '0002_rename_description_comment_text_comment_product_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='is_useful',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='point',
        ),
        migrations.AddField(
            model_name='comment',
            name='helpful_count',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='comment',
            name='negative_points',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='not_helpful_count',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='comment',
            name='positive_points',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='app_market.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_text', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('question', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='answer', to='app_social.question')),
            ],
        ),
        migrations.DeleteModel(
            name='IsUseful',
        ),
        migrations.DeleteModel(
            name='Point',
        ),
    ]
