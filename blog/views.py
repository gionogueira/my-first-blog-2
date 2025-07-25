from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.core.paginator import Paginator
from .models import Post
from django.utils import timezone
from .forms import PostForm

def post_list(request):
    """
    View para listar todos os posts publicados.
    Posts são ordenados por data de publicação (mais recente primeiro).
    """
    posts = Post.objects.filter(
        published_date__lte=timezone.now()
    ).select_related('author').order_by('-published_date')
    
    # Paginação (descomente para ativar)
    paginator = Paginator(posts, 5)  # 5 posts por página
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)
    
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    """
    View para exibir um post específico.
    Inclui otimização com select_related para evitar queries adicionais.
    """
    post = get_object_or_404(
        Post.objects.select_related('author'), 
        pk=pk, 
        published_date__lte=timezone.now()
    )
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    """
    View para criar um novo post.
    Se o método for POST, processa o formulário e salva o post.
    Caso contrário, exibe o formulário vazio.
    """
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            messages.success(request, 'Post criado com sucesso!')
            return render(request, 'blog/post_detail.html', {'post': post})
    else:
        form = PostForm()
    
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    """
    View para editar um post existente.
    Se o método for POST, processa o formulário com os dados do post.
    Caso contrário, exibe o formulário preenchido com os dados do post.
    """
    post = get_object_or_404(Post, pk=pk)
    
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.published_date = timezone.now()
            post.save()
            messages.success(request, 'Post atualizado com sucesso!')
            return render(request, 'blog/post_detail.html', {'post': post})
    else:
        form = PostForm(instance=post)
    
    return render(request, 'blog/post_edit.html', {'form': form})