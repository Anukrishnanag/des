import numpy as np
def create_matrix(mc):
    print("\n ARRAY"+str(mc)+"elements:")
    array=map(int,input().split())
    array=np.array(list(array))
    print("\nARRAY"+str(mc)+"ROW COLUMN:")
    row,column=map(int,input().split())
    if(len(array)!=(row*column)):
        print("\n row and column size are not matched with total element!")
        return create_matrix(mc)
    array=array.reshape(row,column)
    print(array)
    print("\nTRASE")
    return array
print(create_matrix(1).trace())