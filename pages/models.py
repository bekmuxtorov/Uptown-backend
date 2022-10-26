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

    
    class Meta:
        verbose_name = 'Topshirilgan ish'
        verbose_name_plural = "Topshirilgan ishlar"

    def __str__(self):
        return f"{self.id}. {self.name} - {self.location}" 

class HappyClients(models.Model):
    client_name_last = models.CharField(max_length=50, verbose_name='Mijoz ismi va familiyasi:')
    client_position = models.CharField(max_length=40, verbose_name="Mijoz lavozimi:")
    client_image = models.ImageField()
    client_fidback = models.CharField(max_length=200, verbose_name='Mijoz fikr:')
    client_date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Buyurtmachi'
        verbose_name_plural = "Buyurtmachilar"

    def __str__(self):
        return self.client_name_last

class Agents(models.Model):
    agent_name = models.CharField(max_length=40, verbose_name='Agent ismi va familiyasi:')
    agent_img = models.ImageField(verbose_name='Agent rasmini yuklang:')
    date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Ishchi'
        verbose_name_plural = "Ishchilar"

    def __str__(self):
        return self.agent_name

class ResentBlog(models.Model):
    short_text = models.CharField(max_length=55, verbose_name="Qisqa ma'lumot: ")
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    long_text = models.CharField(max_length=200, verbose_name="Ko'proq ma'lumot: ")
    blog_image = models.ImageField()
    
    class Meta:
        verbose_name = 'Maqola'
        verbose_name_plural = "Maqolalar"

    def __str__(self):
        return self.short_text

    def get_date(self):
        now = self.date
        date_time = now.strftime("%d/%m/%Y")
        return date_time

class Contact(models.Model):
    name = models.CharField(max_length=100, verbose_name="Ism:", help_text="Ism:", blank=True, null=False)
    email = models.EmailField(verbose_name="Email:", help_text="Email:", blank=True, null=False)
    subject = models.CharField(max_length=200, verbose_name="Mavzu:", help_text="Mavzu:", blank=True, null=False)
    message = models.TextField(verbose_name="Xabar:", help_text="Xabar:", blank=True, null=False)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Xabar'
        verbose_name_plural = 'Xabarlar'

    def __str__(self):
        return self.name

    def get_date(self):
        now = self.date
        datetime = now.strftime("%d/%m/%Y")
        return datetime





    


