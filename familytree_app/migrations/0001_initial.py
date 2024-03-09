# Generated by Django 4.2.4 on 2024-01-02 10:55

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
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('msg', models.CharField(max_length=500)),
                ('mobile', models.CharField(blank=True, max_length=15, null=True, unique=True)),
                ('surname', models.CharField(max_length=100, verbose_name='અટક')),
                ('name', models.CharField(max_length=100, verbose_name='નામ')),
                ('city', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='FamilyIdentification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='instructions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('srNo', models.CharField(max_length=5, unique=True)),
                ('msg', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='msgKind',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('msgK', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=255)),
                ('photo_url', models.ImageField(upload_to='photos/')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='familytree_app.city')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='sandesha',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo_url', models.ImageField(blank=True, null=True, upload_to='photos/')),
                ('name', models.CharField(max_length=255)),
                ('msg', models.TextField(blank=True, null=True)),
                ('signatureP', models.CharField(max_length=255)),
                ('msgType', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='familytree_app.msgkind')),
            ],
        ),
        migrations.CreateModel(
            name='FamilyMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.CharField(max_length=100, verbose_name='અટક')),
                ('full_name', models.CharField(max_length=100, verbose_name='નામ')),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('date_of_birth', models.DateField(blank=True, null=True, verbose_name='જન્મ તારીખ')),
                ('address', models.TextField(blank=True, null=True, verbose_name='સરનામુ')),
                ('mobile', models.CharField(blank=True, max_length=15, null=True, unique=True)),
                ('email', models.EmailField(blank=True, max_length=100, null=True)),
                ('old_location', models.CharField(blank=True, max_length=100, null=True, verbose_name='મૂળ વતન')),
                ('education', models.CharField(blank=True, max_length=100, null=True, verbose_name='અભ્યાસ')),
                ('work_type', models.CharField(blank=True, max_length=100, null=True)),
                ('remarks', models.TextField(blank=True, null=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='familytree_app.city')),
                ('family_identification', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='familytree_app.familyidentification', verbose_name='ગોત્ર')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='familytree_app.familymember')),
                ('spouse', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='husband_or_wife', to='familytree_app.familymember')),
            ],
        ),
    ]