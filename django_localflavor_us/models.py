from django.utils.translation import ugettext_lazy as _
from django.db.models.fields import CharField
from django.contrib.localflavor.us.us_states import STATE_CHOICES
from django.contrib.localflavor.us.us_states import USPS_CHOICES
from django.contrib.localflavor.us import forms

class USStateField(CharField):

    description = _("U.S. state (two uppercase letters)")

    def __init__(self, *args, **kwargs):
        kwargs['choices'] = STATE_CHOICES
        kwargs['max_length'] = 2
        super(USStateField, self).__init__(*args, **kwargs)

class USPostalCodeField(CharField):

    description = _("U.S. postal code (two uppercase letters)")

    def __init__(self, *args, **kwargs):
        kwargs['choices'] = USPS_CHOICES
        kwargs['max_length'] = 2
        super(USPostalCodeField, self).__init__(*args, **kwargs)

class PhoneNumberField(CharField):

    description = _("Phone number")

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 20
        super(PhoneNumberField, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        defaults = {'form_class': forms.USPhoneNumberField}
        defaults.update(kwargs)
        return super(PhoneNumberField, self).formfield(**defaults)

class USZipCodeField(CharField):

    description = _("Zipcode")

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 10
        super(USZipCodeField, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        defaults = {'form_class': forms.USZipCodeField}
        defaults.update(kwargs)
        return super(USZipCodeField, self).formfield(**defaults)
    

# gracefully fail south introspection if south is not available
try:    
    from south.modelsinspector import add_introspection_rules
    
    add_introspection_rules([], ["^django_localflavor_us\.models\.USStateField"])
    add_introspection_rules([], ["^django_localflavor_us\.models\.USPostalCodeField"])
    add_introspection_rules([], ["^django_localflavor_us\.models\.PhoneNumberField"])
    add_introspection_rules([], ["^django_localflavor_us\.models\.USZipCodeField"])
except ImportError:
    pass

