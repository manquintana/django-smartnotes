from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect

''' Esto reemplazará la query Notes.objects.all y la query Notes.object.get(pk=pk)'''
from django.views.generic import CreateView, UpdateView, DetailView, ListView
from django.views.generic.edit import DeleteView

from .models import Notes
from notes.forms import NotesForm

# authentication
from django.contrib.auth.mixins import LoginRequiredMixin

#CRUD - CREATE Form
class NotesCreateView(LoginRequiredMixin, CreateView):
    model = Notes
    success_url = '/smart/notes'
    # fields = ['title', 'text'] # Esto es reemplazado por form_class que es mas versatil. Está en forms.py
    form_class = NotesForm
    def form_valid(self, form): # for user authentication 
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

#CRUD - UPDATE Form
class NotesUpdateView(UpdateView):
    model = Notes
    success_url = '/smart/notes'    
    form_class = NotesForm

#CRUD - DELETE Form
class NotesDeleteView(DeleteView):
    model = Notes
    success_url = '/smart/notes'
    form_class = NotesForm
    template_name = "notes/notes_delete.html"

# With user authentication 
class NotesListView(LoginRequiredMixin, ListView):
    model = Notes
    context_object_name = "notes"
    template_name = "notes/notes_list.html"
# def list(request):
#     all_notes = Notes.objects.all()
#     return render(request, 'notes/notes_list.html', {'notes' : all_notes})
    ''' User authentication: '''
    login_url = "/admin"
    def get_queryset(self):
        return self.request.user.notes.all()
    ''' End user authentication '''

class NotesDetailView(DetailView):
    model = Notes
    context_object_name = "note"
    template_name = "notes/notes_details.html"
''' El error 404 ya no es mas necesario, con DetailView se hace solo!'''
# def detail(request, pk):
#     try:
#         note = Notes.objects.get(pk=pk)
#     except Notes.DoesNotExist:
#         return render(request, 'notes/404.html')
#         #raise Http404('Note doesn\'t exist')
#     return render(request, 'notes/notes_details.html', {'note': note})
