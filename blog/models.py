from datetime import date
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Blog(models.Model):
    header = models.CharField(("Überschrift"), max_length=50)
    content = models.TextField(("Blog Eintrag"))
    rating = models.IntegerField(("Bewertung"), default = 5)
    created = models.DateTimeField(("Erstellt"), auto_now=False, auto_now_add=True)
    changed = models.DateTimeField(("Verändert"), auto_now=True, auto_now_add=False)
    user = models.ForeignKey(User, verbose_name=("Benutzer"), on_delete=models.CASCADE)
 
    class Meta:
        verbose_name = "Blog"
        verbose_name_plural = "Blogs"

    def __str__(self):
        return f"{self.header} ({self.user})"

#    def get_absolute_url(self):
#        return reverse("Blog_detail", kwargs={"pk": self.pk})

