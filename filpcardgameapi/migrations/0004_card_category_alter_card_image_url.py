# Generated by Django 4.2 on 2024-09-06 05:15

from django.db import migrations, models
import django.db.models.deletion
import filpcardgameapi.models


class Migration(migrations.Migration):

    dependencies = [
        ('filpcardgameapi', '0003_cardcategory_alter_card_image_url_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='cards', to='filpcardgameapi.cardcategory'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='card',
            name='image_url',
            field=models.ImageField(upload_to=filpcardgameapi.models.get_card_image_upload_path),
        ),
    ]
