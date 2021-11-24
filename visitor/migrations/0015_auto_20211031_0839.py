# Generated by Django 3.2.3 on 2021-10-31 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visitor', '0014_alter_userprofile_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userprofile',
            options={'verbose_name_plural': 'UserProfile'},
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='profile_picture',
            new_name='profile_picture_1',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='profile_picture_2',
            field=models.ImageField(default='default.jpg', upload_to='profile_pictures'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='delivery_address',
            field=models.TextField(default='234, Johnson Street, Ikeja, Nigeria'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='telephone_number',
            field=models.CharField(default='080', max_length=200),
        ),
    ]
