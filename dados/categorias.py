# -*- coding: utf-8 -*-
"""Taxonomia das categorias (agrupamento lógico à maneira de John Piper, *What Jesus Demands from the World*).

Cada categoria: código, título, demanda em uma frase, justificativa do agrupamento, correspondência
temática com Piper (sem numeração de capítulo), ênfases (parábolas/discursos/ditos que reforçam o tema),
eminência explícita (quando o próprio Jesus hierarquiza) e o versículo representativo com texto da NAA.

ATENÇÃO: os textos NAA foram transcritos de memória pelo autor do script e devem ser conferidos com a
edição impressa/digital da Nova Almeida Atualizada (SBB, 2017) antes de impressão definitiva.
"""

CATEGORIAS = {
    "ARREP": dict(
        titulo="Arrependa-se e entre pela porta estreita",
        demanda="Mude de mente e de rumo diante do Reino que chegou; entre pela porta estreita; nasça de novo.",
        agrupamento="Reúne os imperativos de conversão inicial e de decisão radical pela entrada no Reino: 'arrependam-se' "
                    "(μετανοεῖτε), 'entrem pela porta estreita', 'esforcem-se'. É o primeiro verbo da pregação pública de "
                    "Jesus (Mt 4:17; Mc 1:15) e, portanto, o portal lógico de todos os demais mandamentos.",
        piper="You must be born again; Repent",
        enfases=["Mt 4:17; Mc 1:15 — pregação inaugural", "Lc 13:1-5 — 'se não se arrependerem, todos perecerão'",
                 "Lc 13:6-9 — figueira estéril", "Lc 15:1-32 — ovelha, dracma e filho pródigo (alegria pelo arrependimento)",
                 "Jo 3:1-8 — novo nascimento", "Mt 7:13-14 — as duas portas"],
        eminencia="Primeira palavra do ministério público (Mt 4:17; Mc 1:15): 'arrependam-se e creiam'.",
        rep_ref="Marcos 1:15",
        rep_naa="O tempo está cumprido, e o Reino de Deus está próximo; arrependam-se e creiam no evangelho.",
    ),
    "FE": dict(
        titulo="Creia em Jesus, venha a ele e permaneça nele",
        demanda="Confie em Jesus como enviado do Pai; venha a ele, creia nele, receba o Espírito e permaneça nele como o ramo na videira.",
        agrupamento="Agrupa 'creiam' (πιστεύετε), 'venham e vejam', 'venha a mim e beba', 'tenham fé em Deus', 'permaneçam em mim'. "
                    "Todos têm Jesus como objeto ou mediador da confiança; a fé é a resposta que recebe o que o arrependimento abre.",
        piper="Come to me; Believe in me; Love me; Abide in me",
        enfases=["Jo 6:22-59 — pão da vida ('a obra de Deus é esta: que creiam')", "Jo 15:1-11 — videira e ramos",
                 "Jo 3:16-18; 11:25-26; 20:29-31 — crer para ter vida", "Mc 9:23 — 'tudo é possível ao que crê'",
                 "Lc 14:15-24 — grande ceia ('venham, está tudo pronto')", "Mt 8:5-13; 15:21-28 — fé do centurião e da cananeia"],
        eminencia="Jo 6:29: 'a obra de Deus é esta: que creiam naquele que ele enviou'.",
        rep_ref="João 7:37",
        rep_naa="Se alguém tem sede, venha a mim e beba.",
    ),
    "SEGUIR": dict(
        titulo="Siga a Jesus, negando-se a si mesmo",
        demanda="Deixe tudo, tome a sua cruz cada dia e siga a Jesus como discípulo; aprenda dele.",
        agrupamento="Reúne o chamado pessoal 'siga-me' (ἀκολούθει μοι), dirigido a Mateus, Levi, Filipe, Pedro e ao jovem rico, "
                    "e sua forma universal: 'negue-se a si mesmo, tome a sua cruz e siga-me'. O princípio é um só: o discipulado "
                    "como adesão pessoal e custosa a Jesus.",
        piper="Take up your cross and follow me; Listen to me (aprender dele)",
        enfases=["Mt 4:18-22; 9:9; Jo 1:35-51 — chamados", "Lc 9:57-62; 14:25-35 — custo do discipulado",
                 "Mt 10:37-39; 16:24-27 — a cruz e a vida", "Mt 19:16-30 — jovem rico", "Jo 12:24-26 — o grão de trigo",
                 "Jo 21:15-22 — 'quanto a você, siga-me'"],
        eminencia="",
        rep_ref="Mateus 16:24",
        rep_naa="Se alguém quer vir após mim, negue-se a si mesmo, tome a sua cruz e siga-me.",
    ),
    "OUVIR": dict(
        titulo="Ouça, entenda e guarde a Palavra",
        demanda="Dê ouvidos ao que Jesus diz, entenda, lembre-se e pratique; quem tem ouvidos, ouça.",
        agrupamento="Agrupa o refrão 'quem tem ouvidos, ouça' (ὁ ἔχων ὦτα ἀκουέτω), 'ouçam e entendam', 'atentem para o que ouvem', "
                    "'vejam como ouvem', 'lembrem-se'. O ouvir bíblico inclui obedecer; por isso a categoria abrange guardar e praticar.",
        piper="Listen to me; Do the will of my Father who is in heaven",
        enfases=["Mt 13; Mc 4; Lc 8 — parábola do semeador e do candeeiro", "Mt 7:24-27 — casa sobre a rocha",
                 "Mt 21:28-32 — dois filhos", "Lc 10:38-42 — Maria aos pés de Jesus", "Lc 11:28 — 'bem-aventurados os que ouvem e guardam'",
                 "Jo 14:15,21,23; 15:10 — guardar os mandamentos como prova de amor"],
        eminencia="",
        rep_ref="Marcos 4:9",
        rep_naa="Quem tem ouvidos para ouvir, ouça.",
    ),
    "DEUS": dict(
        titulo="Ame a Deus acima de tudo e busque primeiro o seu Reino",
        demanda="Ame, tema e adore somente a Deus; busque em primeiro lugar o seu Reino e a sua justiça; zele pela honra do Pai.",
        agrupamento="Reúne 'busquem primeiro o Reino', 'ouça, Israel… amarás', 'temam a Deus', 'não façam da casa do meu Pai casa de negócio'. "
                    "O 'grande e primeiro mandamento' está, no grego, no futuro imperatival (ἀγαπήσεις), e por isso figura no complemento; "
                    "o imperativo morfológico aparece em 'ouça' (ἄκουε) e 'busquem' (ζητεῖτε).",
        piper="Love God with all your heart, soul, mind and strength; Worship God in spirit and truth; Fear him who can destroy both soul and body in hell",
        enfases=["Mt 22:34-40; Mc 12:28-34 — o maior mandamento", "Mt 6:24; Lc 16:13 — dois senhores",
                 "Mt 4:1-11 — tentação ('adorarás ao Senhor')", "Jo 4:21-24 — adoradores em espírito e em verdade",
                 "Mt 6:33; Lc 12:31 — buscar primeiro", "Lc 12:4-5 — temor devido a Deus", "Jo 2:13-17 — zelo pela casa do Pai"],
        eminencia="Mt 22:38: 'este é o grande e primeiro mandamento'. Mt 6:33: 'busquem em primeiro lugar'.",
        rep_ref="Mateus 6:33",
        rep_naa="Mas busquem em primeiro lugar o Reino de Deus e a sua justiça, e todas estas coisas lhes serão acrescentadas.",
    ),
    "ORAR": dict(
        titulo="Ore, peça, jejue e vigie em oração",
        demanda="Ore ao Pai em secreto e com perseverança; peça, busque, bata; ore o Pai-nosso; jejue sem ostentação; vigie e ore para não cair em tentação.",
        agrupamento="Reúne os imperativos de oração (προσεύχεσθε, αἰτεῖτε, ζητεῖτε, κρούετε, δεήθητε), as petições do Pai-nosso "
                    "(imperativos de 3ª pessoa dentro da oração ordenada) e as instruções sobre jejum, que Jesus ensina no mesmo bloco (Mt 6:1-18).",
        piper="Always pray and do not lose heart",
        enfases=["Mt 6:5-15; Lc 11:1-4 — Pai-nosso", "Lc 11:5-13 — amigo importuno", "Lc 18:1-8 — juiz iníquo",
                 "Lc 18:9-14 — fariseu e publicano", "Mt 26:36-46 — Getsêmani", "Jo 14:13-14; 15:7; 16:23-24 — pedir em meu nome",
                 "Mc 11:22-25 — fé e perdão na oração"],
        eminencia="",
        rep_ref="Mateus 7:7",
        rep_naa="Peçam e lhes será dado; busquem e encontrarão; batam, e a porta será aberta para vocês.",
    ),
    "CONFIAR": dict(
        titulo="Não tema nem ande ansioso; tenha bom ânimo",
        demanda="Confie na providência do Pai: não ande ansioso pelo sustento nem pelas ameaças dos homens; tenha bom ânimo porque Jesus venceu o mundo.",
        agrupamento="Reúne 'não temam' (μὴ φοβεῖσθε), 'não andem ansiosos' (μὴ μεριμνᾶτε), 'tenham bom ânimo' (θαρσεῖτε), "
                    "'não se turbe o coração', 'observem as aves', 'considerem os lírios'. É o mandamento mais repetido de Jesus em número de "
                    "ocorrências, tanto a discípulos quanto a indivíduos aflitos.",
        piper="Do not be anxious about the necessities of daily life; Do not be anxious about the threats of man",
        enfases=["Mt 6:25-34; Lc 12:22-32 — aves e lírios", "Mt 10:26-33 — pardais", "Mc 4:35-41 — tempestade ('por que são tão medrosos?')",
                 "Jo 14:1-3,27; 16:33 — paz e bom ânimo", "Lc 12:32 — 'não tenha medo, pequeno rebanho'"],
        eminencia="",
        rep_ref="Mateus 6:25",
        rep_naa="Por isso eu lhes digo: não andem ansiosos quanto à vida de vocês, quanto ao que haverão de comer ou beber; nem quanto ao corpo, quanto ao que haverão de vestir.",
    ),
    "AMAR": dict(
        titulo="Ame o próximo e os inimigos; faça o bem e seja misericordioso",
        demanda="Ame o próximo como a si mesmo e os inimigos como o Pai os ama; faça aos outros o que quer para si; seja misericordioso; não retalie.",
        agrupamento="Reúne 'amem os seus inimigos', 'façam o bem', 'bendigam', 'ofereça a outra face', 'vá com ele duas milhas', regra de ouro, "
                    "'sejam misericordiosos', 'vá e faça o mesmo', 'deem-lhes vocês de comer'. O 'amarás o teu próximo' (futuro) e o "
                    "'mandamento novo' (ἵνα) estão no complemento.",
        piper="Love your enemies; Love your neighbor as yourself; Love one another as I have loved you; Do not resist the one who is evil",
        enfases=["Mt 5:38-48; Lc 6:27-36 — amor aos inimigos", "Lc 10:25-37 — bom samaritano", "Mt 25:31-46 — juízo das nações",
                 "Jo 13:1-17,34-35; 15:12-17 — mandamento novo e lava-pés", "Mt 22:39 — 'o segundo, semelhante a este'",
                 "Mt 7:12 — regra de ouro: 'esta é a Lei e os Profetas'", "Mt 9:13; 12:7 — 'misericórdia quero'"],
        eminencia="Mt 22:39-40: 'o segundo, semelhante a este… destes dois mandamentos dependem toda a Lei e os Profetas'.",
        rep_ref="Mateus 5:44",
        rep_naa="Eu, porém, lhes digo: amem os seus inimigos e orem pelos que perseguem vocês.",
    ),
    "PERDOAR": dict(
        titulo="Perdoe, não julgue, reconcilie-se e corrija com amor",
        demanda="Perdoe como foi perdoado; não julgue nem condene; reconcilie-se antes de adorar; repreenda o irmão a sós e restaure-o.",
        agrupamento="Reúne 'perdoem' (ἀφίετε), 'não julguem' (μὴ κρίνετε), 'tire primeiro a trave', 'vá reconciliar-se', 'repreenda-o a sós', "
                    "'entre em acordo com o adversário'. O fio comum é o tratamento das ofensas dentro das relações, à luz do perdão recebido.",
        piper="Do not be angry — embrace mercy and forgiveness; Judge not",
        enfases=["Mt 18:21-35 — credor incompassivo", "Mt 6:12,14-15 — perdão no Pai-nosso", "Mt 5:21-26 — ira e reconciliação",
                 "Mt 7:1-5; Lc 6:37-42 — cisco e trave", "Lc 17:3-4 — setenta vezes sete", "Mt 18:15-20 — disciplina na igreja",
                 "Lc 23:34 — 'Pai, perdoa-lhes'"],
        eminencia="Mt 6:14-15 condiciona o perdão recebido ao perdão concedido.",
        rep_ref="Lucas 6:37",
        rep_naa="Não julguem e vocês não serão julgados; não condenem e vocês não serão condenados; perdoem e vocês serão perdoados.",
    ),
    "HUMILD": dict(
        titulo="Humilhe-se e sirva",
        demanda="Seja como criança e como servo; ocupe o último lugar; não busque títulos; lave os pés uns dos outros; diga 'somos servos inúteis'.",
        agrupamento="Reúne 'o maior seja como o menor', 'vá sentar-se no último lugar', 'digam: somos servos inúteis', 'aprendam de mim, que sou manso e humilde'. "
                    "As formas 'não sejam chamados Rabi', 'se não se tornarem como crianças', 'quem quiser ser grande será servo' estão no complemento.",
        piper="Humble yourself by making war on your pride; Humble yourself in childlikeness, servanthood and brokenhearted boldness; Do not be served but serve",
        enfases=["Mt 18:1-5; Mc 9:33-37 — a criança no meio", "Mt 20:20-28; Mc 10:35-45 — 'o Filho do Homem veio para servir'",
                 "Mt 23:1-12 — 'o maior entre vocês será o servo'", "Lc 14:7-11 — lugares à mesa", "Lc 18:9-14 — fariseu e publicano",
                 "Lc 22:24-27 — disputa na última ceia", "Jo 13:1-17 — lava-pés", "Lc 17:7-10 — servo inútil"],
        eminencia="",
        rep_ref="Lucas 22:26",
        rep_naa="Mas vocês não são assim; pelo contrário, o maior entre vocês seja como o menor; e aquele que dirige seja como o que serve.",
    ),
    "SANTID": dict(
        titulo="Santidade: pureza, integridade e luta contra o pecado",
        demanda="Corte o que faz tropeçar; fale com verdade sem juramentos; não pratique a justiça para ser visto; guarde o casamento; não peque mais; cuidado com a hipocrisia.",
        agrupamento="Reúne as antíteses do Sermão do Monte com imperativo ('arranque o olho', 'seja o seu sim, sim'), a guarda contra a hipocrisia "
                    "('cuidado com o fermento dos fariseus', 'limpe primeiro o interior'), o casamento ('não separe o homem') e 'não peque mais'. "
                    "'Sejam perfeitos' (futuro) e 'não jurem' (infinitivo) estão no complemento.",
        piper="Do not take an oath; Do not commit adultery / lust; What God has joined together let not man separate; Beware of hypocrisy",
        enfases=["Mt 5:21-37 — antíteses: ira, adultério, divórcio, juramento", "Mt 5:48 — 'sejam perfeitos'", "Mt 6:1-18 — justiça em secreto",
                 "Mt 15:10-20 — o que contamina sai do coração", "Mt 23 — os 'ais' contra a hipocrisia", "Mc 9:42-50; Mt 18:6-9 — radicalidade contra o escândalo",
                 "Mt 19:3-12; Mc 10:1-12 — casamento", "Jo 5:14; 8:11 — 'não peque mais'"],
        eminencia="",
        rep_ref="Mateus 5:30",
        rep_naa="E, se a sua mão direita faz você tropeçar, corte-a e jogue-a fora; pois é melhor perder um dos seus membros do que todo o seu corpo ir para o inferno.",
    ),
    "BENS": dict(
        titulo="Dinheiro e posses: não acumule, dê e guarde-se da avareza",
        demanda="Não acumule tesouros na terra, mas no céu; dê a quem pede; venda e dê esmola; guarde-se da avareza; use as riquezas para fazer amigos eternos.",
        agrupamento="Reúne 'não acumulem tesouros', 'deem', 'dê a quem lhe pede', 'emprestem sem esperar', 'vendam os seus bens e deem esmola', "
                    "'guardem-se de toda avareza', 'façam amigos com as riquezas'. 'Não podem servir a Deus e às riquezas' está no complemento.",
        piper="Do not lay up treasures on earth; Give to the needy; Do not be anxious — seek first the kingdom (dimensão material)",
        enfases=["Mt 6:19-24 — tesouros e dois senhores", "Lc 12:13-21 — rico insensato", "Lc 16:1-13 — administrador infiel",
                 "Lc 16:19-31 — rico e Lázaro", "Mt 19:16-30 — jovem rico ('é difícil o rico entrar')", "Lc 12:33-34; 14:12-14,33 — vender, dar, renunciar",
                 "Mc 12:41-44 — viúva pobre", "Lc 19:1-10 — Zaqueu"],
        eminencia="",
        rep_ref="Mateus 6:19-20",
        rep_naa="Não acumulem para vocês tesouros na terra, onde a traça e a ferrugem corroem e onde ladrões escavam e roubam; mas acumulem para vocês tesouros no céu, onde nem a traça nem a ferrugem corroem, e onde ladrões não escavam, nem roubam.",
    ),
    "MISSAO": dict(
        titulo="Vá, pregue, faça discípulos, cure e brilhe",
        demanda="Vá por todo o mundo e faça discípulos; pregue o Reino; cure e liberte; anuncie o que Deus fez por você; peça obreiros; apascente o rebanho; brilhe a sua luz.",
        agrupamento="Reúne o envio dos Doze e dos Setenta (Mt 10; Lc 9–10), a grande comissão (Mt 28:19; Mc 16:15), 'preguem', 'curem', 'roguem ao Senhor da seara', "
                    "'brilhe a luz de vocês', 'levantem os olhos e vejam os campos', 'apascente as minhas ovelhas' e os envios individuais ('vá contar o que Deus fez').",
        piper="Make disciples of all nations; Let your light shine before others; Pray for laborers",
        enfases=["Mt 9:35–10:42; Lc 9:1-6; 10:1-20 — discursos de envio", "Mt 28:16-20; Mc 16:15; Lc 24:46-49; Jo 20:21 — comissão",
                 "Mt 5:13-16 — sal e luz", "Jo 4:31-38 — campos brancos", "Mt 13:31-33 — mostarda e fermento", "Lc 14:16-24; Mt 22:1-14 — 'obrigue-os a entrar'",
                 "Jo 21:15-17 — 'apascente as minhas ovelhas'"],
        eminencia="Mt 28:18-20: últimas palavras do Ressuscitado em Mateus.",
        rep_ref="Mateus 28:19",
        rep_naa="Portanto, vão e façam discípulos de todas as nações, batizando-os em nome do Pai, e do Filho, e do Espírito Santo.",
    ),
    "VIGIAR": dict(
        titulo="Vigie, esteja pronto para a volta de Cristo e não se deixe enganar",
        demanda="Vigie e esteja preparado, porque o Filho do Homem vem na hora em que você menos espera; acautele-se de falsos profetas, do fermento e do engano; persevere.",
        agrupamento="Reúne 'vigiem' (γρηγορεῖτε), 'estejam preparados', 'cuidado para que ninguém os engane', 'acautelem-se dos falsos profetas', "
                    "'aprendam da figueira', 'lembrem-se da mulher de Ló', 'pela perseverança ganhem a vida'. As ordens de fuga localizadas (Judeia) "
                    "ficam marcadas como situacionais.",
        piper="Watch — be ready for my coming; Beware of false prophets; Beware of the leaven of the Pharisees",
        enfases=["Mt 24–25; Mc 13; Lc 21 — discurso escatológico", "Mt 24:43-51; Lc 12:35-48 — ladrão e servo fiel",
                 "Mt 25:1-13 — dez virgens", "Mt 25:14-30; Lc 19:11-27 — talentos e minas", "Mt 7:15-23 — falsos profetas",
                 "Mt 13:24-30,36-43 — joio", "Lc 17:22-37 — dias de Noé e de Ló", "Lc 21:34-36 — 'vigiem em todo tempo'"],
        eminencia="Mc 13:37: 'o que lhes digo, digo a todos: vigiem'.",
        rep_ref="Mateus 24:42",
        rep_naa="Portanto, vigiem, porque vocês não sabem em que dia virá o seu Senhor.",
    ),
    "COMUNH": dict(
        titulo="Ceia do Senhor, paz e acolhida na comunidade",
        demanda="Celebre a Ceia em memória de Jesus; viva em paz com os irmãos; acolha as crianças e os pequeninos; não impeça quem age em nome de Jesus; fortaleça os irmãos.",
        agrupamento="Reúne 'tomem, comam… bebam', 'façam isto em memória de mim', 'tenham sal em vocês e paz uns com os outros', "
                    "'deixem vir a mim as crianças', 'não o proíbam', 'fortaleça os seus irmãos'. São ordens que constituem a vida da comunidade dos discípulos.",
        piper="Do this in remembrance of me; Love one another (dimensão comunitária)",
        enfases=["Mt 26:26-29; Mc 14:22-25; Lc 22:14-20 — instituição da Ceia", "Jo 6:53-58 — comer a carne e beber o sangue",
                 "Mc 9:38-50 — 'quem não é contra nós é por nós'; sal e paz", "Mt 18:1-6,10-14; 19:13-15 — pequeninos e crianças",
                 "Jo 17:20-23 — unidade", "Mt 18:20 — 'onde dois ou três'"],
        eminencia="",
        rep_ref="Lucas 22:19",
        rep_naa="Isto é o meu corpo oferecido por vocês; façam isto em memória de mim.",
    ),
    "JUST": dict(
        titulo="Justiça e deveres: a Lei, César e a família",
        demanda="Guarde os mandamentos; honre pai e mãe; dê a César o que é de César e a Deus o que é de Deus; cumpra o que a Lei prescreve; faça o que ensinam na cátedra de Moisés.",
        agrupamento="Reúne 'honre o seu pai e a sua mãe' (τίμα, citado e endossado por Jesus), 'guarde os mandamentos', 'deem a César', "
                    "'façam e guardem o que eles dizem', 'mostre-se ao sacerdote e ofereça o que Moisés ordenou'. "
                    "Os demais mandamentos do Decálogo citados por Jesus aparecem no subjuntivo/futuro (complemento).",
        piper="Render to Caesar the things that are Caesar's and to God the things that are God's",
        enfases=["Mt 22:15-22 — o tributo a César", "Mt 5:17-20 — 'não vim revogar, mas cumprir'", "Mt 15:1-9; Mc 7:9-13 — Corbã e honra aos pais",
                 "Mt 19:16-19 — 'guarde os mandamentos'", "Mt 23:23 — justiça, misericórdia e fé", "Mt 17:24-27 — imposto do templo"],
        eminencia="",
        rep_ref="Mateus 22:21",
        rep_naa="Deem, pois, a César o que é de César e a Deus o que é de Deus.",
    ),
    "ALEGR": dict(
        titulo="Alegre-se e exulte",
        demanda="Alegre-se na perseguição por causa de Jesus; alegre-se porque o seu nome está escrito nos céus; levante a cabeça: a redenção se aproxima.",
        agrupamento="Reúne 'alegrem-se e exultem' (χαίρετε καὶ ἀγαλλιᾶσθε), 'saltem de alegria', 'alegrem-se porque os seus nomes estão escritos nos céus'. "
                    "Poucas ocorrências, mas ligadas a motivos centrais (perseguição e salvação) e reforçadas pelas parábolas da alegria.",
        piper="Rejoice and leap for joy",
        enfases=["Mt 5:11-12; Lc 6:22-23 — bem-aventurança dos perseguidos", "Lc 10:17-20 — alegria pela salvação", "Lc 15 — três parábolas da alegria",
                 "Jo 15:11; 16:20-24; 17:13 — 'para que a alegria de vocês seja completa'", "Mt 25:21,23 — 'entre no gozo do seu senhor'",
                 "Mt 13:44 — tesouro escondido ('cheio de alegria')"],
        eminencia="",
        rep_ref="Mateus 5:12",
        rep_naa="Alegrem-se e exultem, porque é grande a recompensa de vocês nos céus; pois assim perseguiram os profetas que viveram antes de vocês.",
    ),
}

ORDEM_CODIGOS = list(CATEGORIAS)  # ordem de definição (não é a prioridade)
