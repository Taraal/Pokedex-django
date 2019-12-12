from django.db import models
import requests

# Create your models here.

class Move(models.Model):
    id_type = models.IntegerField()
    name = models.CharField(max_length=50)
    power = models.IntegerField()
    type = models.ForeignKey(Type)


class Type(models.Model):
    id_type =


class Pokemon(models.Model):
    speed = models.IntegerField()
    atk = models.IntegerField()
    defense = models.IntegerField()
    hp = models.IntegerField()
    name = models.CharField(max_length=50)
    id_poke = models.IntegerField()

    @classmethod
    def create(cls, nom, prenom, username, email, password):
        poke = cls(nom=nom, prenom=prenom, username=username, email=email, password=password)
        return poke

    @classmethod
    def createOne(cls, id):
        if not Pokemon.filter(id_poke=id).exists():
            url = "https://pokeapi.co/api/v2/pokemon/"

            poke = Pokemon.create()
            data = requests.get(url + str(id)).json()

            poke.id = id
            name = data['name']

            speed = data['stats'][0]['base_stat']
            atk = data['stats'][4]['base_stat']
            defense = data['stats'][3]['base_stat']
            hp = data['stats'][5]['base_stat']

            poke = cls(id_poke=id, atk=atk, defense=defense, speed=speed, hp=hp, name=name)
            poke.save()
        else:
            poke = Pokemon.objects.get(id_poke=id)
        return poke

    @classmethod
    def create(cls):
        poke = cls()
        return poke

    @classmethod
    def getList(self, max, min=0):
        pokeList = Pokemon.objects.all().filter(id_poke__lte=max)
        return  pokeList
