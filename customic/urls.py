from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('builder.urls')),
path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

# "refresh": eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTc2MjM0OTcyMCwiaWF0IjoxNzYyMjYzMzIwLCJqdGkiOiJjYjQzNTg5YjdiY2M0OTVlYmE2NGQ5MThjY2RlOGQzMyIsInVzZXJfaWQiOiIyIn0.vYDXNshXodo15_tA_CpgxaWKevHLJEuHkwrp9L2mrcY
# "access": eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzYyMjYzNjIwLCJpYXQiOjE3NjIyNjMzMjAsImp0aSI6Ijk3MmJkNDdmNzMzZDRhMTY4ZjQyNDFjMTRiM2IxYWQ1IiwidXNlcl9pZCI6IjIifQ.M9bkU5TiRxxaCAK1V_0BWtPtYmLVfQN6LGHeFpVq5yg