# Generated by Django 3.2.7 on 2024-04-30 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_bills_property_property_bills_property_meta_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bills',
            name='Created_by',
            field=models.PositiveBigIntegerField(),
        ),
        migrations.AlterField(
            model_name='bills',
            name='ID',
            field=models.PositiveBigIntegerField(),
        ),
        migrations.AlterField(
            model_name='permission',
            name='id',
            field=models.PositiveBigIntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='property',
            name='Created_by',
            field=models.PositiveBigIntegerField(),
        ),
        migrations.AlterField(
            model_name='property',
            name='ID',
            field=models.PositiveBigIntegerField(),
        ),
        migrations.AlterField(
            model_name='property',
            name='Owner',
            field=models.PositiveBigIntegerField(),
        ),
        migrations.AlterField(
            model_name='property',
            name='Property_Type',
            field=models.PositiveBigIntegerField(),
        ),
        migrations.AlterField(
            model_name='property',
            name='Sector',
            field=models.PositiveBigIntegerField(),
        ),
        migrations.AlterField(
            model_name='property',
            name='Society',
            field=models.PositiveBigIntegerField(),
        ),
        migrations.AlterField(
            model_name='property_bills',
            name='Bill_Type',
            field=models.PositiveBigIntegerField(),
        ),
        migrations.AlterField(
            model_name='property_bills',
            name='ID',
            field=models.PositiveBigIntegerField(),
        ),
        migrations.AlterField(
            model_name='property_meta',
            name='Edit_by',
            field=models.PositiveBigIntegerField(),
        ),
        migrations.AlterField(
            model_name='property_meta',
            name='ID',
            field=models.PositiveBigIntegerField(),
        ),
        migrations.AlterField(
            model_name='property_meta',
            name='Property_ID',
            field=models.PositiveBigIntegerField(),
        ),
        migrations.AlterField(
            model_name='property_owner',
            name='Edit_by',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='property_owner',
            name='ID',
            field=models.PositiveBigIntegerField(),
        ),
        migrations.AlterField(
            model_name='property_owner_meta',
            name='Edit_by',
            field=models.PositiveBigIntegerField(),
        ),
        migrations.AlterField(
            model_name='property_owner_meta',
            name='ID',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='property_owner_meta',
            name='Owner_ID',
            field=models.PositiveBigIntegerField(),
        ),
        migrations.AlterField(
            model_name='property_type',
            name='ID',
            field=models.PositiveBigIntegerField(),
        ),
        migrations.AlterField(
            model_name='role',
            name='id',
            field=models.PositiveBigIntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='role_permission',
            name='permissionId',
            field=models.PositiveBigIntegerField(),
        ),
        migrations.AlterField(
            model_name='role_permission',
            name='roleId',
            field=models.PositiveBigIntegerField(),
        ),
        migrations.AlterField(
            model_name='sector',
            name='Created_by',
            field=models.PositiveBigIntegerField(),
        ),
        migrations.AlterField(
            model_name='sector',
            name='ID',
            field=models.PositiveBigIntegerField(),
        ),
        migrations.AlterField(
            model_name='sector',
            name='Zone_ID',
            field=models.PositiveBigIntegerField(),
        ),
        migrations.AlterField(
            model_name='society',
            name='Created_by',
            field=models.PositiveBigIntegerField(),
        ),
        migrations.AlterField(
            model_name='society',
            name='ID',
            field=models.PositiveBigIntegerField(),
        ),
        migrations.AlterField(
            model_name='u_user',
            name='Created_by',
            field=models.PositiveBigIntegerField(),
        ),
        migrations.AlterField(
            model_name='u_user',
            name='id',
            field=models.PositiveBigIntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='u_user',
            name='role_ID',
            field=models.PositiveBigIntegerField(),
        ),
        migrations.AlterField(
            model_name='user_meta',
            name='id',
            field=models.PositiveBigIntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='user_meta',
            name='used',
            field=models.PositiveBigIntegerField(),
        ),
        migrations.AlterField(
            model_name='zone',
            name='Created_by',
            field=models.PositiveBigIntegerField(),
        ),
        migrations.AlterField(
            model_name='zone',
            name='ID',
            field=models.PositiveBigIntegerField(),
        ),
    ]
