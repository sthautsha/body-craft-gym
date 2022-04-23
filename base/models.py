from datetime import date, timezone
from pyexpat import model
from tabnanny import check
from time import time
from datetime import date
from unicodedata import category
from django.db import models
from django.contrib.auth.models import User

from django.utils.dateparse import parse_datetime

# from base.views import membership_plan

# Create your models here.


class MembershipPlan(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Package(models.Model):
    membership_plan_id = models.ForeignKey(MembershipPlan, on_delete=models.CASCADE)
    package_name = models.CharField(max_length=200)
    amount = models.FloatField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.package_name


class Billing(models.Model):
    package_id = models.ForeignKey(Package, on_delete=models.SET_NULL, null=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    discount = models.FloatField(max_length=80, null=True, blank=True)
    membership_start_date = models.DateField()
    billing_date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)

    def remainingDays(self):
        Day = self.membership_start_date - date.today()
        return Day.days

    def totalPrice(self):
        price = self.package_id.amount - (self.discount / 100) * self.package_id.amount
        return price


class Attendance(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    check_in = models.BooleanField(default=False)
    check_in_date = models.DateField(auto_now_add=True)


class DietPlan(models.Model):
    category = models.CharField(max_length=200)

    def __str__(self):
        return self.category

    @classmethod
    def create(cls, category):
        diet_plan = cls(category=category)
        return diet_plan


class ReccommendedDiet(models.Model):
    time = models.CharField(max_length=200)
    recommendation = models.TextField(null=True, blank=True)
    diet_plan_id = models.ForeignKey(DietPlan, on_delete=models.SET_NULL, null=True)


class WorkOutPlan(models.Model):
    category = models.CharField(max_length=200)

    def __str__(self):
        return self.category


class ExerciseCategory(models.Model):
    work_out_plan_id = models.ForeignKey(
        WorkOutPlan, on_delete=models.SET_NULL, null=True
    )
    category = models.CharField(max_length=200)

    def __str__(self):
        return self.category


class Exercise(models.Model):
    exercise_category_id = models.ForeignKey(
        ExerciseCategory, on_delete=models.SET_NULL, null=True
    )
    exercise_name = models.CharField(max_length=200)

    def __str__(self):
        return self.exercise_name


class Equipments(models.Model):
    equipment_name = models.CharField(max_length=200)
    equipment_Desc = models.TextField(null=True , blank=True)

    def __str__(self):
        return self.equipment_name


class ClientUser(models.Model):
    package_id = models.ForeignKey(Package, on_delete=models.SET_NULL, null=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=200)
    contact_number = models.CharField(max_length=50)
    medical_condition = models.TextField(null=True, blank=True)
    profile_image = models.ImageField(
        null=True,
        blank=True,
        upload_to="images/",
    )
    enroll_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user_id.username
