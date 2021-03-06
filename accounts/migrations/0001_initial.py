# Generated by Django 3.1.4 on 2021-01-10 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=60, unique=True, verbose_name='email')),
                ('username', models.CharField(max_length=60, unique=True, verbose_name='username')),
                ('full_name', models.CharField(max_length=255, verbose_name='nama lengkap')),
                ('disp', models.ImageField(upload_to='photos/disp/%Y%m/%d/')),
                ('adress', models.TextField(blank=True, verbose_name='alamat')),
                ('contact', models.CharField(blank=True, max_length=20, verbose_name='nomor telepon')),
                ('is_admin', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
