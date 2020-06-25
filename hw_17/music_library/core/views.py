from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import CreateView, DetailView
from django.views.generic.base import TemplateView
from core.models import Songs

from core.forms import AddSongForm, EditSongForm


class Index(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)
        songs = Songs.objects.all()
        context['songs'] = songs
        return context


class AddSong(TemplateView):
    model = Songs
    template_name = 'add_songs.html'
    form_class = AddSongForm

    def get_context_data(self, **kwargs):
        context = super(AddSong, self).get_context_data(**kwargs)
        context['song_form'] = AddSongForm()
        return context

    def post(self, request):
        song_form = AddSongForm(data=request.POST)
        if song_form.is_valid():
            song_form.save()
            return redirect('/')
        context = self.get_context_data()
        context['song_form'] = song_form
        return self.render_to_response(context)


class DeleteSong(DetailView):
    model = Songs

    def post(self, request, pk):
        del_song = Songs.objects.filter(pk=pk)
        del_song.delete()
        return redirect('/')


class EditSong(DetailView):
    template_name = 'edit_song.html'
    model = Songs

    def get_context_data(self, **kwargs):
        context = super(EditSong, self).get_context_data(**kwargs)
        context['edit_form'] = EditSongForm(instance=Songs.objects.filter(pk=self.kwargs['pk']).first())
        return context

    def post(self, request, pk):
        edit_form = EditSongForm(data=request.POST, instance=Songs.objects.filter(pk=pk).first())
        if edit_form.is_valid():
            edit_form.save()
            return redirect('/')
        else:
            edit_form = EditSongForm()
        context = self.get_context_data()
        context['edit_form'] = edit_form
        return self.render_to_response(context)
