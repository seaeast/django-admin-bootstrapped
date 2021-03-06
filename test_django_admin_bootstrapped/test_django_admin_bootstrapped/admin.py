from django.contrib import admin
from models import TestMe, TestThat, TestMeProxyForFieldsets


class TestThatStackedInline(admin.StackedInline):
    model = TestThat


class TestThatTabularInline(admin.TabularInline):
    model = TestThat


class TestMeAdmin(admin.ModelAdmin):
    list_display = ['test_ip', 'test_url', 'test_int', 'test_img', 'test_file', 'test_date', 'test_char', 'test_bool', 'test_time', 'test_slug', 'test_text', 'test_email', 'test_float', 'test_bigint', 'test_positive_integer', 'test_decimal', 'test_comma_separated_int', 'test_small_int', 'test_nullbool', 'test_filepath', 'test_positive_small_int', ]
    list_search = ['test_url', ]
    list_editable = ['test_url', ]
    list_filter = ['test_ip', 'test_url', 'test_int', ]
    list_per_page = 3
    inlines = [TestThatStackedInline, TestThatTabularInline]
    save_as = True
    save_on_top = True


class TestMeAdminFieldsets(TestMeAdmin):
    fieldsets = (
        ('A fieldset', {
            'fields': ['test_m2m', 'test_ip', 'test_url', 'test_int', 'test_img', 'test_file', 'test_date', 'test_char', 'test_bool', 'test_time', 'test_slug', 'test_text', ],
        }),
        ('Another fieldset', {
            'fields': ['test_email', 'test_float', 'test_bigint', 'test_positive_integer', 'test_decimal', 'test_comma_separated_int', 'test_small_int', 'test_nullbool', 'test_filepath', 'test_positive_small_int', ],
        }),
    )

admin.site.register(TestMeProxyForFieldsets, TestMeAdminFieldsets)
admin.site.register(TestMe, TestMeAdmin)
