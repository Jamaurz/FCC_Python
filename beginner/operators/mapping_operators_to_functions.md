## [Mapping Operators to Functions](https://docs.python.org/3/library/operator.html#mapping-operators-to-functions)  

This table shows how abstract operations correspond to operator symbols in the Python syntax and the functions in the [operator](https://docs.python.org/3/library/operator.html#module-operator) module.  

**Note**  
Some of the terms below, such as slicing, indexing, and bitwise operations, have not been covered yet.  
If you see an unfamiliar term, worry not young padawan. For reference only, this chart is.  


| Operation             | Syntax            | Function                          |
|-----------------------|-------------------|-----------------------------------|
| Addition              | a + b             | add(a, b)                         |
| Concatenation         | seq1 + seq2       | concat(seq1, seq2)                |
| Containment Test      | obj in seq        | contains(seq, obj)                |
| Division              | a / b             | truediv(a, b)                     |
| Division              | a // b            | floordiv(a, b)                    |
| Bitwise And           | a & b             | and\_(a, b)                       |
| Bitwise Exclusive Or  | a ^ b             | xor(a, b)                         |
| Bitwise Inversion     | ~ a               | invert(a)                         |
| Bitwise Or            | a | b             | or\_(a, b)                        |
| Exponentiation        | a \*\* b          | pow(a, b)                         |
| Identity              | a is b            | is\_(a, b)                        |
| Identity              | a is not b        | is_not(a, b)                      |
| Indexed Assignment    | obj[k] = v        | setitem(obj, k, v)                |
| Indexed Deletion      | del obj[k]        | delitem(obj, k)                   |
| Indexing              | obj[k]            | getitem(obj, k)                   |
| Left Shift            | a << b            | lshift(a, b)                      |
| Modulo                | a % b             | mod(a, b)                         |
| Multiplication        | a * b             | mul(a, b)                         |
| Matrix Multiplication | a @ b             | matmul(a, b)                      |
| Negation (Arithmetic) | - a               | neg(a)                            |
| Negation (Logical)    | not a             | not\_(a)                          |
| Positive              | + a               | pos(a)                            |
| Right Shift           | a >> b            | rshift(a, b)                      |
| Slice Assignment      | seq[i:j] = values | setitem(seq, slice(i, j), values) |
| Slice Deletion        | del seq[i:j]      | delitem(seq, slice(i, j))         |
| Slicing               | seq[i:j]          | getitem(seq, slice(i, j))         |
| String Formatting     | s % obj           | mod(s, obj)                       |
| Subtraction           | a - b             | sub(a, b)                         |
| Truth Test            | obj               | truth(obj)                        |
| Ordering              | a < b             | lt(a, b)                          |
| Ordering              | a <= b            | le(a, b)                          |
| Equality              | a == b            | eq(a, b)                          |
| Difference            | a != b            | ne(a, b)                          |
| Ordering              | a >= b            | ge(a, b)                          |
| Ordering              | a > b             | gt(a, b)                          |
