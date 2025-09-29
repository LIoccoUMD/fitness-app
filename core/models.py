from django.db import models
# https://docs.djangoproject.com/en/5.2/ref/models/fields/#model-field-types
# GeneratedField

class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True, blank=True, null=True)
    fitness_level = models.CharField(max_length=25, blank=True)  # Beginner, Advanced -- I don't think i will use this
    # b = models.Field

    def __str__(self):
        return self.name

class Exercise(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50) # Strength / Cardio / etc.
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

# Need something for reps and sets -- not sure if i like frequency right now.
class Program(models.Model):
    name = models.CharField(max_length=100)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="programs")
    exercises = models.ManyToManyField(Exercise, related_name="programs")
    frequency = models.CharField(max_length=50, blank=True)  # 3x/week

    def __str__(self):
        return f"{self.name} ({self.client.name})"

class KPI(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="kpis")
    metric = models.CharField(max_length=100)  # Bench Press Max
    value = models.FloatField()  # e.g., 100 (kg)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.client.name}: {self.metric} = {self.value}"
    
    
    # Check to see if any of these should be ManyToMany or OneToMany
    # if you run in to any problems.
class Type(models.Model):
    TYPE_CHOICES = {
    (1, "Strength"),
    (2, "Strength/Power"),
    (3, "Power/Speed"),
    (4, "Speed/Endurance"),
    (5, "Endurance"),
    }
    
    label = models.IntegerField(choices=TYPE_CHOICES,null=False, blank=False)
    demands = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return dict(self.TYPE_CHOICES).get(self.label, str(self.label))