from django.shortcuts import render
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy
from django.core.mail import send_mail


from sendm.models import Mail
from sendm.forms import MailForm

# # Create your views here.
# def asd(request):
#     return render(request, 'sendm/index.html', context={'text': 'qwsdfhdfghdfghdfg'})

class CreateMail(CreateView):
    model = Mail
    form_class = MailForm
    success_url = reverse_lazy('sendm:list_mail')
    template_name = 'sendm/index.html'

class ListMail(ListView):
    model = Mail
    context_object_name = 'mails'
    template_name = 'sendm/list_mail.html'

    # def get_queryset(self):
    #     print(Mail.objects.all())
    #     return Mail.objects.all()

# def asdf(request):
#     qw = send_mail('dfsdfsdfsd', 'fasdfasdfasd', '3434455@mail.ru', ['kalinkaufa@mail.ru'], fail_silently=False)
#     return render(request, 'sendm/index1.html', context={'text': qw})
    