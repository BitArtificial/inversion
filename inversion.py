import random
def inversion(X):
        if not len(X)==len(X[0]):
            print('X is not square list')
            return
        d=len(X)
        unit_arr=[[1 if i==j else 0 for j in range(d)] for i in range(d)]
    #    print(unit_arr)
        step1_arr=[row+row_unit for row,row_unit in zip(X,unit_arr)]
        
        #add the unit matrix to the X
    #        print(step1_arr)
        
        for i,row in enumerate(step1_arr):
            diagonal=1
            #wait
            new_j=0
            for j,ele in enumerate(row):
                if i==j:
                    diagonal=ele
                    new_j=j
    #                print(diagonal)
                    break
            for k,ele in enumerate(row):
                step1_arr[i][k]/=diagonal
            
            
            for l in range(i+1,d):
                mul=step1_arr[l][new_j]
                for m in range(2*d):
                    step1_arr[l][m]-=step1_arr[i][m]*mul
       
        #make the lower triangular matrix
        
        for i in range(d-1,-1,-1):
            for j in range(i-1,-1,-1):
                #j is row
                mul=step1_arr[j][i]
#                print(mul)
                for k in range(2*d):
                    step1_arr[j][k]-=step1_arr[i][k]*mul
                    
        step2_arr=[[step1_arr[i][j] for j in range(d,2*d)] for i in range(d)]
        
        return step2_arr


def make_array(d):
    random.seed(5)
    return [[random.randint(1,100) for j in range(d)] for i in range(d)]


if __name__=='__main__':
    array=make_array(5)
    inv_array=inversion(array)

    print(array)
    print('*'*20)
    print(inv_array)

    