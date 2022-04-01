from fileinput import FileInput
from pyexpat import model
from django.forms import ModelForm
from .models import (
    Attendance,
    Billing,
    ClientUser,
    DietPlan,
    Equipments,
    Exercise,
    ExerciseCategory,
    MembershipPlan,
    Package,
    ReccommendedDiet,
    WorkOutPlan,
)
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
import re
from django.forms.widgets import DateInput


class MembershipPlanForm(ModelForm):
    class Meta:
        model = MembershipPlan
        fields = "__all__"


class PackageForm(ModelForm):
    class Meta:
        model = Package
        fields = "__all__"


class BillingForm(ModelForm):

    membership_start_date = forms.DateField(widget=DateInput(attrs={"type": "date"}))

    class Meta:
        model = Billing
        fields = "__all__"


class DietPlanForm(ModelForm):
    class Meta:
        model = DietPlan
        fields = "__all__"


class ReccommendedDietForm(ModelForm):
    class Meta:
        model = ReccommendedDiet
        fields = "__all__"


class WorkOutPlanForm(ModelForm):
    class Meta:
        model = WorkOutPlan
        fields = "__all__"


class ExerciseCategoryForm(ModelForm):
    class Meta:
        model = ExerciseCategory
        fields = "__all__"


class ExerciseForm(ModelForm):
    class Meta:
        model = Exercise
        fields = "__all__"


class EquipmentsForm(ModelForm):
    class Meta:
        model = Equipments
        fields = "__all__"


class NewUserForm(UserCreationForm):

    email = forms.EmailField(required=True,
     widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Enter your Email"}
        ),)

    first_name = forms.CharField(
        label="first name",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Enter your first name"}
        ),
        strip=False,
    )

    last_name = forms.CharField(
        label="Last name",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Enter your last name"}
        ),
        strip=False,
    )

    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "Enter your password"}
        ),
        strip=False,
    )

    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "Enter your password again"}
        ),
        strip=False,
    )

    model = User
    fields = [
        "username",
        "email",
        "first_name",
        "last_name",
        "password1",
        "password2",
    ]

    def clean_first_name(self):
        first_name = self.cleaned_data.get("first_name")

        if not re.match(r"[a-zA-Z]{3,30}", str(first_name)):
            raise forms.ValidationError("Invalid First Name")
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data.get("last_name")

        if not re.match(r"[a-zA-Z]{3,30}", str(last_name)):
            raise forms.ValidationError("Invalid Last Name")
        return last_name

    def clean_email(self):
        email = self.cleaned_data.get("email")

        if not re.match(r"^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$", email):
            raise forms.ValidationError("Invalid Email format")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if len(password1) < 8:
            raise forms.ValidationError("Password must be more than 8 character long")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Password mismatch")
        return password2


# class NewUserForm(UserCreationForm):
#     email = forms.EmailField(required=True)

#     class Meta:
#         model = User
#         fields = ("username", "email", "password1", "password2")

#     def save(self, commit=True):
#         user = super(NewUserForm, self).save(commit=False)
#         user.email = self.cleaned_data["email"]
#         if commit:
#             user.save()
#         return user


class NewUserDetailForm(ModelForm):
    # profile_image =forms.widgets(widget=FileInput(attrs={"class": "form-control"}))
    class Meta:
        model = ClientUser
        fields = "__all__"
