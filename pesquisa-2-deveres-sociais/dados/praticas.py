# -*- coding: utf-8 -*-
"""Pesquisa 2, etapa 2 — Lista de práticas do voluntário.

Cada prática é uma ação concreta que uma pessoa pode parar o que está fazendo e realizar imediatamente,
pressupondo que todo tipo de pessoa está disponível ao redor (nas ruas, com fome, doente, presa, só, em dívida…).
Derivada dos 384 versículos julgados em rotulos.py. Inspiração metodológica: as "Regras Gerais" das Sociedades
Metodistas (John Wesley, 1743) — fazer o bem "aos corpos" (dar de comer ao faminto, vestir o nu, visitar ou
ajudar os doentes e presos) e "às almas" (instruir, repreender, exortar) — e o exame diário do Holy Club de Oxford.

Formato: dict(id, grupo, acao, como, base, refs, wesley, nota)
  acao  — a ação em forma de ordem, curta
  como  — como fazer agora, em uma linha
  base  — versículo principal (código)
  refs  — demais versículos (códigos) que sustentam a prática
  wesley — correspondência com a prática metodista histórica (quando houver)
"""

GRUPOS = [
    ("A", "Obras de misericórdia para o corpo", "Mt 25:35-36 — 'tive fome… sede… forasteiro… nu… enfermo… preso'"),
    ("B", "Obras de misericórdia para a alma", "Mc 5:19; Mt 28:20 — anunciar, ensinar, orar, fortalecer"),
    ("C", "Reconciliação e perdão", "Mt 5:24; 18:15 — 'vá primeiro reconciliar-se'; 'vá e repreenda-o a sós'"),
    ("D", "Dar: dinheiro, bens e tempo", "Mt 6:3; Lc 14:13-14 — em secreto; a quem não pode retribuir"),
    ("E", "Família e casa", "Mt 15:4; Jo 19:26-27 — honrar os pais; prover para os seus"),
    ("F", "Serviço, humildade e verdade", "Jo 13:14; Mt 5:37 — lavar os pés; 'sim, sim; não, não'"),
    ("G", "Paz, justiça e cidadania", "Mt 5:9; 22:21 — pacificadores; a César o que é de César"),
]

PRATICAS = [
    # ---------------------------------------------------------------- A. CORPO
    dict(id=1, grupo="A", acao="Dê comida a quem está com fome", como="Compre ou leve uma refeição agora a alguém que não tem o que comer; não o mande embora em jejum.",
         base="Mt 25:35", refs=["Mt 14:16", "Mk 6:37", "Lk 9:13", "Mt 15:32", "Mk 8:2", "Mt 25:42", "Lk 16:21", "Mt 24:45"], wesley="Regras Gerais: 'dar de comer ao faminto'"),
    dict(id=2, grupo="A", acao="Dê água a quem tem sede", como="Ofereça um copo de água fria a quem trabalha, anda ou pede na rua.",
         base="Mt 10:42", refs=["Mk 9:41", "Mt 25:35", "Mt 25:42"], wesley="Regras Gerais: 'dar de beber'"),
    dict(id=3, grupo="A", acao="Vista quem está sem roupa", como="Dê um agasalho, calçado ou peça de roupa a quem precisa; separe hoje o que você tem a mais.",
         base="Mt 25:36", refs=["Mt 25:43"], wesley="Regras Gerais: 'vestir o nu'"),
    dict(id=4, grupo="A", acao="Acolha o forasteiro", como="Ofereça teto, refeição ou orientação a quem é de fora, migrante ou está em situação de rua.",
         base="Mt 25:35", refs=["Mt 25:38", "Mt 25:43", "Mt 10:40", "Mt 10:41", "Jn 13:20", "Lk 11:6"], wesley="Hospitalidade das casas metodistas aos pregadores itinerantes"),
    dict(id=5, grupo="A", acao="Visite um doente", como="Vá hoje à casa ou ao hospital de alguém enfermo; leve o remédio, faça companhia, ore com ele.",
         base="Mt 25:36", refs=["Mt 25:39", "Mt 25:43", "Lk 10:34"], wesley="Regras Gerais: 'visitar ou ajudar os doentes'"),
    dict(id=6, grupo="A", acao="Visite um preso", como="Visite, escreva ou envie algo a uma pessoa presa; apoie a família dela.",
         base="Mt 25:36", refs=["Mt 25:39", "Mt 25:43"], wesley="Regras Gerais: 'visitar os presos'; Wesley pregava nas prisões de Oxford e Bristol"),
    dict(id=7, grupo="A", acao="Socorra o ferido no caminho", como="Pare, preste os primeiros cuidados, leve ao atendimento e fique até que esteja seguro.",
         base="Lk 10:34", refs=["Lk 10:33", "Lk 10:37", "Lk 10:31", "Lk 10:32"], wesley="Wesley: 'Primitive Physick' (1747), remédios simples para os pobres"),
    dict(id=8, grupo="A", acao="Pague o cuidado de quem não pode pagar", como="Custeie o remédio, a consulta, a passagem ou a hospedagem de alguém; diga 'o que gastar a mais, eu pago'.",
         base="Lk 10:35", refs=["Mt 10:8"], wesley="Dispensário médico gratuito de Wesley em Londres (1746)"),
    dict(id=9, grupo="A", acao="Cure e ore pelos enfermos", como="Imponha as mãos e ore pela cura de um doente, em nome de Jesus, hoje.",
         base="Mt 10:8", refs=["Lk 10:9", "Mk 16:18", "Jn 14:12"], wesley=""),
    dict(id=10, grupo="A", acao="Faça o bem sem esperar o dia certo", como="Não adie o socorro por causa de regra, horário ou agenda: salvar a vida vem antes.",
         base="Mk 3:4", refs=["Mt 12:11", "Mt 12:12", "Lk 6:9", "Lk 13:15", "Lk 13:16", "Lk 14:5", "Mk 2:27"], wesley=""),
    dict(id=11, grupo="A", acao="Receba e proteja uma criança", como="Acolha, alimente ou defenda uma criança em nome de Jesus; não a afaste nem a humilhe.",
         base="Mt 18:5", refs=["Mk 9:37", "Lk 9:48", "Mt 19:14", "Mk 10:14", "Lk 18:16", "Mt 18:10", "Mt 18:6", "Mk 9:42", "Lk 17:2"], wesley="Orfanato Bethesda de George Whitefield (Savannah, 1740); escola de Kingswood (1748)"),
    dict(id=12, grupo="A", acao="Alivie o fardo de alguém", como="Ajude a carregar um peso concreto: uma sacola, um formulário, uma fila, uma dívida burocrática.",
         base="Mt 23:4", refs=["Lk 11:46"], wesley=""),
    dict(id=13, grupo="A", acao="Vá a segunda milha", como="Faça mais do que lhe foi pedido ou exigido: entregue além, fique mais, leve até o fim.",
         base="Mt 5:41", refs=["Mt 5:40"], wesley=""),
    # ---------------------------------------------------------------- B. ALMA
    dict(id=14, grupo="B", acao="Conte a alguém o que Deus fez por você", como="Diga hoje, a uma pessoa, com suas palavras, o que o Senhor fez na sua vida.",
         base="Mk 5:19", refs=["Lk 8:39", "Lk 24:48", "Jn 15:27", "Mt 10:27"], wesley="Testemunho pessoal nas reuniões de classe"),
    dict(id=15, grupo="B", acao="Anuncie o Reino de Deus", como="Fale do evangelho a alguém que ainda não ouviu; comece pelos pobres.",
         base="Mt 10:7", refs=["Mk 16:15", "Lk 9:60", "Lk 24:47", "Lk 4:18", "Mt 4:19", "Mk 1:17", "Lk 5:10", "Jn 20:21", "Jn 17:18", "Jn 4:35", "Jn 4:38"],
         wesley="Pregação ao ar livre aos mineiros de Kingswood (Whitefield e Wesley, 1739)"),
    dict(id=16, grupo="B", acao="Convide alguém para a mesa, a igreja e a fé", como="Faça um convite pessoal hoje a quem está de fora: para a refeição, o culto, o grupo.",
         base="Lk 14:23", refs=["Lk 14:21", "Mt 22:9", "Mt 22:10", "Lk 19:5"], wesley=""),
    dict(id=17, grupo="B", acao="Confesse Jesus diante das pessoas", como="Não esconda a sua fé quando a ocasião pedir; diga de quem você é.",
         base="Mt 10:32", refs=["Lk 12:8", "Mt 5:16", "Mt 5:14", "Jn 13:35"], wesley=""),
    dict(id=18, grupo="B", acao="Ore pelos que o perseguem e abençoe quem o amaldiçoa", como="Nomeie na oração, agora, a pessoa que o feriu; peça bem para ela.",
         base="Mt 5:44", refs=["Lk 6:28", "Lk 23:34"], wesley=""),
    dict(id=19, grupo="B", acao="Ensine alguém a guardar o que Jesus ordenou", como="Leia e explique uma instrução de Jesus a uma pessoa; acompanhe-a na prática.",
         base="Mt 28:20", refs=["Mt 28:19", "Mt 5:19", "Mt 13:52"], wesley="Reuniões de classe e de banda: instrução e exame mútuo semanal"),
    dict(id=20, grupo="B", acao="Vá atrás de quem se afastou", como="Procure hoje a pessoa que sumiu da igreja, do grupo ou da família; vá até ela.",
         base="Mt 18:12", refs=["Lk 15:4", "Mt 18:14", "Lk 15:7"], wesley="Visita aos membros ausentes das classes"),
    dict(id=21, grupo="B", acao="Fortaleça um irmão abalado", como="Ligue, visite ou escreva a alguém desanimado ou tentado; firme-o na fé.",
         base="Lk 22:32", refs=["Jn 21:15", "Jn 21:16", "Jn 21:17", "Jn 10:11"], wesley="Regras Gerais: 'exortar'"),
    dict(id=22, grupo="B", acao="Peça ao Senhor da seara que envie obreiros", como="Ore agora por mais pessoas dispostas a servir; ofereça-se.",
         base="Mt 9:38", refs=["Lk 10:2", "Mt 9:37"], wesley=""),
    # ---------------------------------------------------------------- C. RECONCILIAÇÃO
    dict(id=23, grupo="C", acao="Perdoe quem o ofendeu", como="Decida agora perdoar de coração a pessoa que lhe deve algo; faça isso antes de orar.",
         base="Mk 11:25", refs=["Mt 6:14", "Mt 6:15", "Mt 18:22", "Mt 18:35", "Lk 6:37", "Lk 17:4", "Mt 6:12", "Lk 11:4", "Mt 18:33", "Jn 20:23"], wesley=""),
    dict(id=24, grupo="C", acao="Procure quem tem algo contra você e reconcilie-se", como="Antes de qualquer ato religioso, vá até a pessoa que você ofendeu e acerte.",
         base="Mt 5:24", refs=["Mt 5:23", "Mt 5:25", "Lk 12:58"], wesley="Holy Club: 'Há alguém a quem devo pedir perdão?'"),
    dict(id=25, grupo="C", acao="Repreenda a sós quem pecou contra você", como="Fale em particular, com respeito, para ganhar o irmão; só depois envolva outros.",
         base="Mt 18:15", refs=["Mt 18:16", "Mt 18:17", "Lk 17:3"], wesley="Regras Gerais: 'repreender'"),
    dict(id=26, grupo="C", acao="Não julgue nem condene; julgue com justiça", como="Antes de criticar, tire a sua trave; não decida pela aparência.",
         base="Mt 7:1", refs=["Mt 7:5", "Lk 6:37", "Lk 6:42", "Jn 7:24", "Jn 8:7", "Mt 7:3", "Lk 6:41"], wesley="Regras Gerais: 'não falar mal de ninguém'"),
    dict(id=27, grupo="C", acao="Faça as pazes com alguém", como="Resolva hoje uma briga pendente; seja o primeiro a estender a mão.",
         base="Mk 9:50", refs=["Mt 5:9", "Mt 5:22", "Lk 10:5", "Mt 10:12"], wesley=""),
    dict(id=28, grupo="C", acao="Não revide; ofereça a outra face", como="Quando ofendido hoje, não retalie: responda com bem, não com igual.",
         base="Mt 5:39", refs=["Lk 6:29", "Mt 5:40", "Mt 26:52", "Jn 18:11"], wesley=""),
    # ---------------------------------------------------------------- D. DAR
    dict(id=29, grupo="D", acao="Dê a quem lhe pede", como="Não vire o rosto a quem pede ajuda hoje; dê o que puder, sem interrogatório.",
         base="Mt 5:42", refs=["Lk 6:30", "Lk 6:38", "Lk 11:41"], wesley="Regras Gerais: 'dar aos pobres'"),
    dict(id=30, grupo="D", acao="Dê em secreto", como="Faça a sua doação sem contar a ninguém, sem foto, sem placa; que a esquerda não saiba.",
         base="Mt 6:3", refs=["Mt 6:1", "Mt 6:2", "Mt 6:4"], wesley=""),
    dict(id=31, grupo="D", acao="Convide à mesa quem não pode retribuir", como="Chame para comer hoje um pobre, um doente, um desconhecido, não só amigos e parentes.",
         base="Lk 14:13", refs=["Lk 14:12", "Lk 14:14", "Mt 11:19", "Lk 7:34"], wesley="Festas de amor (love-feasts) abertas aos pobres"),
    dict(id=32, grupo="D", acao="Empreste sem esperar de volta", como="Empreste a quem precisa, sem juros e sem cobrar; se não voltar, deixe.",
         base="Lk 6:35", refs=["Lk 6:34", "Mt 5:42"], wesley="Fundo de empréstimos sem juros da Fundição (Londres, 1746)"),
    dict(id=33, grupo="D", acao="Dê da sua necessidade, não só do que sobra", como="Separe hoje uma oferta que lhe custe algo, como a viúva das duas moedas.",
         base="Mk 12:43", refs=["Mk 12:44", "Lk 21:3", "Lk 21:4"], wesley="Wesley: 'ganhe tudo o que puder, poupe tudo o que puder, dê tudo o que puder'"),
    dict(id=34, grupo="D", acao="Venda algo seu e dê aos pobres", como="Escolha um bem que você não precisa, venda ou doe, e entregue o valor a quem precisa.",
         base="Lk 12:33", refs=["Mt 19:21", "Mk 10:21", "Lk 18:22", "Lk 12:21", "Lk 16:9"], wesley="Wesley viveu com 28 libras e deu o restante até o fim da vida"),
    dict(id=35, grupo="D", acao="Lembre-se dos pobres que estão sempre perto", como="Identifique hoje um pobre ao seu alcance e faça-lhe o bem agora, 'quando quiser'.",
         base="Mk 14:7", refs=["Mt 26:11", "Jn 12:8", "Lk 16:25", "Lk 6:24"], wesley=""),
    dict(id=36, grupo="D", acao="Dê de graça o que recebeu de graça", como="Não cobre, nem em dinheiro nem em contrapartida, pelo bem que você faz em nome de Jesus.",
         base="Mt 10:8", refs=["Lk 10:7"], wesley=""),
    # ---------------------------------------------------------------- E. FAMÍLIA
    dict(id=37, grupo="E", acao="Honre e sustente seus pais", como="Ligue, visite ou envie ajuda concreta ao pai ou à mãe hoje; não use 'religião' como desculpa para não ajudar.",
         base="Mt 15:4", refs=["Mt 15:5", "Mt 15:6", "Mk 7:10", "Mk 7:11", "Mk 7:12", "Mt 19:19", "Mk 10:19", "Lk 18:20"], wesley=""),
    dict(id=38, grupo="E", acao="Proveja para quem depende de você", como="Garanta hoje o cuidado de um dependente seu, como Jesus entregou a mãe ao discípulo.",
         base="Jn 19:26", refs=["Jn 19:27", "Mt 7:11", "Mt 24:45", "Lk 12:42"], wesley=""),
    dict(id=39, grupo="E", acao="Guarde a fidelidade no olhar e na conduta", como="Desvie hoje o olhar impuro; honre o seu cônjuge em pensamento e atitude.",
         base="Mt 5:28", refs=["Mt 5:27", "Mt 5:32", "Mt 19:6", "Mt 19:9", "Mk 10:9", "Mk 10:11", "Mk 10:12", "Lk 16:18"], wesley="Holy Club: exame diário da pureza"),
    # ---------------------------------------------------------------- F. SERVIÇO
    dict(id=40, grupo="F", acao="Faça o serviço humilde que ninguém quer", como="Lave os pés: limpe, carregue, sirva à mesa, cuide do que é desagradável.",
         base="Jn 13:14", refs=["Jn 13:15", "Jn 13:17", "Mk 10:45", "Mt 20:28", "Lk 22:27", "Mk 9:35", "Mt 20:26", "Mt 20:27", "Mk 10:43", "Mk 10:44", "Lk 22:26", "Mt 23:11"], wesley=""),
    dict(id=41, grupo="F", acao="Ocupe o último lugar", como="Ceda hoje a vaga, o assento, o microfone, o crédito; não busque título nem destaque.",
         base="Lk 14:10", refs=["Lk 14:8", "Lk 14:11", "Mt 23:8", "Mt 23:9", "Mt 23:10", "Mt 23:12", "Lk 9:48", "Mt 18:4"], wesley=""),
    dict(id=42, grupo="F", acao="Fale a verdade sem jurar", como="Que o seu 'sim' seja sim e o 'não' seja não, hoje, em tudo o que combinar.",
         base="Mt 5:37", refs=["Mt 5:34", "Mt 5:35", "Mt 5:36", "Mt 12:36", "Mt 12:37"], wesley="Regras Gerais: 'não usar o nome de Deus em vão'"),
    dict(id=43, grupo="F", acao="Seja fiel no pouco e no alheio", como="Cuide hoje do que é dos outros (dinheiro, bens, tempo) com mais zelo do que do seu.",
         base="Lk 16:10", refs=["Lk 16:11", "Lk 16:12", "Mt 25:45"], wesley=""),
    dict(id=44, grupo="F", acao="Cumpra o seu dever sem esperar aplauso", como="Depois de fazer o que devia, diga: 'sou servo inútil; fiz o meu dever'.",
         base="Lk 17:10", refs=["Lk 12:48", "Mt 6:1"], wesley=""),
    # ---------------------------------------------------------------- G. PAZ, JUSTIÇA, CIDADANIA
    dict(id=45, grupo="G", acao="Pague o salário justo e no prazo", como="Acerte hoje com quem trabalhou para você; o trabalhador é digno do seu salário.",
         base="Lk 10:7", refs=["Mt 10:10", "Mt 20:8", "Mt 20:4", "Mt 20:13", "Mk 10:19"], wesley=""),
    dict(id=46, grupo="G", acao="Restitua o que tomou injustamente", como="Devolva hoje o que pegou, cobrou ou reteve de alguém; se possível, com acréscimo.",
         base="Lk 19:9", refs=["Mk 10:19", "Mt 23:25", "Mt 21:13", "Jn 2:16"], wesley="Holy Club: 'Devo algo a alguém?'"),
    dict(id=47, grupo="G", acao="Dê a César o que é de César", como="Pague o imposto, a taxa, a conta devida; não dê escândalo por sonegar.",
         base="Mt 22:21", refs=["Mk 12:17", "Lk 20:25", "Mt 17:27", "Mt 17:26"], wesley=""),
    dict(id=48, grupo="G", acao="Resolva a disputa antes do tribunal", como="Procure hoje o acordo com quem o processa ou com quem você tem contenda.",
         base="Mt 5:25", refs=["Lk 12:58", "Mt 5:26"], wesley=""),
    dict(id=49, grupo="G", acao="Defenda a viúva e o pequenino contra quem os explora", como="Não participe nem se cale diante de quem tira o pouco de quem tem pouco.",
         base="Mk 12:40", refs=["Lk 20:47", "Mt 23:14", "Mt 23:23", "Lk 11:42", "Lk 18:3", "Lk 18:5", "Mt 25:40"], wesley="Wesley contra a escravidão: 'Thoughts upon Slavery' (1774)"),
    dict(id=50, grupo="G", acao="Não impeça quem faz o bem em nome de Jesus", como="Coopere hoje com outra igreja ou grupo que ajuda; não compita, não proíba.",
         base="Mk 9:39", refs=["Mk 9:40", "Lk 9:50"], wesley=""),
    dict(id=51, grupo="G", acao="Saúde a todos, não só os seus", como="Cumprimente e deseje paz, hoje, a quem não é do seu círculo: o vizinho, o estranho, o adversário.",
         base="Mt 5:47", refs=["Mt 10:12", "Lk 10:5", "Lk 10:6", "Mt 10:13"], wesley=""),
    dict(id=52, grupo="G", acao="Faça aos outros o que quer para si", como="Antes de cada decisão de hoje, pergunte: é isso que eu gostaria que fizessem comigo?",
         base="Mt 7:12", refs=["Lk 6:31", "Mt 22:39", "Mk 12:31", "Lk 10:28", "Lk 10:37", "Jn 13:34", "Jn 15:12", "Jn 15:17", "Lk 6:36"],
         wesley="Regras Gerais: 'fazer o bem de todas as formas possíveis, a todas as pessoas'"),
]
