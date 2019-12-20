from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver



class Etablissement(models.Model):
    etablissement_code=models.CharField(max_length=1)
    etablissement_desig=models.CharField(max_length=350)
    def __str__(self):
        return self.etablissement_desig


class Classe(models.Model):
    classe_code=models.ForeignKey(Etablissement,on_delete=models.CASCADE,null=True)
    classe_desig=models.CharField(max_length=350)
    def __str__(self):
        return self.classe_desig

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    etablissement=models.ForeignKey(Etablissement,on_delete=models.CASCADE,null=True)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class Enseignant(models.Model):
    enseignant_nom=models.CharField(max_length=300)
    enseignant_prenom=models.CharField(max_length=300)
    enseignant_lieu=models.CharField(max_length=300,null=True,blank=True)
    enseignant_adresse=models.CharField(max_length=300,null=True,blank=True)
    enseignant_sexe=models.CharField(max_length=70)
    enseignant_email=models.CharField(max_length=200,null=True,blank=True)
    enseignant_telephone=models.CharField(max_length=200,null=True,blank=True)
    enseignant_naissance=models.DateField(default='')
    enseignant_etablissement=models.ForeignKey(Etablissement,on_delete=models.CASCADE,null=True,blank=True)
    def __str__(self):
        return self.enseignant_nom
    

class Note(models.Model):
    titre=models.CharField(max_length=200)
    date_note=models.DateField()
    sujet=models.CharField(max_length=800)
    classe=models.ForeignKey(Classe,on_delete=models.CASCADE,null=True)
    enseignant=models.ForeignKey(Enseignant,on_delete=models.CASCADE,null=True)
    def __str__(self):
        return self.titre


