# coding: utf-8
from django.db import models
from django.utils.translation import ugettext_lazy as _


SEX_CHOICES = (
    (1, _(u'Feminino')),
    (2, _(u'Masculino')),
)

PHONE_TYPE = (
    (1, _(u'Celular')),
    (2, _(u'Fixo')),
    (3, _(u'Nextel')),
)

PHONE_OPERATE = (
    (1, _(u'CLARO')),
    (2, _(u'NEXTEL')),
    (3, _(u'OI')),
    (4, _(u'TIM')),
    (5, _(u'VIVO')),
)

STATE_CHOICES = (
    ('AC', u'Acre'),
    ('AL', u'Alagoas'),
    ('AP', u'Amapá'),
    ('AM', u'Amazonas'),
    ('BA', u'Bahia'),
    ('CE', u'Ceará'),
    ('DF', u'Distrito Federal'),
    ('ES', u'Espírito Santo'),
    ('GO', u'Goiás'),
    ('MA', u'Maranhão'),
    ('MT', u'Mato Grosso'),
    ('MS', u'Mato Grosso do Sul'),
    ('MG', u'Minas Gerais'),
    ('PA', u'Pará'),
    ('PB', u'Paraíba'),
    ('PR', u'Paraná'),
    ('PE', u'Pernambuco'),
    ('PI', u'Piauí'),
    ('RJ', u'Rio de Janeiro'),
    ('RN', u'Rio Grande do Norte'),
    ('RS', u'Rio Grande do Sul'),
    ('RO', u'Rondônia'),
    ('RR', u'Roraima'),
    ('SC', u'Santa Catarina'),
    ('SP', u'São Paulo'),
    ('SE', u'Sergipe'),
    ('TO', u'Tocantins'),
)


class Customer(models.Model):
    name = models.CharField(_(u'Nome'), max_length=255)
    cnpj = models.CharField(_(u'CNPJ'), max_length=20, blank=True, null=True)
    site = models.URLField(_(u'Site'), blank=True, null=True)
    address = models.CharField(_(u'Endereço'), max_length=200,
                               null=True, blank=True)
    number = models.IntegerField(_(u'Número'), null=True, blank=True)
    district = models.CharField(_(u'Bairro'), max_length=150, null=True,
                                blank=True)
    complement = models.CharField(_(u'Complemento'), max_length=200,
                                  null=True, blank=True)
    zip_code = models.CharField(_(u'CEP'), max_length=10, null=True,
                                blank=True)
    city = models.CharField(_(u'Cidade'), max_length=150, null=True,
                            blank=True)
    state = models.CharField(_(u'UF'), max_length=2, choices=STATE_CHOICES,
                             null=True, blank=True)
    observation = models.TextField(_(u'Observação'), blank=True, null=True)

    def __unicode__(self):
        return unicode(self.name)

    class Meta:
        verbose_name = _(u'Cliente')
        verbose_name_plural = _(u'Clientes')
        ordering = ['name']


class Job(models.Model):
    name = models.CharField(_(u'Cargo'), max_length=30, null=True, blank=True)

    def __unicode__(self):
        return unicode(self.name)

    class Meta:
        verbose_name = _(u'Cargo')
        verbose_name_plural = _(u'Cargos')
        ordering = ['name']


class People(models.Model):
    name = models.CharField(_(u'Nome'), max_length=200)
    cpf = models.CharField(_(u'CPF'), max_length=14, null=True, blank=True)
    rg = models.CharField(_(u'RG'), max_length=20, null=True, blank=True)
    expeditor = models.CharField(_(u'Orgão Expedidor'), max_length=10,
                                 null=True, blank=True)
    expeditor_date = models.DateField(_(u'Data de Expedição'), null=True,
                                      blank=True)
    brith_date = models.DateField(_(u'Data de Nascimento'), null=True,
                                  blank=True)
    sex = models.IntegerField(_(u'Sexo'), choices=SEX_CHOICES,
                              blank=True, null=True)
    address = models.CharField(_(u'Endereço'), max_length=200,
                               null=True, blank=True)
    number = models.IntegerField(_(u'Número'), null=True, blank=True)
    district = models.CharField(_(u'Bairro'), max_length=150, null=True,
                                blank=True)
    complement = models.CharField(_(u'Complemento'), max_length=200,
                                  null=True, blank=True)
    zip_code = models.CharField(_(u'CEP'), max_length=10, null=True,
                                blank=True)
    city = models.CharField(_(u'Cidade'), max_length=150, null=True,
                            blank=True)
    state = models.CharField(_(u'UF'), max_length=2, choices=STATE_CHOICES,
                             null=True, blank=True)
    job = models.ForeignKey('Job', verbose_name=u'Cargo Correto', null=True,
                            blank=True)
    capacity = models.CharField(_(u'Lotação'), max_length=50, null=True,
                                blank=True)
    registration = models.IntegerField(_(u'Matrícula'), null=True, blank=True)
    ord_date = models.DateField(_(u'Data da Portaria'), null=True, blank=True)
    observation = models.TextField(_(u'Observação'), blank=True, null=True)
    customer = models.ForeignKey('Customer', verbose_name=u'Cliente')

    def __unicode__(self):
        return unicode(self.name)

    class Meta:
        verbose_name = _(u'Pessoa')
        verbose_name_plural = _(u'Pessoas')
        ordering = ['name']


class ContactPhone(models.Model):
    number = models.CharField(_(u'Número'), max_length=20)
    type = models.IntegerField(_(u'Tipo'), choices=PHONE_TYPE,
                               blank=True, null=True)
    operate = models.IntegerField(_(u'Operadora'), choices=PHONE_OPERATE,
                                  blank=True, null=True)
    customer = models.ForeignKey('Customer', verbose_name=u'Cliente',
                                 null=True, blank=True)
    people = models.ForeignKey('People', verbose_name=u'Pessoa', null=True,
                               blank=True)

    def __unicode__(self):
        return unicode(self.number)

    class Meta:
        verbose_name = _(u'Fone')
        verbose_name_plural = _(u'Fones')
        ordering = ['number']


class ContactEmail(models.Model):
    email = models.EmailField(_(u'Email'))
    customer = models.ForeignKey('Customer', verbose_name=u'Cliente',
                                 null=True, blank=True)
    people = models.ForeignKey('People', verbose_name=u'Pessoa', null=True,
                               blank=True)

    def __unicode__(self):
        return unicode(self.email)

    class Meta:
        verbose_name = _(u'Email')
        verbose_name_plural = _(u'Emails')
        ordering = ['email']
