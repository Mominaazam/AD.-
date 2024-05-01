# Generated by Django 3.2.7 on 2024-05-01 15:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ID', models.PositiveBigIntegerField()),
                ('Name', models.CharField(max_length=255)),
                ('Created_by', models.PositiveBigIntegerField()),
                ('Created_at', models.DateTimeField()),
                ('Updated_at', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Internal_User',
            fields=[
                ('id', models.PositiveBigIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('Emp_ID', models.PositiveBigIntegerField()),
                ('CNIC', models.CharField(max_length=255)),
                ('Data', models.TextField()),
                ('is_active', models.BooleanField()),
                ('Password', models.TextField()),
                ('Created_at', models.TextField()),
                ('updated', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='permission',
            fields=[
                ('id', models.PositiveBigIntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=75)),
                ('slug', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('active', models.TextField(max_length=1)),
                ('createdAt', models.DateTimeField()),
                ('updatedAt', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ID', models.PositiveBigIntegerField()),
                ('Property_key', models.CharField(max_length=255)),
                ('Sector', models.PositiveBigIntegerField()),
                ('Owner', models.PositiveBigIntegerField()),
                ('Property_Type', models.PositiveBigIntegerField()),
                ('Plot_No', models.CharField(max_length=255)),
                ('Society', models.PositiveBigIntegerField()),
                ('Street_No', models.CharField(max_length=255)),
                ('Phase', models.CharField(max_length=255)),
                ('Gali_No', models.CharField(max_length=255)),
                ('Society_Sector', models.CharField(max_length=255)),
                ('Flat_No', models.CharField(max_length=255)),
                ('Block_No', models.CharField(max_length=255)),
                ('Created_by', models.PositiveBigIntegerField()),
                ('Created_at', models.DateTimeField()),
                ('Updated_at', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Property_Bills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ID', models.PositiveBigIntegerField()),
                ('Consumer_ID', models.CharField(max_length=255)),
                ('Bill_Type', models.PositiveBigIntegerField()),
                ('Property_key', models.CharField(max_length=255)),
                ('Created_at', models.DateTimeField()),
                ('Updated_at', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Property_meta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ID', models.PositiveBigIntegerField()),
                ('Key', models.CharField(max_length=255)),
                ('Value', models.TextField()),
                ('Property_ID', models.PositiveBigIntegerField()),
                ('Edit_by', models.PositiveBigIntegerField()),
                ('Created_at', models.DateTimeField()),
                ('Updated_at', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Property_Owner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ID', models.PositiveBigIntegerField()),
                ('Owner_Name', models.CharField(max_length=255)),
                ('CNIC', models.CharField(max_length=255)),
                ('Edit_by', models.BigIntegerField()),
                ('Created_at', models.DateTimeField()),
                ('Uploaded_at', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Property_Owner_meta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ID', models.BigIntegerField()),
                ('Key', models.CharField(max_length=255)),
                ('Value', models.TextField()),
                ('Owner_ID', models.PositiveBigIntegerField()),
                ('Edit_by', models.PositiveBigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Property_Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ID', models.PositiveBigIntegerField()),
                ('Name', models.CharField(max_length=255)),
                ('Created_at', models.DateTimeField()),
                ('Updated_at', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='role',
            fields=[
                ('id', models.PositiveBigIntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=75)),
                ('slug', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('active', models.TextField(max_length=1)),
                ('createdAt', models.DateTimeField()),
                ('updatedAt', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='role_permission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roleId', models.PositiveBigIntegerField()),
                ('permissionId', models.PositiveBigIntegerField()),
                ('createdAT', models.DateTimeField()),
                ('updatedAt', models.DateTimeField()),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.role')),
            ],
        ),
        migrations.CreateModel(
            name='Sector',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ParentID', models.PositiveBigIntegerField()),
                ('Name', models.CharField(max_length=255)),
                ('Created_by', models.PositiveBigIntegerField()),
                ('Created_at', models.DateTimeField()),
                ('Updated_at', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Society',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ID', models.PositiveBigIntegerField()),
                ('Image', models.TextField()),
                ('Name', models.CharField(max_length=255)),
                ('Created_by', models.PositiveBigIntegerField()),
                ('Created_at', models.DateTimeField()),
                ('Updated_at', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='U_user',
            fields=[
                ('id', models.PositiveBigIntegerField(primary_key=True, serialize=False)),
                ('role_ID', models.PositiveBigIntegerField()),
                ('firstName', models.CharField(max_length=255)),
                ('LastName', models.CharField(max_length=255)),
                ('passwordHash', models.CharField(max_length=255)),
                ('CNIC', models.CharField(max_length=255)),
                ('Created_by', models.PositiveBigIntegerField()),
                ('registered', models.DateTimeField()),
                ('LastLogin', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='user_meta',
            fields=[
                ('id', models.PositiveBigIntegerField(primary_key=True, serialize=False)),
                ('key', models.CharField(max_length=75)),
                ('value', models.CharField(max_length=75)),
                ('used', models.PositiveBigIntegerField()),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.u_user')),
            ],
        ),
        migrations.CreateModel(
            name='Zone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ID', models.PositiveBigIntegerField()),
                ('Name', models.CharField(max_length=255)),
                ('Created_by', models.PositiveBigIntegerField()),
                ('Created_at', models.DateTimeField()),
                ('Updated_at', models.DateTimeField()),
            ],
        ),
        migrations.RemoveField(
            model_name='message',
            name='room',
        ),
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.ImageField(default='avatar.svg', null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='user',
            name='bio',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, null=True, unique=True),
        ),
        migrations.DeleteModel(
            name='Room',
        ),
        migrations.AddField(
            model_name='sector',
            name='Zone_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.zone'),
        ),
        migrations.AddField(
            model_name='role',
            name='parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.u_user'),
        ),
        migrations.AddField(
            model_name='permission',
            name='parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.role'),
        ),
        migrations.AddField(
            model_name='internal_user',
            name='parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.u_user'),
        ),
    ]