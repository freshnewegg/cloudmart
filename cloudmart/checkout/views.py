import braintree
from django.conf import settings

#overriding these key oscar modules with braintree specific data
# see http://django-oscar.readthedocs.io/en/releases-1.2/howto/how_to_integrate_payment.html
from oscar.apps.checkout import views
from oscar.apps.payment import models
from oscar.apps.payment.exceptions import PaymentError
from oscar.apps.payment.models import SourceType, Source

braintree.Configuration.configure(braintree.Environment.Sandbox,
		merchant_id=settings.BRAINTREE_MERCHANT_ID,
		public_key=settings.BRAINTREE_PUBLIC_KEY,
		private_key=settings.BRAINTREE_PRIVATE_KEY)

#implement PaymentDetailsView and override handle_payments
class PaymentDetailsView(views.PaymentDetailsView):
    def get_context_data(self, **kwargs):
        """
        Add data for Braintree flow.
        """
        # Override method so the bankcard and billing address forms can be
        # added to the context.
        ctx = super(PaymentDetailsView, self).get_context_data(**kwargs)
        ctx['bankcard_form'] = kwargs.get(
            'bankcard_form', forms.BankcardForm())
        ctx['billing_address_form'] = kwargs.get(
            'billing_address_form', forms.BillingAddressForm())
        return ctx

    """Complete payment with Braintree - this calls the '____'
    method to capture the money from the initial transaction."""
    def handle_payment(self, order_number, total, **kwargs):
        try:
            #confirm the payment action?
            confirm_txn = confirm_transaction(
            kwargs['payer_id'], kwargs['token'], kwargs['txn'].amount,
            kwargs['txn'].currency)
        except BraintreeError:
            raise UnableToTakePayment()

        if not confirm_txn.is_successful:
            raise UnableToTakePayment()

        # Record payment source and event
        source_type, is_created = SourceType.objects.get_or_create(
            name='PayPal')
        source = Source(source_type=source_type,
                        currency=confirm_txn.currency,
                        amount_allocated=confirm_txn.amount,
                        amount_debited=confirm_txn.amount)
        self.add_payment_source(source)
        self.add_payment_event('Settled', confirm_txn.amount,
                               reference=confirm_txn.correlation_id)
