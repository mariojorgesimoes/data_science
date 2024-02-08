# TCD Ficha de introdução

# A . Elaboração de um conjunto de scripts e funções para manipulação de som

import numpy as np;
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from scipy.io import wavfile;
import sounddevice as sd;

[fs, data] = wavfile.read('saxriff.wav');

sd.play(data, fs)
status = sd.wait()  # Wait until file is done playing

nrBitsQuant = data.shape[1] * 8


def apresentarInfo(nomeFicheiro, fs, nrBitsQuant):
    print("Informação sobre o ficheiro\nNome do ficheiro: " + str(nomeFicheiro) +
          "\nTaxa de amostragem: " + str(fs / 1000) + " kHz\nQuantização: " + str(nrBitsQuant) + " bits")


apresentarInfo('saxriff.wav', fs, nrBitsQuant)

def visualizacaoGrafica(*args):
#def visualizacaoGrafica(sinal, fs, tIni=0, tFim=data.shape[0]/fs)

    sinal=args[0]
    fs=args[1]
    if (len(args)==2):
        tIni=0
        tFim=data.shape[0]/fs
    else:
        tIni = args[2]
        tFim = args[3]

    Ts = 1 / fs
    duracao = sinal.shape[0] * Ts
    tempo = np.linspace(0, duracao, sinal.shape[0])
    #print(sinal)

    """
        data.shape[0] - valores
         data.shape[1] - numero de canais
    """
    # UNIDADES ERRADAS Y
    if(data.shape[1] == 2):
        plt.subplot(211)
        plt.plot(tempo, sinal[:,0], 'b')
        plt.xlabel('Tempo (seg)')
        plt.ylabel('Amplitude [-1:1]')
        plt.title('Canal Esquerdo')
        plt.xlim([tIni, tFim])

        plt.subplot(212)
        plt.plot(tempo, sinal[:, 1], 'b')
        plt.xlabel('Tempo (seg)')
        plt.ylabel('Amplitude [-1:1]')
        plt.title('Canal Direito')
        plt.xlim([tIni, tFim])

        # plt.axis([xmin,xMax,ymin,yMax])
        plt.show()

#visualizacaoGrafica(data, fs, 0, 1)

def ruido(sinal, fs, amp):
    for i in range(0,sinal.shape[0]-1):
        for j in range(0,2):
            sinal[i,j] = sinal[i,j] + 2*amp*np.random.random() - amp

ruido(data,fs,500)
visualizacaoGrafica(data, fs, 0, 1)

def calculoEnergia(sinal,fs):
    v = np.sum(sinal.astype(np.float32) ** 2, axis=0)
    print("Energia= "+ str(v))

calculoEnergia(data,fs)

def audioDireito(sinal,fs):
    [fs_beats, data_beats] = wavfile.read('beats.wav')
    divisao_inteira = sinal.shape[0]//data_beats.shape[0]
    resto = sinal.shape[0]%data_beats.shape[0]

    # tentar criar forma de juntar os vetores através da div. inteira e de um vetor auxiliar
    for i in range(0, sinal.shape[0] - data_beats.shape[0] ):
        data_beats=np.append(data_beats, data_beats[i])

    sinal[:,1]=data_beats

    sd.play(data, fs)
    status = sd.wait()  # Wait until file is done playing

audioDireito(data,fs)

def contornoAmplitude(x, W):
    for i in range(0,x.shape[0]-1):
