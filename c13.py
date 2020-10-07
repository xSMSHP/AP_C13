import re
import matplotlib.pyplot as plt
import numpy as np

class A1:
    def __init__(self, file, name):
        self.k = []
        self.o = []
        self.f = []
        self.name = name
        
        for i, line in enumerate(file):
            l = re.split(',', line)
            if i < 2:
                V_U = float(l[1]) / (float(l[2]) * 10 ** (-3))
                print('V_U = ' + str(V_U))
                I_k = float(l[1]) / (float(l[0]) * 10 ** 3)
                print('I_{Kollektor} = ' + str(I_k))
                V_I = I_k / (float(l[3]) * 10 ** (-6))
                print('V_I = ' + str(V_I))
                print('V_P = ' + str(V_I * V_U))
            else:
                if l[0] == 'ohne':
                    self.o.append(float(l[1]))
                else:
                    self.k.append(float(l[1]))
                    self.f.append(float(l[3]))
    
    def plot(self):
        plt.figure()
        plt.plot(self.f, self.k, 'rs')
        plt.plot(self.f, self.o, 'bd')
        plt.legend(['mit Kondensator', 'ohne Kondensator'])
        plt.xlabel(r'Frequenz $\nu$ [Hz]')
        plt.ylabel(r'Ausgangsspannung $U_{ASS}$ [V]')
        plt.xscale('log')
        plt.autoscale(True)
        plt.grid(True)
        plt.savefig(self.name + '.png', dpi = 900)
        plt.show()

class A2:
    def __init__(self, file, name):
        self.name = name
        self.VU = []
        self.f = []
        self.VU1 = []
        self.VU2 = []
        
        UE = 0
        UA = 0
        
        rE = 0
    
        for i, line in enumerate(file):
            l = re.split(',', line)
            if i < 5:
                if i == 0:
                    UE = float(l[0])
                    UA = float(l[1])
                else:
                    print('dU_E: ' + str(float(l[0]) - UE) + ' dU_A/dU_E = ' + str((float(l[1]) - UA) / (float(l[0]) - UE)))
            elif i < 10:
                print('U_ESS: ' + str(float(l[0])) + ' U_ASS / U_ESS = ' + str(float(l[1]) * float(l[2]) / (float(l[0]) * 10 ** (-3))))
                if float(l[0]) == 50:
                    self.VU.append(float(l[1]) * float(l[2]) / (float(l[0]) * 10 ** (-3)))
            elif i < 15:
                self.VU.append(float(l[1]) * float(l[2]) / (float(l[0]) * 10 ** (-3)))
            elif i == 15:
                rE = float(l[1]) * 10 ** (-3) / (float(l[0]) * 10 ** (-6))
                print('r_E = ' + str(rE))
            elif i == 16:
                I_ESS = (float(l[0]) * 10 ** (-3)) / rE
                print('I_ESS = ' + str(I_ESS))
                print('V_U1 = ' + str(float(l[1]) * float(l[2]) / (float(l[0]) * 10 ** (-3))))
                print('V_U2 = ' + str(float(l[3]) * float(l[4]) / (float(l[1]) * float(l[2]))))
                V_U = float(l[3]) * float(l[4]) / (float(l[0]) * 10 ** (-3))
                print('V_U = ' + str(V_U))
                V_I = float(l[3]) * float(l[4]) / float(l[5]) / I_ESS
                print('V_I = ' + str(V_I))
                print('V_P = ' + str(V_U * V_I))
            elif i < 24:
                self.f.append(float(l[0]))
                self.VU1.append(float(l[1]) * float(l[2]) / 0.02)
            else:
                self.VU2.append(float(l[0]) * float(l[1]) / 0.02)
                
    def plot(self):
        plt.figure()
        plt.bar(np.arange(0, len(self.VU), 1), self.VU, tick_label = ['ohne', 'R₃', 'R₄', 'R₇', 'R₈', 'R₉'])
        plt.ylabel(r'Verstärkung $V_U$')
        plt.grid(True)
        plt.savefig(self.name + '.png', dpi = 900)
        plt.show()
        
        plt.figure()
        plt.plot(self.f, self.VU1, 'rs')
        plt.ylabel(r'Verstärkung $V_U$')
        plt.xlabel(r'Frequenz $\nu$ [Hz]')
        plt.xscale('log')
        plt.grid(True)
        plt.savefig(self.name + '_1.png', dpi = 900)
        plt.show()

        plt.figure()
        plt.plot(self.f, self.VU2, 'bd')
        plt.ylabel(r'Verstärkung $V_U$')
        plt.xlabel(r'Frequenz $\nu$ [Hz]')
        plt.xscale('log')
        plt.grid(True)
        plt.savefig(self.name + '_2.png', dpi = 900)
        plt.show()
        
a1 = A1(open('c13_a11.txt', 'r'), 'a1_2')
a1.plot()
a2 = A2(open('c13_a2.txt', 'r'), 'a2')
a2.plot()
            