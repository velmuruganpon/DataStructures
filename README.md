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
@@ findText(xs:list, finStr:str) @@
```


| Content           | Values                                                                                  |
| ----------------- | --------------------------------------------------------------------------------------- |
| Date              |       2021-11-15                                                                        |
| Updated Date      |       2021-11-15                                                                        |
| two parameters    |       list of strings, text to be found                                                 |
| Description       |       To check the string in the given list                                             |
| Ex                |       findText( xs['xxx'], 'xxx' )                                                      |
| result            |       string Found!!!                                                                   |


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
  common.findText(xs,findStr.lower())
  

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
