# testando e implementando o conceito de modularização no python

# importando meu módulo cor e chamando ele de cor para facilitar
import cores as cor

txt_verde_negrito = cor.cores('verde', negrito=True)
txt_padrao = cor.cores('padrao')

print(f'{txt_verde_negrito}TESTANDO O MODULO DE CORES{txt_padrao}')
print('AGORA TESTANDO O PRINT SEM USAR NADA DE FORMATAÇÃO')
