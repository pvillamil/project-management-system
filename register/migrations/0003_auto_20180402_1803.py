# Generated by Django 2.0.3 on 2018-04-02 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0002_invite'),
    ]

    operations = [
        migrations.CreateModel(
            name='Friends',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='company',
            name='friends',
            field=models.ManyToManyField(related_name='_company_friends_+', to='register.Company'),
        ),
    ]