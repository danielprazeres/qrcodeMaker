# qrcodeMaker

Este repositório contém um script Python simples para gerar QR Codes personalizados que incorporam uma logo centralizada. O QR Code é configurado para ter uma cor de preenchimento personalizada e uma margem branca ao redor da logo para melhorar a legibilidade.

## Requisitos

Para rodar este script, você precisará de Python instalado em seu sistema e as seguintes bibliotecas Python:

- Pillow
- qrcode

Instale-as usando o comando `pip`:
pip install Pillow qrcode


## Uso

Para gerar um QR Code com a sua logo, siga estes passos:

1. Clone este repositório para sua máquina local.
2. Substitua o URL na variável `data` dentro do arquivo `meu_qrcode.py` pelo link desejado.
3. Substitua o caminho da logo no arquivo `meu_qrcode.py` pelo caminho da sua imagem de logo.
4. Execute o script com `python meu_qrcode.py`.
5. O QR Code gerado será salvo no caminho especificado dentro do script.

## Configurações Personalizáveis

Dentro do script `meu_qrcode.py`, você pode personalizar as seguintes configurações:

- `fill_color` e `back_color`: Cores de preenchimento e de fundo do QR Code.
- `logo_size`: Tamanho da logo dentro do QR Code.
- `margin_size`: Tamanho da margem branca ao redor da logo.

## Exemplo de QR Code Gerado

Você pode incluir uma imagem de um QR Code de exemplo gerado pelo script, caso deseje.

![Exemplo de QR Code](https://github.com/danielprazeres/qrcodeMaker/assets/51274652/116334f6-e0cb-444b-b711-c20112ad12f7)

## Contribuindo

Se você gostaria de contribuir para este projeto, por favor faça um fork do repositório, faça suas mudanças, e submeta um pull request.
