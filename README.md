# Ocarina of Python 🎵

Um instrumento virtual inspirado na mecânica da ocarina de *The Legend of Zelda: Ocarina of Time*, desenvolvido em Python com Pygame.

O projeto permite tocar notas pelo teclado, alternar entre duas oitavas com `Shift`, reconhecer sequências de músicas e reproduzir a canção correspondente.

## Funcionalidades

- 🎹 Reprodução de notas musicais pelo teclado.
- ⬆️ `Shift` como alavanca para tocar a oitava superior.
- 🔇 Uma nova nota interrompe a anterior.
- 🎵 Reconhecimento de músicas por sequência de notas.
- 🔄 Reconhecimento de novos trechos mesmo quando o usuário muda de música no meio da sequência.
- 🖼️ Imagem e cor próprias para cada música reconhecida.
- ⏱️ Exibição das notas da música sincronizada com tempos configuráveis.
- 🎼 Livro de Canções para consultar as sequências disponíveis.
- 🎛️ Modo Livre e Modo Músicas.

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

## Como funciona

As sequências das músicas ficam separadas da lógica principal do programa. O `main.py` processa os eventos do teclado, atualiza a interface e verifica as sequências tocadas.

Quando uma sequência completa corresponde a uma música, o programa:

1. reproduz o efeito de reconhecimento;
2. exibe o nome, a imagem e a sequência da música;
3. apresenta as notas da canção em sequência;
4. reproduz o arquivo de áudio correspondente.

Os tempos de exibição das notas podem ser ajustados separadamente no arquivo `tempos.py`.

## Estrutura

```text
ocarina-of-python/
├── main.py
├── musicas.py
├── sons.py
├── tempos.py
├── assets/
└── sounds/
```

## Requisitos

- Python 3.13
- Pygame 2.6.1

Instale a dependência com:

```bash
pip install -r requirements.txt
```

Depois execute:

```bash
python main.py
```

## Observações

Este projeto foi desenvolvido como um projeto de estudo para praticar Python, Pygame, manipulação de eventos, organização de dados, temporização e lógica de reconhecimento de sequências.

The Legend of Zelda: Ocarina of Time é propriedade da Nintendo. Este projeto não possui finalidade comercial.
