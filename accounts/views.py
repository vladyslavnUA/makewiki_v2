from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView
from django.utils import timezone


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

class QuestionCreateView(CreateView):
    def get(self, request, *args, **kwargs):
        context = {'form': QuestionCreateForm()}
      return render(request, 'polls/new.html', context)

  def post(self, request, *args, **kwargs):
      form = QuestionCreateForm(request.POST)
      if form.is_valid():
          question = form.save()
          return HttpResponseRedirect(reverse_lazy('polls:detail', args=[question.id]))
      return render(request, 'polls/new.html', {'form': form})
