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
    print("\nDETERMINANT")
    return array
print(np.linalg.det(create_matrix(1)))