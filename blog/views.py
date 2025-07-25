from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.core.paginator import Paginator
from .models import Post
from django.utils import timezone

def post_list(request):
    """
    View para listar todos os posts publicados.
    Posts são ordenados por data de publicação (mais recente primeiro).
    """
    posts = Post.objects.filter(
        published_date__lte=timezone.now()
    ).select_related('author').order_by('-published_date')
    
    # Paginação (descomente para ativar)
    # paginator = Paginator(posts, 5)  # 5 posts por página
    # page_number = request.GET.get('page')
    # posts = paginator.get_page(page_number)
    
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