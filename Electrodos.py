from numpy import arange, sin, pi
import numpy as np

class Electrodos():
    def __init__(self):
        self.electrodosAngle = np.zeros(32)
        self.electrodosR = np.zeros(32)

        #Lista de la posicion de cada electrodo (Θ,r) coordenadas polares
        #1
        self.electrodosAngle[0] = 0;
        self.electrodosR[0] = 0
        #2
        self.electrodosAngle[1] = 0;
        self.electrodosR[1] = .5
        #3
        self.electrodosAngle[2] = 0;
        self.electrodosR[2] = .5
        #4
        self.electrodosAngle[3] = 0;
        self.electrodosR[3] = .5
        #5
        self.electrodosAngle[4] = 0;
        self.electrodosR[4] = .5
        #6
        self.electrodosAngle[5] = 0;
        self.electrodosR[5] = .5
        #7
        self.electrodosAngle[6] = 0;
        self.electrodosR[6] = .5
        #8
        self.electrodosAngle[7] = 0;
        self.electrodosR[7] = .5
        #9
        self.electrodosAngle[8] = 0;
        self.electrodosR[8] = .5
        #10
        self.electrodosAngle[9] = 0;
        self.electrodosR[9] = .5
        #11
        self.electrodosAngle[10] = 0;
        self.electrodosR[10] = .5
        #12
        self.electrodosAngle[11] = 0;
        self.electrodosR[11] = .5
        #13
        self.electrodosAngle[12] = 0;
        self.electrodosR[12] = .5
        #14
        self.electrodosAngle[13] = 0;
        self.electrodosR[13] = .5
        #15
        self.electrodosAngle[14] = 0;
        self.electrodosR[14] = .5
        #16
        self.electrodosAngle[15] = 0;
        self.electrodosR[15] = .5
        #17
        self.electrodosAngle[16] = 0;
        self.electrodosR[16] = .5
        #18
        self.electrodosAngle[17] = 0;
        self.electrodosR[17] = .5
        #19
        self.electrodosAngle[18] = 0;
        self.electrodosR[18] = .5
        #20
        self.electrodosAngle[19] = 0;
        self.electrodosR[19] = .5
        #21
        self.electrodosAngle[20] = 0;
        self.electrodosR[20] = .5
        #22
        self.electrodosAngle[21] = 0;
        self.electrodosR[21] = .5
        #23
        self.electrodosAngle[22] = 0;
        self.electrodosR[22] = .5
        #24
        self.electrodosAngle[23] = 0;
        self.electrodosR[23] = .5
        #25
        self.electrodosAngle[24] = 0;
        self.electrodosR[24] = .5
        #26
        self.electrodosAngle[25] = 0;
        self.electrodosR[25] = .5
        #27
        self.electrodosAngle[26] = 0;
        self.electrodosR[26] = .5
        #28
        self.electrodosAngle[27] = 0;
        self.electrodosR[27] = .5
        #29
        self.electrodosAngle[28] = 0;
        self.electrodosR[28] = .5
        #30
        self.electrodosAngle[29] = 0;
        self.electrodosR[29] = .5
        #31
        self.electrodosAngle[30] = 0;
        self.electrodosR[30] = .5
        #32
        self.electrodosAngle[31] = 0;
        self.electrodosR[31] = 1



        
    def GetAngleElectrode(self):
        return self.electrodosAngle
    def GetRElectrode(self):
        return self.electrodosR