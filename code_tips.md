# 🏆 Google code golf

- Optimize for minimal character count
- Execution time or memory usage does not count, only bytes matters here, you have to optimize it. Write a correct code but as small as possible.

## 📚 Our tips

1. Be as crazy as possible, **if you can understand it, you can write less**
2. Use **white spaces** instead of tabs for indexing
3. Double for loop? Probably can be optimized with a single loop or list comprehension, see how [task010.py](task010.py) change over time.
4. Use lambda functions for one-line functions and with no variables, see [task006.py](task006.py).
5. Use lambda functions for one-line functions and with one constant, see [task016.py](task016.py).
6. We can assign a name to functions that occurs many times in the program, for 5 letter functions (like `range`) that occurs only 2 times is not worth it, but with more letter functions or with many repetitions it can save at least **1 byte!** See [task014.py](task014.py).
7. rotation clockwise code -> `r=lambda m:[*map(list,zip(*m[::-1]))]` and counter-clockwise -> `l=lambda m:[*map(list,zip(*m))][::-1]`, of course it holds that `l=r \circ r \circ r` and this identity can be useful in many situations, so I only implement `l` or `r`, see [task214.py](task214.py).
8. Sometimes can be better substitute a `range(len(...))` with `enumerate(...)`, in particular when there is already one or more enumerate in the code and combine this observation with tips 5., see [task215.py](task215.py).
9. For alternating colors I can make a full line and then color alternating over the previous one, see [task232.py](task232.py).
10. Symmetry respect main diagonal can be useful in many situations -> `p=lambda m:[*map(list,zip(*m))]`, see [task241.py](task241.py).
11. To mind the maximum of a matrix, I can use `max(L:=sum(g,[]),key=L.count)` with `g` the original matrix, see [task129.py](task129.py).
12. Function for all the permutation -> `f=lambda a:[p+[x]for x in a for p in f(a-{x})]or[[]]`. This is an alternative of `permutations` from `combinatorics` library -> see discussione [here](https://codegolf.stackexchange.com/questions/5056/code-golf-permutations)
13. This is how to unroll a matrix into a vector: `sum(g,[])` where `g` is the original matrix, see [task007.py](task007.py). This can be also useful when I need to iterate over all the element of the matrix, save 6 Bytes in [task115.py](task115.py), using it instead of the double for loop. If I need to rool back the matrix I can use this `[*map(list,zip(*[iter(L)]*m))]`.
14. To iterate over the column of the matrix I find that this can be useful `for c in zip(*m)`, now `c` is a tuple but you can transform as a list with `[*c]`. In other words **the zip operator is equivalent to the transposition of the matrix**. See [task057.py](task057.py). Recently optimized with `[*map(list,zip(*m))]` in [task179.py](task179.py).
15. I notice that sometimes `collections.Counter.most_common()` is useful, but it is long due to the importation and vary long name of library and functions. So I try to avoid it and do something from scratch, see for example [task049.py](task049.py).
16. Sometimes reorder stuff can avoid a pair of brackets, see [task052.py](task052.py).
17. I can set the item of a matrix in a double for loop on a single line with `__setitem__`, see [task068.py](task068.py). Or sometimes can be useful recreate the entire matrix, see [task273.py](task273.py).
18. I can use `dict.fromkeys` to remove duplicates from a list while preserving the order, exactly like an ordered `set`, see [task115.py](task115.py).
19. How to color the anti-diagonal of a matrix (from bottom-left to upper-right) -> `[g[i].__setitem__(~i,2)for i in range(n)]`, see [task084.py](task084.py). For the main diagonal I think is the same but without the `~`.
20. `sorted()` save 1 Byte respect to `.sort()`, see [task246.py](task246.py), [task013.py](task013.py) and [task091.py](task091.py).
21. Instead of `sum(r)>0` I can use `any(r)` to check if a row is not empty, see [task290.py](task290.py).
22. In [task372.py](task372.py) there is my implementation to sum two matrices. The implementation is based on the `zip` function, so the matrices do not need to be the same size, and the function will automatically handle any differences in shape and make the sum on the smallest size, this is useful so I can avoid to resize all the matrices to be sum and save a lot of bytes.
23. I find that [task271.py](task271.py) is interesting. I have to cicle through all the possible 3x3 submatrices of a 7x7 matrix and find the one with the maximum number of 1, I do this with a `max` over a list with all the possible 3x3 matrices and a custom `key` function for the `max`.
24. I find that [task291.py](task291.py) is interesting. I have to find the holes. I realize that I have an hole when in a 2x2 matrix there is only one 0 and all the other numbers are the same.
25. I find that [task40.py](task40.py) is interesting. I have solved the problem in the simple case of row dominant, and then I use a very stupid recursion for the transpose case.
26. To up-scale pixels, the code in [task223.py](task223.py) can be used as a reference. [task218.py](task218.py) can be a reference for down-scaling.
27. To coloring like gravity effect see [task322.py](task322.py) and [task032.py](task032.py) as reference.
28. [task218.py](task218.py): how to apply f(g) on g and g transposed using the double transposition: [*map(list,zip(*f([*zip(*f(g))])))]
29. Sussy tricks `{x:x,...}[x] >>> {...}.get(x,x)` and `[*filter(None,sum(g,[]))] >>> [x for x in sum(g,[])if x]` |
30. [task301.py](task301.py) is interesting for ordering stuffs.
31. [task294.py](task294.py) is interesting for coloring the interior of the matrix.
32. `.setdefault()` can be useful to initialize a dictionary key with a default value if it doesn't exist, see [task010.py](task010.py).
33. DFS in [task286.py](task286.py).
34. For extract non zero matrix see [task031.py](task031.py).
35. Sometimes `*` and `+` can be useful in logical expressions to write less instead of `and` and `or`.
36. Sometimes the first element non zero or the last element can be obtained with `or` and `and` respectively.
37. The code `[x[c]for x in g[r:]]` can be rewrite as `[*zip(*g)][c][r:]`
38. Sometime the `if` condition can be simplified with `and` and `or` to avoid extra indentation, see [task286.py](task286.py)
39. `b"01234"[i] == ord("01234"[i])`, so `b"0564312798"[x]-48` is equal to `[0,5,6,4,3,1,2,7,9,8][x]`.
40. `g[0]` returns a the first value, `g[:1]` returns a list with inside the first value. This can be useful if we need to concatenate it with another list.
41. To get the non zero element we can use `max(map(max,g))`, see [task028.py](task028.py).
42. To see how to color the matrix with angular effect see [task123.py](task123.py) as reference. The idea is to color the rows and then make the diagonal simmetry.
43. In task [task353.py](task353.py) we can see how to transform a method `.index` to a callable function `E=sum(j,[]).index` for example.
44. `[a+b for a,b in zip(g[0],g[1])]` a sum with a for loop could be replaced by a map(sum,...) `[*map(sum,zip(g[0],g[1]))]`. See [task082.py](task082.py).
45. `def p(g):n=len(g)//2;return ...` the assignment of a variable can be done in one line by attaching it to the return value through an "and". See [task109.py](task109.py).