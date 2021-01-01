Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
=================== RESTART: C:\Users\HP\Downloads\testpy.py ===================
>>> create("yasica",20)
>>> read("yasica")
'yasica:20'
>>> create("uma",18)
>>> read("uma")
'uma:18'
>>> create("freshworks",9)
>>> read("freshworks")
'freshworks:9'
>>> delete("yasica")
key is successfully deleted
>>> create("deepa",99999999999999999999999999999999999999999999999)
error: Memory limit exceeded!! 
>>> create("uij90h",9)
error: Invalind key_name!! key_name must contain only alphabets and no special characters or numbers
>>> create("priya",7,1)
>>> read("priya")
error: time-to-live of priya has expired
>>> create("uma",18)
error: this key already exists
>>> read("pp")
error: given key does not exist in database. Please enter a valid key
>>> 