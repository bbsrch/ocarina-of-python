import pygame

pygame.mixer.init()
sons = {
    # Notas naturais
    pygame.K_z: pygame.mixer.Sound("sounds/do.wav"),
    pygame.K_x: pygame.mixer.Sound("sounds/re.wav"),
    pygame.K_c: pygame.mixer.Sound("sounds/mi.wav"),
    pygame.K_v: pygame.mixer.Sound("sounds/fa.wav"),
    pygame.K_b: pygame.mixer.Sound("sounds/sol.wav"),
    pygame.K_n: pygame.mixer.Sound("sounds/la.wav"),
    pygame.K_m: pygame.mixer.Sound("sounds/si.wav"),

    # Sustenidos
    pygame.K_s: pygame.mixer.Sound("sounds/do#.wav"),
    pygame.K_d: pygame.mixer.Sound("sounds/re#.wav"),
    pygame.K_g: pygame.mixer.Sound("sounds/fa#.wav"),
    pygame.K_h: pygame.mixer.Sound("sounds/sol#.wav"),
    pygame.K_j: pygame.mixer.Sound("sounds/la#.wav"),
}

sons_oitava = {
    # Notas naturais
    pygame.K_z: pygame.mixer.Sound("sounds/do8.wav"),
    pygame.K_x: pygame.mixer.Sound("sounds/re8.wav"),
    pygame.K_c: pygame.mixer.Sound("sounds/mi8.wav"),
    pygame.K_v: pygame.mixer.Sound("sounds/fa8.wav"),
    pygame.K_b: pygame.mixer.Sound("sounds/sol8.wav"),
    pygame.K_n: pygame.mixer.Sound("sounds/la8.wav"),
    pygame.K_m: pygame.mixer.Sound("sounds/si8.wav"),

    # Sustenidos
    pygame.K_s: pygame.mixer.Sound("sounds/do#8.wav"),
    pygame.K_d: pygame.mixer.Sound("sounds/re#8.wav"),
    pygame.K_g: pygame.mixer.Sound("sounds/fa#8.wav"),
    pygame.K_h: pygame.mixer.Sound("sounds/sol#8.wav"),
    pygame.K_j: pygame.mixer.Sound("sounds/la#8.wav"),
}

nomes_notas = {         # Dict para adicionar as notas na variável "sequencia" quando as teclas forem pressionadas
    pygame.K_z: "do",
    pygame.K_x: "re",
    pygame.K_c: "mi",
    pygame.K_v: "fa",
    pygame.K_b: "sol",
    pygame.K_n: "la",
    pygame.K_m: "si",

    pygame.K_s: "do#",
    pygame.K_d: "re#",
    pygame.K_g: "fa#",
    pygame.K_h: "sol#",
    pygame.K_j: "la#",
}

nomes_exibicao = {
    "do": "Dó",
    "do#": "Dó#",
    "re": "Ré",
    "re#": "Ré#",
    "mi": "Mi",
    "fa": "Fá",
    "fa#": "Fá#",
    "sol": "Sol",
    "sol#": "Sol#",
    "la": "Lá",
    "la#": "Lá#",
    "si": "Si",

    "do8": "^DÓ^",
    "do#8": "^DÓ#^",
    "re8": "^RÉ^",
    "re#8": "^RÉ#^",
    "mi8": "^MI^",
    "fa8": "^FÁ^",
    "fa#8": "^FÁ#^",
    "sol8": "^SOL^",
    "sol#8": "^SOL#^",
    "la8": "^LÁ^",
    "la#8": "^LÁ#^",
    "si8": "^SI^",
}