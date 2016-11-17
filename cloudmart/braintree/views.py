import braintree
from django.conf import settings

#overriding these key oscar modules with braintree specific data
# see http://django-oscar.readthedocs.io/en/releases-1.2/howto/how_to_integrate_payment.html
from oscar.apps.checkout.views import PaymentDetailsView
from oscar.apps.payment.exceptions import PaymentError
from oscar.apps.payment.models import SourceType, Source

braintree.Configuration.configure(braintree.Environment.Sandbox,
		merchant_id=settings.BRAINTREE_MERCHANT_ID,
		public_key=settings.BRAINTREE_PUBLIC_KEY,
		private_key=settings.BRAINTREE_PRIVATE_KEY)

#implement PaymentDetailsView and override handle_payments
class SuccessResponseView(PaymentDetailsView):
	#do payment stuff...

def payment_view(request):
	if request.method == 'GET':
		request.session['braintree_client_token'] = braintree.ClientToken.generate()
		
		#do stuff...

		return render(request, ‘path/to/payment_template.html’)
	else: #assume this is a POST request
		if not form.is_valid():
			return render(render, ‘path/to/payment_template.html’)
		else:  # The transaction can be finalized.