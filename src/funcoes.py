import psutil
import os

# Função para uso da CPU como porcentagem
def get_cpu_usage_pct():
    """
    Obtém a carga média da CPU do sistema medida durante um período de 500 milissegundos.
    :returns: Carga da CPU do sistema como uma porcentagem.
    :rtype: float
    """
    return psutil.cpu_percent(interval=0.5)

# Função para frequência da CPU
def get_cpu_frequency(): 
    """
    Obtém o valor em tempo real da frequência atual da CPU.
    :returns: Frequência atual da CPU em MHz.
    :rtype:int
    """
    return int ( psutil.cpu_freq () .current ) 

# Função para temperatura da CPU
def get_cpu_temp(): 
    """
    Obtém o valor atual da temperatura da CPU.
    :returns: Valor atual da temperatura da CPU se for bem sucedido, valor zero caso contrário.
    :rtype: float
    """
   # Inicializa o resultado.
    result = 0.0
   # A primeira linha neste arquivo contém a temperatura da CPU como um número inteiro vezes 1000.
   # Leia a primeira linha e remova o caractere de nova linha no final da string.
    if os.path.isfile('/sys/class/thermal/thermal_zone0/temp'):
        with open('/sys/class/thermal/thermal_zone0/temp') as f:
            line = f.readline().strip()
       # Testa se a string é um inteiro como esperado.
        if line.isdigit():
           # Converte a string com a temperatura da CPU para um float em graus Celsius.
            result = float(line) / 1000
   # Devolva o resultado ao chamador.
    return result

# Função para uso de RAM em bytes
def get_ram_usage(): 
    """
    Obtém o número absoluto de bytes de RAM atualmente em uso pelo sistema.
    :returns: Uso de RAM do sistema em bytes.
    :rtype:int
    """
    return int(psutil.virtual_memory().total - psutil. virtual_memory().available) 
 
# Função para RAM total em bytes
def get_ram_total(): 
    """
    Obtém a quantidade total de RAM em bytes disponível para o sistema.
    :returns: RAM total do sistema em bytes.
    :rtype:int
    """
    return int (psutil.virtual_memory().total) 

# Função para uso de RAM como porcentagem
def get_ram_usage_pct() : 
    """
    Obtém o uso atual de RAM do sistema.
    :returns: Uso de RAM do sistema como porcentagem.
    :rtype: float
    """
    return psutil.virtual_memory().percent

# Função para troca de uso em bytes
def get_swap_usage() : 
    """
    Obtém o número absoluto de bytes Swap atualmente em uso pelo sistema.
    :returns: Uso do System Swap em bytes.
    :rtype:int
    """
    return int (psutil.swap_memory().used ) 

# Função para Swap total em bytes
def get_swap_total(): 
    """
    Obtém a quantidade total de Swap em bytes disponíveis para o sistema.
    :returns: Total do sistema Swap em bytes.
    :rtype:int
    """
    return int (psutil.swap_memory().total) 

# Função para o uso do Swap em porcentagem
def get_swap_usage_pct () : 
    """
    Obtém o uso de Swap atual do sistema.
    :returns: Uso do System Swap como porcentagem.
    :rtype: float
    """
    return psutil.swap_memory().percent

