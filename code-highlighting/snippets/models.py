from django.db import models
from .helper import LANGUAGE_CHOICES, STYLE_CHOICES

class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default="")
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language= models.CharField(
        choices=LANGUAGE_CHOICES, 
        default="python", 
        max_length=100
    )
    style = models. CharField(
        choices=STYLE_CHOICES, 
        default="friendly",
        max_length=100
    )

    class Meta:
        ordering = ["created"]

    def __str__(self):
        return self.title