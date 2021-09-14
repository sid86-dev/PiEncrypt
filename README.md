## PiEncrypt

### `pip install piencrypt`

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

### Step 1

 #### Initialize and create a backup of the picture as bytes 
 
 ```python
    r = pie.PiEncrypt('pic.png')

    r.get_data()
```
> *pic.jpg should be replaced by your picture name present in the root directory*

### Step 2

#### Hide the disired data into the picture 
 
 ```python
    r.hide_data("Hello my name is Sid")
```

### Step 3

 #### Read the hidden data from the picture
 
 ```python    
   read = r.read_data()

   print(read)
```

### Step 4

 #### Revert the picture from the backup file
 
 ```python
    r.revert()
```

<br>

https://pypi.org/project/piencrypt/

## Repeat !
