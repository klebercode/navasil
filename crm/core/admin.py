# coding: utf-8
from django.contrib import admin
from django.contrib.admin.options import TabularInline

from import_export.admin import ImportExportModelAdmin
from import_export import resources

from crm.core.models import Customer, ContactPhone, ContactEmail


class ContactPhoneInline(TabularInline):
    model = ContactPhone
    fields = ('number', 'type', 'operate', 'name')
    extra = 1


class ContactEmailInline(TabularInline):
    model = ContactEmail
    fields = ('email', 'name')
    extra = 1


class CustomerResource(resources.ModelResource):
    class Meta:
        model = Customer


class CustomerAdmin(ImportExportModelAdmin):
    list_display = ('name', )
    list_filter = ('state', 'city', 'user')
    search_fields = ('name', 'cpnj', 'site', 'address', 'district',
                     'city', 'state', 'zip_code', 'observation', 'user')
    inlines = [ContactPhoneInline, ContactEmailInline]
    resource_class = CustomerResource

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


class ContactPhoneAdmin(ImportExportModelAdmin):
    list_display = ('name', 'number', 'type', 'operate', 'customer')
    search_fields = ('name', 'number', 'type', 'operate', 'customer')


class ContactEmailAdmin(ImportExportModelAdmin):
    list_display = ('name', 'email')
    search_fields = ('name', 'email')


admin.site.register(Customer, CustomerAdmin)
admin.site.register(ContactPhone, ContactPhoneAdmin)
admin.site.register(ContactEmail, ContactEmailAdmin)
