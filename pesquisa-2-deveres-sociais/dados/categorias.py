# -*- coding: utf-8 -*-
"""Pesquisa 2 — taxonomia dos deveres sociais ensinados por Jesus.

ATENÇÃO: os textos NAA foram transcritos de memória e devem ser conferidos com a edição da SBB.
"""

CATEGORIAS = {
    "ALIM": dict(
        titulo="Alimentar, dar de beber e vestir quem passa necessidade",
        demanda="Dar comida a quem tem fome, água a quem tem sede e roupa a quem está nu; não despedir ninguém em jejum; lembrar que 'os pobres vocês sempre terão'.",
        agrupamento="Reúne o critério do juízo final (Mt 25:35-36,42-43), as ordens 'deem-lhes vocês de comer' (Mt 14:16; Mc 6:37; Lc 9:13), "
                    "a compaixão de Jesus pela multidão faminta (Mt 15:32; Mc 8:2-3), o 'copo de água fria' (Mt 10:42; Mc 9:41), o mordomo que dá "
                    "a ração no tempo certo (Mt 24:45; Lc 12:42) e a mesa aberta aos pobres (Lc 14:13).",
        enfases=["Mt 25:31-46 — juízo das nações", "Mt 14:13-21; Mc 6:30-44; Lc 9:10-17; Jo 6:1-13 — multiplicação dos pães", "Mt 15:32-39; Mc 8:1-9 — segunda multiplicação",
                 "Lc 16:19-31 — rico e Lázaro", "Lc 14:12-14 — convide os pobres", "Mc 14:7; Mt 26:11; Jo 12:8 — 'os pobres sempre tereis'"],
        eminencia="Mt 25:31-46: 'tive fome e me deram de comer' é o primeiro critério do juízo final.",
        rep_ref="Mateus 25:35", rep_naa="Porque tive fome, e vocês me deram de comer; tive sede, e me deram de beber; era forasteiro, e me hospedaram;",
    ),
    "ENF": dict(
        titulo="Cuidar dos enfermos, dos presos e dos que sofrem",
        demanda="Visitar e cuidar do doente e do preso; curar e aliviar o sofrimento; pôr a pessoa acima da regra ('é lícito fazer o bem no sábado').",
        agrupamento="Reúne 'enfermo e me visitaram, preso e foram me ver' (Mt 25:36,43), a comissão 'curem os enfermos' (Mt 10:8; Lc 10:9), os cuidados do "
                    "samaritano (Lc 10:34-35), as controvérsias de sábado em que Jesus afirma o dever de salvar a vida (Mt 12:11-12; Mc 3:4; Lc 6:9; 13:15-16; 14:5) "
                    "e a missão programática de Lc 4:18.",
        enfases=["Mt 25:36,39,43 — juízo das nações", "Lc 10:30-37 — bom samaritano", "Mt 12:9-14; Mc 3:1-6; Lc 6:6-11; 13:10-17; 14:1-6 — curas no sábado",
                 "Lc 4:18-19 — 'curar os quebrantados, libertar os cativos'", "Mt 9:35-36; 14:14 — compaixão de Jesus pelos enfermos", "Mt 10:1,8; Lc 9:1-2; 10:9 — comissão de curar"],
        eminencia="Mt 25:36: visitar o enfermo e o preso é critério do juízo final.",
        rep_ref="Mateus 25:36", rep_naa="estava nu, e me vestiram; estava enfermo, e me visitaram; estava preso, e foram me ver.",
    ),
    "ESTR": dict(
        titulo="Acolher o forasteiro e praticar a hospitalidade",
        demanda="Hospedar o forasteiro; receber a criança, o enviado e o pequenino em nome de Jesus; convidar à mesa quem não pode retribuir; dar água para os pés, saudação e acolhida.",
        agrupamento="Reúne 'forasteiro e me hospedaram' (Mt 25:35,43), 'quem recebe vocês recebe a mim' (Mt 10:40-41; 18:5; Mc 9:37; Lc 9:48; Jo 13:20), "
                    "'convide os pobres, aleijados, coxos e cegos' (Lc 14:12-14), os gestos de hospitalidade cobrados de Simão (Lc 7:44-46) e o exemplo "
                    "de Jesus à mesa com publicanos (Mt 11:19; Lc 19:5).",
        enfases=["Mt 25:35,38,43 — juízo das nações", "Mt 10:40-42 — receber os enviados", "Lc 14:7-24 — lugares à mesa, convidados pobres, grande ceia",
                 "Lc 7:36-50 — a mulher e o fariseu", "Lc 19:1-10 — Zaqueu", "Lc 10:38-42; 24:28-32 — hospitalidade recebida por Jesus"],
        eminencia="Mt 25:35: 'era forasteiro e me hospedaram' é critério do juízo final.",
        rep_ref="Lucas 14:13-14", rep_naa="Mas, quando der um banquete, convide os pobres, os aleijados, os coxos e os cegos. E você será feliz, porque eles não têm com que retribuir; a sua recompensa, porém, você a terá na ressurreição dos justos.",
    ),
    "DAR": dict(
        titulo="Dar com generosidade, em secreto e sem esperar retorno",
        demanda="Dar a quem pede; emprestar sem esperar nada; dar esmola em secreto; vender e repartir com os pobres; guardar-se da avareza; usar as riquezas para o bem.",
        agrupamento="Reúne 'dê a quem lhe pede' (Mt 5:42; Lc 6:30), 'que a mão esquerda não saiba' (Mt 6:1-4), 'emprestem sem esperar nada' (Lc 6:34-35), 'deem e lhes será dado' (Lc 6:38), "
                    "'vendam os bens e deem esmola' (Lc 12:33; Mt 19:21), a viúva pobre (Mc 12:43-44), o rico insensato e o rico e Lázaro, 'de graça deem' (Mt 10:8).",
        enfases=["Mt 6:1-4 — esmola em secreto", "Lc 6:30-38 — dar e emprestar", "Lc 12:13-34 — rico insensato; 'vendam e deem'", "Lc 16:1-13,19-31 — administrador; rico e Lázaro",
                 "Mt 19:16-30 — jovem rico", "Mc 12:41-44; Lc 21:1-4 — viúva pobre", "Lc 19:1-10 — Zaqueu restitui e dá aos pobres"],
        eminencia="",
        rep_ref="Mateus 6:3-4", rep_naa="Mas, quando você der esmola, que a sua mão esquerda não saiba o que faz a direita, para que a sua esmola fique em secreto; e o seu Pai, que vê em secreto, o recompensará.",
    ),
    "AMAR": dict(
        titulo="Amar o próximo e o inimigo; ser misericordioso; não retaliar",
        demanda="Amar o próximo como a si mesmo e os inimigos como o Pai os ama; fazer aos outros o que se quer para si; ser misericordioso; oferecer a outra face; amar uns aos outros como Jesus amou.",
        agrupamento="Reúne o segundo grande mandamento (Mt 22:39; Mc 12:31; Lc 10:27-28), o amor aos inimigos (Mt 5:38-48; Lc 6:27-36), a regra de ouro (Mt 7:12; Lc 6:31), "
                    "'misericórdia quero' (Mt 9:13; 12:7), o bom samaritano, o mandamento novo (Jo 13:34-35; 15:12-17) e 'a mim o fizestes' (Mt 25:40).",
        enfases=["Mt 22:34-40; Mc 12:28-34 — o maior mandamento", "Mt 5:38-48; Lc 6:27-36 — amor aos inimigos", "Lc 10:25-37 — bom samaritano",
                 "Jo 13:1-17,34-35; 15:12-17 — mandamento novo", "Mt 25:31-46 — 'a um destes pequeninos'", "Mt 7:12 — regra de ouro", "Mt 23:23 — 'justiça, misericórdia e fé'"],
        eminencia="Mt 22:39-40: 'o segundo, semelhante a este… destes dois mandamentos dependem toda a Lei e os Profetas'. Jo 13:35: o amor mútuo é a marca do discípulo.",
        rep_ref="João 13:34", rep_naa="Novo mandamento lhes dou: que vocês amem uns aos outros; assim como eu os amei, que também vocês amem uns aos outros.",
    ),
    "PERD": dict(
        titulo="Perdoar, reconciliar-se, não julgar e restaurar o irmão",
        demanda="Perdoar sem limite; reconciliar-se antes de adorar; entrar em acordo com o adversário; não julgar; tirar a trave do próprio olho; repreender o irmão a sós e restaurá-lo.",
        agrupamento="Reúne reconciliação (Mt 5:23-26), perdão (Mt 6:12-15; 18:21-35; Mc 11:25; Lc 17:3-4; Jo 20:23), não julgar (Mt 7:1-5; Lc 6:37-42; Jo 7:24; 8:7), "
                    "disciplina restauradora (Mt 18:15-17), o pai do pródigo e 'Pai, perdoa-lhes'.",
        enfases=["Mt 18:15-35 — correção fraterna e credor incompassivo", "Mt 5:21-26 — ira e reconciliação", "Mt 6:12,14-15 — perdão no Pai-nosso",
                 "Mt 7:1-5; Lc 6:37-42 — cisco e trave", "Lc 15:11-32 — filho pródigo", "Lc 23:34 — 'Pai, perdoa-lhes'", "Jo 7:53–8:11 — a mulher adúltera"],
        eminencia="Mt 6:14-15: o perdão recebido é condicionado ao perdão concedido.",
        rep_ref="Mateus 6:14", rep_naa="Porque, se vocês perdoarem as ofensas das pessoas, o Pai celestial também lhes perdoará.",
    ),
    "FAM": dict(
        titulo="Família: honrar e sustentar os pais, guardar o casamento, cuidar dos filhos",
        demanda="Honrar e sustentar pai e mãe (sem 'Corbã'); guardar a fidelidade conjugal no coração e na conduta; não repudiar; prover para a família, como Jesus proveu para a mãe.",
        agrupamento="Reúne 'honre o seu pai e a sua mãe' com a denúncia do Corbã (Mt 15:4-6; Mc 7:10-13; Mt 19:19; Mc 10:19; Lc 18:20), as antíteses sobre adultério e divórcio "
                    "(Mt 5:27-32; 19:4-9; Mc 10:6-12; Lc 16:18), 'vocês sabem dar boas coisas aos seus filhos' (Mt 7:11) e Jo 19:26-27.",
        enfases=["Mt 15:1-9; Mc 7:1-13 — Corbã", "Mt 19:3-12; Mc 10:1-12 — casamento e divórcio", "Mt 5:27-32 — adultério no coração",
                 "Jo 19:25-27 — Jesus entrega a mãe ao discípulo", "Mt 7:9-11; Lc 11:11-13 — pais que dão boas coisas", "Mt 19:13-15 — crianças"],
        eminencia="",
        rep_ref="Mateus 15:4", rep_naa="Porque Deus ordenou: 'Honre o seu pai e a sua mãe'",
    ),
    "VULN": dict(
        titulo="Proteger os pequeninos e vulneráveis; não escandalizar, não desprezar, não explorar",
        demanda="Receber e não desprezar os pequeninos; não escandalizar; não devorar as casas das viúvas; não impor fardos; não transformar a casa de Deus em negócio; não espancar os subordinados.",
        agrupamento="Reúne os pequeninos (Mt 18:6-14; Mc 9:42; Lc 17:1-2; Mt 19:14 par.), as denúncias contra exploradores (Mc 12:40; Lc 20:47; Mt 23:4,13-14; Lc 11:46,52), "
                    "a purificação do templo, o servo que espanca os conservos (Mt 24:49; Lc 12:45), a viúva diante do juiz e 'o sábado foi feito para o homem'.",
        enfases=["Mt 18:1-14 — pequeninos e ovelha perdida", "Mt 23; Lc 11:37-54 — 'ais' contra opressores", "Mc 12:38-40; Lc 20:45-47 — devorar casas de viúvas",
                 "Mt 21:12-13; Mc 11:15-17; Lc 19:45-46; Jo 2:13-17 — purificação do templo", "Lc 18:1-8 — viúva e juiz", "Mt 24:45-51; Lc 12:42-48 — servo fiel e servo mau"],
        eminencia="Mt 25:40,45: o que se faz ou deixa de fazer 'a um destes pequeninos' é feito ao próprio Cristo.",
        rep_ref="Mateus 18:10", rep_naa="Cuidado para não desprezar nenhum destes pequeninos; porque eu lhes digo que os anjos deles nos céus veem continuamente a face de meu Pai celeste.",
    ),
    "JUSTV": dict(
        titulo="Justiça, verdade e honestidade nas relações",
        demanda="Falar a verdade sem juramentos; não defraudar nem dar falso testemunho; ser fiel no pouco e no alheio; pagar o salário justo; praticar justiça e misericórdia, não só ritos.",
        agrupamento="Reúne 'seja o seu sim, sim' (Mt 5:33-37), 'não defraude' e o Decálogo social (Mc 10:19 par.), 'fiel no pouco' (Lc 16:10-12), 'o trabalhador é digno do salário' (Lc 10:7; Mt 10:10), "
                    "o pagamento justo dos trabalhadores da vinha (Mt 20:1-15), 'justiça, misericórdia e fé' (Mt 23:23; Lc 11:42), palavras inúteis (Mt 12:36-37) e as listas de pecados do coração.",
        enfases=["Mt 5:33-37 — juramentos", "Mt 23:16-28; Lc 11:39-44 — hipocrisia, extorsão, justiça omitida", "Lc 16:1-13 — fidelidade no pouco",
                 "Mt 20:1-16 — trabalhadores da vinha", "Mt 15:19; Mc 7:21-23 — o que sai do coração", "Lc 19:1-10 — restituição de Zaqueu"],
        eminencia="Mt 23:23: justiça, misericórdia e fé são 'os preceitos mais importantes da Lei'.",
        rep_ref="Lucas 16:10", rep_naa="Quem é fiel no pouco também é fiel no muito; e quem é injusto no pouco também é injusto no muito.",
    ),
    "SERV": dict(
        titulo="Servir e liderar como servo",
        demanda="Ser o servo de todos; não buscar títulos nem os primeiros lugares; lavar os pés uns dos outros; quem governa, como quem serve; dar a ração à casa no tempo certo.",
        agrupamento="Reúne 'quem quiser ser grande seja servo' (Mt 20:25-28; Mc 9:35; 10:42-45; Lc 22:25-27), 'não sejam chamados Rabi' (Mt 23:8-12), o último lugar (Lc 14:7-11), "
                    "o lava-pés (Jo 13:12-17), 'somos servos inúteis' (Lc 17:10) e o mordomo fiel (Mt 24:45; Lc 12:42).",
        enfases=["Mt 20:20-28; Mc 10:35-45 — 'veio para servir'", "Jo 13:1-17 — lava-pés", "Lc 22:24-27 — disputa na ceia", "Mt 23:1-12 — títulos e primeiros lugares",
                 "Lc 14:7-11 — lugares à mesa", "Mt 18:1-5; Mc 9:33-37; Lc 9:46-48 — a criança no meio"],
        eminencia="",
        rep_ref="Marcos 10:45", rep_naa="Pois o próprio Filho do Homem não veio para ser servido, mas para servir e dar a sua vida em resgate por muitos.",
    ),
    "CIV": dict(
        titulo="Deveres cívicos: César, impostos e autoridades",
        demanda="Dar a César o que é de César; pagar o imposto para não escandalizar; reconhecer a autoridade que vem de cima; resolver disputas antes do tribunal; cumprir o que a Lei prescreve.",
        agrupamento="Reúne 'deem a César' (Mt 22:21; Mc 12:17; Lc 20:25), o imposto do templo (Mt 17:24-27), 'ir a segunda milha' (Mt 5:41), o acordo com o adversário (Mt 5:25-26; Lc 12:58), "
                    "'façam o que dizem na cátedra de Moisés' (Mt 23:3), Jo 19:11 e as ordens de apresentar-se ao sacerdote.",
        enfases=["Mt 22:15-22 par. — o tributo", "Mt 17:24-27 — imposto do templo", "Mt 5:38-42 — requisição romana", "Jo 18:33-38; 19:8-11 — Jesus diante de Pilatos"],
        eminencia="",
        rep_ref="Mateus 22:21", rep_naa="Deem, pois, a César o que é de César e a Deus o que é de Deus.",
    ),
    "PAZ": dict(
        titulo="Promover a paz e renunciar à violência",
        demanda="Ser pacificador; não se irar nem insultar; não resistir ao perverso com violência; guardar a espada; saudar com paz; ter paz uns com os outros; não destruir vidas.",
        agrupamento="Reúne a bem-aventurança dos pacificadores (Mt 5:9), a antítese da ira (Mt 5:21-22), a não-retaliação (Mt 5:38-42; Lc 6:29), 'guarde a espada' (Mt 26:52; Jo 18:11), "
                    "'paz a esta casa' (Mt 10:12-13; Lc 10:5-6), 'tenham paz uns com os outros' (Mc 9:50), 'quem não é contra nós é por nós' e Jo 18:36.",
        enfases=["Mt 5:9,21-26,38-48 — Sermão do Monte", "Mt 26:47-56; Lc 22:47-53; Jo 18:1-11 — a prisão de Jesus", "Lc 9:51-56 — 'não veio destruir vidas'",
                 "Mc 9:38-50 — 'não o proíbam… paz uns com os outros'", "Lc 19:41-44 — 'as coisas que pertencem à paz'"],
        eminencia="",
        rep_ref="Mateus 5:9", rep_naa="Bem-aventurados os pacificadores, porque serão chamados filhos de Deus.",
    ),
    "EVANG": dict(
        titulo="Evangelizar e testemunhar: anunciar o Reino, ser sal e luz",
        demanda="Pregar o Reino a todas as pessoas; brilhar diante dos outros com boas obras; confessar Jesus; contar o que Deus fez; pedir obreiros; ir como enviado do Pai.",
        agrupamento="Reúne 'pescadores de gente' (Mt 4:19; Mc 1:17; Lc 5:10), sal e luz (Mt 5:13-16), 'preguem' (Mt 10:7,27; Mc 16:15; Lc 9:60; 24:47-48), 'roguem ao Senhor da seara' (Mt 9:37-38; Lc 10:2), "
                    "'vá contar o que Deus fez' (Mc 5:19; Lc 8:39), 'os campos estão brancos' (Jo 4:35-38), confessar Jesus (Mt 10:32-33; Lc 12:8-9), 'eu os envio' (Jo 17:18; 20:21) e as parábolas do convite.",
        enfases=["Mt 9:35–10:42; Lc 9:1-6; 10:1-20 — discursos de envio", "Mt 28:16-20; Mc 16:15; Lc 24:46-49; Jo 20:21 — comissão", "Mt 5:13-16 — sal e luz",
                 "Jo 4:31-38 — campos brancos", "Lc 4:16-21,43 — missão programática", "Lc 14:16-24; Mt 22:1-14 — convite aos de fora", "Mt 13; Mc 4; Lc 8 — o semeador"],
        eminencia="Mt 28:18-20; Mc 16:15; Lc 24:47; Jo 20:21: últimas palavras do Ressuscitado nos quatro Evangelhos.",
        rep_ref="Mateus 5:16", rep_naa="Assim brilhe também a luz de vocês diante das pessoas, para que vejam as suas boas obras e glorifiquem o Pai de vocês, que está nos céus.",
    ),
    "DISC": dict(
        titulo="Fazer discípulos, ensinar e pastorear",
        demanda="Fazer discípulos, batizar e ensinar a guardar tudo o que Jesus ordenou; buscar a ovelha perdida; apascentar; fortalecer os irmãos; não fechar o Reino a ninguém.",
        agrupamento="Reúne a grande comissão (Mt 28:19-20), 'quem praticar e ensinar' (Mt 5:19), a ovelha perdida (Mt 18:12-14; Lc 15:4-7), 'apascente as minhas ovelhas' (Jo 21:15-17), "
                    "'fortaleça os seus irmãos' (Lc 22:32), o bom pastor versus o mercenário (Jo 10:11-13) e as denúncias contra quem fecha o Reino ou forma mal (Mt 23:13,15; Lc 11:52).",
        enfases=["Mt 28:16-20 — grande comissão", "Jo 21:15-19 — 'apascenta'", "Jo 10:1-18 — bom pastor", "Mt 18:10-14; Lc 15:1-7 — ovelha perdida",
                 "Mt 23:13-15; Lc 11:52 — guias que fecham o Reino", "Mt 13:51-52 — o escriba discípulo"],
        eminencia="Mt 28:19-20: mandato final do Ressuscitado em Mateus.",
        rep_ref="Mateus 28:19-20", rep_naa="Portanto, vão e façam discípulos de todas as nações, batizando-os em nome do Pai, e do Filho, e do Espírito Santo; ensinando-os a guardar todas as coisas que tenho ordenado a vocês. E eis que estou com vocês todos os dias até o fim dos tempos.",
    ),
}
