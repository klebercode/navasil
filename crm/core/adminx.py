# coding: utf-8
import xadmin

from crm.core.models import Customer, ContactPhone, ContactEmail


class ContactPhoneInline(object):
    model = ContactPhone
    fields = ('number', 'type', 'operate', 'name', 'position')
    extra = 1
    style = 'accordion'


class ContactEmailInline(object):
    model = ContactEmail
    fields = ('email', 'name', 'position')
    extra = 1
    style = 'accordion'


class CustomerAdmin(object):
    list_display = ('name', )
    search_fields = ('name', )
    inlines = [ContactPhoneInline, ContactEmail]

    # def get_phone(self, obj):
    #     out = []
    #     for k in obj.get_phone_set.all():
    #         out.append(
    #             '%s<br>' % k.number
    #         )
    #     return '\n'.join(out)

    # def contact_phone(self, obj):
    #     return ", ".join([k.numero for k in obj.fone_set.all()])

    # def contact_email(self, obj):
    #     return ", ".join([k.numero for k in obj.fone_set.all()])


xadmin.site.register(Customer, CustomerAdmin)
