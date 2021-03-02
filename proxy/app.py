from proxy import Proxy  # Funciona como VPS
from numeros import Numeros  # Seríamos nosotros

# Números es el objeto que sería el tráfico
proxy = Proxy(Numeros)
print(proxy.proxy())
