import math


def formata_tamanho(tamanho_em_bytes: int,
                    base: int = 1024,
                    tamanho_real: bool = True) -> str:
    """Formata um tamanho, de bytes para o tamanho apropriado"""

    if not tamanho_real:
        base = 1000

    # Original:
    # https://stackoverflow.com/questions/5194057/better-way-to-convert-file-sizes-in-python

    # Se o tamanho for menor ou igual a 0, 0B.
    if tamanho_em_bytes <= 0:
        return "0B"

    # Tupla com os tamanhos
    #                      0    1     2     3     4     5
    abreviacao_tamanhos = "B", "KB", "MB", "GB", "TB", "PB"
    # Logaritmo -> https://brasilescola.uol.com.br/matematica/logaritmo.htm
    # math.log vai retornar o logaritmo do tamanho_em_bytes
    # com a base (1000 por padrão), isso deve bater
    # com o nosso índice na abreviação dos tamanhos
    indice_abreviacao_tamanhos = int(math.log(tamanho_em_bytes, base))
    # Por quanto nosso tamanho deve ser dividido para
    # gerar o tamanho correto.
    potencia = base ** indice_abreviacao_tamanhos
    # Nosso tamanho final
    tamanho_final = tamanho_em_bytes / potencia
    # A abreviação que queremos
    abreviacao_tamanho = abreviacao_tamanhos[indice_abreviacao_tamanhos]
    return f'{tamanho_final:.2f} {abreviacao_tamanho}'


if __name__ == "__main__":
    aaa = True

    print(formata_tamanho(1000, tamanho_real=aaa))
    print(formata_tamanho(1_000_000, tamanho_real=aaa))
    print(formata_tamanho(1_000_000_000, tamanho_real=aaa))
    print(formata_tamanho(1_000_000_000_000, tamanho_real=aaa))
    print(formata_tamanho(1_000_000_000_000_000, tamanho_real=aaa))