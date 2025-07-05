from django.shortcuts import render, get_object_or_404, reverse
from django.urls import reverse_lazy
from django.views import generic, View
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView
from django.db.models import Q
from posting.models import Posting

# Halaman utama
def index(request):
    postings = Posting.objects.all()
    return render(request, 'posting/index.html', {'postings': postings})

# Fitur pencarian
class SearchPosting(View):
    def get(self, request):
        query = request.GET.get('q', '')
        results = []

        if query:
            results = Posting.objects.filter(
                Q(judul__icontains=query) |
                Q(konten__icontains=query)
            )

        return render(request, 'posting/search.html', {
            'query': query,
            'hasil': results
        })

# Registrasi pengguna
class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/SignUp.html'

# Detail postingan
class DetailPosting(generic.DetailView):
    model = Posting
    template_name = 'posting/detail.html'
    context_object_name = 'posting'

# Tambah posting
class AddPost(LoginRequiredMixin, generic.CreateView):
    model = Posting
    fields = ['judul', 'image', 'konten']
    template_name = 'posting/addpost.html'

    def get_success_url(self):
        return reverse('detail', kwargs={'pk': self.object.pk})

# Edit posting
class UpdatePost(LoginRequiredMixin, UpdateView):
    model = Posting
    fields = ['judul', 'image', 'konten']
    template_name = 'posting/addpost.html'

    def get_success_url(self):
        return reverse('detail', kwargs={'pk': self.object.pk})