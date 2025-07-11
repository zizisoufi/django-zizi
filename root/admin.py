from django.contrib import admin
from .models import pricing, Item, FrequentlyQuestion, Team, Skills,Star



# تعریف admin سفارشی
class customepricing(admin.ModelAdmin):
    list_display = ["title", "amount", "status"]

# ثبت مدل‌ها
admin.site.register(Item)
admin.site.register(pricing, customepricing)
admin.site.register(FrequentlyQuestion)
admin.site.register(Skills)
admin.site.register(Team)
admin.site.register(Star)

