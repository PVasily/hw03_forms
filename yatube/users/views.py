from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.core.mail import send_mail

from .forms import CreationForm, ExchangeForm


class SugnUp(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy('posts:index')
    template_name = 'users/signup.html'


def send_msg(email, name, title, artist, genre, price, comment):
    subject = f"Обмен {artist}-{title}"
    body = f"""Предложение на обмен диска от {name} ({email})

    Название: {title}
    Исполнитель: {artist}
    Жанр: {genre}
    Стоимость: {price}
    Комментарий: {comment}

    """
    send_mail(
        subject, body, email, ["admin@rockenrolla.net", ],
    )


def mail_page(request):
    if request.method == 'POST':
        form = ExchangeForm(request.POST)
        if form.is_valid():
            send_msg(**form.cleaned_data)
            return redirect('users:thankyou')
        return render(request, 'users/send_mail.html', {'form': form})
    else:
        form = ExchangeForm()
        return render(request, 'users/send_mail.html', {'form': form})


def thankyou(request):
    return render(request, 'users/thankyou.html')
