## 🌱 Projeto

- Recuperar informações de uso de CPU e RAM

1. Relacionado à CPU
```
get_cpu_usage_pct()lê a carga atual da CPU como uma porcentagem.
get_cpu_frequency()obtém a frequência atual da CPU em MHz.
get_cpu_temp()relata a temperatura atual da CPU em graus Celsius.
```

2. Relacionado a RAM
```
get_ram_usage()recupera o uso atual de RAM em bytes.
get_ram_total()retorna o total de RAM instalada em bytes.
get_ram_usage_pct()relata o uso de RAM como uma porcentagem.
```

3. Troca relacionada
```
get_swap_usage()determina o uso de swap atual em bytes.
get_swap_total()informa sobre a troca total disponível em bytes.
get_swap_usage_pct()para obter o uso de swap como uma porcentagem.
```

## ✨ Tecnologias

- Telebot
- Telegram
- Python3
- Psutil
- Pyyaml
- Coçorama

## 🛠️ Ambiente 
1. sudo apt install python3.9-venv
2. python3 -m venv .env
3. source .env/bin/activate
4. deactivate

# Compartilhamento do ambiente
1. pip freeze > requirements.txt
2. pip install -r requirements.txt

# Removendo o ambiente
1. deactivate
2. rm -r .env

## 🚀 Execução

## 📄 Licença
Esse projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 🙇 Referências

- https://pypi.org/project/psutil/
- https://pypi.org/project/PyYAML/
- https://pypi.org/project/colorama/
- https://pypi.org/project/pyTelegramBotAPI/0.3.0/