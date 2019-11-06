# Generated by Django 2.2.7 on 2019-11-06 12:46

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
            name='Libro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isbn', models.CharField(help_text='ISBN', max_length=30, unique=True)),
                ('paginas', models.IntegerField()),
                ('editorial', models.CharField(default='Sintesis', max_length=50)),
                ('modo', models.CharField(choices=[('BN', 'Blanco y Negro'), ('C', 'Color'), ('H', 'Hibrido')], default='Blanco y Negro', max_length=30)),
                ('papel', models.CharField(choices=[('B', 'Blanco'), ('A', 'Ahuesado'), ('EM', 'Estucado Mate'), ('EB', 'Estucado Brillo')], max_length=30)),
                ('gramaje', models.IntegerField(choices=[('70', 70), ('80', 80), ('90', 90), ('100', 100), ('115', 115), ('125', 125)])),
                ('tamaño', models.CharField(choices=[('13x21', '130x210'), ('13,5x21,5', '135x215'), ('14x21', '140x210'), ('14x21,5', '140x215'), ('14x22', '140x220'), ('14x23', '140x230'), ('14x24', '140x240'), ('14x24,5', '140x245'), ('14,5x21', '145x210'), ('14,5x21,5', '145x215'), ('14,8x21,5', '148x215'), ('15x20,5', '150x205'), ('15x21', '150x210'), ('15x21,5', '150x215'), ('15x22,5', '150x225'), ('15x23', '150x230'), ('15,5x21', '155x210'), ('15,5x21,5', '155x215'), ('15,5x23', '155x230'), ('16x23', '160x230'), ('16,5x22,5', '165x225'), ('16,5x23', '165x230'), ('16,5x23,5', '165x235'), ('17x22,5', '170x225'), ('17x23', '170x230'), ('17x23,5', '170x235'), ('17x24', '170x240'), ('18x24,7', '180x247'), ('19x26', '190x260'), ('19,5x24', '195x240'), ('19,5x26', '195x260'), ('19,5x27', '195x270'), ('20x22', '200x220'), ('21x29,7', '210x297')], max_length=30)),
                ('estado', models.BooleanField(default=True)),
                ('fc', models.DateTimeField(auto_now_add=True)),
                ('fm', models.DateTimeField(auto_now=True)),
                ('um', models.IntegerField(blank=True, null=True)),
                ('uc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Libros',
            },
        ),
    ]
