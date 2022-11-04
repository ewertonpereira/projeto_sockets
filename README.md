# Desafio Sockets

## Objetivo
Fazer uma aplicação que envie uma mensagem através da rede ethernet usando um  proprietário padrão, e outra que receba uma mensagem enviada pelo aplicativo anterior com o `protocolo proprietário`. Esse aplicativo deve verificar se a mensagem recebida está correta  ou não. Se a mensagem estiver correta, apresentar a mesma na tela e informar que a  mensagem está correta. Se a mensagem não estiver correta, apenas informar que a  mensagem está errada.

## Regras
### Protocolo proprietário

    O protocolo é descrito da seguinte forma:

             |STX|Mensagem|EXT|BCC|

    STX = 0x02 ou 2
    ETX = 0x03 ou 3
    BCC é igual a operação ou-exclusivo de todos os bytes do frame do STX até o ETX.


              ![image](file:///C:/Users/Ewerton/Desktop/protocol.jpg)