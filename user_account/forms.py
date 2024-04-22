from django import forms
from .models import ContactForm


class ContactForm(forms.ModelForm):
    subject_options = (
        ('general', 'general'),
        ('order', 'order'),        
    )
    subject = forms.ChoiceField(label='Subject', widget=forms.Select, choices=subject_options)

    class Meta:
        model = ContactForm
        fields = (
            'email',
            'order_number',
            'subject',
            'message',        
        )
    
    
    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)        
        placeholders = {
            'email': 'email',
            'order_number': 'order_number (optional)',
            'subject': 'subject',
            'message': 'message',     
        }
        for field in self.fields:
            placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'contact-field'