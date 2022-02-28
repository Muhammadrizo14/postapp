from django.db import models
from django.urls import reverse


class Tag(models.Model):
    title = models.CharField(max_length=50, )
    slug = models.SlugField(max_length=50, verbose_name='Url', unique=True, )

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse("tag", kwargs={"slug": self.slug})


class Category(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return self.title



    def get_absolute_url(self):
        return reverse("category", kwargs={"slug": self.slug})


class Blog(models.Model):
    title = models.CharField(max_length=200, verbose_name="Загаловок")
    category = models.ForeignKey(Category, related_name='category', on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag, related_name='tags')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', )
    author = models.CharField(max_length=120, blank=True, verbose_name="Автор")
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    slug = models.SlugField(max_length=50, unique=True, verbose_name='url')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog_detail", kwargs={"slug": self.slug})

    class Meta:
        ordering = ['-created_at']



class Reviews(models.Model):
    email = models.EmailField()
    name = models.CharField("Name", max_length=100)
    text = models.TextField("Message", max_length=500)
    parent = models.ForeignKey('self', verbose_name="Parent", on_delete=models.SET_NULL, blank=True, null=True)
    blog = models.ForeignKey(Blog, verbose_name="blog", on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} - {self.blog}'

    class Meta:
        verbose_name = "Review"
        verbose_name_plural = "Reviews"
