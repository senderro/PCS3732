# Projeto: DOOM no Raspberry Pi 3B+ com Controles Customizados

## 1. Motivação
Este projeto busca explorar na prática conceitos fundamentais da engenharia, integrando componentes eletrônicos físicos a um sistema de software clássico. A motivação principal é compreender a fundo a comunicação entre hardware e software utilizando protocolos de baixo nível, como I2C e GPIO. Ao utilizar o Raspberry Pi 3B+ e a nostalgia do jogo DOOM como plataforma de validação do aprendizado, o projeto proporciona um cenário real para aplicar conhecimentos de arquitetura de sistemas, desenvolvimento de middleware e controle de periféricos, competências essenciais na resolução de problemas de engenharia.

## 2. Especificação de Requisitos
* **REQ-01**: O sistema deve executar o motor gráfico do jogo DOOM original com uma taxa de quadros estável, garantindo a jogabilidade.
* **REQ-02**: O sistema deve capturar comandos de movimentação via um módulo analógico (Joystick) e ações (atirar, abrir portas) via 4 botões físicos, traduzindo-os para comandos reconhecidos pelo jogo.
* **REQ-03**: O sistema deve renderizar o vídeo na tela dedicada conectada à placa.

## 3. Arquitetura Proposta
A arquitetura proposta baseia-se em um modelo em camadas, desacoplando o hardware físico, a lógica de integração e a aplicação final. Esta abordagem garante modularidade e facilita o desenvolvimento paralelo da equipe.

A escolha do Raspberry Pi 3B+ em conjunto com o sistema operacional Raspberry Pi OS garante capacidade de processamento amplamente superiores aos requisitos originais do jogo. Para maximizar o desempenho, optou-se por rodar um Source Port nativo (como o Chocolate Doom) em vez de utilizar emuladores como o DOSBox. O Source Port é compilado nativamente para a arquitetura ARM, aproveitando as bibliotecas modernas do Linux e evitando a sobrecarga de tradução de instruções.

A decisão de utilizar um Script Python atuando como Middleware (via biblioteca uinput) resolve o problema de incompatibilidade nativa do jogo com sensores GPIO “crus”. O Raspberry Pi não possui conversores Analógico-Digitais (ADC) nativos nos pinos. Portanto, a arquitetura utiliza o chip ADS7830 (presente no kit Freenove) comunicando-se via barramento I2C, enquanto os botões físicos utilizam pinos digitais com resistores de pull-up internos. O script traduz esses sinais elétricos em eventos de teclado virtuais padrão do Linux. Isso permite que o jogo receba os comandos sem necessidade de alteração em seu código-fonte original.

O motor gráfico do jogo utiliza a biblioteca SDL (Simple DirectMedia Layer), que abstrai o hardware de vídeo e áudio do sistema operacional. Isso permite que a renderização seja enviada diretamente ao servidor gráfico do Linux, que gerencia a saída para o display conectado.

### 3.1 Diagramas da Arquitetura:


**Diagrama de Blocos:**
<img width="3647" height="4995" alt="Raspberry Pi Application-2026-07-16-223156" src="https://github.com/user-attachments/assets/01649555-2a4e-453a-8114-e2664d1a65aa" />


**Diagrama de Sequência:**
<img width="8192" height="1685" alt="Raspberry Pi Application-2026-07-16-223313" src="https://github.com/user-attachments/assets/dda60bbd-4754-4ece-8613-6a3fb356ec17" />



**Fluxograma:**
<img width="3168" height="5995" alt="Raspberry Pi Application-2026-07-16-223625" src="https://github.com/user-attachments/assets/3f4c5c92-4085-455c-b77d-19a798f77794" />
