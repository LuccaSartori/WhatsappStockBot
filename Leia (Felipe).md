# WhatsappStockBot
WPP bot that sends Stock information

Oi felipe, aqui vou dar uma explicada pra você não se perder...

Basicamente o que o programa faz é enviar o preço de fechamento das suas ações na ulima abertura do mercado pelo seu whatsapp... Ele guarda sua carteira de ações em um arquivo .csv chamado data.csv

O programa tem três comandos iniciais:
Adicionar um ticker
Adicionar um telefone para enviar a mensagem
Trocar de telefone

Dentro da função ''introdução'' acontece os 3 comandos acima, utilizando if e elif para isso. Os comandos que mexem com os telefones usam um .csv chamado telefone.csv...

As funções que buscam o preço no API são a Price__ e a price_2. A price__ retorna um dicionario com o ticker da ação e o preço, e ele vai diretamente na mensagem, e a price_2 retorna diretamente o preço que vai no data.csv quando você registra um ticker novo...

A função send_message é a mais importante, eu usei uma library chamada pywhatkit, que é uma maneira basica de enviar mensagens por whatsapp sem criar um bot. Ela abre seu whatsapp web, e envia a mensagem pelo seu telefone... (mais pra frente pretendo criar um bot para a mensagem não sair do meu telefone)

Documentação do pywhatkit para ficar mais fácil de vc entender https://pypi.org/project/pywhatkit/

Agora eu tenho uma pergunta felipe, o final desse projeto pra mim seria conseguir marcar um horario para as mensagens serem enviadas, por exemplo antes da abertura do mercado, e depois, as 10 da manhã e as 19 da noite por exemplo. Mas não achei um jeito viável de fazer isso, pensei em transformar em um .exe, mas aí teria que aprender um monte de coisa a mais... Você tem alguma ideia?
