#!/usr/bin/env python
# coding: utf-8

# **Trabalho 02 - Convolução** <br>
# **Disicplina:** Tópicos em Metodologia e Técnicas de Computação: Visão Computacional <br/>
# **Professor:** Wesley Nunes Goncalves <br/>
# **Discente:** <br/>
# Antonio Ronaldo da Silva <br/>
# Calebe Pereira Lemos <br/>
# Mario de Araújo Carvalho <br/>
# <br>
# **Discrição da atividade** <br>
# 3. Subtracao de Fundo <br>
#     3.1 Implementar a estrategia de subtração de fundo e subtração de fundo adaptativo. <br>
#     3.2 Comparar as duas estratégias em vıdeos com câmera fixa e objeto em movimento. <br>

# Carregando as bibliotecas necessárias
import cv2 as cv

# Carrega o Video
capture = cv.VideoCapture('/Users/Calebe/Downloads/videoplayback.mp4')

# subtracao de fundo adaptativa, usando MOG2
def sub_adaptativa():
    subtractor = cv.createBackgroundSubtractorMOG2(history=100, varThreshold=50, detectShadows=True)

    while True:
        ret, frame = capture.read()
    
        fgmask = subtractor.apply(frame)
    
        cv.imshow('fgmask', fgmask)
        cv.imshow('Frame', frame)
    
        keyboard = cv.waitKey(30)
        if keyboard == 'q' or keyboard == 27:
            break
    capture.release()
    cv.destroyAllWindows()

# Subtracao de fundo manual
def sub_manual():
    _, first_frame = capture.read()
    first_gray = cv.cvtColor(first_frame, cv.COLOR_BGR2GRAY)
    first_gray = cv.GaussianBlur(first_gray, (5, 5), 0)

    while True:
        _, frame = capture.read()
        gray_frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        gray_frame = cv.GaussianBlur(gray_frame, (5, 5), 0)

        diff = cv.absdiff(first_gray, gray_frame)
        _, diff = cv.threshold(diff, 25, 255, cv.THRESH_BINARY)

        cv.imshow("First frame", first_frame)
        cv.imshow("Frame", frame)
        cv.imshow("difference", diff)
   
        key = cv.waitKey(30)
        if key == 27:
            break
    capture.release()
    cv.destroyAllWindows()

# chama a funcao da subtração manual ou adaptativa 
sub_adaptativa()