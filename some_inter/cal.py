def cal(p0):                ##this is used for calculating the next positions of a electron 
    p=np.random.random_integers(4)
    if p==1:
        p0=p0+np.array([1,0],dtype=np.float)
    elif p==2:
        p0=p0+np.array([-1,0],dtype=np.float)
    elif p==3:
        p0=p0+np.array([0,1],dtype=np.float)
    elif p==4:
        p0=p0+np.array([0,-1],dtype=np.float)
    else : p0=p0
    return p0
