from django.db import models

# Create your models here.
class OfferWorks(models.Model):
    name = models.CharField(max_length=50, verbose_name="Nomi:")
    location = models.CharField(max_length=128, verbose_name="Manzili:")
    old_prize = models.IntegerField(verbose_name='Eski narxi:')
    new_prize = models.IntegerField(verbose_name='Yangi narxi:')
    bath_room = models.IntegerField(verbose_name='Yuvinish xonalar soni:')
    room = models.IntegerField(verbose_name='Mehmonxonalar soni: ')
    area = models.FloatField(verbose_name='Umumiy maydon: ', null=True)
    image = models.ImageField(verbose_name='Rasm yuklang:')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.id}. {self.name} - {self.location}" 

class HappyClients(models.Model):
    client_name_last = models.CharField(max_length=50, verbose_name='Mijoz ismi va familiyasi:')
    client_position = models.CharField(max_length=40, verbose_name="Mijoz lavozimi:")
    client_image = models.ImageField()
    client_fidback = models.CharField(max_length=200, verbose_name='Mijoz fikr:')
    client_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.client_name_last

class Agents(models.Model):
    agent_name = models.CharField(max_length=40, verbose_name='Agent ismi va familiyasi:')
    agent_img = models.ImageField(verbose_name='Agent rasmini yuklang:')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.agent_name

class ResentBlog(models.Model):
    short_text = models.CharField(max_length=55, verbose_name="Qisqa ma'lumot: ")
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    long_text = models.CharField(max_length=200, verbose_name="Ko'proq ma'lumot: ")
    blog_image = models.ImageField()

    def __str__(self):
        return self.short_text

    def get_date(self):
        now = self.date
        date_time = now.strftime("%d/%m/%Y")
        return date_time


    


