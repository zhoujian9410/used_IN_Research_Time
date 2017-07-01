import numpy as np

def get_J(data,center):
    data_len=data.shape[1]
    tmp=np.zeros((2,center.shape[1],data_len),dtype=np.float64)
    center_len=center.shape[1]
    for i in range(2):
        for j in range(center_len):
            for k in range(data_len):
                tmp[i][j][k]=data[i][k]-center[i][j]
    tmp=np.square(tmp)
    tmp=np.sum(tmp,axis=0)
    minpos=np.argmin(tmp,axis=0)
    J=0
    for j in range(data_len):
        a=minpos[j]
        J=J+tmp[a][j]

    return J,minpos

def cal_center(data,num_k,minpos):
    newc=np.zeros((2,num_k))
    newc=np.array(newc,dtype=np.float64)
    for i in range(2):
        for j in range(num_k):
            num_in_=0
            for k in range(data.shape[1]):
                if j==minpos[k]:    #judue the data is j type or not?
                    num_in_=num_in_+1
                    newc[i][j]=newc[i][j]+data[i][k]
                else :
                    num_in_=num_in_
                    newc=newc
            newc[i][j]=newc[i][j]/num_in_
    return newc
    

def keans_2(data,k):##the data is 2D,(x,y)
    data=np.array(data,dtype=np.float64)
    data=data.reshape((2,-1))
    data_len=data.shape[1]
    #get k center for each demensions 
    chose=np.random.random(k)
    chose = chose*data_len
    chose=np.floor(chose)
    chose=np.array(chose,dtype=np.int64)
    center=np.zeros((2,k),dtype=np.float64)
    for i in range(2):
        center[i]=np.take(data[i],chose)
    J,minpos=get_J(data,center)
    #Jold=J
    #new_center=cal_center(data,center,shape[1],minpos)
    done=True
    while done:
        new_center=cal_center(data,k,minpos)
        Jold=J
        J,minpos=get_J(data,new_center)
        aa=(Jold-J)/J
        #Jold=J
        if aa<np.float64(1e-6):
            done=False
    new_center=cal_center(data,center.shape[1],minpos)
    return J,Jold,minpos
    
    
    
    
    
        

	
