# Generated by Django 3.2.13 on 2022-05-23 14:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customer_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=50)),
                ('middle_name', models.CharField(blank=True, max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('contact_no', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=100)),
                ('email_address', models.EmailField(blank=True, max_length=254, null=True)),
            ],
            options={
                'ordering': ['first_name', 'middle_name', 'last_name'],
                'permissions': (('can_view_customer', 'Can view customer'),),
            },
        ),
        migrations.CreateModel(
            name='Facility',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('price', models.PositiveSmallIntegerField()),
            ],
            options={
                'verbose_name_plural': 'Facilities',
            },
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('reservation_id', models.AutoField(primary_key=True, serialize=False)),
                ('no_of_children', models.PositiveSmallIntegerField(default=0)),
                ('no_of_adults', models.PositiveSmallIntegerField(default=1)),
                ('reservation_date_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('expected_arrival_date_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('expected_departure_date_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reservation.customer')),
            ],
            options={
                'permissions': (('can_view_reservation', 'Can view reservation'), ('can_view_reservation_detail', 'Can view reservation detail')),
            },
        ),
        migrations.CreateModel(
            name='RoomType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('price', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('profile_picture', models.ImageField(default='images/staff.png', upload_to='staff_img/')),
                ('staff_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=50)),
                ('middle_name', models.CharField(blank=True, max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('contact_no', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=100)),
                ('email_address', models.EmailField(max_length=254)),
                ('user', models.OneToOneField(editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['first_name', 'middle_name', 'last_name'],
                'permissions': (('can_view_staff', 'Can view staff'), ('can_view_staff_detail', 'Can view staff detail')),
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('room_no', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('availability', models.BooleanField(default=0)),
                ('facility', models.ManyToManyField(to='reservation.Facility')),
                ('reservation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='reservation.reservation')),
                ('room_type', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='reservation.roomtype')),
            ],
            options={
                'ordering': ['room_no'],
                'permissions': (('can_view_room', 'Can view room'),),
            },
        ),
        migrations.AddField(
            model_name='reservation',
            name='staff',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='reservation.staff'),
        ),
    ]
