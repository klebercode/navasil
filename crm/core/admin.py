# coding: utf-8
from django.contrib import admin
from django.contrib.admin.options import TabularInline

from import_export.admin import ImportExportModelAdmin
from import_export import resources

from crm.core.models import Customer, People, ContactPhone, ContactEmail


class ContactPhoneInline(TabularInline):
    model = ContactPhone
    fields = ('number', 'type', 'operate')
    extra = 1


class ContactEmailInline(TabularInline):
    model = ContactEmail
    fields = ('email',)
    extra = 1


class CustomerResource(resources.ModelResource):
    class Meta:
        model = Customer


class CustomerAdmin(ImportExportModelAdmin):
    list_display = ('name', 'get_phone', 'get_email')
    list_filter = ('state', 'city')
    search_fields = ('name', 'cpnj', 'site', 'address', 'number', 'district',
                     'city', 'state', 'zip_code', 'observation')
    fieldsets = (
        (None, {
            'fields': ('name', ('cnpj', 'site'), ('address', 'number'),
                       ('district', 'zip_code'), 'complement',
                       ('city', 'state'))
        }),
    )
    inlines = [ContactPhoneInline, ContactEmailInline]
    resource_class = CustomerResource

    def get_phone(self, obj):
        out = []
        for k in obj.contactphone_set.all():
            out.append(
                '<strong>%s:</strong> %s (%s)<br>' % (
                    k.get_type_display(),
                    k.number,
                    k.get_operate_display()
                )
            )
        return '\n'.join(out)
    get_phone.allow_tags = True
    get_phone.short_description = 'Fone'

    def get_email(self, obj):
        out = []
        for k in obj.contactemail_set.all():
            out.append(
                '%s<br>' % k.email
            )
        return '\n'.join(out)
    get_email.allow_tags = True
    get_email.short_description = 'Email'


class PeopleResource(resources.ModelResource):
    class Meta:
        model = People


class PeopleAdmin(ImportExportModelAdmin):
    list_display = ('name', 'cpf', 'rg', 'expeditor', 'brith_date',
                    'customer', 'get_phone', 'get_email')
    list_filter = ('customer', 'job', 'sex', 'state', 'city')
    search_fields = ('name', 'cpf', 'rg', 'expeditor', 'expeditor_date',
                     'brith_date', 'sex', 'address', 'number', 'district',
                     'complement', 'zip_code', 'city', 'state', 'job',
                     'capacity', 'registration', 'ord_date', 'observation',
                     'customer')
    fieldsets = (
        (None, {
            'fields': ('customer', 'name', ('brith_date', 'sex', 'cpf'),
                       ('rg', 'expeditor', 'expeditor_date'))
        }),
        ('Endereço', {
            'classes': ('grp-collapse grp-closed',),
            'fields': (('address', 'number'), ('district', 'zip_code'),
                       'complement', ('city', 'state'))
        }),
        ('Profissional', {
            'classes': ('grp-collapse grp-open',),
            'fields': (('job', 'registration', 'ord_date'), 'observation')
        }),

    )
    inlines = [ContactPhoneInline, ContactEmailInline]
    resource_class = PeopleResource

    def get_phone(self, obj):
        out = []
        for k in obj.contactphone_set.all():
            out.append(
                '<strong>%s:</strong> %s (%s)<br>' % (
                    k.get_type_display(),
                    k.number,
                    k.get_operate_display()
                )
            )
        return '\n'.join(out)
    get_phone.allow_tags = True
    get_phone.short_description = 'Fone'

    def get_email(self, obj):
        out = []
        for k in obj.contactemail_set.all():
            out.append(
                '%s<br>' % k.email
            )
        return '\n'.join(out)
    get_email.allow_tags = True
    get_email.short_description = 'Email'


class ContactPhoneAdmin(ImportExportModelAdmin):
    list_display = ('number', 'type', 'operate', 'customer', 'people')
    search_fields = ('number', 'type', 'operate', 'customer', 'people')


class ContactEmailAdmin(ImportExportModelAdmin):
    list_display = ('email', 'customer', 'people')
    search_fields = ('email', 'customer', 'people')


admin.site.register(Customer, CustomerAdmin)
admin.site.register(People, PeopleAdmin)
admin.site.register(ContactPhone, ContactPhoneAdmin)
admin.site.register(ContactEmail, ContactEmailAdmin)
