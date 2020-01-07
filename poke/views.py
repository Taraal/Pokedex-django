from django.shortcuts import render
from .models import Pokemon
import requests

# Create your views here.

def importTwenty(request):
    for i in range(1,152):
        poke = Pokemon.createOne(i)
    return getAll(request)

def purge(request):
    Pokemon.removeAll()
    return getAll(request)


def getAll(request):
    pokelist = Pokemon.getList()
    context = {'data' : pokelist}
    return render(request, "poke/index.html", context)

def fight(request, id1, id2):
    poke1 = Pokemon.objects.get(id_poke=id1)
    poke2 = Pokemon.objects.get(id_poke=id2)
    fight = []
    death = True
    while death:
        topspeed = max(poke1.speed, poke2.speed)
        if poke1.speed == topspeed:
            dmg = round(poke1.atk - (poke2.defense/2))
            fight.append(poke1.name + " attaque ! Il inflige " + str(dmg) + " points de dégat")
            poke2.hp = poke2.hp - dmg
            fight.append(poke2.name + " a désormais " + str(poke2.hp) + " hp")
            if poke2.hp <= 0:
                death = False
        else :
            dmg = round(poke2.atk - (poke1.defense / 2))
            fight.append(poke2.name + " attaque ! Il inflige " + str(dmg) + " points de dégat")
            poke1.hp = poke1.hp - dmg
            fight.append(poke1.name + " a désormais " + str(poke1.hp) + " hp")
            if poke1.hp <= 0:
                death = False

    context = {"data" : fight}
    return render(request, "poke/fight.html", context)