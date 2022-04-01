from django.contrib import admin

# Register your models here.

from .models import MembershipPlan,  Package, Billing, Attendance, DietPlan, ReccommendedDiet, WorkOutPlan, ExerciseCategory, Exercise, Equipments, ClientUser

admin.site.register(MembershipPlan)
admin.site.register(Package)
admin.site.register(Billing)
admin.site.register(Attendance)
admin.site.register(DietPlan)
admin.site.register(ReccommendedDiet)
admin.site.register(WorkOutPlan)
admin.site.register(ExerciseCategory)
admin.site.register(Exercise)
admin.site.register(Equipments)
admin.site.register(ClientUser)
