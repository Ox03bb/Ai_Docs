import numpy as np

one_dimensional_arr = np.array([10, 12])
print(one_dimensional_arr)

o_d_r = np.arange(1,10,3)
print(o_d_r)

lin_spaced_arr = np.linspace(0, 100, 5,dtype=int)
print(lin_spaced_arr, lin_spaced_arr.shape)

ones_arr = np.ones(3,dtype=int)
print(ones_arr)

zeros_arr = np.zeros(3)
print(zeros_arr)

empt_arr = np.empty(3)
print(empt_arr)

rand_arr = np.random.rand(3)
print(rand_arr)

n_dim = np.array([[1,2],[3,4]])
print(n_dim)

print(n_dim.reshape((1,4)))
# -----------------------
print("\n\n")
a1 = np.array([[1,1], 
               [2,2]])
a2 = np.array([[3,3],
              [4,4]])
print(f'a1:\n{a1}')
print(f'a2:\n{a2}')

vert = np.vstack((a1,a2))
hr   = np.hstack((a1,a2))

print(vert,"\n\n",hr)


#! =========================================================
print("\n=========================================================")
A = np.array([
        [-1, 3],
        [-2, 6]
    ], dtype=np.dtype(float))

b = np.array([7, 1], dtype=np.dtype(float))

print("Matrix A:")
print(A)
print("\nArray b:")
print(b)

x = np.linalg.solve(A, b)

print(f"Solution: {x}")

d = np.linalg.det(A)

print(f"Determinant of matrix A: {d:.2f}")
