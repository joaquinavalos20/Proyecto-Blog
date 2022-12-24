from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name="Titulo")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Autor")
    body = RichTextField(blank=True, null=True, verbose_name="Cuerpo")
    #body = models.TextField( verbose_name="Cuerpo")
    create_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title + " | " + str(self.author)

    def get_absolute_url(self):
        return reverse("home")

    def create_user_profile(sender, instance, created, **kwargs):     
        if created:         
            instance.groups.add(Group.objects.get(name='estudiante'))

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments" ,on_delete=models.CASCADE, verbose_name="Publicación")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Autor")
    body = models.TextField(verbose_name="Comentario")
    create_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s - %s" % (self.post.title, self.author.first_name)