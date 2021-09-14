## PEncrypt

### `pip install pencrypt`

> ### Encrypt your crucial data into Image file.

<br>

### Minimal app

```python
from pencrypt import PEncrypt

m = PEncrypt('Skilljam.png')

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
    p = PEncrypt('pic.jpg')
    
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

https://pypi.org/project/pencrypt/1.11/

## Repeat !
