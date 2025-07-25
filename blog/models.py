from django.conf import settings
from django.db import models
from django.utils import timezone
from django.urls import reverse

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, help_text="Título do post")
    text = models.TextField(help_text="Conteúdo do post")
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        ordering = ['-published_date', '-created_date']
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    def publish(self):
        """Publica o post definindo a data de publicação como agora."""
        self.published_date = timezone.now()
        self.save()

    def get_absolute_url(self):
        """Retorna a URL absoluta para o post."""
        return reverse('post_detail', kwargs={'pk': self.pk})

    def is_published(self):
        """Verifica se o post está publicado."""
        return self.published_date is not None and self.published_date <= timezone.now()

    def get_excerpt(self, words=50):
        """Retorna um resumo do texto do post."""
        text_words = self.text.split()
        if len(text_words) > words:
            return ' '.join(text_words[:words]) + '...'
        return self.text

    def __str__(self):
        return self.title
