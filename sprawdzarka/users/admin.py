from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import Account


class AccountAdmin(UserAdmin):
	list_display = ('username','snumber','date_joined', 'last_login', 'is_admin','is_staff')
	search_fields = ('username','snumber')
	readonly_fields=('date_joined', 'last_login')

	filter_horizontal = ()
	list_filter = ()
	fieldsets = ()


admin.site.register(Account, AccountAdmin)