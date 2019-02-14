from django.shortcuts import render, redirect, get_list_or_404
from .forms import PostForm
from .models import Barang

# Create your views here.
def halamanHome(request):
    artikel_barang = Barang.objects.all()
    return render(request,'home.html', {'artikel_barang':artikel_barang})


def lengkap_barang(request, post_id):
    post_num = get_list_or_404(Artikel, id=post_id)
    return render(request, 'home_lengkap.html', {'artikel_barang':post_num})


# def input_barang(request):
#     if request.method == "POST":
#         form = PostForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('input_barang')
#     else:
#         form = PostForm()

    # return render(request, 'home_tambah.html', {'form':form})