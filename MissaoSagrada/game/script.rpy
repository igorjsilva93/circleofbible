# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    # Definindo cenas (backgrounds)
    image black = "#000000"  # Tela preta simples
    image darkness = "images/Genesis/darkness.png"  # Caminho para o arquivo
    image light = "images/Genesis/light.png"
    image brighter_light = "images/Genesis/brighter_light.png"
    image sky = "images/Genesis/sky.jpg"
    image dry_land = "images/Genesis/dry_land.png"
    image stars = "images/Genesis/stars.jpg"
    image plants = "images/Genesis/plants.jpg"
    image ocean_animals = "images/Genesis/ocean_animals.png"
    image land_animals = "images/Genesis/land_animals.jpg"
    image all_creation = "images/Genesis/all_creation.jpeg"


    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.

    # Definindo os personagens
    define narrador = Character('Narrador', color="#FFFFFF")
    define deus = Character('Deus', color="#FFD700")
    image deus_sorrindo = "images/personagens/God.png"  # Nome do arquivo da imagem

    # Início da cena
    image cena1_ceuEstrelas = "images/Genesis/cena1_estrelas.jpeg"

    # Configurando o fundo inicial
    scene black with fade
    show deus_sorrindo at center with dissolve

    # Primeira fala de Deus
    deus "No princípio, Eu criei os céus e a terra."

    # Trevas e Espírito
    scene darkness:
        zoom 4
    show deus_sorrindo at center with fade
    deus "A terra estava sem forma e vazia; havia trevas sobre o abismo..."
    deus "...e o Meu Espírito se movia sobre a face das águas."

    # Primeiro dia
    scene light:
        zoom 1.3
    deus "Haja luz!"
    scene brighter_light with fade:
        zoom 2.3
    narrador "E houve luz."
    show deus_sorrindo at center with fade
    deus "A luz é boa. Vou separá-la das trevas."
    narrador "Deus chamou a luz de Dia e as trevas de Noite. Assim foi o primeiro dia."

    # Segundo dia
    scene sky:
        zoom 1.3
    show deus_sorrindo at center with fade
    deus "Haja uma expansão no meio das águas, para separá-las."
    narrador "E assim Deus criou os céus, separando as águas acima e abaixo."
    deus "Chamarei esta expansão de Céus."
    narrador "Assim foi o segundo dia."

    # Terceiro dia
    scene dry_land:
        zoom 3
    show deus_sorrindo at center with dissolve
    deus "Ajuntem-se as águas num só lugar, e que apareça a terra seca."
    narrador "Deus chamou a terra seca de Terra, e as águas de Mares. E viu que era bom."
    deus "Agora, a Terra produzirá erva verde, plantas que deem sementes, e árvores frutíferas."
    scene plants:
        zoom 3
    narrador "E assim aconteceu. Foi o terceiro dia."

    # Quarto dia
    scene stars:
        zoom 2.6
    show deus_sorrindo at center with dissolve
    deus "Haja luminares no céu para separar o dia e a noite!"
    narrador "Deus fez o sol para governar o dia, a lua para governar a noite, e também as estrelas."
    deus "Eles servirão como sinais para marcar dias e anos."
    narrador "Assim foi o quarto dia."

    # Quinto dia
    scene ocean_animals:
        zoom 3
    show deus_sorrindo at center with dissolve
    deus "Que as águas se encham de criaturas viventes, e que aves voem pelo céu!"
    narrador "Deus criou os peixes, as grandes baleias, e todas as aves, e viu que era bom."
    deus "Frutifiquem e multipliquem-se nas águas e na terra."
    narrador "Assim foi o quinto dia."

    # Sexto dia
    scene land_animals:
        zoom 1.5
    show deus_sorrindo at center with dissolve
    deus "Que a terra produza criaturas viventes: gado, répteis e animais selvagens."
    narrador "E assim foi. Deus viu que era bom."

    # Criação do homem
    show deus_sorrindo at center with dissolve
    deus "Façamos o homem à nossa imagem, conforme a nossa semelhança."
    narrador "E assim Deus criou o homem e a mulher, abençoando-os para frutificarem e multiplicarem-se na terra."
    deus "Vocês dominarão os peixes, as aves e todos os animais da terra."

    # Encerramento
    scene all_creation:
        zoom 0.44
    narrador "Deus viu tudo o que havia feito, e era muito bom."
    narrador "E assim foi o sexto dia."
    show deus_sorrindo at center with dissolve
    deus "Agora vou descansar no sétimo dia."



    # This ends the game.

    return
