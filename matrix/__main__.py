from PIL import Image, ImageFont, ImageDraw
from sexy.video import VideoEncoder
import random

FRAMERATE = 60
FONT_SIZE = 35
WIDTH, HEIGHT = 1920, 1080

class Rect:
    def __init__(self):
        self.w = FONT_SIZE
        self.h = random.random() * HEIGHT
        self.x = round(random.randint(0, WIDTH) / FONT_SIZE) * FONT_SIZE
        self.y = -self.h
        self.duration = random.random() * 10.0 + 3.0
        self.speed = (HEIGHT + self.h) / (FRAMERATE * self.duration)
        self.color = (0, random.randint(50, 255), 0, 255)

text = (
    'LAINFORMATICASEHAVUELTOUNAPARTEIMPORTANTE'
    'DENUESTRASVIDASALPUNTODETENERUNAGRAN'
    'DEPENDENCIAASUSSERVICIOSYAPLICACIONES'
    'PRINCIPALMENTELOSQUEUSAMOSENINTERNETOLANUBE'
    'SINEMBARGOENELTEMADELASEGURIDADINFORMATICA'
    'HAYUNAESCASESDEEDUCACIONHACIALOSUSUARIOSFINALES'
    'DEMANERAQUEESTOFACILITALAELROBODEINFORMACION'
    'ALOSHACKERSYCYBERDELINCUENTESQUIENESPUEDEN'
    'HACERCOMPRASILEGALESCONTARJETASCLONADAS'
    'ROBARCUENTASDEVIDEOJUEGOSEXTORCIONARPORFOTOS'
    'VERGONZOSASOINAPROPIADASSABOTEARSERVIDORES'
    'ENCRIPTARCOMPUTADORASREUTILIZARPALABRASDEPASO'
    'LASPOSIBILIDADESONINFINITASESPORESOQUEELMUNDO'
    'REQUIEREUNAMAYOREDUCACIONENCYBERSEGURIDAD'
    'TAMBIENCABEMENCIONARQUEDECADASDEINVESTIGACION'
    'ENMETODOSMATEMATICOSYALGORITMOSINFORMATICOS'
    'SEHALOGRADOPOCOAPOCOMITIGARUNAPARTEDELOS'
    'DEFECTOSDELOSSISTEMASINFORMATICOSYREDES'
    'SINEMBARGOMUCHOSDEELLOSYAHANSIDOVULNERADOS'
    'EINCLUSOHECHOOBSOLETOSPORLOSQUELOSEXPERTOS'
    'DEBENIRIDEANDONUEVASMANERASDEPROTEGERSEMEJOR'
    'CADAVEZDESAFORTUNADAMENTENOPUEDOAFIRMARQUEEXISTA'
    'LASEGURIDADPERFECTAESUNAGUERRADENUNCAACABAR'
    'DEMEJORARSEGURIDADYROMPERLAYLOMENOSQUEDEBEMOS'
    'HACERESTOMARMEDIDASDESEGURIDADPERSONALES'
    'COMONOSOLODESCARGARAPLICACIONESDESITIOSDECONFIANZA'
    'USARSOLOSITIOSWEBCONCIFRADOSSLPONERMASATENCIONCON'
    'QUESITIOSSECOMPARTENUESTRAINFORMACIONDEPAGO'
    'EVITARPUBLICARCOSASDEMASIADOPERSONALES'
    'QUEDENIDEADECUALESNUESTRARUTINADIARIA'
    'INFORMARSEALMOMENTODEVEROFERTASDEMASIADOBUENASPARASERCIERTAS'
    'INSTALARLASACTUALIZACIONESDESISTEMALOMASPRONTOPOSIBLE'
    'NOUTILIZALAMISMAPALABRADEPASOPARADIFERENTESCUENTASDEINTERNET'
    'NODUDESENPREGUNTARAALGUNEXPERTOENFINFORMATICAQUESEGURO'
    'HASDECONOCERAALAGUIENQUEPODRIAORIENTARTEPARAMEJORAR'
    'TUPRIVACIDADANONIMATOYEXPERIENCIAENINTERNETENGENERAL'
    'ESTONOVAPARARHAYQUESEGUIRBUSCANDOMEJORESMANERAS'
    'YTENGOLAESPERANZADETENERUNINTERNETMASSEGUROPARATODOS'
)

# print(len(text))

chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
nchars = len(chars)
image = Image.new('RGBA', (WIDTH, HEIGHT))
draw = ImageDraw.Draw(image)
rects = [Rect() for x in range(300)]

font = ImageFont.truetype('Courier New Bold.ttf', size=FONT_SIZE)
width, height = font.getsize('A')
max_x = int(round(WIDTH / FONT_SIZE))
max_y = int(round(HEIGHT / FONT_SIZE))

for y in range(max_y):
    for x in range(max_x):
        c = text[y * max_x + x]
        char_width, char_height = font.getsize(c)
        draw.text((x * FONT_SIZE, y * FONT_SIZE), c,
            font=font,
            fill=(0, 0, 0, 255)
        )

data = bytearray(image.tobytes())

for index in range(WIDTH * HEIGHT):
    data[index * 4 + 3] = 255 - data[index * 4 + 3]

mask = Image.frombytes('RGBA', (WIDTH, HEIGHT), bytes(data))

encoder = VideoEncoder(framerate=FRAMERATE, filename='aja.mp4')
encoder.do_pipe = False
encoder.start()

for frame in range(FRAMERATE * 60):
    draw.rectangle((0, 0, WIDTH, HEIGHT), fill=(0, 0, 0, 255))
    
    for rect in rects:
        draw.rectangle(
            (
                rect.x, rect.y,
                rect.x + rect.w,
                rect.y + rect.h
            ),
            fill=rect.color,
        )
        rect.y += rect.speed
        if rect.y >= HEIGHT:
            rect.y = -rect.h
            rect.x = round(random.randint(0, WIDTH) / FONT_SIZE) * FONT_SIZE
            rect.color = (0, random.randint(50, 255), 0, 255)

    image.alpha_composite(mask)
    encoder.append_frame(image)


    if frame % FRAMERATE == 0:
        print('{} frames ({} seconds) processed'.format(frame + 1, frame / FRAMERATE))

encoder.finalize()