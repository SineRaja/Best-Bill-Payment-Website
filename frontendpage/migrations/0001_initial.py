# Generated by Django 4.1.3 on 2023-01-02 11:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Coupons',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('couponcode', models.CharField(max_length=15, null=True)),
                ('active', models.CharField(max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usercontactnumber', models.CharField(max_length=15, null=True)),
                ('useraddress', models.CharField(max_length=200, null=True)),
                ('usercity', models.CharField(max_length=100, null=True)),
                ('userstate', models.CharField(max_length=100, null=True)),
                ('userregdate', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Connection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customerconnectionid', models.CharField(max_length=10, null=True)),
                ('customerconnectiontype', models.CharField(max_length=100, null=True)),
                ('customerconnectionstartdate', models.DateField(null=True)),
                ('customeroccupation', models.CharField(max_length=100, null=True)),
                ('customerconnectionload', models.CharField(max_length=100, null=True)),
                ('customerplotno', models.CharField(max_length=50, null=True)),
                ('customercity', models.CharField(max_length=100, null=True)),
                ('customerpincode', models.CharField(max_length=10, null=True)),
                ('customeraddress', models.CharField(max_length=200, null=True)),
                ('customerstate', models.CharField(max_length=100, null=True)),
                ('customerdescription', models.CharField(max_length=250, null=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='frontendpage.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('billformonth', models.CharField(max_length=50, null=True)),
                ('dayelectricitycurrentreading', models.CharField(max_length=50, null=True)),
                ('dayelectricitypreviousreading', models.CharField(max_length=50, null=True)),
                ('dayelectricitytotalunit', models.CharField(max_length=100, null=True)),
                ('dayelectricitychargeperunit', models.CharField(max_length=100, null=True)),
                ('nightelectricitycurrentreading', models.CharField(max_length=50, null=True)),
                ('nightelectricitypreviousreading', models.CharField(max_length=50, null=True)),
                ('nightelectricitytotalunit', models.CharField(max_length=100, null=True)),
                ('nightelectricitychargeperunit', models.CharField(max_length=100, null=True)),
                ('gascurrentreading', models.CharField(max_length=50, null=True)),
                ('gaspreviousreading', models.CharField(max_length=50, null=True)),
                ('gastotalunit', models.CharField(max_length=100, null=True)),
                ('gaschargeperunit', models.CharField(max_length=100, null=True)),
                ('standingcharge', models.CharField(max_length=50, null=True)),
                ('finalamount', models.CharField(max_length=100, null=True)),
                ('duedate', models.DateField(null=True)),
                ('status', models.CharField(max_length=20, null=True)),
                ('connection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='frontendpage.connection')),
            ],
        ),
    ]
