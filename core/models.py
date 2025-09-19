from django.db import models
# https://docs.djangoproject.com/en/5.2/ref/models/fields/#model-field-types
# GeneratedField

class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True, blank=True, null=True)
    fitness_level = models.CharField(max_length=50, blank=True)  # e.g., Beginner, Advanced
    b = models.Field

    def __str__(self):
        return self.name

class Exercise(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50)  # e.g., Strength, Cardio
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Program(models.Model):
    name = models.CharField(max_length=100)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="programs")
    exercises = models.ManyToManyField(Exercise, related_name="programs")
    frequency = models.CharField(max_length=50, blank=True)  # e.g., 3x/week

    def __str__(self):
        return f"{self.name} ({self.client.name})"

class KPI(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="kpis")
    metric = models.CharField(max_length=100)  # e.g., Bench Press Max
    value = models.FloatField()  # e.g., 100 (kg)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.client.name}: {self.metric} = {self.value}"