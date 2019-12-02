import os 
from peewee import *

arq = 'cadastro.db'
db = SqliteDatabase(arq)


class BaseModel(Model):
    class Meta:
        database = db

class Pessoa(BaseModel):
    nome = CharField()
    data_nascimento = CharField()

    def __str__(self):
        return str(self.nome) + "\n" + str(self.data_nascimento)

class Noticia(BaseModel):
    titulo = CharField()
    assunto = CharField()
    data = CharField()

    def __str__(self):
        return str(self.titulo) + "\n" + str(self.assunto) + "\n" + str(self.data)

class Musica(BaseModel):
    nome = CharField()
    cantor = ForeignKeyField(Pessoa)
    gravadora = CharField()
    album = CharField()

    def __str__(self):
        return str(self.nome) + "\n" + str(self.cantor.nome) + "\n" + str(self.gravadora) + "\n" + str(self.album) 

class Propaganda(BaseModel):
    empresa = CharField()
    duracao = CharField()

    def __str__(self):
        return str(self.empresa) + "\n" + str(self.duracao)

class Locutor(BaseModel):
    nome = ForeignKeyField(Pessoa)
    contrato = CharField()
    
    def __str__(self):
        return str(self.nome.nome) + "\n" + str(self.contrato)

class Ouvinte(BaseModel):
    nome = ForeignKeyField(Pessoa)
    cidade = CharField()

    def __str__(self):
        return str(self.nome.nome) + "\n" + str(self.cidade)

class NotaDeFalecimento(BaseModel):
    falecido = ForeignKeyField(Pessoa)
    data = CharField()
    motivo = CharField()

    def __str__(self):
        return 'Falecido(a): ' + str(self.falecido.nome) + "\n" + 'Data: ' + str(self.data) + "\n" + 'Motivo: ' + str(self.motivo)

class NotaDeAniversariante(BaseModel):
    aniversariante = ForeignKeyField(Pessoa)
    data = CharField()

    def __str__(self):
        return str(self.aniversariante.nome) + "\n" + str(self.data)

class Frequencia(BaseModel):
    tipo = CharField()
    hertz = CharField()

    def __str__(self):
        return str(self.hertz) + str(self.tipo)

class Programacao(BaseModel):
    locutor = ForeignKeyField(Locutor)
    propaganda = ForeignKeyField(Propaganda)
    musica = ForeignKeyField(Musica)
    noticia = ForeignKeyField(Noticia)
    notadefalecimento = ForeignKeyField(NotaDeFalecimento)
    notadeaniversariante = ForeignKeyField(NotaDeAniversariante)

    def __str__(self):
        return 'Locutor: ' + str(self.locutor) + "\n" + 'Propaganda: ' + str(self.propaganda) +  "\n" + 'Música: ' + str(self.musica) + "\n" + 'Notícia: ' + str(self.noticia) + "\n" + 'Anúncio de falecimento: ' + str(self.notadefalecimento.falecido) + "\n" + 'Anúncio de aniversário: ' + str(self.notadeaniversariante)

class Radio(BaseModel):
    nome = CharField()
    frequencia = ForeignKeyField(Frequencia)
    programacao = ForeignKeyField(Programacao)

    def __str__(self):
        return 'Radio: ' + str(self.nome) + "\n" + 'Identificação: ' + str(self.frequencia) + "\n" + "\n" + 'Programação: '  + "\n" + str(self.programacao) 

if __name__ == "__main__":
    if os.path.exists(arq):
        os.remove(arq)

    db.connect()
    db.create_tables([Pessoa, Noticia, Musica, Propaganda, Locutor, Ouvinte, NotaDeFalecimento, NotaDeAniversariante, Frequencia, Programacao, Radio])

    shawn = Pessoa.create(nome = 'Shawn Mendes', data_nascimento = '08/08/1998')
    gugu = Pessoa.create(nome = 'Gugu Liberato', data_nascimento = '10/04/1959')
    scarlett = Pessoa.create(nome = 'Scarlett Johanson', data_nascimento = '22/11/1995')
    nikolas = Pessoa.create(nome = 'Nikolas Starke', data_nascimento = '22/03/2001')
    rafa = Pessoa.create(nome = 'Rafa Steinbach', data_nascimento = '08/08/1990')

    lulalivre = Noticia.create(titulo= 'Lula Livre', assunto= 'Política', data='08-11-2019')
    neverbealone = Musica.create(nome='Never Be Alone', cantor=shawn, gravadora='Island Records', album='Handwritten')
    propaganda = Propaganda.create(empresa='Omo', duracao='30 seg')
    rafinha = Locutor.create(nome=rafa, contrato='1234566789')
    ouvinte = Ouvinte.create(nome=nikolas, cidade='Blumenau')
    falecimentoGugu = NotaDeFalecimento.create(falecido=gugu, data='22-11-2019', motivo='Queda')
    aniversarioScarlett= NotaDeAniversariante.create(aniversariante=scarlett, data='22-11')
    freqatlantida= Frequencia.create(tipo='fm', hertz='102.7')
    programacao2211 = Programacao.create(locutor=rafinha, propaganda=propaganda, musica=neverbealone, noticia=lulalivre, notadefalecimento=falecimentoGugu, notadeaniversariante=aniversarioScarlett)
    atlantida = Radio.create(nome = 'Atlântida', frequencia = freqatlantida, programacao = programacao2211)


    print(atlantida)