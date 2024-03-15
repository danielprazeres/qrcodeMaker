import qrcode
from PIL import Image

# Dados que você deseja que o QR Code contenha
data = "https://www.mconfea.com/in%C3%ADcio/nossos-links"

# Gerando o QR Code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,  # Alta correção de erro
    box_size=10,
    border=4,
)
qr.add_data(data)
qr.make(fit=True)

# Criando uma imagem do QR Code
img_qr = qr.make_image(fill_color="#14212D", back_color="white").convert('RGB')

# Carregando a logo
logo = Image.open("/Users/danielprazeres/Downloads/Ativo 3-100.jpg")  # Substitua pelo caminho correto da sua logo
# Tamanho da logo no QR Code, ajuste conforme necessário
logo_size = 100  # ou qualquer tamanho que você achar adequado para a sua logo

# Tamanho da margem branca ao redor da logo
margin_size = 10  # Ajuste conforme necessário para criar uma margem branca visível


# Calculando as dimensões da logo
width, height = img_qr.size
logo = logo.resize((logo_size, logo_size))

# Criando uma imagem de fundo branca maior que a logo para a margem
logo_with_margin_size = (logo_size + margin_size * 2, logo_size + margin_size * 2)
background = Image.new('RGB', logo_with_margin_size, 'white')
background.paste(logo, (margin_size, margin_size))

# Calculando posição para colocar a logo com margem no meio do QR Code
box = (
    (width - logo_with_margin_size[0]) // 2,
    (height - logo_with_margin_size[1]) // 2,
    (width + logo_with_margin_size[0]) // 2,
    (height + logo_with_margin_size[1]) // 2
)

# Colocando a logo com margem branca no QR Code
img_qr.paste(background, box)

# Salvando o QR Code com logo
img_qr.save("/Users/danielprazeres/Downloads/meu_qr_code_com_logo2.png")