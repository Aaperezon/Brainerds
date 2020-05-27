from numpy import arange, sin, pi
import numpy as np

class Electrodos():
    def __init__(self):
        self.electrodosAngle = np.zeros(32)
        self.electrodosR = np.zeros(32)

        #Lista de la posicion de cada electrodo (theta,r) coordenadas polares
        #1
        self.electrodosAngle[0] = 0;
        self.electrodosR[0] = 0
        #2
        self.electrodosAngle[1] = 3*pi/2;
        self.electrodosR[1] = 2
        #3
        self.electrodosAngle[2] = 3*pi/2;
        self.electrodosR[2] = 4
        #4
        self.electrodosAngle[3] = pi/2;
        self.electrodosR[3] = 2
        #5
        self.electrodosAngle[4] = 0;
        self.electrodosR[4] = 2
        #6
        self.electrodosAngle[5] = 0;
        self.electrodosR[5] = 4
        #7
        self.electrodosAngle[6] = pi;
        self.electrodosR[6] = 2
        #8
        self.electrodosAngle[7] = pi;
        self.electrodosR[7] = 4
        #9
        self.electrodosAngle[8] = 3*pi/4;
        self.electrodosR[8] = 1
        #10
        self.electrodosAngle[9] = 5*pi/4;
        self.electrodosR[9] = 1
        #11
        self.electrodosAngle[10] = pi/4;
        self.electrodosR[10] = 1
        #12
        self.electrodosAngle[11] = 7*pi/4;
        self.electrodosR[11] = 1
        #13
        self.electrodosAngle[12] = 5*pi/6;
        self.electrodosR[12] = 3
        #14
        self.electrodosAngle[13] = 2*pi/3;
        self.electrodosR[13] = 3
        #15
        self.electrodosAngle[14] = 5*pi/3;
        self.electrodosR[14] = 3
        #16
        self.electrodosAngle[15] = 11*pi/6;
        self.electrodosR[15] = 3
        #17
        self.electrodosAngle[16] = pi/6;
        self.electrodosR[16] = 3
        #18
        self.electrodosAngle[17] = 7*pi/6;
        self.electrodosR[17] = 3
        #19
        self.electrodosAngle[18] = 4*pi/3;
        self.electrodosR[18] = 3
        #20
        self.electrodosAngle[19] = 13*pi/6;
        self.electrodosR[19] = 3
        #21
        self.electrodosAngle[20] = pi/6;
        self.electrodosR[20] = 5
        #22
        self.electrodosAngle[21] = 7*pi/6;
        self.electrodosR[21] = 5
        #23
        self.electrodosAngle[22] = 4*pi/3;
        self.electrodosR[22] = 5
        #24
        self.electrodosAngle[23] = 13*pi/6;
        self.electrodosR[23] = 5
        #25
        self.electrodosAngle[24] = 5*pi/6;
        self.electrodosR[24] = 5
        #26
        self.electrodosAngle[25] = 2*pi/3;
        self.electrodosR[25] = 5
        #27
        self.electrodosAngle[26] = 5*pi/3;
        self.electrodosR[26] = 5
        #28
        self.electrodosAngle[27] = 11*pi/6;
        self.electrodosR[27] = 5
        #29
        self.electrodosAngle[28] = pi/6;
        self.electrodosR[28] = 6
        #30
        self.electrodosAngle[29] = -pi/6;
        self.electrodosR[29] = 6
        #31
        self.electrodosAngle[30] = 7*pi/6;
        self.electrodosR[30] = 6
        #32
        self.electrodosAngle[31] = 5*pi/6;
        self.electrodosR[31] = 6
        
    def GetAngleElectrode(self):
        return self.electrodosAngle
    def GetRElectrode(self):
        return self.electrodosR