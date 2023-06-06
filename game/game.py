import random, pygame, sys
from pygame.locals import *

FPS = 30 # кадров в секунду, общая скорость работы программы
WINDOWWIDTH = 640 # размер ширины окна в пикселях
WINDOWHEIGHT = 480 # размер высоты окон в пикселях
REVEALSPEED = 8 # выдвижные ящики speed boxes открывают и закрывают рубашки клеток
BOXSIZE = 40 # размер высоты и ширины коробки в пикселях
GAPSIZE = 10 # размер промежутка между ячейками в пикселях
BOARDWIDTH = 10 # количество столбцов с иконками
BOARDHEIGHT = 7 # количество рядов значков

assert (BOARDWIDTH * BOARDHEIGHT) % 2 == 0, 'Board needs to have an even number of boxes for pairs of matches.'
XMARGIN = int((WINDOWWIDTH - (BOARDWIDTH * (BOXSIZE + GAPSIZE))) / 2)
YMARGIN = int((WINDOWHEIGHT - (BOARDHEIGHT * (BOXSIZE + GAPSIZE))) / 2)
# Для того, чтобы игровая программа могла создавать иконки всех возможных комбинаций цветов и форм, нам нужен кортеж для хранения всех этих значений.
# У нас должно быть игровое поле общей площадью 70 квадратов (35 × 2 или 7 × 5 × 2).

#            R    G    B
GRAY     = (100, 100, 100)
NAVYBLUE = ( 60,  60, 100)
WHITE    = (255, 255, 255)
RED      = (255,   0,   0)
GREEN    = (  0, 255,   0)
BLUE     = (  0,   0, 255)
YELLOW   = (255, 255,   0)
ORANGE   = (255, 128,   0)
PURPLE   = (255,   0, 255)
CYAN     = (  0, 255, 255)

BGCOLOR = NAVYBLUE
LIGHTBGCOLOR = GRAY
BOXCOLOR = WHITE
HIGHLIGHTCOLOR = BLUE

DONUT = 'donut'
SQUARE = 'square'
DIAMOND = 'diamond'
LINES = 'lines'
OVAL = 'oval'

ALLCOLORS = (RED, GREEN, BLUE, YELLOW, ORANGE, PURPLE, CYAN)
ALLSHAPES = (DONUT, SQUARE, DIAMOND, LINES, OVAL)
assert len(ALLCOLORS) * len(ALLSHAPES) * 2 >= BOARDWIDTH * BOARDHEIGHT, "Board is too big for the number of shapes/colors defined."

def main():
    global FPSCLOCK, DISPLAYSURF
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))

    mousex = 0 # используется для хранения координаты x события мыши
    mousey = 0 # используется для хранения координаты y события мыши
    pygame.display.set_caption('Memory Game')

    mainBoard = getRandomizedBoard()
    revealedBoxes = generateRevealedBoxesData(False)

    firstSelection = None # сохраняет значение (x, y) первого щелкнутого поля

    DISPLAYSURF.fill(BGCOLOR)
    startGameAnimation(mainBoard)

    while True: # основной игровой цикл
        mouseClicked = False

        DISPLAYSURF.fill(BGCOLOR) # рисование окна
        drawBoard(mainBoard, revealedBoxes)

        for event in pygame.event.get(): # цикл обработки событий
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                mousex, mousey = event.pos
            elif event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos
                mouseClicked = True

        boxx, boxy = getBoxAtPixel(mousex, mousey)
        if boxx != None and boxy != None:
            # В данный момент мышь находится над полем
            if not revealedBoxes[boxx][boxy]:
                drawHighlightBox(boxx, boxy)
            if not revealedBoxes[boxx][boxy] and mouseClicked:
                revealBoxesAnimation(mainBoard, [(boxx, boxy)])
                revealedBoxes[boxx][boxy] = True # установите флажок "открыто"
                if firstSelection == None: # текущее поле было первым, на котором был щелчок
                    firstSelection = (boxx, boxy)
                else: # текущее поле было вторым, на которое был нажат щелчок
                    # Проверка совпадений между двумя значками
                    icon1shape, icon1color = getShapeAndColor(mainBoard, firstSelection[0], firstSelection[1])
                    icon2shape, icon2color = getShapeAndColor(mainBoard, boxx, boxy)

                    if icon1shape != icon2shape or icon1color != icon2color:
                        # Значки не совпадают. Повторно закрываются обе иконки.
                        pygame.time.wait(1000) # 1000 миллисекунд = 1 секунда
                        coverBoxesAnimation(mainBoard, [(firstSelection[0], firstSelection[1]), (boxx, boxy)])
                        revealedBoxes[firstSelection[0]][firstSelection[1]] = False
                        revealedBoxes[boxx][boxy] = False
                    elif hasWon(revealedBoxes): # проверьте, все ли пары найдены
                        gameWonAnimation(mainBoard)
                        pygame.time.wait(2000)

                        # Перезагрузите поле
                        mainBoard = getRandomizedBoard()
                        revealedBoxes = generateRevealedBoxesData(False)

                        # Покажите на секунду полностью нераскрытую доску
                        drawBoard(mainBoard, revealedBoxes)
                        pygame.display.update()
                        pygame.time.wait(1000)

                        # Воспроизведите анимацию начала игры
                        startGameAnimation(mainBoard)
                    firstSelection = None # сбросить первую переменную firstSelection

        # Перезагрузите экран и подождите
        pygame.display.update()
        FPSCLOCK.tick(FPS)


def generateRevealedBoxesData(val): #Функции generateRevealedBoxesData() необходимо создать список логических значений.
    # Логическим значением будет только значение, переданное функции в качестве параметра val.
    # Мы начинаем с переменной структуры данных revealBoxes в виде пустого списка.
    revealedBoxes = []
    for i in range(BOARDWIDTH):
        revealedBoxes.append([val] * BOARDHEIGHT)
    return revealedBoxes


def getRandomizedBoard(): #Структура данных доски - это список кортежей, в котором каждый кортеж имеет два значения:
    # одно - форма значка, а другое - цвет значка.
    # Получите список всех возможных форм во всех возможных цветах
    icons = []
    for color in ALLCOLORS:
        for shape in ALLSHAPES:
            icons.append( (shape, color) )

    random.shuffle(icons) # измените порядок расположения значков в списке случайным образом
    numIconsUsed = int(BOARDWIDTH * BOARDHEIGHT / 2) # подсчитайте, сколько значков необходимо
    icons = icons[:numIconsUsed] * 2 # использует фрагмент списка, чтобы получить первое использованное количество значков в списке.
    random.shuffle(icons) # вызываем метод shuffle(), чтобы случайным образом перемешать порядок значков.

    # Создайте структуру данных доски со случайно расположенными значками
    board = []
    for x in range(BOARDWIDTH):
        column = []
        for y in range(BOARDHEIGHT):
            column.append(icons[0])
            del icons[0] # удаляйте значки по мере того, как мы их находим
        board.append(column)
    return board


def splitIntoGroupsOf(groupSize, theList):
    # Функция splitIntoGroupsOf() (которая будет вызвана функцией startGameAnimation())
    # разделяет список и помещает его в новый список в виде элемента списка,
    # где внутренний список содержит список количественных элементов groupsize.
    result = []
    for i in range(0, len(theList), groupSize):# В строке 160 при разрезании списка на части с помощью параметра List[i:i + groupSize] создается список
        # , добавленный в список результатов. На каждой итерации, где i равно 0, 8 и 16 (а groupSize равно 8),
        # выражением фрагмента списка будет список [0: 8]
        # , затем список [8:16] на второй итерации, а затем список [16:24] на третьей итерации.
        result.append(theList[i:i + groupSize])
    return result


def leftTopCoordsOfBox(boxx, boxy):
    # Преобразуйте координаты доски в пиксельные координаты
    left = boxx * (BOXSIZE + GAPSIZE) + XMARGIN
    top = boxy * (BOXSIZE + GAPSIZE) + YMARGIN
    return (left, top)
    # Функция · leftTopCoordsOfBox() · принимает координаты прямоугольника и пиксельные координаты.
    # Поскольку поле занимает несколько пикселей на экране, мы всегда будем возвращать один пиксель в верхнем левом углу поля.
    # Значение возвращается в виде двух целых кортежей.
    # Когда нам нужно нарисовать пиксельные координаты этих блоков, мы часто вызываем leftTopCoordsOfBox().



def getBoxAtPixel(x, y):
    for boxx in range(BOARDWIDTH): # диапазон ширины
        for boxy in range(BOARDHEIGHT): # даиапазон высоты
            left, top = leftTopCoordsOfBox(boxx, boxy)
            boxRect = pygame.Rect(left, top, BOXSIZE, BOXSIZE)
            if boxRect.collidepoint(x, y):
                return (boxx, boxy)
    return (None, None)
# Нам также нужна функция для преобразования координат пикселей (координат, используемых для событий щелчка мыши и перемещения мыши) в координаты поля
# (чтобы мы могли узнать, в каком поле происходит событие мыши).
# Объект Rect имеет метод collidepoint(). Вы также можете передавать координаты X и Y.
# Если координаты находятся в области прямоугольного объекта (т. Е. столкновения), он вернет значение True.


def drawIcon(shape, color, boxx, boxy): # Однако во многих вызовах функций рисования фигур также используется средняя точка
    # прямоугольника и точки по четырем углам.
    # Мы можем вычислить его и сохранить в переменных quarter и half.
    quarter = int(BOXSIZE * 0.25)
    half = int(BOXSIZE * 0.5)

    left, top = leftTopCoordsOfBox(boxx, boxy) # получите пиксельные координаты из координат доски
    # Рисуются фигуры
    if shape == DONUT:
        pygame.draw.circle(DISPLAYSURF, color, (left + half, top + half), half - 5)
        pygame.draw.circle(DISPLAYSURF, BGCOLOR, (left + half, top + half), quarter - 5)
    elif shape == SQUARE:
        pygame.draw.rect(DISPLAYSURF, color, (left + quarter, top + quarter, BOXSIZE - half, BOXSIZE - half))
    elif shape == DIAMOND:
        pygame.draw.polygon(DISPLAYSURF, color, ((left + half, top), (left + BOXSIZE - 1, top + half), (left + half, top + BOXSIZE - 1), (left, top + half)))
    elif shape == LINES:
        for i in range(0, BOXSIZE, 4):
            pygame.draw.line(DISPLAYSURF, color, (left, top + i), (left + i, top))
            pygame.draw.line(DISPLAYSURF, color, (left + i, top + BOXSIZE - 1), (left + BOXSIZE - 1, top + i))
    elif shape == OVAL:
        pygame.draw.ellipse(DISPLAYSURF, color, (left, top + quarter, BOXSIZE, half))


def getShapeAndColor(board, boxx, boxy):
    # значение формы для точек x, y сохраняется на доске[x][y][0]
    # значение цвета для точек x, y сохраняется на плате[x][y][1]
    return board[boxx][boxy][0], board[boxx][boxy][1]


def drawBoxCovers(board, boxes, coverage):
    #Рисует коробки, которые закрываются / раскрываются
    # из списков из двух элементов, в которых есть точки x и y в поле
    for box in boxes:
        left, top = leftTopCoordsOfBox(box[0], box[1]) # Функция leftTopCoordsOfBox() возвращает пиксельные координаты верхнего левого угла окна.
        pygame.draw.rect(DISPLAYSURF, BGCOLOR, (left, top, BOXSIZE, BOXSIZE))
        shape, color = getShapeAndColor(board, box[0], box[1])
        drawIcon(shape, color, box[0], box[1])
        if coverage > 0: # рисуется обложка только в том случае, если есть покрытие
            pygame.draw.rect(DISPLAYSURF, BOXCOLOR, (left, top, coverage, BOXSIZE))
    pygame.display.update()
    FPSCLOCK.tick(FPS)


def revealBoxesAnimation(board, boxesToReveal):
    # делается анимация "раскрытия иконки"
    for coverage in range(BOXSIZE, (-REVEALSPEED) - 1, -REVEALSPEED):
        drawBoxCovers(board, boxesToReveal, coverage)# В строке 12 мы устанавливаем эту константу равной 8, что означает, что при каждом вызове drawBoxCovers()
        # белый прямоугольник будет уменьшаться на 8 пикселей за итерацию.


def coverBoxesAnimation(board, boxesToCover):
    # делается анимация "обложки иконки"
    for coverage in range(0, BOXSIZE + REVEALSPEED, REVEALSPEED):
        drawBoxCovers(board, boxesToCover, coverage)# В строке 12 мы устанавливаем эту константу равной 8, что означает, что при каждом вызове drawBoxCovers()
        # белый прямоугольник увеличиваться на 8 пикселей за итерацию.


def drawBoard(board, revealed):
    # Рисует все ячейки в их закрытом или раскрытом состоянии
    for boxx in range(BOARDWIDTH):
        for boxy in range(BOARDHEIGHT):
            left, top = leftTopCoordsOfBox(boxx, boxy)
            if not revealed[boxx][boxy]:
                #Нарисуется закрытая иконка
                pygame.draw.rect(DISPLAYSURF, BOXCOLOR, (left, top, BOXSIZE, BOXSIZE))
            else:
                #Нарисуется открытая иконка
                shape, color = getShapeAndColor(board, boxx, boxy)
                drawIcon(shape, color, boxx, boxy)
                # Функция drawBoard() вызывает DrawIcon() из поля на доске. Вложенный цикл for в строках 236 и 237 пересечет все возможные координаты X и Y
                # прямоугольника и нарисует значок или белый квадрат в этой позиции (для представления закрытого прямоугольника).

def drawHighlightBox(boxx, boxy):
    left, top = leftTopCoordsOfBox(boxx, boxy)
    pygame.draw.rect(DISPLAYSURF, HIGHLIGHTCOLOR, (left - 5, top - 5, BOXSIZE + 10, BOXSIZE + 10), 4)
    # Чтобы помочь игрокам понять, что они могут нажать на закрытое поле, чтобы отобразить его, мы выделим его синим контуром вокруг поля.
    # Этот профиль создается с помощью вызова pyGame draw. Rect() для создания прямоугольника шириной в 4 пикселя.


def startGameAnimation(board):
    coveredBoxes = generateRevealedBoxesData(False)
    boxes = [] # сначала создадим список всех возможных мест на доске
    for x in range(BOARDWIDTH):
        for y in range(BOARDHEIGHT):
            boxes.append( (x, y) )
    random.shuffle(boxes) # Чтобы изменить поле в начале каждой игры, мы вызовем функцию random Shuffle(),
    # чтобы случайным образом нарушить порядок кортежей в списке полей
    boxGroups = splitIntoGroupsOf(8, boxes)
    # Чтобы получить список из 8 блоков, мы вызываем нашу функцию splitIntoGroupsOf(), передавая списки 8 и box.
    # Список в списке, возвращаемом функцией, хранится в переменной с именем boxGroups.

    drawBoard(board, coveredBoxes)
    for boxGroup in boxGroups:
        revealBoxesAnimation(board, boxGroup) # начало анимации \ отображение
        coverBoxesAnimation(board, boxGroup) # развертывание анимации
        # выполнение анимации откурытия иконки


def gameWonAnimation(board):
    # мигает цвет фона, когда игрок выиграл
    coveredBoxes = generateRevealedBoxesData(True)
    color1 = LIGHTBGCOLOR
    color2 = BGCOLOR

    for i in range(13):
        color1, color2 = color2, color1 # смена цвета
        DISPLAYSURF.fill(color1)
        drawBoard(board, coveredBoxes)
        pygame.display.update()
        pygame.time.wait(300) # отображение цветов на экране игры


def hasWon(revealedBoxes):
    # Возвращает значение True, если все поля были открыты, в противном случае значение False
    for i in revealedBoxes:
        if False in i:
            return False # возвращает значение False, если какие-либо поля закрыты
    return True


if __name__ == '__main__':
    main()