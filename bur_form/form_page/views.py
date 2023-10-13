from django.core.mail import EmailMessage
from django.shortcuts import render
from .forms import ContactForm
from django.http import HttpResponse, BadHeaderError
from django.core.mail import send_mail

# Функциональное представление домашней страницы с контактной формой
def home(request):
    f = open("form_page/templates/bur_page/text.txt", "r", encoding="utf-8")
    file_contents = f.read()
    f.close()

    if request.method == "GET":
        form = ContactForm()
    elif request.method == "POST":
        # если метод POST, проверим форму и отправим письмо
        form = ContactForm(request.POST)
        # Проверка правильности контактной формы
        if form.is_valid():
            subject = form.cleaned_data["subject"]
            from_email = form.cleaned_data["from_email"]
            message = form.cleaned_data["message"]
            message_form =  from_email + '\n' + subject + '\n' + message
            try:
                # Отправка сообщения
                send_mail(
                    'Заявка на скважину !!!', message_form, 'bogdansizon@yandex.ru',
                    ['bogdansizon@yandex.ru'], fail_silently=False)
            except BadHeaderError:
                return HttpResponse("Ошибка в теме письма.")
            return HttpResponse("Сообщение отправлено.")
        else:
            return HttpResponse("Неверный запрос.")
    data = {"text_file": file_contents, "form": form}
    return render(request, "bur_page/home.html", context=data)