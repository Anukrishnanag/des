import numpy as np
def create_metrix(mc):
    print("\nARRAY" +str(mc)+"element:")
    array=map(int,input().split())
    array=np.array(list(array))
    print("\nARRAY"+str(mc)+ "row colum:")
    row,column=map(int,input().split())
    if(len(array)!=(row*column)):
        print("\n ROW AND COLUMN SIZE NOT MATCH WITH TOTAL ELEMENTS! RETRY")
        return create_metrix(mc)
    array=array.reshape(row,column)
    print("\narray"+str(mc))
    print(array) 
    return(array)
arr1=create_metrix(1)
arr2=create_metrix(2)
if(arr1.shape==arr2.shape):
    print("\n dot product")
    print(np.dot(arr1,arr2))
else:
    print("\n dimension doesnot matching")    
