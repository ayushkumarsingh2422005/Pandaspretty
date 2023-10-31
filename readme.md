# Project Description

![Logo](https://github.com/ayushkumarsingh2422005/Pandaspretty/blob/main/Pandaspretty.png)


## Previous releases :
- [1.0.0](https://pypi.org/project/Pandaspretty/1.0.0/)

- [1.1.0](https://pypi.org/project/Pandaspretty/1.1.0/)

## What is it ?

Pandaspretty is a python package which provides you feature to convert your DataFrame in a good looking table, just in few steps.
It aims to make everything simple.

## What's new ?
- More customizable options
- New methods to create


## Main features

1. Custom styles
2. Attractive tables
3. Fast
4. Automatically resizable cells

## Where to get it

The source code is currently available on [github](https://github.com/ayushkumarsingh2422005/Pandaspretty)

## Installation from sources

To install it using PIP use the following command
```
pip install Pandaspretty
```



## Usage 

#### **here is an example :**

Let's suppose you have a DataFrame named **_df_** having value

&nbsp;|Name  | Class  | Roll_no  |  Section |
----|----| ----|----|----|
0|Ayush kumar  | 12 | 8 | A |
1|Prince kumar  | 12 | 23 | A |
2|Khushi singh  | 12  | 18  | B |
3|Prathisha | 12  | 23 | B |

#### Code to prettify your DataFrame (**_df_**)
```python
import Pandaspretty as pp
[...]
prettyfied = pp.pretty(df)
print(prettyfied)
```

#### Output :

```
+----------------+---------+-----------+-----------+
|           Name |   Class |   Roll_no |   Section |
+----------------+---------+-----------+-----------+
|    Ayush kumar |      12 |         8 |         A |
+----------------+---------+-----------+-----------+
|   Prince kumar |      12 |        23 |         A |
+----------------+---------+-----------+-----------+
|   Khushi singh |      12 |        18 |         B |
+----------------+---------+-----------+-----------+
|      Prathisha |      12 |        23 |         B |
+----------------+---------+-----------+-----------+
```


## More About it

#### Importing

```python
import Pandaspretty as pp 
```

### Methods :

- pretty(data = df, corner='%', separator=';', joins='=')

- to_sql(data, index = True)

- tabulate(data,index = True ,corner = '+', separator='|', joins='-')

### Parameters :

- **data** : Accepts a dataframe object.

- **index** : Set index True/False to see the index of dataframe in table _(default value is "True")_.

- **corner** : Accepts character to be shown on corner points _(default value is "+")_.

- **separator** : Accepts character to be shown in place to the line separating two values _(default value is "|")_.

- **joins** : Accepts character to be shown in place to the line joining two rows _(default value is "-")_.

#### Passing parameter

```python
[...]
prettyfied = pp.pretty(data = df, index = True ,corner='%', separator=';', joins='=')
print(prettyfied)
```

#### Output :

```
%=====%================%=========%===========%===========%
;     ;           Name ;   Class ;   Roll_no ;   Section ;
%=====%================%=========%===========%===========%
;   0 ;    Ayush kumar ;      12 ;         8 ;         A ;
%=====%================%=========%===========%===========%
;   1 ;   Prince kumar ;      12 ;        23 ;         A ;
%=====%================%=========%===========%===========%
;   2 ;   Khushi singh ;      12 ;        18 ;         B ;
%=====%================%=========%===========%===========%
;   3 ;      Prathisha ;      12 ;        23 ;         B ;
%=====%================%=========%===========%===========%
```


## More examples

### Example 1 :

#### Code
```python
[...]
prettyfied = pp.pretty(data = df, corner='#')
print(prettyfied)
```

#### Output

```
#-----#----------------#---------#-----------#-----------#
|     |           Name |   Class |   Roll_no |   Section |
#-----#----------------#---------#-----------#-----------#
|   0 |    Ayush kumar |      12 |         8 |         A |
#-----#----------------#---------#-----------#-----------#
|   1 |   Prince kumar |      12 |        23 |         A |
#-----#----------------#---------#-----------#-----------#
|   2 |   Khushi singh |      12 |        18 |         B |
#-----#----------------#---------#-----------#-----------#
|   3 |      Prathisha |      12 |        23 |         B |
#-----#----------------#---------#-----------#-----------#
```
----
### Example 2:

#### Code
```python
[...]
prettyfied = pp.pretty(data = df, index = False, separator='!')
print(prettyfied)
```

#### Output

```
+----------------+---------+-----------+-----------+
!           Name !   Class !   Roll_no !   Section !
+----------------+---------+-----------+-----------+
!    Ayush kumar !      12 !         8 !         A !
+----------------+---------+-----------+-----------+
!   Prince kumar !      12 !        23 !         A !
+----------------+---------+-----------+-----------+
!   Khushi singh !      12 !        18 !         B !
+----------------+---------+-----------+-----------+
!      Prathisha !      12 !        23 !         B !
+----------------+---------+-----------+-----------+
```
----
### Example 3 :

#### Code
```python
[...]
prettyfied = pp.to_sql(data = df, index = False)
print(prettyfied)
```

#### Output

```
+----------------+---------+-----------+-----------+
|           Name |   Class |   Roll_no |   Section |
+----------------+---------+-----------+-----------+
|    Ayush kumar |      12 |         8 |         A |
|   Prince kumar |      12 |        23 |         A |
|   Khushi singh |      12 |        18 |         B |
|      Prathisha |      12 |        23 |         B |
+----------------+---------+-----------+-----------+
```
----

### Example 4 :

#### Code
```python
[...]
prettyfied = pp.to_sql(data = df, index = True)
print(prettyfied)
```

#### Output

```
+-----+----------------+---------+-----------+-----------+
|     |           Name |   Class |   Roll_no |   Section |
+-----+----------------+---------+-----------+-----------+
|   0 |    Ayush kumar |      12 |         8 |         A |
|   1 |   Prince kumar |      12 |        23 |         A |
|   2 |   Khushi singh |      12 |        18 |         B |
|   3 |      Prathisha |      12 |        23 |         B |
+-----+----------------+---------+-----------+-----------+
```
----

### Example 5 :

#### Code
```python
[...]
prettyfied = pp.tabulate(data = df, separator=':')
print(prettyfied)
```

#### Output

```
+-----+----------------+---------+-----------+-----------+
:     :           Name :   Class :   Roll_no :   Section :
+-----+----------------+---------+-----------+-----------+
:   0 :    Ayush kumar :      12 :         8 :         A :
:   1 :   Prince kumar :      12 :        23 :         A :
:   2 :   Khushi singh :      12 :        18 :         B :
:   3 :      Prathisha :      12 :        23 :         B :
+-----+----------------+---------+-----------+-----------+
```
----

### Example 6 :

#### Code
```python
[...]
prettyfied = pp.tabulate(data = df, separator=':', index = False, joins = '—', corner='#')
print(prettyfied)
```

#### Output

```
#————————————————#—————————#———————————#———————————#
:           Name :   Class :   Roll_no :   Section :
#————————————————#—————————#———————————#———————————#
:    Ayush kumar :      12 :         8 :         A :
:   Prince kumar :      12 :        23 :         A :
:   Khushi singh :      12 :        18 :         B :
:      Prathisha :      12 :        23 :         B :
#————————————————#—————————#———————————#———————————#
```
----

> Social Handles : [github](https://github.com/ayushkumarsingh2422005) | [sololearn](https://www.sololearn.com/Profile/16882555/?ref=app) | [instagram](https://instagram.com/ayush_the_dev?utm_medium=copy_link) | [stackoverflow](https://stackoverflow.com/users/13060979/ayush-kumar)
----
