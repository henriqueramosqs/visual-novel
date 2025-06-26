# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define renata = Character("Renata")
define carlos = Character("Carlos")
define diana = Character("Diana")
define camila = Character("Camila")

# The game starts here.

label start:

    $ privacidade = 0
    $ responsabilidade_social = 0
    $ integridade = 0
    $ inclusao = 0
    $ responsabilidade_tecnica = 0
    $ consciencia_ambiental = 0
    $ respeito_na_empresa = 0

    scene office_morning with fade

    "Lucas chega ao escritório para seu primeiro dia liderando o projeto InsightPro."
    "Na sala de reuniões, Renata, Carlos e Diana estão reunidos."

    show renata
    renata "Gente, precisamos lançar a funcionalidade de predição essa semana. Se entregarmos a tempo, ganhamos visibilidade no app."

    show carlos
    carlos "Temos dados anônimos suficientes. Dá pra usar sem pedir permissão."

    show diana
    diana "Mas o aviso de privacidade não fala nada disso. Pode ser problemático."

    "O que Lucas propõe como próximo passo?"
    menu:
        "Versão reduzida da coleta, revisar depois":
            $ responsabilidade_tecnica += 10
            $ responsabilidade_social -= 10
            "Lucas sugere uma versão mais segura para não atrasar a entrega."

        "Consultar comitê de ética antes de usar os dados":
            $ integridade += 15
            $ responsabilidade_social += 15
            "Lucas propõe uma consulta ética antes de seguir."

        "Usar os dados anônimos e entregar logo":
            $ privacidade -= 20
            $ integridade -= 10
            "Lucas decide usar os dados mesmo com dúvidas legais."

        "Exibir banner explicativo sem atrasar entrega":
            $ privacidade += 10
            $ responsabilidade_tecnica += 5
            $ respeito_na_empresa += 10
            "Lucas propõe transparência mínima para mitigar o impacto."

    scene slack_alert with dissolve

    "Mais tarde, um alerta mostra que dados de usuários foram expostos internamente."

    show carlos
    carlos "Corrigi tudo. Melhor não criar alarde."

    show camila
    camila "Tudo certo com a privacidade do projeto, Lucas?"

    "Como Lucas responde?"
    menu:
        "Conta o ocorrido a Camila":
            $ integridade += 20
            $ privacidade += 15
            $ respeito_na_empresa += 10
            "Lucas opta por ser transparente com Camila."

        "Fica em silêncio":
            $ integridade -= 15
            $ responsabilidade_social -= 10
            "Lucas decide não comentar nada."

        "Conversa com Carlos e Diana antes de decidir":
            $ integridade += 10
            $ responsabilidade_tecnica += 10
            $ respeito_na_empresa += 10
            "Lucas procura apoio dos colegas antes de agir."

        "Envia aviso no canal geral":
            $ integridade += 5
            $ respeito_na_empresa -= 10
            "Lucas divulga o ocorrido de forma ampla."

    scene corridor_evening with fade

    "Após a daily, Diana parece abatida."

    show diana
    diana "Estou pensando em sair do projeto. Não aguento mais as piadas e a falta de escuta."

    "Como Lucas reage?"
    menu:
        "Promete intervir nas reuniões":
            $ respeito_na_empresa += 15
            $ inclusao += 10
            "Lucas promete agir nas próximas reuniões para apoiá-la."

        "Sugere conversar com Camila":
            $ integridade += 10
            $ respeito_na_empresa += 15
            "Lucas sugere buscar apoio institucional."

        "Diz que apoia qualquer decisão dela":
            $ responsabilidade_social += 10
            "Lucas respeita a decisão pessoal de Diana."

        "Conversa com Renata sobre o clima":
            $ respeito_na_empresa += 20
            $ integridade += 15
            "Lucas decide conversar diretamente com a gerente."

    scene deploy_night with fade

    "Na véspera do lançamento, o modelo preditivo quebra o servidor."

    show carlos
    carlos "Achei um modelo leve num repositório obscuro. Só usar e pronto."

    show renata
    renata "Não me importa de onde veio. Só entregue isso."

    "Decisão final de Lucas"
    menu:
        "Usa o modelo e planeja refatorar depois":
            $ integridade -= 20
            "Lucas decide usar o atalho e refatorar depois."

        "Recusa e reescreve do zero":
            $ integridade += 25
            $ responsabilidade_tecnica += 10
            "Lucas decide refazer tudo, mesmo com esforço extra."

        "Consulta o CTO sobre os riscos":
            $ integridade += 15
            $ respeito_na_empresa += 10
            "Lucas decide envolver a liderança na decisão."

        "Prototipa localmente, mas sem publicar":
            $ responsabilidade_tecnica += 10
            $ respeito_na_empresa += 5
            "Lucas testa localmente, mas não arrisca produção."

    scene office_end with fade

    "Na manhã seguinte, Camila convida Lucas para uma conversa sobre o projeto."
    "Ela comenta que ouviu diferentes visões sobre sua postura e decisões."

    "Seu perfil ético será avaliado com base nas suas escolhas..."

    call mostrar_perfil_etico
    return

label mostrar_perfil_etico:

    scene profile_result with fade

    "Aqui está o perfil ético de Lucas, baseado nas suas decisões ao longo do projeto:"

    "Privacidade e Dados: [privacidade]"
    "Responsabilidade Social: [responsabilidade_social]"
    "Integridade e Honestidade: [integridade]"
    "Inclusão e Equidade: [inclusao]"
    "Responsabilidade Técnica: [responsabilidade_tecnica]"
    "Consciência Ambiental: [consciencia_ambiental]"
    "Respeito na Empresa: [respeito_na_empresa]"

    "Obrigado por jogar 'Código Fonte: Decisões'. Reflita sobre as escolhas que fez."

    return
