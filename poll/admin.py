from django.contrib import admin
from .models import Poll

# Register your models here.
@admin.register(Poll)
class PollModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'question', 'option_one', 'option_two', 'option_three', 'option_four', 'option_one_count', 'option_two_count', 'option_three_count', 'option_four_count']
