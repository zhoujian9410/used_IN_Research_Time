import numpy as np

def get_J(data,center):
    data_len=data.shape[1]
    tmp=np.zeros((3,center.shape[1],data_len),dtype=np.float64)
    center_len=center.shape[1]
    for i in range(3):
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
    newc=np.zeros((3,num_k))
    newc=np.array(newc,dtype=np.float64)
    for i in range(3):
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
    

def keans_3(data,k):##the data is 2D,(x,y)
    data_len=data.shape[1]
    #get k center for each demensions 
    chose=np.random.random(k)
    chose = chose*data_len
    chose=np.floor(chose)
    chose=np.array(chose,dtype=np.int64)
    center=np.zeros((3,k),dtype=np.float64)
    for i in range(3):
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
    return new_center,minpos

def new_image(data,k):
    center,minpos=keans_3(data,k)
    for i in range(3):
        for j in range(k):
            for ij in range(data.shape[1]):
                if minpos[ij]==j:
                    data[i][ij]=center[1][j]
                else:  
                    data[i][ij]=data[i][ij]
    return data 
    
def change_shape(data,k):
    data=np.array(data,dtype=np.float64)
    size=data.shape
    lenth=size[0]*size[1]
    data=data.reshape((lenth,3))
    new_data1=new_image(data.T,k)
    new_data=new_data.T
    new_data=new_data.reshape((size[0],size[1],size[2]),dtype=np.uint64)
    return new_data
    
    
    
        
	
