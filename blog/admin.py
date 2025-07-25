from django.contrib import admin
from django.utils.html import format_html
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'created_date', 'published_date', 'is_published_status']
    list_filter = ['created_date', 'published_date', 'author']
    search_fields = ['title', 'text']
    date_hierarchy = 'published_date'
    ordering = ['-published_date', '-created_date']
    
    # Campos do formulário de edição
    fields = ['title', 'text', 'author', 'published_date']
    
    # Ações personalizadas
    actions = ['make_published', 'make_unpublished']
    
    def is_published_status(self, obj):
        """Mostra um ícone indicando se o post está publicado."""
        if obj.is_published():
            return format_html(
                '<span style="color: green;">✓ Publicado</span>'
            )
        return format_html(
            '<span style="color: red;">✗ Rascunho</span>'
        )
    is_published_status.short_description = 'Status'
    
    def make_published(self, request, queryset):
        """Ação para publicar posts selecionados."""
        updated = 0
        for post in queryset:
            if not post.is_published():
                post.publish()
                updated += 1
        
        if updated:
            self.message_user(
                request, 
                f'{updated} post(s) publicado(s) com sucesso.'
            )
        else:
            self.message_user(
                request, 
                'Nenhum post foi publicado (já estavam publicados).'
            )
    make_published.short_description = 'Publicar posts selecionados'
    
    def make_unpublished(self, request, queryset):
        """Ação para despublicar posts selecionados."""
        updated = queryset.update(published_date=None)
        self.message_user(
            request, 
            f'{updated} post(s) despublicado(s) com sucesso.'
        )
    make_unpublished.short_description = 'Despublicar posts selecionados'

# Customização do site admin
admin.site.site_header = "Django Girls Blog - Administração"
admin.site.site_title = "Django Girls Admin"
admin.site.index_title = "Bem-vinda ao painel administrativo"