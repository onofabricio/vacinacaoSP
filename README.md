# vacinacaoSP
  O objetivo principal deste projeto é verificar, pela lei de Benford, a veracidade dos dados de vacinação do estado de SP.
Para isso, utilizaremos o dataset que pode ser acessado diretamente do portal do [governo](https://vacinaja.sp.gov.br/vacinometro/?utm_source=portal&utm_medium=banner-topo&utm_campaign=Vacinometro-Municipios) 
## Como a Lei de Benford funciona?
  Em 1881, o astrônomo Simon Newcomb percebeu que as primeiras páginas de livros de logaritmo estavam mais usadas do que as últimas, pelo fato de serem mais utilizadas em cálculos. Ele então percebe esse fenômeno se repetir muitas vezes de modo que, em conjuntos de dados aleatórios e distrubuidos em diferentes ordens de grandeza,a probabilidade do número 1 surgir no primeiro digito é maior que o número 2, que é maior que o número 3, e assim por diante. De acordo com a seguinte fórmula:
 
 ![benford](https://wikimedia.org/api/rest_v1/media/math/render/svg/48649074b19e71dc8dc5e8dd82717f05bc541b67)
 


A probabilidade de cada número pode ser representada como no gráfico abaixo: 
![grafico](https://upload.wikimedia.org/wikipedia/commons/thumb/4/46/Rozklad_benforda.svg/800px-Rozklad_benforda.svg.png)


  Este fato foi esquecido por um tempo. Até que em 1938, Frank Benford resgata as memórias de Newcomb realizando um experimento. Benford coletou dezenas de milhares de números de 20 domínios diferentes, dentre eles estavam áreas de superfície de 335 rios, tamanho de populações de 3259 locais dos EUA, 104 constantes físicas, 1800 pesos moleculares, 5000 entradas de um livro matemático, 308 números contidos em uma edição da Reader’s Digest, os 342 primeiros endereços listados na American Men of Science e 418 taxas de mortalidade. O total de números utilizados no paper chegou a 20.229   e todos seguiam a mesma distribuição. A descoberta deste padrão foi nomeada posteriormente de Lei de Benford.

  Desde então, a Lei de Benford pode ser aplicada para detectar fraudes em bancos de dados, desde que os dados tenham as propriedades necessárias para tal aplicação. Em alguns países, este fenômeno pode ser utilizado como prova judicial de fraude

