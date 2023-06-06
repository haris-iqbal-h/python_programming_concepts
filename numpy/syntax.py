import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print(arr)

arr = np.array([1, 2, 3, 4, 5])
print(arr)

print(np.__version__)

arr = np.array([1, 2, 3, 4, 5])
print(arr)
print(type(arr))

arr = np.array((1, 2, 3, 4, 5))
print(arr)

arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr)

a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)

arr = np.array([1, 2, 3, 4])
print(arr[0])

arr = np.array([1, 2, 3, 4])
print(arr[2] + arr[3])

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('5th element on 2nd row: ', arr[1, 4])

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('Last element from 2nd dim: ', arr[1, -1])

arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
arr[0] = 42

print(arr)
print(x)


arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
arr[0] = 42

print(arr)
print(x)

arr = np.array([1, 2, 3, 4, 5])

x = arr.copy()
y = arr.view()

print(x.base)
print(y.base)