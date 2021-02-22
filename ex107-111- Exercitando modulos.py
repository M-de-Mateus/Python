from Pacotes.utilidadescev import moeda
from Pacotes.utilidadescev import dados

preco = dados.leiaDinheiro('Digite o preço: R$ ')
moeda.resumo(preco, 10, 5)
