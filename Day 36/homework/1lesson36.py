def return_area(l,w):
    if l == w :
      return l * w
    else: 
       return  (2 * l) + (2 * w)

print(return_area(int(input()), int(input())))



def array_plus_array(arr1,arr2):
    return sum(arr1) + sum(arr2)

print(array_plus_array([1,2,3], [2,3,4]))