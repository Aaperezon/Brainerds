from numpy import arange, sin, pi
import numpy as np

class Electrodos():
    def __init__(self):
        self.electrodosAngle = np.zeros(32)
        self.electrodosR = np.zeros(32)
        self.electrodosName = []
        self.electrodosInfo = []
        #Lista de la posicion de cada electrodo (theta,r) coordenadas polares
         #1
        self.electrodosName.append('Fp1')
        self.electrodosAngle[0] = 0;
        self.electrodosR[0] = 0
        #2
        self.electrodosName.append('AF3')      
        self.electrodosAngle[1] = 3*pi/2;
        self.electrodosR[1] = 2
        #3
        self.electrodosName.append('F3')           
        self.electrodosAngle[2] = 3*pi/2;
        self.electrodosR[2] = 4
        #4
        self.electrodosName.append('F7')
        self.electrodosAngle[3] = pi/2;
        self.electrodosR[3] = 2
        #5
        self.electrodosName.append('FC5')
        self.electrodosAngle[4] = 0;
        self.electrodosR[4] = 2
        #6
        self.electrodosName.append('FC1')
        self.electrodosAngle[5] = 0;
        self.electrodosR[5] = 4
        #7
        self.electrodosName.append('C3')
        self.electrodosAngle[6] = pi;
        self.electrodosR[6] = 2
        #8
        self.electrodosName.append('T7')
        self.electrodosAngle[7] = pi;
        self.electrodosR[7] = 4
        #9
        self.electrodosName.append('CP5')
        self.electrodosAngle[8] = 3*pi/4;
        self.electrodosR[8] = 1
        #10
        self.electrodosName.append('CP1')
        self.electrodosAngle[9] = 5*pi/4;
        self.electrodosR[9] = 1
        #11
        self.electrodosName.append('P3')
        self.electrodosAngle[10] = pi/4;
        self.electrodosR[10] = 1
        #12
        self.electrodosName.append('P7')
        self.electrodosAngle[11] = 7*pi/4;
        self.electrodosR[11] = 1
        #13
        self.electrodosName.append('PO3')
        self.electrodosAngle[12] = 5*pi/6;
        self.electrodosR[12] = 3
        #14
        self.electrodosName.append('O1')
        self.electrodosAngle[13] = 2*pi/3;
        self.electrodosR[13] = 3
        #15
        self.electrodosName.append('Oz')
        self.electrodosAngle[14] = 5*pi/3;
        self.electrodosR[14] = 3
        #16
        self.electrodosName.append('Pz')
        self.electrodosAngle[15] = 11*pi/6;
        self.electrodosR[15] = 3
        #17                                      
        self.electrodosName.append('Fp2')
        self.electrodosAngle[16] = pi/3;
        self.electrodosR[16] = 5
        #18
        self.electrodosName.append('AF4')
        self.electrodosAngle[17] = 7*pi/6;
        self.electrodosR[17] = 3
        #19
        self.electrodosName.append('Fz')
        self.electrodosAngle[18] = 4*pi/3;
        self.electrodosR[18] = 3
        #20
        self.electrodosName.append('F4')
        self.electrodosAngle[19] = 13*pi/6;
        self.electrodosR[19] = 3
        #21
        self.electrodosName.append('F8')        #Este
        self.electrodosAngle[20] = pi/3;
        self.electrodosR[20] = 3
        #22
        self.electrodosName.append('FC6')
        self.electrodosAngle[21] = 7*pi/6;
        self.electrodosR[21] = 5
        #23
        self.electrodosName.append('FC2')
        self.electrodosAngle[22] = 4*pi/3;
        self.electrodosR[22] = 5
        #24
        self.electrodosName.append('Cz')
        self.electrodosAngle[23] = 13*pi/6;
        self.electrodosR[23] = 5
        #25
        self.electrodosName.append('C4')
        self.electrodosAngle[24] = 5*pi/6;
        self.electrodosR[24] = 5
        #26
        self.electrodosName.append('T8')
        self.electrodosAngle[25] = 2*pi/3;
        self.electrodosR[25] = 5
        #27
        self.electrodosName.append('CP6')
        self.electrodosAngle[26] = 5*pi/3;
        self.electrodosR[26] = 5
        #28
        self.electrodosName.append('CP2')
        self.electrodosAngle[27] = 11*pi/6;
        self.electrodosR[27] = 5
        #29
        self.electrodosName.append('P4')
        self.electrodosAngle[28] = pi/6;
        self.electrodosR[28] = 6
        #30
        self.electrodosName.append('P8')
        self.electrodosAngle[29] = -pi/6;
        self.electrodosR[29] = 6
        #31
        self.electrodosName.append('PO4')
        self.electrodosAngle[30] = 7*pi/6;
        self.electrodosR[30] = 6
        #32
        self.electrodosName.append('O2')
        self.electrodosAngle[31] = 5*pi/6;
        self.electrodosR[31] = 6


    def GetElectrodeInfo(self):
        newList = []
        a=0
        for i in range (0,len(self.electrodosR)):
            self.electrodosInfo.append(self.electrodosName[i])
            self.electrodosInfo.append(self.electrodosR[i])
            self.electrodosInfo.append(self.electrodosAngle[i])
            newList.append(self.electrodosInfo[a:a+3])
            a+=3
        #print (newList)
        return zip(*newList)

"""
    def GetAngleElectrode(self):
        return self.electrodosAngle
    def GetRElectrode(self):
        return self.electrodosR
"""