from django.conf.urls import *
from django.views.decorators.csrf import csrf_exempt

from paypal.express import views

urlpatterns = patterns(
	#Views for flow that starts on the basket page
	#note: the 3rd argument is an optional name
	 url(r'^cancel/(?P<basket_id>\d+)/$', views.CancelResponseView.as_view(),
        name='braintree-cancel-response'),
)