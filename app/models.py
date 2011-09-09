from django.db import models

class Coltura(models.Model):
    id_coltura = models.AutoField(primary_key = True)
    coltura = models.CharField(max_length = 30)
    codice = models.PositiveSmallIntegerField(unique =True)
    name ="Coltura"

    def __unicode__(self):
        return self.name

class Azienda(models.Model):
    id_azienda = models.AutoField(primary_key = True)
    nome = models.CharField(max_length = 45)
    cognome = models.CharField(max_length = 45)
    indirizzo = models.CharField(max_length =  100)
    piva =  models.CharField(max_length=18)
    name = "Azienda"

    def __unicode__(self):
        return self.name

class Appezzamento(models.Model):
    id_appezzamento = models.AutoField(primary_key = True)
    id = models.CharField(max_length = 4)
    sau = models.PositiveIntegerField()
    coltivazione = models.PositiveSmallIntegerField()
    anno_impianto = models.PositiveSmallIntegerField()
    ultimo_tratt = models.DateField()
    coltura = models.ForeignKey(Coltura , to_field = 'codice')
    ##catasto = models.ManyToManyField(Catasto, through = 'Appezzamenti_catasti')

    name = "Appezzamento"
    def __unicode__(self):
        return self.name


class Proprietario(models.Model):
    id_proprietario = models.AutoField(primary_key = True)
    nome = models.CharField(max_length = 45)
    cognome = models.CharField(max_length = 45)
    
    name = "Proprietario"
    def __unicode__(self):
        return self.name

class Catasto(models.Model):
    id_catasto = models.AutoField(primary_key = True)
    provincia = models.PositiveIntegerField()
    comune = models.PositiveSmallIntegerField()
    foglio = models.PositiveSmallIntegerField()
    particella = models.PositiveSmallIntegerField()
    sub = models.CharField(max_length = 3)
    sup_tot =  models.PositiveIntegerField()
    coltura = models.ForeignKey(Coltura, to_field = 'codice')
    id_proprietario = models.ForeignKey(Proprietario, to_field = 'id_proprietario')
    azienda = models.ManyToManyField(Azienda, through = 'Appezzamenti_catasti')

    name = "Catasto"
    def __unicode__(self):
        return self.name



class Appezzamenti_catasti (models.Model):
    idappezzamenti_catasti = models.AutoField(primary_key = True)
    id_appezzamento = models.ForeignKey(Appezzamento, to_field = 'id_appezzamento')
    id_catasto = models.ForeignKey(Catasto, to_field = 'id_catasto')
    id_azienda = models.ForeignKey(Azienda , to_field = 'id_azienda')

    name = "Appezzamenti_catasto"
    def __unicode__(self):
        return self.name

