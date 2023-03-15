from django.urls    import path
from pets.views     import OwnersView, CatsView

urlpatterns = [
    path('owners', OwnersView.as_view()),
    path('cats', CatsView.as_view()),
]