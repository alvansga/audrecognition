# BIGPROJECT5
# which one
# by ejra
# start date 3 agustus 2021
# finish date -------------

import pygame,sys,random, time
import speech_recognition as sr

from pygame.locals import *

# ===================================================
FPS = 60
WINDOW_W = 320
WINDOW_H = 480

COL_PANEL = 2
ROW_PANEL = 2

ROW_H = 200
COL_W = 160

#############
MAXLEVEL = 7
#############

#ukuran margin
# XMARGIN = int((WINDOW_W - (COL_PANEL * (UKURANMARBLE + UKURANCELAH))) / 2)
# YMARGIN = int((WINDOW_H - (ROW_PANEL * (UKURANMARBLE + UKURANCELAH))) / 2)
XMARGIN = 40
YMARGIN = 40

HEADER_X = 0
HEADER_Y = 0
HEADER_W = WINDOW_W
HEADER_H = 80

FOOTER_X = 0
FOOTER_Y = WINDOW_H-40
FOOTER_W = WINDOW_W
FOOTER_H = 40


TABLE = [80,80+160]

# warna yang dibutuhkan
#               R   G   B
PUTIH       = (255,255,255)
JINGGA      = (255,180,  0)
JINGGATUA   = (150, 75,  0)
UNGU        = (200, 10,255)
LIMEHIJAU   = (150,255,  0)
BIRU        = (170,100,255)
BIRUTUA     = (100,  0,150)
MERAH       = (255,  0,  0)
KUNING      = (255,255,  0)
HITAM       = (  0,  0,  0)
ABU2        = ( 10, 10, 10)
ABU2_1      = ( 20, 20, 20)

#dark theme
# BGCOLOR1 = HITAM
# BGCOLOR2 = ABU2

# MARBLECOLOR = ABU2_1
# MARBLECOLOR2 = HITAM
# RINGCOLOR = ABU2
# BOARDCOLOR = HITAM
# BOARDCOLOR2 = ABU2
# WINTEKSCOLOR = PUTIH

#original
BGCOLOR1 = BIRU
BGCOLOR2 = LIMEHIJAU

MARBLECOLOR = JINGGA
MARBLECOLOR2 = JINGGATUA
RINGCOLOR = PUTIH
BOARDCOLOR = BIRU
BOARDCOLOR2 = BIRUTUA
WINTEKSCOLOR = PUTIH


# gambar objek
MARBLE = 'marble'
CURMARBLE = 'curmarble'
RING = 'ring'

# ===================================================

def recognize_speech_from_mic(recognizer, microphone):
    """Transcribe speech from recorded from `microphone`.

    Returns a dictionary with three keys:
    "success": a boolean indicating whether or not the API request was
               successful
    "error":   `None` if no error occured, otherwise a string containing
               an error message if the API could not be reached or
               speech was unrecognizable
    "transcription": `None` if speech could not be transcribed,
               otherwise a string containing the transcribed text
    """
    # check that recognizer and microphone arguments are appropriate type
    if not isinstance(recognizer, sr.Recognizer):
        raise TypeError("`recognizer` must be `Recognizer` instance")

    if not isinstance(microphone, sr.Microphone):
        raise TypeError("`microphone` must be `Microphone` instance")

    # adjust the recognizer sensitivity to ambient noise and record audio
    # from the microphone
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    # set up the response object
    response = {
        "success": True,
        "error": None,
        "transcription": None
    }

    # try recognizing the speech in the recording
    # if a RequestError or UnknownValueError exception is caught,
    #     update the response object accordingly
    try:
        response["transcription"] = recognizer.recognize_google(audio)
    except sr.RequestError:
        # API was unreachable or unresponsive
        response["success"] = False
        response["error"] = "API unavailable"
    except sr.UnknownValueError:
        # speech was unintelligible
        response["error"] = "Unable to recognize speech"

    return response

def hearing_words():
    '''
    TODO:
    have to return numbers from 1 to n glasses
    '''

    # set the list of words, maxnumber of guesses, and prompt limit
    WORDS = ["spider", "wolf", "tiger", "shark", "eagle", "snake"]
    NUM_GUESSES = 1
    PROMPT_LIMIT = 5

    # create recognizer and mic instances
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    # get a random word from the list
    word = random.choice(WORDS)

    # format the instructions string
    instructions = (
        "I'm thinking of one of these animals:\n"
        "{words}\n"
        "You have {n} tries to guess which one.\n"
    ).format(words=', '.join(WORDS), n=NUM_GUESSES)

    # show instructions and wait 3 seconds before starting the game
    # print(instructions)
    # time.sleep(3)

    for i in range(NUM_GUESSES):
        # get the guess from the user
        # if a transcription is returned, break out of the loop and
        #     continue
        # if no transcription returned and API request failed, break
        #     loop and continue
        # if API request succeeded but no transcription was returned,
        #     re-prompt the user to say their guess again. Do this up
        #     to PROMPT_LIMIT times
        for j in range(PROMPT_LIMIT):
            print('Guess {}. Speak!'.format(i+1))
            guess = recognize_speech_from_mic(recognizer, microphone)
            if guess["transcription"]:
                break
            if not guess["success"]:
                break
            print("I didn't catch that. What did you say?\n")

        # if there was an error, stop the game
        if guess["error"]:
            print("ERROR: {}".format(guess["error"]))
            break

        # show the user the transcription
        # print("You said: {}".format(guess["transcription"]))
        return guess["transcription"].lower()

        # determine if guess is correct and if any attempts remain
        guess_is_correct = guess["transcription"].lower() == word.lower()
        user_has_more_attempts = i < NUM_GUESSES - 1

        # determine if the user has won the game
        # if not, repeat the loop if user has more attempts
        # if no attempts left, the user loses the game
        if guess_is_correct:
            print("Correct! You win!".format(word))
            # break
        elif user_has_more_attempts:
            print("Incorrect. Try again.\n")
        else:
            print("Sorry, you lose!\nI was thinking of '{}'.".format(word))
            break

# WINDOW_W = 320
# WINDOW_H = 480

# UKURANMARBLE = 50
# JARI2MARBLE = int (UKURANMARBLE* 0.5)
# UKURANCELAH = 10

# COL_PANEL = 2
# ROW_PANEL = 2

# #############
# MAXLEVEL = 7
# #############

# #ukuran margin
# XMARGIN = int((WINDOW_W - (COL_PANEL * (UKURANMARBLE + UKURANCELAH))) / 2)
# YMARGIN = int((WINDOW_H - (ROW_PANEL * (UKURANMARBLE + UKURANCELAH))) / 2)

def panel2xy(baris,kolom):
    left = baris * COL_W + XMARGIN
    top = kolom * ROW_H + YMARGIN + HEADER_H
    return (left,top)


def drawBall((x,y)):
    global DISPLAYSURF
    marble = pygame.image.load("resource/marbles.png")
    adjust_x = 25
    adjust_y = 55
    DISPLAYSURF.blit(marble,(x + adjust_x,y + adjust_y))

def drawGlass((x,y)):
    global DISPLAYSURF
    gelas = pygame.image.load("resource/gelas.png")
    adjust_x = 15
    adjust_y = 20
    DISPLAYSURF.blit(gelas,(x + adjust_x,y + adjust_y))

# teks = "1"
# size = 24
# color = (0,0,0) --> hitam
def drawNum(teks,size,color,(x,y)):
    global DISPLAYSURF
    font = pygame.font.Font('freesansbold.ttf',size)
    text = font.render(teks,True,color)
    textRect = text.get_rect()
    adjust_x = 40
    adjust_y = 65
    textRect.center = (x+adjust_x,y+adjust_y)
    DISPLAYSURF.blit(text,textRect)

def drawTitle(teks,size,color,(x,y)):
    global DISPLAYSURF
    font = pygame.font.Font('freesansbold.ttf',size)
    text = font.render(teks,True,color)
    textRect = text.get_rect()
    adjust_x = 0
    adjust_y = 0
    textRect.center = (x+adjust_x,y+adjust_y)
    DISPLAYSURF.blit(text,textRect)


def drawPanel():
    # header
    global DISPLAYSURF
    pygame.draw.rect(DISPLAYSURF,(255,255,255),(HEADER_X,HEADER_Y,HEADER_W,HEADER_H))
    pygame.draw.rect(DISPLAYSURF,(255,255,255),(FOOTER_X,FOOTER_Y,FOOTER_W,FOOTER_H))
    # DISPLAYSURF.blit(x,textRect)

def main():
    global FPSCLOCK, DISPLAYSURF
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOW_W,WINDOW_H))
    DISPLAYSURF.fill(BGCOLOR1)
    pygame.display.set_caption('Pong')
    '''
    TODO:
    make anim function to randomized gelas.jpg
    make anim function to show/hide ball.jpg
    show number until randomize animation
    '''
    # drawPanel() # sementar, hanya utk liat pembagian panel

    drawBall(panel2xy(0,0))
    drawGlass(panel2xy(0,0))
    drawGlass(panel2xy(0,1))
    drawGlass(panel2xy(1,0))
    drawGlass(panel2xy(1,1))
    drawNum("1",24,(0,0,0),panel2xy(0,0))
    drawNum("2",24,(0,0,0),panel2xy(0,1))
    drawNum("3",24,(0,0,0),panel2xy(1,0))
    drawNum("4",24,(0,0,0),panel2xy(1,1))
    drawTitle("Which One?",24,(0,0,0),(int(HEADER_W/2),int(HEADER_H/2)))
    


    pygame.display.update() #dont update here, move me later
    print(hearing_words())

    # player = pygame.image.load("media/marble.png")
    # DISPLAYSURF.blit(player,(0,0))

    xmouse = 0
    ymouse = 0
    prevselect = (None,None)
    mousehold = False
    win = False

    while True:
        mouseklik = False
        mouserelease = False

        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            
            elif event.type == MOUSEMOTION and mousehold == True:
                print ("mouse hold")
                xmouse, ymouse = event.pos
            
            elif event.type == MOUSEBUTTONUP:
                print ("mouse lepas")
                xmouse, ymouse = event.pos
                mousehold = False
                mouserelease = True

            elif event.type == MOUSEBUTTONDOWN:
                xmouse, ymouse = event.pos
                mouseklik = True
                print("mouse tekan")
                # if(hearing_words() != ""):

            elif event.type == MOUSEMOTION:
                xmouse, ymouse = event.pos

            elif (event.type == KEYUP and event.key == K_d):
                print("panah kanan")
            elif (event.type == KEYUP and event.key == K_w):
                print("panah atas")
            elif (event.type == KEYUP and event.key == K_a):
                print("panah kiri")
            elif (event.type == KEYUP and event.key == K_s):
                print("panah bawah")
        
        pygame.display.update()
        FPSCLOCK.tick(FPS)

if __name__ == '__main__':
    main()
