# Generated by Django 2.2.4 on 2023-04-22 13:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0009_auto_20230422_1319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commit',
            name='commitOwner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='commitConmmits', to='forum.Commit', verbose_name='主评论'),
        ),
    ]
