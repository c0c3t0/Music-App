from django.shortcuts import render, redirect

from music_project.my_music_app.forms import CreateProfileForm, CreateAlbumForm, EditAlbumForm, DeleteAlbumForm, \
    DeleteProfileForm
from music_project.my_music_app.models import Profile, Album


def get_profile():
    profile = Profile.objects.all()
    if profile:
        return profile[0]
    return None


def show_home(request):
    profile = get_profile()
    if not profile:
        return redirect('create profile')

    albums = Album.objects.all()
    album = Album.objects.all()

    context = {
        'albums': albums,
    }
    return render(request, 'home-with-profile.html', context)


def create_album(request):
    if request.method == "POST":
        form = CreateAlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CreateAlbumForm()

    context = {
        'form': form,
    }
    return render(request, 'add-album.html', context)


def album_details(request, pk):
    album = Album.objects.get(pk=pk)

    context = {
        'album': album,
    }
    return render(request, 'album-details.html', context)


def edit_album(request, pk):
    album = Album.objects.get(pk=pk)
    if request.method == "POST":
        form = EditAlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = EditAlbumForm(instance=album)

    context = {
        'album': album,
        'form': form,
    }
    return render(request, 'edit-album.html', context)


def delete_album(request, pk):
    album = Album.objects.get(pk=pk)
    if request.method == "POST":
        form = DeleteAlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DeleteAlbumForm(instance=album)

    context = {
        'album': album,
        'form': form,
    }
    return render(request, 'delete-album.html', context)


def create_profile(request):
    if request.method == "POST":
        form = CreateProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CreateProfileForm()

    context = {
        'form': form,
    }
    return render(request, 'home-no-profile.html', context)


def profile_details(request):
    profile = get_profile()
    albums = Album.objects.count()
    context = {
        'profile': profile,
        'albums': albums,
    }
    return render(request, 'profile-details.html', context)


def profile_delete(request):
    if request.method == "POST":
        form = DeleteProfileForm(request.POST, instance=get_profile())
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DeleteProfileForm(instance=get_profile())

    context = {
        'form': form,

    }
    return render(request, 'profile-delete.html', context)
