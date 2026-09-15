"""Jogo de aventura com uma floresta encantada, uma caverna, uma trilha e uma cabana.
Adicionei finais diferentes, incluindo vitórias e derrotas, para tornar cada escolha importante e incentivar outras pessoas a jogar novamente."""

def jogo_aventura():
    print("--- O MISTÉRIO DA FLORESTA ENCANTADA ---")
    print("Você acorda na entrada de uma floresta misteriosa com apenas uma lanterna.")
    
    # NIVEL 1: 3 escolhas possíveis
    escolha1 = input("Você deseja entrar na CAVERNA, seguir pela TRILHA ou investigar a CABANA? ").strip().upper()

    if escolha1 == "CAVERNA":
        print("\nVocê entra na caverna escura e ouve um ruído estranho vindo do fundo.")
        
        # NIVEL 2 (Caverna): 2 escolhas
        escolha2 = input("Você decide ACENDER a lanterna para ver melhor ou CORRER de volta? ").strip().upper()
        
        if escolha2 == "ACENDER":
            print("\nA luz revela um dragão adormecido sobre um monte de moedas de ouro!")
            
            # NIVEL 3 (Caverna -> Acender): 2 escolhas
            escolha3 = input("Você quer PEGAR o ouro ou SAIR de mansinho? ").strip().upper()
            
            if escolha3 == "PEGAR":
                print("\n[FIM 1] O dragão acorda com o barulho e o transforma em cinzas! Fim de jogo.")
            elif escolha3 == "SAIR":
                print("\n[FIM 2] Você escapa ileso e descobre que a verdadeira riqueza é continuar vivo. Vitória!")
            else:
                print("\n[Opção Inválida] Você hesitou demais, o dragão acordou e te devorou.")

        elif escolha2 == "CORRER":
            print("\nVocê corre desesperadamente para fora e tropeça em um buraco escondido.")
            
            # NIVEL 3 (Caverna -> Correr): 2 escolhas
            escolha3 = input("Você tenta ESCALAR para fora ou GRITAR por socorro? ").strip().upper()
            
            if escolha3 == "ESCALAR":
                print("\n[FIM 3] Com muito esforço você consegue sair do buraco e voltar em segurança para casa. Vitória!")
            elif escolha3 == "GRITAR":
                print("\n[FIM 4] Um bando de lobos escuta seus gritos e se aproxima... Fim de jogo.")
            else:
                print("\n[Opção Inválida] Você ficou travado de medo e ninguém veio te resgatar.")
                
        else:
            print("\n[Opção Inválida] Enquanto você pensava no que fazer, a entrada da caverna desmoronou!")

    elif escolha1 == "TRILHA":
        print("\nVocê caminha pela trilha e encontra um rio com uma ponte de madeira bastante antiga.")
        
        # NIVEL 2 (Trilha): 2 escolhas
        escolha2 = input("Você prefere ATRAVESSAR a ponte ou NADAR pelo rio? ").strip().upper()
        
        if escolha2 == "ATRAVESSAR":
            print("\nA ponte rangem a cada passo e você chega ao meio dela.")
            
            # NIVEL 3 (Trilha -> Atravessar): 2 escolhas
            escolha3 = input("Você decide CORRER para terminar rápido ou ANDAR devagar? ").strip().upper()
            
            if escolha3 == "CORRER":
                print("\n[FIM 5] As tábuas quebraram com seu impacto e você caiu no abismo! Fim de jogo.")
            elif escolha3 == "ANDAR":
                print("\n[FIM 6] Você cruza a ponte com cuidado e encontra o caminho para a cidade sagrada. Vitória!")
            else:
                print("\n[Opção Inválida] Você ficou parado na ponte até que uma ventania a derrubou.")

        elif escolha2 == "NADAR":
            print("\nVocê pula na água fria. A correnteza está surpreendentemente forte.")
            
            # NIVEL 3 (Trilha -> Nadar): 2 escolhas
            escolha3 = input("Você decide MERGULHAR para fugir da força da água ou BOIAR para economizar energia? ").strip().upper()
            
            if escolha3 == "MERGULHAR":
                print("\n[FIM 7] Você encontra um túnel subaquático que o leva para uma câmara secreta cheia de joias! Vitória!")
            elif escolha3 == "BOIAR":
                print("\n[FIM 8] A correnteza te leva para uma cachoeira perigosa. Fim de jogo.")
            else:
                print("\n[Opção Inválida] Você engoliu água por não tomar uma decisão e se afogou.")
                
        else:
            print("\n[Opção Inválida] Você demorou a escolher e a noite caiu, deixando você perdido na trilha.")

    elif escolha1 == "CABANA":
        print("\nVocê chega a uma velha cabana abandonada com a porta entreaberta.")
        
        # NIVEL 2 (Cabana): 2 escolhas
        escolha2 = input("Você quer ENTRAR na cabana ou ESPIAR pela janela? ").strip().upper()
        
        if escolha2 == "ENTRAR":
            print("\nDentro da cabana há um livro antigo brilhando em cima da mesa.")
            
            # NIVEL 3 (Cabana -> Entrar): 2 escolhas
            escolha3 = input("Você escolhe LER o livro ou QUEIMAR o livro? ").strip().upper()
            
            if escolha3 == "LER":
                print("\n[FIM 9] O livro era um grimório de feitiços que concede poderes mágicos! Vitória!")
            elif escolha3 == "QUEIMAR":
                print("\n[FIM 10] Ao queimar o livro, uma maldição se liberta e incendiará toda a floresta! Fim de jogo.")
            else:
                print("\n[Opção Inválida] Você hesitou ao tocar no livro e uma armadilha foi disparada.")

        elif escolha2 == "ESPIAR":
            print("\nVocê olha pela janela suja e vê uma figura misteriosa preparando uma poção.")
            
            # NIVEL 3 (Cabana -> Espiar): 2 escolhas
            escolha3 = input("Você decide BATER na porta para se apresentar ou FUGIR em silêncio? ").strip().upper()
            
            if escolha3 == "BATER":
                print("\n[FIM 11] A figura era um bruxo bondoso que te oferece comida e um mapa seguro. Vitória!")
            elif escolha3 == "FUGIR":
                print("\n[FIM 12] Ao fugir, você faz barulho nos galhos secos e a figura misteriosa te lança um feitiço do sono. Fim de jogo.")
            else:
                print("\n[Opção Inválida] A figura viu sua sombra na janela e te capturou.")
                
        else:
            print("\n[Opção Inválida] Você vacilou na porta e uma matilha de criaturas cercou a cabana.")

    else:
        print("\n[Opção Inválida] Essa não era uma das caminhos disponíveis. Você ficou parado até a escuridão te consumir!")

# Executa o jogo
jogo_aventura()