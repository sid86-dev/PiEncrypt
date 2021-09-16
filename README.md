## PiEncrypt

[![Pie Test](https://github.com/sid86-dev/PiEncrypt/actions/workflows/python-app.yml/badge.svg)](https://github.com/sid86-dev/PiEncrypt/actions/workflows/python-app.yml)
[![DevSkim](https://github.com/sid86-dev/PiEncrypt/actions/workflows/devskim-analysis.yml/badge.svg)](https://github.com/sid86-dev/PiEncrypt/actions/workflows/devskim-analysis.yml)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/piencrypt)

 
## `pip install piencrypt`
 

<br>

> ### Encrypt your crucial data into Image file.

<br>

### Minimal app

```python
from piencrypt import pie

r = pie.PiEncrypt('pic.png')
r.get_data()

r.hide_data("Hello my name is Sid")

read = r.read_data()

r.revert()
print(read)
```

<br>

<!-- ### Step 1 -->

 #### Initialize and create a backup of the picture as bytes 
 
 ```python
    r = pie.PiEncrypt('pic.png')

    r.get_data()
```
> *pic.jpg should be replaced by your picture name present in the root directory*

<br>

<!-- ### Step 2 -->

#### Hide the disired data into the picture 
 
 ```python
    r.hide_data("Hello my name is Sid")
```

<br>

<!-- ### Step 3 -->

 #### Read the hidden data from the picture
 
 ```python    
   read = r.read_data()

   print(read)
```
<br>

<!-- ### Step 4 -->

 #### Revert the picture from the backup file
 
 ```python
    r.revert()
```

<br>

https://pypi.org/project/piencrypt/

## Repeat !
