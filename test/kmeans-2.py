import numpy as np

def cal_dis(data,center,J,k,data_len):
    tmp=np.zeros((2,k,data_len),dtype=np.float64)
    
    for i in range(2):
        for j in range(k):
            for ij in range(data_len):
                tmp[i][j][ij]=data[i][ij]-center[i][j]
    tmp=np.square(tmp)
    tmp=np.sum(tmp,axis=0)
    minpos=argmin(tmp,axis=0)
    ;
    

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
    
    
    
    
    
        

	
