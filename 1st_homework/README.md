## Exact methods for solving a system of linear algebraic equations 
<dl>
    <dt> LU decomposition </dt> 
    <dd> is a representation of the matrix A as the product of two matrices A= LU, where L is the lower triangular matrix with units on the diagonal and U is the upper triangular matrix. </dd>
    <dt> Gauss method </dt> 
    <dd> is the classical method for solving the system of linear algebraic equations Ax = f, which consists of forward and reverse moves. A forward move is the reduction of matrix A to the upper triangular form by elementary row transformations. Reverse move is the process of sequentially finding unknowns from the last equation to the first.</dd>
    <dt> Running method or Thomas algorithm </dt>
    <dd> is used to solve systems of linear equations Ax = f, where A is a three-diagonal matrix. It is a variant of the method of sequential exclusion of unknowns.</dd>
    <dt> Cholesky method </dt>
    <dd> is a representation of a symmetric positive matrix A in the form A = LL^T where L is a lower triangular matrix with strictly positive elements on the diagonal. </dd>
</dl>

#### Run program
To check the work of these programs you need to run program using command `python3 programName.py`. Then you need to enter a number in the terminal - the dimension of the matrix. Program will automatically create matrix A and vector f. After that, it will solve this system of equations by your chosen method.
#### For example:
```
python3 2_Gauss.py
8
***Матрица А***
[[0.79831846 0.64283593 0.22216285 0.70155715 0.63606195 0.10704158
  0.27543079 0.51429402]
 [0.63990799 0.55715913 0.59557625 0.51543619 0.53096068 0.60679272
  0.8915946  0.38766275]
 [0.03627874 0.92436367 0.34517522 0.18113124 0.50883913 0.61040662
  0.94018698 0.16973704]
 [0.10606821 0.29963001 0.50463929 0.07812379 0.49699788 0.63847479
  0.53375428 0.01375086]
 [0.87994359 0.27070015 0.78502849 0.12771713 0.53676955 0.09521896
  0.5341058  0.6044661 ]
 [0.90219943 0.09379113 0.77197825 0.2035633  0.36393212 0.17511799
  0.75712231 0.54198565]
 [0.60585044 0.88626633 0.71769707 0.08745595 0.46084684 0.678023
  0.6600963  0.25733654]
 [0.81089448 0.67427275 0.76454151 0.15583374 0.17343434 0.71582585
  0.55173018 0.97743573]]

***Вектор f***
[0.85160685 0.63682707 0.68765071 0.56875317 0.05502992 0.82101112
 0.70527758 0.68515852]

***Вектор x***
[ 5.85097317 -5.76072576  3.87638157 -2.66215397  0.9007615  -3.74198593
  0.70368054  0.68515852]
***Проверка решения***
[ 5.85097317 -5.76072576  3.87638157 -2.66215397  0.9007615  -3.74198593
  0.70368054  0.68515852]
Time
0.0071620941162109375

```
#### Gauss method
![alt-текст](https://github.com/i-n-d-i/num_methods/blob/master/images/Gauss.png)

#### Running method
![alt-текст](https://github.com/i-n-d-i/num_methods/blob/master/images/Running.png)
