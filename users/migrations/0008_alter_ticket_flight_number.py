# Generated by Django 4.1.2 on 2023-02-15 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_remove_ticket_user_ticket_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='flight_number',
            field=models.CharField(max_length=100),
        ),
    ]