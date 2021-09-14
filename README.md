## PiEncrypt

### `pip install piencrypt`

> ### Encrypt your crucial data into Image file.

<br>

### Minimal app

```python
from piencrypt import PiEncrypt

m = PiEncrypt('test.jpg')

m.get_data()
m.revert()

m.hide_data("Hello my name is SID")

read = m.read_data()
print(read)

```

<br>

### Step 1

 #### Initialize and create a backup of the picture as bytes 
 
 ```python
    p = PiEncrypt('pic.jpg')
    
    p.get_data()
```
> *pic.jpg should be replaced by your picture name*

### Step 2

#### Hide the disired data into the picture 
 
 ```python
    p.hide_data("Hello my name is SID")
```

### Step 3

 #### Read the hidden data from the picture
 
 ```python
    read = p.read_data()
    print(read)
```

### Step 4

 #### Revert the picture from the backup file
 
 ```python
    p.revert()
```

<br>

https://pypi.org/project/piencrypt/

## Repeat !
