from django.urls import path

from analytics import views

urlpatterns = [
    path('cyclelength', views.avg_cycle_length, name='avg_cycle_length'),
    path('cyclelengthoverperiod', views.avg_cycle_over_period,
         name='avg_cycle_over_period'),
    path('predictnextcycle', views.predict_future_periods_view, name="predict_cycle"),
    path('symptompatterns', views.identify_symptom_patterns,
         name='identify_symptom_patterns')
]
