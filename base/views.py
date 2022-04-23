from ast import If
from multiprocessing import context
import uuid
from urllib import request
from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.core.mail import send_mail
from .models import (
    Attendance,
    Billing,
    DietPlan,
    Equipments,
    Exercise,
    ExerciseCategory,
    MembershipPlan,
    Package,
    ReccommendedDiet,
    WorkOutPlan,
    ClientUser,
)
from .form import (
    BillingForm,
    DietPlanForm,
    ExerciseCategoryForm,
    ExerciseForm,
    MembershipPlanForm,
    PackageForm,
    ReccommendedDietForm,
    WorkOutPlanForm,
    Package,
    NewUserForm,
    NewUserDetailForm,
    EquipmentsForm,
)


def contact_page(request):
    
    if request.method == "POST":
       
        subject = "BODY CRAFT GYM"
        message = request.POST["message"]
        body = "Email"+ request.user.email + "username" + request.user.username +" "+message
        print(message)
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ["jhigudoctor@gmail.com"]
        send_mail(subject, body, email_from, recipient_list)
        context = {"sucess_message": "We recieved your email will respond shortly !!"}
        return render(request, "base/contact_form.html", context)
    else:
        return render(request, "base/contact_form.html")


def profile(request):
    user_list = ClientUser.objects.get(user_id=request.user.id)
    context = {"user_list": user_list}
    return render(request, "base/user_profile.html", context)


def landingpage(request):
    return render(request, "main.html")






@login_required
def dashboard(request):
    print("ddd")
    user = ClientUser.objects.get(user_id=request.user)
    user_list = ClientUser.objects.all()
    print("shsh")
    # print(user.profile_image)
    package_list = Package.objects.all()
    equipment_list = Equipments.objects.all()
    workout_plan_list = WorkOutPlan.objects.all()

    print(workout_plan_list.count())
   
    bill_list = (
        Billing.objects.all()
        .select_related("package_id")
        .filter(user_id=request.user, status=True)
    )   
    print(package_list.count())
    if request.user.username == "admin": 
        context = {
        "user_count": user_list.count(),
        "bill_count": package_list.count(),
        "equipment_count": equipment_list.count(),
        "work_out_list": workout_plan_list.count(),
        "user": user,
    }
    else : 
        context = {
        "attendance": user_attendance_status(request),
        "bill_list": bill_list,
        "user": user,
        "user_count": user_list.count(),
        }

    
    return render(request, "base/dashboard.html", context)


def home(request):
    user = ClientUser.objects.get(user_id=request.user)
    context = {
        "membership_plan_list": display_membership_plans(),
        "workout_plan_list": display_workout_plan(),\
    "user": user,
    }
    return render(request, "base/home.html", context)


# diet plans


@login_required
def dietplan(request):
    user = ClientUser.objects.get(user_id=request.user)
    context = {
        "diet_plan_list": display_diet_plans(),
        "user": user,
        
    }
    return render(request, "base/diet_Plan.html", context)


def display_diet_plans():
    diet_plan_list = DietPlan.objects.all
    return diet_plan_list


@login_required
def create_diet_plan(request):
    user = ClientUser.objects.get(user_id=request.user)
    form = DietPlanForm()
    if request.method == "POST":
        form = DietPlanForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("dietPlan")
    context = {"form": form,
      "user": user,}
    return render(request, "base/diet_plan_form.html", context)


@login_required
def update_diet_plan(request, pk):
    user = ClientUser.objects.get(user_id=request.user)
    diet_plan = DietPlan.objects.get(id=pk)
    form = DietPlanForm(instance=diet_plan)
    if request.method == "POST":
        form = DietPlanForm(request.POST, instance=diet_plan)
        if form.is_valid():
            form.save()
            return redirect("dietPlan")
    context = {"form": form,"user": user,}
    return render(request, "base/diet_plan_form.html", context)


@login_required
def delete_diet_plan(request, pk):
   
    diet_plan = DietPlan.objects.get(id=pk)
    if request.method == "POST":
        diet_plan.delete()
        return redirect("dietPlan")
    return render(request, "base/delete.html", {"obj": diet_plan})


# reccomended diet


@login_required
def display_reccomended_diet(request, pk):
    user = ClientUser.objects.get(user_id=request.user)
    diet_plan = DietPlan.objects.get(id=pk)
    reccomended_diet_list = ReccommendedDiet.objects.filter(diet_plan_id=pk)
    context = {"diet_plan": diet_plan, "reccomended_diet_list": reccomended_diet_list,"user": user,}
    return render(request, "base/dietPlan_category.html", context)


@login_required
def create_reccomended_diet(request, pk):
    form = ReccommendedDietForm()
    if request.method == "POST":
        form = ReccommendedDietForm(request.POST)
        if form.is_valid():
            diet_plan = DietPlan.objects.get(id=pk)
            data = form.save(commit=False)
            data.diet_plan_id = diet_plan
            data.save()
            return redirect("display_reccomended_diet", pk)
    context = {"form": form}
    return render(request, "base/reccommended_diet_form.html", context)


@login_required
def update_reccomended_diet(request, diet_plan_id, pk):
    diet_plan = ReccommendedDiet.objects.get(id=pk)
    form = ReccommendedDietForm(instance=diet_plan)
    if request.method == "POST":
        form = ReccommendedDietForm(request.POST, instance=diet_plan)
        if form.is_valid():
            form.save()
            return redirect("display_reccomended_diet", diet_plan_id)
    context = {"form": form}
    return render(request, "base/reccommended_diet_form.html", context)


@login_required
def delete_reccomended_diet(request, diet_plan_id, pk):
    diet_plan = ReccommendedDiet.objects.get(id=pk)
    if request.method == "POST":
        diet_plan.delete()
        return redirect("display_reccomended_diet", diet_plan_id)
    return render(request, "base/delete.html", {"obj": diet_plan})


# Membership plan
@login_required
def create_membership_plan(request):
    form = MembershipPlanForm()
    if request.method == "POST":
        form = MembershipPlanForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("membership")
    context = {"form": form}
    return render(request, "base/membership_plan/membership_form.html", context)


def display_membership_plans():
    membership_plan_list = MembershipPlan.objects.all
    return membership_plan_list


@login_required
def memberShip(request):
    context = {"membership_plan_list": display_membership_plans()}
    return render(request, "base/membership_plan/memberShip.html", context)


@login_required
def update_membership_plan(request, pk):
    membership_plan = MembershipPlan.objects.get(id=pk)
    form = MembershipPlanForm(instance=membership_plan)
    if request.method == "POST":
        form = MembershipPlanForm(request.POST, instance=membership_plan)
        if form.is_valid():
            form.save()
            return redirect("membership")
    context = {"form": form}
    return render(request, "base/membership_plan/membership_form.html", context)


@login_required
def delete_membership_plan(request, pk):
    membership_plan = MembershipPlan.objects.get(id=pk)
    if request.method == "POST":
        membership_plan.delete()
        return redirect("membership")
    return render(request, "base/delete.html", {"obj": membership_plan})


# packages
@login_required
def create_package(request, pk):
    form = PackageForm()
    if request.method == "POST":
        form = PackageForm(request.POST)
        if form.is_valid():
            membership_plan = MembershipPlan.objects.get(id=pk)
            data = form.save(commit=False)
            data.membership_plan_id = membership_plan
            data.save()
            return redirect("display_packages", pk)
    context = {"form": form}
    return render(request, "base/package_form.html", context)


@login_required
def display_packages(request, pk):
    membership_plan = MembershipPlan.objects.get(id=pk)
    package_list = Package.objects.filter(membership_plan_id=pk)
    context = {"membership_plan": membership_plan, "package_list": package_list}
    return render(request, "base/membership_plan.html", context)


@login_required
def update_package(request, membership, pk):
    package = Package.objects.get(id=pk)
    form = PackageForm(instance=package)
    if request.method == "POST":
        form = PackageForm(request.POST, instance=package)
        if form.is_valid():
            form.save()
            return redirect("display_packages", membership)
    context = {"form": form}
    return render(request, "base/package_form.html", context)


@login_required
def delete_package(request, membership, pk):
    package = Package.objects.get(id=pk)
    if request.method == "POST":
        package.delete()
        return redirect("display_packages", membership)
    return render(request, "base/delete.html", {"obj": package})


# workout plan
@login_required
def workout_plan(request):
    context = {
        "workout_plan_list": display_workout_plan(),
    }
    return render(request, "base/workout.html", context)


def display_workout_plan():
    workout_plan_list = WorkOutPlan.objects.all
    return workout_plan_list


@login_required
def create_workout_plan(request):
    form = WorkOutPlanForm()
    if request.method == "POST":
        form = WorkOutPlanForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("workout")
    context = {"form": form}
    return render(request, "base/work_out_plan_form.html", context)


@login_required
def update_workout_plan(request, pk):
    workout_plan = WorkOutPlan.objects.get(id=pk)
    form = WorkOutPlanForm(instance=workout_plan)
    if request.method == "POST":
        form = WorkOutPlanForm(request.POST, instance=workout_plan)
        if form.is_valid():
            form.save()
            return redirect("workout")
    context = {"form": form}
    return render(request, "base/work_out_plan_form.html", context)


@login_required
def delete_workout_plan(request, pk):
    workout_plan = WorkOutPlan.objects.get(id=pk)
    if request.method == "POST":
        workout_plan.delete()
        return redirect("workout")
    return render(request, "base/delete.html", {"obj": workout_plan})


# exrcise category
@login_required
def display_exercise_category(request, pk):
    work_out_plan = WorkOutPlan.objects.get(id=pk)
    exercise_category_list = ExerciseCategory.objects.filter(work_out_plan_id=pk)
    context = {
        "work_out_plan": work_out_plan,
        "exercise_category_list": exercise_category_list,
    }
    return render(request, "base/work_out_plan.html", context)


@login_required
def create_exercise_category(request, pk):
    form = ExerciseCategoryForm()
    if request.method == "POST":
        form = ExerciseCategoryForm(request.POST)
        if form.is_valid():
            workout_plan = WorkOutPlan.objects.get(id=pk)
            data = form.save(commit=False)
            data.work_out_plan_id = workout_plan
            data.save()
            return redirect("display_exercise_category", pk)
    context = {"form": form}
    return render(request, "base/exercise_category_form.html", context)


@login_required
def update_exercise_category(request, work_out_plan_id, pk):
    exercise_category = ExerciseCategory.objects.get(id=pk)
    form = ExerciseCategoryForm(instance=exercise_category)
    if request.method == "POST":
        form = ExerciseCategoryForm(request.POST, instance=exercise_category)
        if form.is_valid():
            form.save()
            return redirect("display_exercise_category", work_out_plan_id)
    context = {"form": form}
    return render(request, "base/exercise_category_form.html", context)


@login_required
def delete_exercise_category(request, work_out_plan_id, pk):
    exercise_category = ExerciseCategory.objects.get(id=pk)
    if request.method == "POST":
        exercise_category.delete()
        return redirect("display_exercise_category", work_out_plan_id)
    return render(request, "base/delete.html", {"obj": exercise_category})


# exercise
@login_required
def display_exercise(request, pk):
    exercise_category = ExerciseCategory.objects.get(id=pk)
    exercise_list = Exercise.objects.filter(exercise_category_id=pk)
    context = {"exercise_category": exercise_category, "exercise_list": exercise_list}
    return render(request, "base/exercise_category.html", context)


@login_required
def create_exercise(request, pk):
    form = ExerciseForm()
    if request.method == "POST":
        form = ExerciseForm(request.POST)
        if form.is_valid():
            exercise_category = ExerciseCategory.objects.get(id=pk)
            data = form.save(commit=False)
            data.exercise_category_id = exercise_category
            data.save()
            return redirect("display_exercise", pk)
    context = {"form": form}
    return render(request, "base/exercise_form.html", context)


@login_required
def update_exercise(request, exercise_category_id, pk):
    diet_plan = Exercise.objects.get(id=pk)
    form = ExerciseForm(instance=diet_plan)
    if request.method == "POST":
        form = ExerciseForm(request.POST, instance=diet_plan)
        if form.is_valid():
            form.save()
            return redirect("display_exercise", exercise_category_id)
    context = {"form": form}
    return render(request, "base/exercise_form.html", context)


@login_required
def delete_exercise(request, exercise_category_id, pk):
    diet_plan = Exercise.objects.get(id=pk)
    if request.method == "POST":
        diet_plan.delete()
        return redirect("display_exercise", exercise_category_id)
    return render(request, "base/delete.html", {"obj": diet_plan})


# billing
@login_required
def display_bill(request):

    if request.user.username == "admin":
        bill_list = Billing.objects.all().select_related("package_id")

    else:
        bill_list = (
            Billing.objects.all()
            .select_related("package_id")
            .filter(user_id=request.user.id)
        )

    context = {
        "bill_list": bill_list,
    }

    return render(request, "base/billing.html", context)


@login_required
def create_bill(request):
    form = BillingForm()
    if request.method == "POST":
        form = BillingForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            return redirect("bill")
    context = {"form": form}
    return render(request, "base/bill_form.html", context)


@login_required
def update_bill(request, pk):
    bill = Billing.objects.get(id=pk)
    form = BillingForm(instance=bill)
    if request.method == "POST":
        form = BillingForm(request.POST, instance=bill)
        if form.is_valid():
            form.save()
            return redirect("bill")
    context = {"form": form}
    return render(request, "base/bill_form.html", context)


@login_required
def delete_bill(request, pk):
    bill = Billing.objects.get(id=pk)
    if request.method == "POST":
        bill.delete()
        return redirect("bill")
    return render(request, "base/delete.html", {"obj": bill})


# attendance
@login_required
def display_attendance(request):
        if request.user.username == "admin":
         attendance_list = Attendance.objects.all()

        else:
         attendance_list = Attendance.objects.all().filter(user_id=request.user.id)
        current_time = datetime.now().date()
        context = {"attendance_list": attendance_list, "current_time": current_time}
        return render(request, "base/attendance.html", context)


@login_required
def check_in(request):
    user = request.user
    check_in = True
    form = Attendance(user_id=user, check_in=check_in)
    form.save()
    return redirect("dashboard")


@login_required
def check_out(request):
    user = request.user
    check_in = False
    form = Attendance(user_id=user, check_in=check_in)
    form.save()
    return redirect("dashboard")


@login_required
def user_attendance_status(request):
    attendance = Attendance.objects.all().filter(
        user_id=request.user, check_in_date=datetime.now().date()
    )
    if attendance.count() == 0:
        return 1
    if attendance.count() == 1:
        return 2
    else:
        return 3


# equipments
@login_required
def display_equipment(request):
    equipment_list = Equipments.objects.all()
    context = {"equipment_list": equipment_list}
    return render(request, "base/equipment.html", context)


@login_required
def create_equipment(request):
    form = EquipmentsForm()
    if request.method == "POST":
        form = EquipmentsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("equipment")
    context = {"form": form}
    return render(request, "base/equipment_form.html", context)


@login_required
def update_equipment(request, pk):
    equipment = Equipments.objects.get(id=pk)
    form = EquipmentsForm(instance=equipment)
    if request.method == "POST":
        form = EquipmentsForm(request.POST, instance=equipment)
        if form.is_valid():
            form.save()
            return redirect("equipment")
    context = {"form": form}
    return render(request, "base/equipment_form.html", context)


@login_required
def delete_equipment(request, pk):
    equipment = Equipments.objects.get(id=pk)
    if request.method == "POST":
        equipment.delete()
        return redirect("equipment")


    return render(request, "base/delete.html", {"obj": equipment})


# login and registration authentications
def loginPage(request):

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            
            return redirect("dashboard")
        else:
            messages.error(request, 'Username or password is incorrect')    

    return render(request, "authentication/login.html")


def logout_view(request):
    logout(request)
    return redirect("landingpage")


@login_required
def register_request(request):
    form = NewUserForm()
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            password1 = form.cleaned_data["password1"]
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            # unique username with the help of uuid
            user.set_password(password1)
            pre_name = str(uuid.uuid4())
            pre_name = pre_name[:3]
            user.username = pre_name + first_name
            user.email = form.cleaned_data["email"]
            user.first_name = first_name
            user.last_name = last_name
            user.save()
            print(user.id)
            return redirect("add_user_detail")
    context = {"register_form": form}

    # if not user.is_verified:
    #     messages.success(request, "Check your email!")
    #     messages.add_message(request, messages.INFO, "Hello world.")

    return render(request, "base/register.html", context)


@login_required
def add_user_detail(request):
    form = NewUserDetailForm()
    if request.method == "POST":
        form = NewUserDetailForm(request.POST, request.FILES)
        if form.is_valid():
            # print(pk)
            form.save()
            return redirect("users")
    context = {"form": form}
    return render(request, "base/register_user_detail.html", context)


@login_required
def display_user_detail(request):
    user_list = ClientUser.objects.all()
    context = {"user_list": user_list}
    return render(request, "base/user_detail.html", context)
