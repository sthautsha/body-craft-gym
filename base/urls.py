from django.urls import URLPattern, path
from . import views

urlpatterns = [
    path("", views.landingpage, name="landingpage"),
    path("dashboard", views.dashboard, name="dashboard"),
    # diet plan url
    path("dietPlan", views.dietplan, name="dietPlan"),
    path("dietPlan/create_diet_plan", views.create_diet_plan, name="create_diet_plan"),
    path(
        "dietPlan/update_diet_plan/<str:pk>/",
        views.update_diet_plan,
        name="update_diet_plan",
    ),
    path(
        "dietPlan/delete_diet_plan/<str:pk>/",
        views.delete_diet_plan,
        name="delete_diet_plan",
    ),
    # packages url
    path("display_packages/<str:pk>/", views.display_packages, name="display_packages"),
    path("create_package/", views.create_package, name="create_package"),
    path("update_package/<str:pk>/", views.update_package, name="update_package"),
    path("delete_package/<str:pk>/", views.delete_package, name="delete_package"),
    # membership plan
    path("membership/", views.memberShip, name="membership"),
    path(
        "create_membership_plan/",
        views.create_membership_plan,
        name="create_membership_plan",
    ),
    path(
        "update_membership_plan/<str:pk>/",
        views.update_membership_plan,
        name="update_membership_plan",
    ),
    path(
        "delete_membership_plan/<str:pk>/",
        views.delete_membership_plan,
        name="delete_membership_plan",
    ),
    # reccomemnded diet url
    path(
        "dietPlan/display_reccomended_diet/<str:pk>/",
        views.display_reccomended_diet,
        name="display_reccomended_diet",
    ),
    path(
        "dietPlan/create_reccomended_diet/",
        views.create_reccomended_diet,
        name="create_reccomended_diet",
    ),
    path(
        "dietPlan/update_reccomended_diet/<str:pk>/",
        views.update_reccomended_diet,
        name="update_reccomended_diet",
    ),
    path(
        "dietPlan/delete_reccomended_diet/<str:pk>/",
        views.delete_reccomended_diet,
        name="delete_reccomended_diet",
    ),
    # workout url
    path("workout", views.workout_plan, name="workout"),
    path(
        "workout/create_workout_plan/",
        views.create_workout_plan,
        name="create_workout_plan",
    ),
    path(
        "workout/update_workout_plan/<str:pk>/",
        views.update_workout_plan,
        name="update_workout_plan",
    ),
    path(
        "workout/delete_workout_plan/<str:pk>/",
        views.delete_workout_plan,
        name="delete_workout_plan",
    ),
    # display exercise category url
    path(
        "workout/display_exercise_category/<str:pk>/",
        views.display_exercise_category,
        name="display_exercise_category",
    ),
    path(
        "workout/create_exercise_category/",
        views.create_exercise_category,
        name="create_exercise_category",
    ),
    path(
        "workout/update_exercise_category/<str:pk>/",
        views.update_exercise_category,
        name="update_exercise_category",
    ),
    path(
        "workout/delete_exercise_category/<str:pk>/",
        views.delete_exercise_category,
        name="delete_exercise_category",
    ),
    # exercise url
    path("create_exercise/", views.create_exercise, name="create_exercise"),
    path("update_exercise/<str:pk>/", views.update_exercise, name="update_exercise"),
    path("delete_exercise/<str:pk>/", views.delete_exercise, name="delete_exercise"),
    path(
        "workout/display_exercise/<str:pk>/",
        views.display_exercise,
        name="display_exercise",
    ),
    # bill
    path("bill/", views.display_bill, name="bill"),
    path("bill/create_bill/", views.create_bill, name="create_bill"),
    path("bill/update_bill/<str:pk>/", views.update_bill, name="update_bill"),
    path("bill/delete_bill/<str:pk>/", views.delete_bill, name="delete_bill"),
    # login
    path("login/", views.loginPage, name="login"),
    path("logout/", views.logout_view, name="logout"),
    # attendance
    path("attendance/", views.display_attendance, name="attendance"),
    path("attendance/check_in", views.check_in, name="check_in"),
    path("attendance/check_out", views.check_out, name="check_out"),
    # user
    path("register", views.register_request, name="register"),
    path("add_user_detail/", views.add_user_detail, name="add_user_detail"),
    path("users", views.display_user_detail, name="users"),
    # equpiment
    path("equipment", views.display_equipment, name="equipment"),
    path(
        "equipment/create_equipment/", views.create_equipment, name="create_equipment"
    ),
    path(
        "equipment/update_equipment/<str:pk>/",
        views.update_equipment,
        name="update_equipment",
    ),
    path(
        "equipment/delete_equipment/<str:pk>/",
        views.delete_equipment,
        name="delete_equipment",
    ),
]
