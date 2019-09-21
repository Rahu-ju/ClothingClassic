from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import CustomUserCreationForm

# Create your views here.
class SignUpPageView(CreateView):
    template_name = 'signup.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')

