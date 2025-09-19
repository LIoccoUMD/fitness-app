from django.contrib import admin
from .models import Client, Exercise, Program, KPI

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'fitness_level')

@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')

@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ('name', 'client', 'frequency')

@admin.register(KPI)
class KPIAdmin(admin.ModelAdmin):
    list_display = ('client', 'metric', 'value', 'date')