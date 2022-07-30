# Generated by Django 4.0.6 on 2022-07-30 08:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('qna', '0005_qnaanswer_image_qnaquestion_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='qnaquestion',
            name='hashtag',
            field=models.TextField(default=django.utils.timezone.now, verbose_name='해시태그'),
            preserve_default=False,
        ),
    ]
