# Generated by Django 4.2.11 on 2024-06-04 20:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_user_first_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Upload_images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=20)),
                ('image', models.ImageField(upload_to='images')),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='cat',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='users.upload_images'),
        ),
    ]
