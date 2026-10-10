# -*- coding: utf-8 -*-
"""Atividades que a ONG Santidade Integral em Cristo pratica (ou planeja) em obediência a cada dever social.

PROPOSTA INICIAL, elaborada a partir dos documentos institucionais já existentes (Anamnese Social da Família,
Prestação de Contas, Política de Boas Práticas). Deve ser validada pela diretoria: ajuste o status de cada item.

STATUS: "Praticada" | "Em implantação" | "A definir"
Formato: código da categoria → lista de (atividade, status, evidência/instrumento)
"""

ATIVIDADES = {
    "ALIM": [
        ("Entrega mensal de cestas básicas às famílias cadastradas", "Praticada", "Anamnese Social (item 1); Prestação de Contas (itens 2 e 5)"),
        ("Controle de estoque de alimentos com validade, para que 'nada se perca'", "Praticada", "Prestação de Contas (item 5)"),
        ("Triagem de insegurança alimentar (EBIA) para priorizar quem tem fome hoje", "Praticada", "Anamnese Social (item 6)"),
        ("Doação de roupas e itens de higiene", "A definir", ""),
    ],
    "ENF": [
        ("Entrega de medicamentos mediante prescrição, com conferência de lote e validade", "Praticada", "Anamnese Social (item 5); Política de Boas Práticas (5)"),
        ("Visitas domiciliares a enfermos, acamados e idosos", "Praticada", "Anamnese Social (item 12: registro de acompanhamento)"),
        ("Encaminhamento à UBS/ESF, CAPS e CRAS/CREAS", "Praticada", "Anamnese Social (item 10: encaminhamentos)"),
        ("Visita e apoio a pessoas presas e suas famílias", "A definir", ""),
    ],
    "ESTR": [
        ("Acolhida sem distinção de credo, origem ou situação, com entrega em local e horário dignos", "Praticada", "Política de Boas Práticas (5)"),
        ("Atendimento a migrantes e pessoas em situação de rua", "A definir", ""),
        ("Refeições ou encontros comunitários com as famílias atendidas", "A definir", ""),
    ],
    "DAR": [
        ("Ajuda sem contrapartida: nenhuma assistência é condicionada à adesão religiosa", "Praticada", "Política de Boas Práticas (5)"),
        ("Entrega discreta e sigilosa ('que a mão esquerda não saiba'): sem exposição do beneficiário", "Praticada", "Política de Boas Práticas (5); LGPD"),
        ("Captação de doadores pessoas físicas, jurídicas e igrejas parceiras", "Praticada", "Prestação de Contas (item 3)"),
        ("Prioridade a quem 'não tem com que retribuir' (critérios objetivos de vulnerabilidade)", "Praticada", "Anamnese Social (itens 7 e 10)"),
    ],
    "AMAR": [
        ("Atendimento com dignidade e respeito, sem filas vexatórias ou discursos constrangedores", "Praticada", "Política de Boas Práticas (5)"),
        ("Inclusão por critérios objetivos, sem favorecimento pessoal", "Praticada", "Declaração de Conformidade"),
        ("Plano de Desenvolvimento Familiar: amar ao próximo com vistas à sua autonomia", "Praticada", "Anamnese Social (item 11)"),
    ],
    "PERD": [
        ("Mediação de conflitos familiares identificados na anamnese", "A definir", "Anamnese Social (item 8: situações de risco)"),
        ("Aconselhamento e reconciliação com apoio das igrejas parceiras", "A definir", ""),
    ],
    "FAM": [
        ("Anamnese Social da Família: cadastro de toda a composição familiar e plano pactuado", "Praticada", "Anamnese Social"),
        ("Fortalecimento de vínculos e atenção a idosos e pais dependentes no domicílio", "Praticada", "Anamnese Social (itens 3 e 8)"),
        ("Projetos de geração de renda que permitam à família sustentar os seus", "Praticada", "Anamnese Social (item 11)"),
    ],
    "VULN": [
        ("Prioridade a crianças, idosos, gestantes, pessoas com deficiência e viúvas", "Praticada", "Anamnese Social (item 3)"),
        ("Sigilo de dados e proibição de exposição de beneficiários em imagens", "Praticada", "Política de Boas Práticas (5); LGPD"),
        ("Encaminhamento ao Conselho Tutelar/CREAS em situações de violência ou negligência", "Praticada", "Anamnese Social (item 10)"),
        ("Nenhum dirigente ou voluntário se beneficia dos recursos (não 'devorar casas de viúvas')", "Praticada", "Política de Boas Práticas (4)"),
    ],
    "JUSTV": [
        ("Prestação de contas mensal com balancete conciliado e parecer do Conselho Fiscal", "Praticada", "Prestação de Contas Mensal"),
        ("Comprovantes, três cotações, princípio dos quatro olhos", "Praticada", "Política de Boas Práticas (4)"),
        ("Orientação sobre direitos: CadÚnico, BPC, Bolsa Família, documentação", "Praticada", "Anamnese Social (itens 7 e 10)"),
        ("Declaração anual de conformidade assinada pela diretoria", "Praticada", "Declaração de Conformidade"),
    ],
    "SERV": [
        ("Trabalho voluntário; dirigentes e conselheiros não remunerados", "Praticada", "Política de Boas Práticas (4)"),
        ("Voluntário como acompanhante da família, não como superior", "Praticada", "Anamnese Social (item 11: plano pactuado)"),
        ("Formação de voluntários em liderança servidora", "A definir", ""),
    ],
    "CIV": [
        ("Regularidade legal, fiscal e contábil da organização (ITG 2002, MROSC)", "Praticada", "Prestação de Contas; Política de Boas Práticas (3)"),
        ("Parcerias com o poder público prestadas de contas conforme o termo", "Praticada", "Prestação de Contas (item 3)"),
        ("Apoio à regularização documental dos beneficiários", "Praticada", "Anamnese Social (item 9)"),
    ],
    "PAZ": [
        ("Cultura de paz e não-violência no atendimento e nas comunidades", "A definir", ""),
        ("Canal de dúvidas e denúncias sem retaliação", "Praticada", "Política de Boas Práticas (6)"),
    ],
    "EVANG": [
        ("Apresentação do evangelho e oração oferecidas, nunca impostas, no atendimento", "Em implantação", ""),
        ("Parceria com igrejas locais que acolhem as famílias", "Praticada", "Prestação de Contas (item 3)"),
        ("Boas obras públicas e transparentes 'para que glorifiquem o Pai'", "Praticada", "Política de Boas Práticas (6)"),
    ],
    "DISC": [
        ("Acompanhamento continuado das famílias (visitas e reavaliações do plano)", "Praticada", "Anamnese Social (item 12)"),
        ("Grupos de estudo bíblico e discipulado para beneficiários e voluntários", "A definir", ""),
        ("Formação de voluntários nos documentos 'Mandamentos de Jesus' e 'Deveres Sociais'", "Em implantação", "este repositório"),
    ],
}
