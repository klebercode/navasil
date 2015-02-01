# coding: utf-8
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User

from crm.current_user import get_current_user


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
    cpnj = models.CharField(_(u'CNPJ'), max_length=20, blank=True, null=True)
    site = models.URLField(_(u'Site'), blank=True, null=True)
    address = models.CharField(_(u'Endereço'), max_length=255,
                               blank=True, null=True)
    district = models.CharField(_(u'Bairro'), max_length=150,
                                blank=True, null=True)
    city = models.CharField(_(u'Cidade'), max_length=100,
                            blank=True, null=True)
    state = models.CharField(_(u'UF'), max_length=2, choices=STATE_CHOICES,
                             blank=True, null=True)
    zip_code = models.CharField(_(u'CEP'), max_length=10,
                                blank=True, null=True)
    observation = models.TextField(_(u'Observação'), blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, verbose_name=_(u'Usuário'),
                             editable=False, default=get_current_user)

    def __unicode__(self):
        return unicode(self.name)

    class Meta:
        verbose_name = _(u'Cliente')
        verbose_name_plural = _(u'Clientes')
        ordering = ['name']


class ContactPhone(models.Model):
    number = models.CharField(_(u'Número'), max_length=20)
    type = models.IntegerField(_(u'Tipo'), choices=PHONE_TYPE,
                               blank=True, null=True)
    operate = models.IntegerField(_(u'Operadora'), choices=PHONE_OPERATE,
                                  blank=True, null=True)
    name = models.CharField(_(u'Nome'), max_length=255, blank=True, null=True)
    customer = models.ForeignKey(Customer)

    def __unicode__(self):
        return unicode(self.number)

    class Meta:
        verbose_name = _(u'Fone')
        verbose_name_plural = _(u'Fones')
        ordering = ['name', 'number']


class ContactEmail(models.Model):
    email = models.EmailField(_(u'Email'))
    name = models.CharField(_(u'Nome'), max_length=255, blank=True, null=True)
    customer = models.ForeignKey(Customer)

    def __unicode__(self):
        return unicode(self.email)

    class Meta:
        verbose_name = _(u'Email')
        verbose_name_plural = _(u'Emails')
        ordering = ['name', 'email']
