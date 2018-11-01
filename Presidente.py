import random
import os
import sys
import time

propbolso = ['1 Acabar com o Ministério das Cidades e dar dinheiro direto para as prefeituras, para reduzir riscos de corrupção.',
             '2 Fusão dos ministérios da agricultura com o meio ambiente e fim do ministério da Segurança Pública,\n'
             'que voltaria a ter status de secretaria, no âmbito do Ministério da Justiça.',
             '3 “ Redefinição” dos direitos humanos, em que o ministério funcionaria como secretaria, e agiria com uma \n'
             'orientação mais voltada à defesa de policiais.',
             '4 Endurecimento com as relações comerciais com a China e, aumento da parceria com Israel.',
             '5 Esforço para aprovar no Congresso o dispositivo do “excludente de ilicitude”, que daria cobertura legal \n'
             'a ações de militares em combate contra o crime.',
             '6 Esforço para aprovar no congresso a redução da maioridade penal para 16 anos.',
             '7 Flexibilizar o Estatuto do Desarmamento e facilitar o porte de arma para o cidadão. ',
             '8 Levar o modelo de escolas militares de sucesso no Brasil para toda a rede de educação pública do País. ',
             '9 Manutenção do tripé macroeconômico (com regime de meta fiscal e de inflação, com câmbio flutuante) e \n'
             'simplificação tributária rumo a um imposto único federal.',]

propmarina = ['10 Plano de retomada econômica centrado nos pilares de superávit primário, câmbio flutuante e regime de \n'
              'metas para inflação, além de autonomia operacional do Banco Central, e investimentos intensivos em \n'
              'inovação, ciência e tecnologia.',
              '11 Reinvenção da educação, “com ensino dinâmico, que atraia os estudantes com metodologias inovadoras e \n'
              'novas tecnologias”. ',
              '12 Não-aumento da carga tributária',
              '13 Simplificação dos tributos',
              '14 Eliminação da regressividade',
              '15 Redução da taxação dos investimentos',
              '16 Transparência e melhor repartição das receitas entre os entes federados.',
              '17 Fortalecimento do SUS, com abertura a uma prestação de serviços que combine órgãos públicos, privados \n'
              'e filantrópicos.']

propalvaro = ['18 Investidas variadas em uma economia forte, como aprovar a Reforma da Previdência, reduzir gastos públicos e controlar a inflação.',
              '19 Capitalizar a Caixa sem recursos do FGTS, criação do “cartão da família” para complementar o Bolsa Família.',
              '20 Criação de um programa de infraestrutura chamado “Brasil Integrado” para reduzir distâncias e melhorar o transporte no país.',
              '21 Programa “Pró-Infância” para destinar vagas em creches particulares para famílias que recebem o Bolsa Família.',
              '22 Programa “Brasil Seguro e Forte” na área de segurança pública, com “cooperação intensiva de inteligência” com os estados.',]


propciro = ['23 Revisão da Reforma da Previdência, adotando um novo modelo de aposentadorias, baseado em capitalização.',
            '24 Plebiscito para revogar a Reforma Trabalhista.',
            '25 Revogação da medida de Teto de Gastos Públicos.',
            '26 Defende a tributação sobre dividendos e lucros de acionistas, aumento do imposto sobre heranças de 8 para \n'
            '24% e corte de 15% nas isenções tributárias, com exceção da Zona Franca de Manaus. ',
            '27 Pretende criar mecanismos para fortalecer a geração de empregos nas áreas da construção civil, serviços e \n'
            'comércio a fim de alavancar a economia brasileira.',
            '28 Interferência nos juros dos bancos públicos para baixar o custo do investimento no país.',
            '29 Atuação do governo federal em “limpar” o nome dos brasileiros endividados no Serviço de Proteção ao Crédito (SPC).',]



proplula = ['30 Ampliar o programa de investimentos públicos, fortalecer os bancos e empresas públicas e a exploração de petróleo do pré-sal.',
            '31 Enfrentar um “referendo revogatório” de medidas adotadas pelo governo de Michel Temer (MDB), como a Reforma da Previdência e a Reforma Tributária.',]

propmerenda = ['32 Pretende criar uma Guarda Nacional, formada por homens que encerrarem o serviço militar obrigatório \n'
               'e não seguirem a carreira, e uma central de inteligência que reúna informações de todos os órgãos públicos.',
               '33 Propõe aumentar o tempo máximo de internação de menores infratores de três para até oito anos.',
               '34 Defende flexibilizar o Estatuto do Desarmamento, para pedir a posse de armas em áreas rurais.',
               '35 Promete incrementar o Bolsa Família e adotar políticas voltadas para os negros e índios, além de \n'
               'estabelecer um pacto nacional voltado para a redução da violência contra idosos, mulheres e o público LGBTI.',
               '36 Também promete zerar o déficit primário até 2020, atraindo capital externo, reduzindo isenções tributárias \n'
               'e aumentando os impostos sobre os mais ricos.',
               '37 Investimento nas regiões Norte e Nordeste do país, abertura do País ao comércio exterior e prioridade \n'
               'nos investimentos em infraestrutura através de parcerias com o setor privado.',]

propboulos = ['38 Pacote de medidas emergenciais para recuperar o emprego e a renda, em que o governo usaria suas reservas \n'
              'internacionais e o compulsório dos bancos (dinheiro, na verdade, dos correntistas) para fazer investimentos \n'
              'públicos que movimentem a economia. ',
              '39 Redução drástica da taxa de juros e controle estatal de câmbio e capitais.',
              '40 Ampliação do crédito para a população com menor renda e pequenos empreendedores, possivelmente por meio de bancos públicos. ',
              '41 Reestatização de “setores estratégicos” (telefonia, energia, abastecimento de água e mineração).',
              '42 E a revogação de todas as reformas do governo Temer: a PEC do Teto de Gastos Públicos, a reforma trabalhista, \n'
              'a lei das terceirizações e a reforma da Previdência (caso venha a ser aprovada).',
              '43 Fortes investimentos sociais.',
              '44 A Lei de Responsabilidade Fiscal também seria revogada para permitir que o Estado fizesse mais investimentos.',]

propdeus = ['45 Defende a privatização da Petrobras, Banco do Brasil e Caixa.',
            '46 É simpático ao programa Bolsa Família. ',
            '47 A favor da Reforma da Previdência e da Reforma Trabalhista, aprovada pelo governo Temer, apesar de achar \n'
            'que pode ser melhorada. ',
            '48 Quando se trata de segurança pública, é a favor da revisão do Estatuto do Desarmamento, visando o direito do cidadão se armar.',
            '49 Vê o congelamento dos gastos públicos de maneira positiva e  defende a simplificação de tributos.']

random.shuffle(propmerenda)
random.shuffle(propbolso)
random.shuffle(propmarina)
random.shuffle(propalvaro)
random.shuffle(propboulos)
random.shuffle(propciro)
random.shuffle(proplula)
random.shuffle(propdeus)

geral = propbolso + propmarina + propalvaro + propboulos + propciro + proplula + propmerenda + propdeus
random.shuffle(geral)

done = 'false'
def animate():
    while done == 'false':
        sys.stdout.write('\rAguardando |')
        time.sleep(0.1)
        sys.stdout.write('\rAguardando /')
        time.sleep(0.1)
        sys.stdout.write('\rAguardando -')
        time.sleep(0.1)
        sys.stdout.write('\rAguardando \\')
        time.sleep(0.1)
        sys.stdout.write('\rAguardando |')
        time.sleep(0.1)
        sys.stdout.write('\rAguardando /')
        time.sleep(0.1)
        sys.stdout.write('\rAguardando -')
        time.sleep(0.1)
        sys.stdout.write('\rAguardando \\')
        time.sleep(0.1)
    sys.stdout.write('\rDone!     ')

def menu():
    print('-' * 130)
    print(f'MENU                                                        LEGENDA\n'
          f'Nota 3 = Grande Progresso                                   ED: Educação e Saúde \n'
          f'Nota 2 = Proposta Boa                                       SEG: Segurança\n'
          f'Nota 1 = Intenção boa, ideia vaga                           DH: Políticas Sociais e Direitos Humanos\n'
          f'Nota 0 = Nenhum impacto ou Não entendi                      ECO: Economia e Emprego\n'
          f'Nota -1 = Impacto negativo, ideia vaga                      POL: Política e Corrupção\n'
          f'Nota -2 = Contra meus interesses como cidadão               MEIO: Política Externa e Meio Ambiente\n'
          f'Nota -3 = Grande retrocesso\n ')


notaciro = 0
notamarina = 0
notaamoedo = 0
notabolso = 0
notaalvaro = 0
notaboulos = 0
notahaddad = 0
notaalckmin = 0


def somatória(geral, contagem, notaciro, notamarina, notaamoedo, notabolso, notaalvaro, notaboulos, notahaddad, notaalckmin, nota):
    if geral[contagem] in propciro:
        notaciro += nota

    if geral[contagem] in propmarina:
        notamarina += nota

    if geral[contagem] in propdeus:
        notaamoedo += nota

    if geral[contagem] in propbolso:
        notabolso += nota

    if geral[contagem] in propalvaro:
        notaalvaro += nota

    if geral[contagem] in propboulos:
        notaboulos += nota

    if geral[contagem] in proplula:
        notahaddad += nota

    if geral[contagem] in propmerenda:
        notaalckmin += nota


def main(geral, notaciro, notamarina, notaamoedo, notabolso, notaalvaro, notaboulos, notahaddad, notaalckmin):
    contagem = 0
    while contagem < len(geral):
        menu()
        print(f'Proposta {contagem+1} de {len(geral)}:\n{geral[contagem]}')
        #nota = int(input("Nota: "))
        nota = random.randint(-3, 3)
        contagem += 1
        os.system("cls")

        if geral[contagem-1] in propciro:
            notaciro += nota

        if geral[contagem-1] in propmarina:
            notamarina += nota

        if geral[contagem-1] in propdeus:
            notaamoedo += nota

        if geral[contagem-1] in propbolso:
            notabolso += nota

        if geral[contagem-1] in propalvaro:
            notaalvaro += nota

        if geral[contagem-1] in propboulos:
            notaboulos += nota

        if geral[contagem-1] in proplula:
            notahaddad += nota

        if geral[contagem-1] in propmerenda:
            notaalckmin += nota


    todos = [notaalvaro, notaamoedo, notaalckmin, notabolso, notaboulos, notaciro, notahaddad, notamarina]
    print(sorted(todos))
    print(f'\nPLACAR:\n'
          f'Meirelles: {notaalvaro}\n'
          f'Amoedo: {notaamoedo}\n'
          f'Alckmin:  {notaalckmin}\n'
          f'Bolsonaro: {notabolso}\n'
          f'Boulos: {notaboulos}\n'
          f'Ciro: {notaciro}\n'
          f'Haddad: {notahaddad}\n'
          f'Marina: {notamarina}\n')

    animate()


main(geral, notaciro, notamarina, notaamoedo, notabolso, notaalvaro, notaboulos, notahaddad, notaalckmin)
done = 'false'
