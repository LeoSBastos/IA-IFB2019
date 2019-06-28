def variancia(valores):
    _media = media(valores)
    soma = 0
    _variancia = 0
 
    for valor in valores:
        soma += math.pow( (valor - _media), 2)
    _variancia = soma / float( len(valores) )
    return _variancia
 



import statistics
data_points = [ random.randint(1, 100) for x in range(1,1001) ]
statistics.mean(data_points)


"""
Podemos usar pvariance(data, mu=None) para calcular a variação da população de um conjunto.

O segundo argumento é opcional. O valor de mu, quando passado, deve ser igual à
media do conjunto. A média é calculada automaticamente se não for passada.
A função é útil quando queremos calcular a variação de uma população inteira.
Se os dados são apenas uma amostra da população, podemos usar variance(data, xBar=None)
para calcular variança de exemplo. xBar é a média do exemplo dado e é calculada automaticamente
se não for passada.

Para calcular o desvio padrão e desvio padrão de amostra de população, podemo
usar pstdev(data, mu=None) e stdev(data, xBar=None), respectivamente.
"""
import statistics
from fractions import Fraction as F
 
data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
 
statistics.pvariance(data)     # returns 6.666666666666667
statistics.pstdev(data)        # returns 2.581988897471611
statistics.variance(data)      # returns 7.5
statistics.stdev(data)         # returns 2.7386127875258306
 
more_data = [3, 4, 5, 5, 5, 5, 5, 6, 6]
 
statistics.pvariance(more_data)   # returns 0.7654320987654322
statistics.pstdev(more_data)      # returns 0.8748897637790901
 
some_fractions = [F(5, 6), F(2, 3), F(11, 12)]
statistics.variance(some_fractions)
# returns Fraction(7, 432)