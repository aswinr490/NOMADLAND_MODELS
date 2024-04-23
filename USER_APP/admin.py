from django.contrib import admin

from .models import *

admin.site.register(UserModel)
admin.site.register(FeedbackModel)
admin.site.register(PaymentType)
admin.site.register(BookingModel)
admin.site.register(PaymentModel)


# Register your models here.
