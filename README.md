# Peso do Boi

Aplicativo de linha de comando que calcula as quantidades e os valores unitários
dos cortes de carne a partir dos pesos e valores informados para as peças do boi.
Ao final, gera o arquivo `cortes_calculados.txt` no formato de importação
separado por ponto e vírgula.

## Requisitos

- Python 3
- Os arquivos `main.py` e `cortes.py` na mesma pasta

O programa usa apenas a biblioteca padrão do Python e o módulo local `cortes.py`.

## Como executar

Abra um terminal na pasta do projeto e execute:

```powershell
python main.py
```

Informe o peso em quilogramas de cada peça:

- Dianteiro
- Traseiro
- Ponta de agulha com fraldinha
- Ponta de agulha sem fraldinha

Para cada peça com peso maior que zero, informe também o valor total em reais.
Os números podem ser digitados com ponto ou vírgula decimal. Peso zero indica que
a peça não será considerada no preço por quilo.

## Cálculo

Os cortes e seus fatores de peso estão definidos em `cortes.py`. A quantidade de
cada corte é calculada pela soma do peso de cada peça multiplicado pelo fator
correspondente.

O preço por quilo de uma peça é calculado dividindo o valor total informado pelo
seu peso. O valor unitário exportado para cada corte é a média simples dos preços
por quilo das peças com peso positivo que possuem fator aplicável àquele corte.
Se nenhuma dessas peças tiver peso positivo, o valor unitário fica vazio no
arquivo exportado.

Pesos negativos não são aceitos. Cortes com quantidade zero são omitidos da
exportação.

## Arquivo exportado

O programa cria ou sobrescreve `cortes_calculados.txt` na pasta de execução.
Cada linha contém quatro campos separados por ponto e vírgula, nesta ordem:

1. Código do corte
2. Quantidade calculada
3. Quantidade da embalagem, fixa em `1`
4. Valor unitário calculado

Exemplo:

```text
1937;12,7803;1;10
```

Os valores são escritos com vírgula decimal e até quatro casas decimais,
removendo zeros finais.

## Gerar o executável

O projeto inclui a configuração `PesoDoBoi.spec` para gerar um executável no
Windows com o PyInstaller. Com o PyInstaller instalado, execute na pasta do
projeto:

```powershell
pyinstaller PesoDoBoi.spec
```

O executável será criado em `dist/PesoDoBoi.exe`.
