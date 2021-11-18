# Documentation Tips

# Table structure
| First Header  | Second Header |
| ------------- | ------------- |
| Content Cell  | Content Cell  |
| Content Cell  | Content Cell  |

 # Coloured text 

```diff
- text in red
+ text in green
! text in orange
# text in gray
@@ text in purple (and bold)@@
```

# code block

```
#!/bin/bash
set -vx
```


# DataStructures

## Functions 
``` diff
@@ findListElement(xs:list, finStr:str) @@
```


| Content           | Values                                                                                  |
| ----------------- | --------------------------------------------------------------------------------------- |
| Date              |       2021-11-15                                                                        |
| Updated Date      |       2021-11-18                                                                        |
| two parameters    |       list of strings, text to be found                                                 |
| Description       |       To check the string in the given list                                             |
| Ex                |       findText( xs['xxx'], 'xxx' )                                                      |
| result            |       string Found!!!                                                                   |
| Complexity        |       O(n)                                                                              |


### Example

```
~/DataStructures$ python findStr.py 
string found!!!
string found!!!

~/DataStructures$ cat findStr.py 
import common

xs = ['vel', 'vel', 'raj']
findStr = 'vel'

def main(xs:list, findStr : str):
  common.findListElement(xs,findStr.lower())
  

if __name__ == "__main__":
  main(xs, findStr)
  ```

``` diff
@@ timer @@
```


| Content           | Values                                                                                  |
| ----------------- | --------------------------------------------------------------------------------------- |
| Creation Date     |       2021-11-16                                                                        |
| Updated Date      |       2021-11-16                                                                        |
| Arguments         |       Decorator, function to be passed                                                  |
| Description       |       To check the ececution time                                                       |




### Example

```
~/DataStructures$ python3 findStr.py 
string found!!!
string found!!!

"main" took 0.044 ms to execute

     6  @timer
     7  def main(xs:list, findStr : str):
     8    findText(xs,findStr.lower())  
     
  ```

``` diff
@@ profile @@
```


| Content           | Values                                                                                  |
| ----------------- | --------------------------------------------------------------------------------------- |
| Creation Date     |       2021-11-18                                                                        |
| Updated Date      |       2021-11-18                                                                        |
| Arguments         |       Decorator, function to be passed                                                  |
| Description       |       To check the memory usage                                                         |




### Example

```
~/DataStructures/bin$ python findStr.py 
string found!!!
string found!!!

"findListElement" took 0.393 ms to execute

Filename: /home/runner/DataStructures/bin/common.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    11     17.4 MiB     17.4 MiB           1     @wraps(myFunc)
    12                                           def timing(*args, **kwargs):
    13     17.4 MiB      0.0 MiB           1       startTime = time.time()
    14     17.4 MiB      0.0 MiB           1       retVal = myFunc(*args, **kwargs)
    15     17.4 MiB      0.0 MiB           1       endTime = time.time()
    16     17.4 MiB      0.0 MiB           1       print('"{}" took {:.3f} ms to execute\n'.format(myFunc.__name__, (endTime - startTime) * 1000))
    17     17.4 MiB      0.0 MiB           1       return retVal
  ```
  
  ``` diff
@@ subArray @@
```


| Content           | Values                                                                                  |
| ----------------- | --------------------------------------------------------------------------------------- |
| Creation Date     |       2021-11-18                                                                        |
| Updated Date      |       2021-11-18                                                                        |
| Arguments         |       function, list to be passed                                                       |
| Description       |       This will generate all possible list out of the given list                        |




### Example

```
xs = [ i for i in range(0,5) ]

if __name__ == "__main__":
  outXs = subArray(xs)
  print(outXs)

~/DataStructures/bin$ python subArray.py 
"subArray" took 0.443 ms to execute

Filename: /home/runner/DataStructures/bin/common.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    11     17.3 MiB     17.3 MiB           1     @wraps(myFunc)
    12                                           def timing(*args, **kwargs):
    13     17.3 MiB      0.0 MiB           1       startTime = time.time()
    14     17.3 MiB      0.0 MiB           1       retVal = myFunc(*args, **kwargs)
    15     17.3 MiB      0.0 MiB           1       endTime = time.time()
    16     17.3 MiB      0.0 MiB           1       print('"{}" took {:.3f} ms to execute\n'.format(myFunc.__name__, (endTime - startTime) * 1000))
    17     17.3 MiB      0.0 MiB           1       return retVal


[[0], [0, 1], [0, 1, 2], [0, 1, 2, 3], [0, 1, 2, 3, 4], [1], [1, 2], [1, 2, 3], [1, 2, 3, 4], [2], [2, 3], [2, 3, 4], [3], [3, 4], [4]]
~/DataStructures/bin$ 
  ```



