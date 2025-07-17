# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define thiago = Character("Thiago", color="#c8ffc8")
define alissa = Character("Alissa", color="#ffc8c8")
define carlos = Character("Carlos", color="#c8c8ff")
define maria = Character("Maria", color="#ffc8ff")
define wellington = Character("Wellington", color="#ffff99")
define julio = Character("Julio", color="#ffff99")
define leticia = Character("Letícia", color="#ffff99")
define recepcionista = Character("Recepcionista", color="#cccccc")


transform scale:
    zoom 0.3

transform scale2:
    zoom 0.7
# The game starts here.
label start:

    $ bem_estar = 50
    $ privacidade = 50
    $ responsabilidade_social = 50
    $ integridade = 50
    $ inclusao = 50
    $ respeito_com_equipe = 5
    $ respeito_com_chefe = 5
    $ respeito_na_empresa = 5

    $ pontuacoes = {
        "Bem estar": bem_estar,
        "Respons. Social": responsabilidade_social,
        "Integridade": integridade,
        "Inclusão": inclusao,
        "Resp. com Equipe": respeito_com_equipe,
        "Resp. com Chefe": respeito_com_chefe,
        "Resp. com Empresa": respeito_na_empresa,
    }

    scene bg_office with fade

    # Dia 0 - Contexto
    "Thiago era programador pleno numa empresa de médio porte, onde nunca se sentiu realizado profissionalmente."
    "Recentemente, ele decidiu dar um passo ousado: aceitou uma vaga júnior na GigaHard - a empresa dos seus sonhos desde a época da faculdade."
    "Apesar da queda na senioridade e na remuneração, Thiago viu na GigaHard uma oportunidade única:  sempre admirou os produtos da empresa e sabe que, além da boa  reputação, ela oferece ótimas perspectivas de crescimento e bons salários no longo prazo."
    "Com este contexto, Thiago está determinado (e um pouco pressionado) a ascender profissionalmente e conquistar seu espaço na  GigaHard. Para isso, ele planeja ser participativo e empenhado nas atividades dentro da GigaHard"

    # Dia 1
    scene bg_reception with fade
    "Dia 1"

    show thiago normal at left
    thiago "Olá… meu nome é Thiago. Recebi um e-mail de confirmação dizendo que hoje seria meu primeiro dia de trabalho."

    show alissa normal at right
    alissa "Oi… eu sou a Alissa. Também recebi um e-mail assim."

    show recepcionista normal at center
    recepcionista "Ah, claro! Vocês devem fazer parte da nova leva de contratados. Vou ligar para o andar de cima, alguém já deve vir recebê-los."

    hide recepcionista
    show carlos normal at center
    carlos "Olá! Meu nome é Carlos. Provavelmente serei o gerente de vocês. Gostariam de conhecer o prédio?"

    thiago "Sim, claro."
    alissa "Sim!"

    hide carlos
    hide thiago
    hide alissa

    scene bg_office_tour with fade
    show thiago "Uau… a estrutura aqui é realmente impressionante."

    show carlos normal at center
    carlos "Então… vocês já devem ter ouvido um pouco sobre a área de atuação. Foram designados para trabalhar no InsightPro, uma ferramenta que pretende reunir dados de várias fontes - redes sociais, marketplaces, indicadores econômicos, entre outros - para oferecer insights a pequenos comércios."
    carlos "Como devem saber, nossa concorrente, a Gluglu, anunciou há alguns meses o desenvolvimento de uma ferramenta semelhante, com previsão de lançamento até novembro deste ano."
    carlos "Estamos desconfiados de um possível vazamento de informações. Por isso, precisamos acelerar nosso processo."
    carlos "Queremos lançar algo melhor, e antes de novembro. Essa urgência motivou a contratação de vocês dois e de muitos outros profissionais."

    show thiago normal at left
    thiago "Entendi… o clima deve estar bem intenso aqui…"

    carlos "Ainda não começamos os trabalhos, mas acredito que em breve as coisas estarão bem intensas sim."

    show alissa worried at right
    alissa "..."

    carlos "Bem… deixe-me apresentar os colegas de squad de vocês."

    show maria normal at scale
    carlos "Essa é a Maria, a funcionária mais antiga e esforçada do squad."
    maria "Prazer, eu sou a Maria."

    hide maria
    show wellington normal at scale
    carlos "E este é o Wellington, também trabalha há uns anos na empresa."
    wellington "Oi, eu sou o Wellington."

    hide wellington
    carlos "Bem, para hoje devemos focar em buscar as nossas fontes de dados. Foquem em confiabilidade. Precisamos de dados robustos e de boa qualidade."
    carlos "Amanhã, nesta mesma sala, às 16h teremos nossa primeira reunião."

    "Todos: Ok"

    # Dia 2
    scene bg_meeting_room with fade
    "Dia 2"

    show carlos normal at center
    carlos "Então… todos trouxeram as fontes de dados que se comprometeram a trazer?"

    show thiago normal at left
    thiago "Encontrei uma fonte de dados financeiros mantida por uma empresa privada. O acesso é pago, mas parece bastante promissora."

    show alissa normal at right
    alissa "Eu achei duas fontes… não são muito abrangentes, mas eu achei os dados bem estruturados e robustos."

    show wellington normal at scale
    wellington "Consegui encontrar uma API feita por uma associação de produtores rurais. Esses dados são ótimos, oferecem informações únicas sobre um nicho que é muito importante para nós."
    wellington "Estarmos de posse desses dados nos colocaria em uma posição muito privilegiada, mas o problema é que não encontrei a licença atrelada ao serviço."
    wellington "Temo que, se entrarmos em contato diretamente, por se tratar de um produto com fins lucrativos, eles possam negar o acesso."

    hide wellington
    carlos "E o que vocês acham que devemos fazer com essa API? Lembrem-se: se não tivermos acesso a esses dados, e a Gluglu conseguir, ficaremos em desvantagem."

    menu:
        "Mesmo sem encontrar uma licença explícita, a organização pode ter diretrizes internas sobre o uso da API. O correto é entrar em contato antes de utilizar qualquer dado. Enquanto não houver autorização formal, não devemos acessar nem armazenar essas informações":
            $ integridade += 10
            $ respeito_com_equipe -= 10

        "A API está aberta, e conseguimos baixar os dados sem obstáculos. Podemos coletar tudo agora e só depois perguntar sobre a licença. Se houver uma negativa futura, ao menos já teremos uma base histórica valiosa salva para trabalhar.a":
            $ integridade -= 5
            $ respeito_com_equipe += 5
            "Thiago sugere coletar os dados primeiro para garantir uma base histórica valiosa, independentemente da licença."

        "Enquanto não houver uma restrição clara, devemos aproveitar. Se deixarmos passar, a Gluglu pode sair na frente. Vamos extrair o máximo possível agora - depois vemos como lidar com a parte legal.":
            $ integridade -= 10
            $ respeito_com_chefe += 5

    hide thiago
    hide alissa
    show maria normal at center
    maria "Consegui montar um script simples para extrair dados das conversas entre usuários de outros aplicativos nossos."
    maria "Ainda é algo básico, mas no futuro dá para otimizar e estruturar melhor. Como se trata de um chat, conseguimos informações praticamente em tempo real."

    carlos "Esses dados parecem extremamente valiosos, Maria. Excelente trabalho. Como sempre, você se destaca nas entregas."

    show alissa worried at right
    alissa "Mas… os usuários desses apps sabem que as conversas deles podem ser utilizadas para treinar modelos como o do InsightPro?"

    maria "Algo nesse sentido está mencionado no rodapé dos termos de uso, mas é um texto bem genérico. Não tenho certeza se está claro para os usuários."

    menu:
        "Mesmo que esteja nos termos de uso, se a informação não estiver clara e destacada, não é ético usar esses dados. Precisamos suspender o uso até termos um parecer jurídico e uma política de transparência mais explícita.":
            $ privacidade += 10
            $ respeito_com_equipe -= 10
            $ respeito_com_chefe -= 10

        "Se está nos termos, temos respaldo legal. Podemos seguir usando os dados, mas deveríamos considerar rever os termos e criar uma política mais clara para o futuro":
            $ privacidade -= 5
            $ respeito_com_equipe += 5
            $ respeito_com_chefe += 5

        "Os dados estão acessíveis, e são valiosos demais para ignorar. Podemos continuar usando normalmente - a maioria dos usuários não se importa ou nem lê os termos de uso.":
            $ integridade -= 5
            $ privacidade -= 10
            $ respeito_com_equipe += 5
            $ respeito_com_chefe += 5

        "E se lançássemos uma campanha de comunicação explicando como os dados são usados e dando opção de opt-out? Isso seria trabalhoso, mas poderia até melhorar a imagem do produto, apesar de provavelmente, perdemos acesso a parte desses dados":
            $ integridade += 10
            $ privacidade += 5


    # Dias posteriores - Trabalho intenso
    scene bg_office with fade
    "Desde a coleta inicial dos dados, dias se passaram, com todos os membros do squad trabalhando intensamente…"

    # Durante a reunião
    scene bg_meeting_room with fade
    "Durante a reunião"

    show alissa worried at right
    alissa "Thiago… acabei de perceber que o último PR que você subiu pro repositório aberto estava com dados reais no commit."

    show maria shocked at center
    maria "Sério? Informações pessoais de centenas de usuários estão expostas!"

    show carlos serious at left
    carlos "Precisamos agir rápido, mas se alguém perguntar, melhor dizer que foi uma falha genérica de configuração. Se gerarmos pânico interno, nosso squad inteiro perderá credibilidade com a diretoria."

    "O que fazer após o vazamento acidental?"
    menu:
        "Entendo, Carlos…Vou seguir sua orientação, minimizar o ocorrido para a diretoria e apagar os rastros":
            $ privacidade -= 20
            $ integridade -= 10

        "Acho importante reportar imediatamente o erro ao setor jurídico e de compliance da empresa. Isso pode gerar represálias mas devemos estar abertos a isso":
            $ privacidade += 15
            $ respeito_com_equipe -= 10
            $ respeito_com_chefe -= 10
            $ respeito_na_empresa +=5

        "Vou tentar corrigir o problema, mas só falarei do assunto com algum superior se me perguntarem":
            $ integridade -= 5
            $ privacidade -= 5
            $ respeito_com_equipe += 5
            $ respeito_com_chefe += 5

        "Posso tentar entrar em contato com os usuários afetados, mesmo sem aval oficial":
            $ privacidade += 5
            $ respeito_na_empresa -=10

    maria "Ah, e antes que eu esqueça, tem outro ponto. Revendo os testes, notei que o nosso algoritmo entrega resultados menos precisos e com menor relevância para usuários da região Norte. Ainda não descobri por quê, mas me parece algo estrutural nos dados de entrada."

    show wellington normal at scale
    wellington "Você não acha isso problemático?"

    maria "Tecnicamente sim, mas é uma região que representa uma fatia bem pequena da nossa base de clientes. Não sei se vale a pena atrasar o projeto por isso."

    carlos "O tempo está contra nós. Precisamos decidir rápido o que fazer com esse modelo."

    "O que sugerir que seja feito?"
    menu:
        "Podemos lançar o modelo como está e planejar melhorias depois":
            $ integridade -= 10
            $ respeito_com_equipe += 5

        "Acho que devemos reportar o problema para os superiores, e se sentirmos que esse problema vai demorar para ser resolvido, devemos sugerir o adiamento":
            $ integridade += 10
            $ respeito_com_chefe -= 10
            $ respeito_com_equipe -= 10
            $ respeito_na_empresa -= 10

        "Podemos tentar 'compensar' o viés manualmente, ajustando os pesos de forma empírica":
            $ integridade -= 5

        "Podemos tentar lançar aquela versão antiga que fizemos, que era menos precisa mas não tinha vieses tão gritantes":
            $ integridade += 5
            $ respeito_com_equipe -= 5

    carlos "Certo. Ainda temos muito a fazer nesta sprint. Thiago, além de lidar com o problema do vazamento e revisar a parte de análise preditiva, vou precisar que você contribua com a documentação da nossa API."

    show thiago stressed at right
    thiago "Carlos, eu entendo, mas estou acumulando tarefas das duas últimas sprints. Nem consegui revisar os testes que ficaram pendentes da semana passada…"

    carlos "Infelizmente, o cronograma está apertado. Contamos com você."

    menu:
        "Okay… Assim farei, posso trabalhar até tarde por uns dias":
            $ bem_estar-=15
            $ respeito_com_chefe += 10
            $ respeito_com_equipe += 5

        "Carlos, eu entendo que o cronograma está apertado, mas infelizmente eu estou sobrecarregado. O que acha de re-priorizar as tarefas então?":
            $ respeito_com_chefe -= 10
            $ bem_estar+=5

        "Certo, chefe (depois tentarei passar a tarefa discretamente pro Wellington)":
            $ integridade -= 10
            $ respeito_com_equipe -= 5

        "Certo chefe (semana que vem entregarei apenas uma versão parcial da documentação)":
            $ respeito_com_chefe -= 5
            $ integridade -= 5
            $ respeito_com_equipe -= 10

    # Happy Hour
    scene bg_bar with fade
    carlos "De fato eu ando percebendo que todos estão cansados. O que acham de sairmos para um happy hour quinta, para distrairmos do trabalho?"

    "Todos: Vamos!!"

    "No happy hour"

    show julio normal at left
    julio "Opa, eai Thiago!"

    show thiago normal at right
    thiago "Júlio! Como está! Que coisa boa te ver aqui! Veio com os amigos?"

    julio "Não, vim com o pessoal do trabalho."

    thiago "Que coincidência, eu também! Vou ali me sentar à mesa, já conversamos!"

    hide julio
    hide thiago

    show wellington normal at left
    wellington "Acho que o pessoal da Gluglu também está fazendo happy hour aqui hoje. Reconheço aquele rapaz sentado na ponta, trabalhamos juntos no passado."

    show maria normal at center
    maria "O Thiago também conhece alguém ali pelo visto."

    show thiago normal at right
    thiago "Ah sim… é o Júlio, estudamos juntos na faculdade."

    wellington "Imagina a vantagem se soubéssemos o estado do app que eles estão fazendo para concorrer com o InsightPro… Uma conversa entre amigos... não custa, né?"

    menu:
        "Ah.. não acho certo usar uma relação pessoal para obter vantagem competitiva. Contem comigo pra melhorar o InsightPro do jeito certo.":
            $ integridade += 10
            $ respeito_com_equipe -= 10

        "Posso puxar assunto e tentar entender o que ele anda fazendo... se ele comentar algo naturalmente, não é problema nosso, né?":
            $ integridade -= 5
            $ respeito_com_equipe += 5

        "Vou conversar com ele depois e ver se consigo algo. Mas isso fica só entre nós.":
            $ integridade -= 15
            $ respeito_com_equipe += 10

        "hahaha….essa batata está boa, né? (jamais vou fazer isso)":
            "Thiago desconversa e evita completamente a situação."

    # Dia 20 - Nova integrante
    scene bg_meeting_room with fade
    "Dia 20"

    show carlos normal at center
    carlos "Pessoal, essa é a Letícia. Ela foi realocada de outro time e vai trabalhar com a gente a partir de hoje."

    show leticia normal at left
    leticia "Oi, gente. Prazer em conhecer vocês. Estou animada pra contribuir no que puder."

    "Todos: Prazer, Letícia"

    carlos "A Letícia tem bastante experiência com engenharia de dados, então gostaria que vocês se organizassem e atribuíssem a ela alguma tarefa da sprint atual para que ela possa começar a se integrar."

    show wellington normal at right
    wellington "(sussurrando) Trabalhei com a Letícia num projeto no passado. Ela é gente boa, mas tem algumas limitações… é PcD, e às vezes leva mais tempo nas entregas."

    show maria normal at scale
    maria "Logo agora que estamos com prazos tão apertados? Talvez pudéssemos passar para ela a refatoração das páginas da interface do usuário. Não é bem da área dela, mas pelo menos se atrasar, não afeta tanto o cronograma."

    show alissa normal at scale
    alissa "Também temos que terminar o pipeline da ingestão de dados externos, que é algo mais voltado para a área de atuação dela."

    menu:
        "A Letícia tem experiência com engenharia de dados. Vamos colocá-la no pipeline, onde ela pode mostrar seu valor de verdade.":
            $ inclusao += 15
            $ integridade += 5
            $ respeito_com_equipe -= 5

        "Acho melhor ela começar pela interface. Não é a área dela, mas evita riscos enquanto avaliamos o ritmo dela.":
            $ inclusao -= 15
            $ respeito_com_equipe += 5
        "Podemos passar a documentação de pipeline. Assim ela participa, mas sem afetar código de produção.":
            $ inclusao -= 10
            $ integridade -= 10
            $ respeito_com_equipe += 5

        "Talvez devêssemos expor a situação dos prazos para ela e perguntar diretamente para ela qual tarefa ela prefere. Assim a gente respeita o tempo e o perfil dela.":
            $ inclusao += 10
            $ integridade += 5

    # Finalização do projeto
    scene bg_office with fade
    "Semanas de trabalho intenso chegaram ao fim. Com o código estabilizado, as funcionalidades testadas e a interface final aprovada, o InsightPro estava finalmente pronto para ser entregue. A equipe estava exausta - mas também orgulhosa. Agora, restava apresentar os resultados, escrever os relatórios finais… e lidar com os detalhes que não apareciam nos dashboards."

    show carlos normal at center
    carlos "Gente, estamos prestes a receber o bônus de performance. Cumprimos os prazos, entregamos tudo o que estava previsto… mas temos que garantir que o relatório esteja 'alinhado' com isso."

    show wellington normal at left
    wellington "Alinhado como?"

    carlos "Não precisamos falar tudo sobre os testes de viés regional? A gente só começou a tratar isso, então não precisa entrar nos detalhes. Um relatório técnico demais pode dar margem para problemas com a diretoria."

    show maria normal at right
    maria "Mas se formos muito vagos, não soa como manipulação?"

    carlos "Nada disso. Só precisamos focar no que funcionou. O objetivo é garantir o bônus de todos aqui."

    "Como agir diante da proposta de omissão no relatório técnico?"
    menu:
        "Devemos incluir os pontos críticos, mesmo que isso comprometa o bônus. A transparência importa.":
            $ integridade += 10
            $ respeito_com_chefe -= 10
            $ respeito_com_equipe -= 5
            $ respeito_ne_empresa +=10

        "Vamos citar os problemas, mas de forma bem superficial. Assim mostramos algo sem criar alarde.":
            $ integridade += 5
            $ respeito_com_equipe += 5

        "Concordo com Carlos. O foco é a entrega. Ser transparente demais pode sair caro.":
            $ integridade -= 10
            $ respeito_com_chefe += 10
            $ respeito_com_equipe += 5

    # Apresentação para diretores
    scene bg_boardroom with fade
    "Dias depois, durante a apresentação oficial do projeto para os diretores da GigaHard, Carlos conduz a reunião com entusiasmo, destacando os pontos fortes da entrega e agradecendo nominalmente a alguns membros da equipe."

    show carlos presenting at center
    carlos "...E o sistema de recomendação de fontes, integrado à API de parceiros, foi brilhantemente construído. Wellington foi peça-chave nessa parte."

    show alissa frustrated at right
    alissa "Poxa…isso foi literalmente minha feature. Foi muito trabalhoso fazer essa parte e ele sabe disso."

    menu:
        "Na hora das perguntas, destaco que você cuidou da arquitetura, Alissa. É o certo a fazer.":
            $ integridade += 10
            $ respeito_com_equipe += 10
            $ respeito_com_chefe -= 5

        "Depois eu converso com Carlos e sugiro que ele corrija a informação no Slack.":
            $ integridade += 5
            $ respeito_com_equipe += 5

        "Vamos deixar essa passar, Alissa. Não é o melhor momento para criar desconforto com a diretoria.":
            $ integridade -= 10
            $ respeito_com_equipe -= 5

    # Solicitações externas
    scene bg_meeting_room with fade
    "Com o InsightPro oficialmente lançado, a equipe recebe feedbacks positivos, propostas de integração… e algumas solicitações inesperadas."

    carlos "Surgiram consultas externas inesperadas sobre o uso da plataforma. Algumas prefeituras estão interessadas, e também chegou um pedido informal de um partido político - querem testar o InsightPro para levantar tendências de opinião pública em campanhas eleitorais."

    show maria worried at left
    maria "Isso é bem diferente do que pensamos no início. Não sei se me sinto confortável com esse tipo de uso."

    show wellington concerned at right
    wellington "Tecnicamente, o sistema está pronto pra qualquer domínio. Mas usar isso para fins eleitorais…não sei se esse é o mais correto a se fazer. E se ele for usado para manipulação?"

    carlos "Olha… não somos responsáveis pelo uso. Entregamos a ferramenta. Cabe a outras áreas decidirem."

    menu:
        "Devemos estabelecer diretrizes claras de uso ético e sugerir a criação de restrições de acesso.":
            $ responsabilidade_social += 10
            $ integridade += 5
            $ respeito_com_chefe -=5

        "Podemos liberar o uso, desde que assinem termos deixando claro que é por conta e risco deles.":
            $ integridade += 5
            $ respeito_com_chefe += 5

        "Se querem usar para fins políticos, que usem. Nosso trabalho está entregue.":
            $ responsabilidade_social -= 10
            $ respeito_com_chefe += 10
    
    scene bg_office with fade
    "Fim da jornada de Thiago na GigaHard. Suas escolhas moldaram não apenas sua carreira, mas também o impacto ético do projeto InsightPro."


    # Mostrar pontuações finais
    "Suas pontuações atuais:"
    "Bem estar: [bem_estar]"
    "Responsabilidade Social [responsabilidade_social]"
    "Privacidade: [privacidade]"
    "Integridade: [integridade]"
    "Inclusão: [inclusao]"
    "Respeito com a Equipe: [respeito_com_equipe]"
    "Respeito com o Chefe: [respeito_com_chefe]"
    "Respeito na empresa: [respeito_na_empresa]"



   

    return
