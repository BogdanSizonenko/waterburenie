from django import forms
from django.conf import settings
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox


# Контактная форма для связи по email
class ContactForm(forms.Form):
    # Поля формы для заполнения
    from_email = forms.EmailField(label="Email", required=True)
    subject = forms.CharField(label="Тема", required=True)
    message = forms.CharField(
        label="Сообщение",
        widget=forms.Textarea(attrs={"placeholder": "Напишите тут свое сообщение"}),
        required=True,
    )
    # Поле для капчи
    recaptcha = ReCaptchaField(widget=ReCaptchaV2Checkbox, public_key=settings.RECAPTCHA_PUBLIC_KEY,
                                private_key=settings.RECAPTCHA_PRIVATE_KEY, label='ReCAPTCHA')

    class Media:
        '''Медиа класс Django, определяющий файл стиля для данной формы'''
        css = {"all": ("css/style.css",)}
