from django.db import models

# Create your models here.

from django.contrib.auth.models import User



# Create your models here.
class Libro(models.Model):

    modos = (
    ('BN', 'Blanco y Negro'),
    ('C', 'Color'),
    ('H', 'Hibrido'),
    )

    papeles = (
        ('B', 'Blanco'),
        ('A', 'Ahuesado'),
        ('EM', 'Estucado Mate'),
        ('EB', 'Estucado Brillo'),
    )

    gramajes = (
        ('70',70),
        ('80',80),
        ('90',90),
        ('100',100),
        ('115',115),
        ('125',125),
    )

    tamaños = (
        ('13x21','130x210'),
        ('13,5x21,5','135x215'),
        ('14x21', '140x210'),
        ('14x21,5', '140x215'),
        ('14x22','140x220'),
        ('14x23','140x230'),
        ('14x24','140x240'),
        ('14x24,5','140x245'),
        ('14,5x21','145x210'),
        ('14,5x21,5','145x215'),
        ('14,8x21,5','148x215'),
        ('15x20,5','150x205'),
        ('15x21','150x210'),
        ('15x21,5','150x215'),
        ('15x22,5','150x225'),
        ('15x23','150x230'),
        ('15,5x21','155x210'),
        ('15,5x21,5','155x215'),
        ('15,5x23','155x230'),
        ('16x23','160x230'),
        ('16,5x22,5','165x225'),
        ('16,5x23','165x230'),
        ('16,5x23,5','165x235'),
        ('17x22,5','170x225'),
        ('17x23','170x230'),
        ('17x23,5','170x235'),
        ('17x24','170x240'),
        ('18x24,7','180x247'),
        ('19x26','190x260'),
        ('19,5x24','195x240'),
        ('19,5x26','195x260'),
        ('19,5x27','195x270'),
        ('20x22','200x220'),
        ('21x29,7','210x297'),
    )

    isbn = models.CharField(
        max_length = 30,
        help_text = 'ISBN',
        unique = True)
    paginas = models.IntegerField(blank = False)
    editorial = models.CharField(
        max_length = 50,
        default = 'Sintesis'
    )
    modo = models.CharField(
        choices = modos,
        default = 'Blanco y Negro',
        max_length = 30,
    )
    papel = models.CharField(
        choices = papeles,
        max_length = 30,
    )
    gramaje = models.IntegerField(
        choices = gramajes,
        
    )
    tamaño = models.CharField(
        choices = tamaños,
        max_length = 30,
    )
    estado = models.BooleanField(default=True)
    fc = models.DateTimeField(auto_now_add=True)
    fm = models.DateTimeField(auto_now=True)
    uc = models.ForeignKey(User, on_delete=models.CASCADE)
    um = models.IntegerField(blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Libros'