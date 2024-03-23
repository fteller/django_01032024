from django import forms
from django.conf import settings
from django.core.mail import EmailMessage

class ContactForm(forms.Form):
    name = forms.CharField(max_length=255, required=True)
    email = forms.EmailField(max_length=255, required=True)
    subject = forms.CharField(max_length=255, required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)

    def send_mail(self):
        if self.is_valid():
            name = str(self.cleaned_data['name'])
            email = str(self.cleaned_data['email'])
            subject = str(self.cleaned_data['subject'])
            message = str(self.cleaned_data['message'])

            message_context = 'message received.\n\n' \
                              'name:%s\n' \
                              'subject:%s\n' \
                              'email:%s\n' \
                              'message:%s\n' % (name, subject, email, message)

            #send email here
            email = EmailMessage(
                subject,
                message_context,
                to=[settings.DEFAULT_FROM_EMAIL],
                reply_to=[email]
            )
            email.send()