import numpy as np

##este programa entra como 15 parametro de torque e angulo como entrada e define o estado do Robô
##@autor Diego Silva Caldeira rocha
stateRobot = "failure"
def existeState (comp,InTA):
    find=False
    for id in range(0, 6):
        if(np.array_equal(comp[id],InTA)):
            find=True
    return find
def  find_state(InR, stateRobot):
    result=False
    stateRobot = "failure"
    ref_arquivo = open("lp1.data", "r")
    MOfState= np.empty((15,6))
    countBank=2;
    while(not result and countBank<6):
        i=0
        j=0
        for linha in ref_arquivo:
            valores = linha.split()
            if (len(valores)==1):
                 stateRobot=valores
            elif(len(valores)>1):
                 for te in valores:
                     MOfState[j,i]=int(te)
                     i=i+1
                 j=j+1
                 if (j==15):
                     comp=MOfState.transpose()
                     result=existeState(comp,InR)
                     j=0
                     print(comp)
                     if (result):
                      print("fdsf");
                      break
            i=0
        countBank=countBank+1
        if(countBank==2):
            ref_arquivo.close()
            ref_arquivo = open("lp2.data", "r")
        elif(countBank==3):
            ref_arquivo.close()
            ref_arquivo = open("lp3.data", "r")
        elif(countBank==4):
             ref_arquivo.close()
             ref_arquivo = open("lp4.data", "r")
        elif(countBank==5):
            ref_arquivo.close()
            ref_arquivo = open("lp5.data", "r")
        
    ref_arquivo.close()
    return stateRobot
#if int(texto[2]) == 63:
def main():#parte Principal do programa
    InR = np.array([ 63,62,61,63,63,63,63,63,63,61,61,64,64,60,64])#alguns valores de torque e angulo do robo
    print("o Robo está no estado:",find_state(InR,stateRobot),"para o teste com os respectivos torque e angulos",InR)
    print("\nPara testar digite as mediçoes de torque e força para dizer o estado do robo")
    for i in range (0,6):
         print("\ndigite v[",i,"]")
         inR[i]=input()
print("o Robo está no estado:",find_state(InR,stateRobot),"para o teste com os respectivos torque e angulos",InR)
if __name__ == "__main__":
    main()




