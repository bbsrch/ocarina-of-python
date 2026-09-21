# Ocarina of Python

Uma ocarina virtual inspirada na mecânica de *The Legend of Zelda: Ocarina of Time*, desenvolvida em Python com Pygame.

O projeto transforma uma ideia que mistura programação e música em uma aplicação interativa: o usuário pode tocar notas pelo teclado, alternar entre oitavas, tocar livremente ou reproduzir as sequências das músicas cadastradas.

## Funcionalidades

### 🍃 Modo Livre

Permite tocar as notas livremente, sem que o programa tente reconhecer uma música.

### 🎵 Modo Músicas

O programa registra as notas tocadas e verifica continuamente se a sequência ainda pode corresponder ao início de alguma canção.

Quando a sequência completa é reconhecida:

- a música é identificada;
- um efeito sonoro de reconhecimento é reproduzido;
- o nome, a imagem e a cor da música aparecem na interface;
- a sequência de notas é exibida progressivamente;
- a gravação correspondente da música é reproduzida.

O reconhecimento também consegue aproveitar trechos finais de uma sequência. Isso permite mudar de uma música para outra no meio da execução sem precisar reiniciar manualmente toda a tentativa.

### 📖 Livro de Canções

Uma tela de consulta com as músicas disponíveis e suas respectivas sequências de notas.

Pode ser aberta com `3` e fechada com `3` novamente ou `ESC`.

## Áudio produzido para o projeto

Uma das partes do projeto foi a produção dos próprios áudios.

Em vez de utilizar gravações prontas, **gravei individualmente todas as notas utilizando minha própria flauta doce**. Depois, realizei a edição e os ajustes dos áudios no **Better Audio Editor**, um aplicativo gratuito de edição de áudio.

Os arquivos editados foram então integrados à aplicação para a reprodução das notas individuais e das canções reconhecidas.

## Interface

A interface foi desenvolvida em Pygame e inclui:

- representação visual do teclado;
- exibição da nota atualmente tocada;
- identidade visual própria para cada música, com cores e imagens;
- sequência de notas exibida progressivamente durante a reprodução;
- indicação do modo atual;
- Livro de canções para consulta.

## Controles

| Tecla | Função |
|---|---|
| `Z X C V B N M` | Notas naturais |
| `S D G H J` | Sustenidos |
| `Shift + tecla` | Oitava superior |
| `1` | Modo Livre |
| `2` | Modo Músicas |
| `3` | Abrir/fechar Livro de Canções |
| `ESC` | Fechar Livro de Canções |

## Estrutura do projeto

```text
ocarina-of-python/
├── main.py
├── musicas.py
├── sons.py
├── tempos.py
├── requirements.txt
├── README.md
├── assets/
└── sounds/
```

### Organização dos arquivos

**`main.py`**  
Contém a lógica principal da aplicação, processamento de eventos e desenho das interfaces.

**`musicas.py`**  
Contém as sequências das músicas, caminhos dos arquivos de áudio, imagens e cores associadas a cada canção.

**`sons.py`**  
Contém os sons das notas, os sons da oitava superior e o mapeamento entre teclas e notas.

**`tempos.py`**  
Contém os intervalos utilizados para sincronizar a exibição progressiva das notas de cada música.

## Tecnologias

- Python 3.13.15
- Pygame 2.6.1
- Better Audio Editor
- Git
- GitHub

## Como executar

Clone o repositório e instale as dependências:

```bash
pip install -r requirements.txt
```

Depois execute:

```bash
python main.py
```

## Observações

O projeto foi desenvolvido como uma forma de praticar **Python, Pygame, manipulação de eventos, estruturas de dados, reconhecimento de sequências, temporização, reprodução de áudio, organização de código e desenvolvimento de interfaces gráficas**.

Também foi uma oportunidade de integrar programação e produção de conteúdo próprio, unindo código, interface e áudio gravado e editado especificamente para a aplicação.

The Legend of Zelda: Ocarina of Time é propriedade da Nintendo. Este projeto não possui finalidade comercial.
