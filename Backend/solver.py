def resolver_selos(valor: int, denominacoes: list[int]):
    INF = float('inf')

    if not isinstance(valor, int) or valor <= 0:
        return {
            'possivel': False,
            'minimo': None,
            'combinacao': [],
            'denominacoes': [],
            'erro': 'O valor a selar deve ser um número inteiro positivo.',
        }

    if not denominacoes or any(not isinstance(d, int) or d <= 0 for d in denominacoes):
        return {
            'possivel': False,
            'minimo': None,
            'combinacao': [],
            'denominacoes': [],
            'erro': 'As denominações devem ser números inteiros positivos.',
        }

    dp = [INF] * (valor + 1)
    dp[0] = 0
    escolhas = [None] * (valor + 1)

    for i in range(1, valor + 1):
        for selo in denominacoes:
            if selo <= i and dp[i - selo] + 1 < dp[i]:
                dp[i] = dp[i - selo] + 1
                escolhas[i] = selo

    if dp[valor] == INF:
        return {
            'possivel': False,
            'minimo': None,
            'combinacao': [],
            'denominacoes': sorted(denominacoes),
            'erro': None,
        }

    combinacao = []
    atual = valor
    while atual > 0:
        selo_usado = escolhas[atual]
        combinacao.append(selo_usado)
        atual -= selo_usado

    return {
        'possivel': True,
        'minimo': dp[valor],
        'combinacao': sorted(combinacao, reverse=True),
        'denominacoes': sorted(denominacoes),
        'erro': None,
    }