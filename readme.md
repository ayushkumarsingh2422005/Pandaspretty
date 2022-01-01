# Project description
----

## What is it ?

PandasPretty is a python package which provides you feature to convert your DataFrame in a good looking table, just in few steps.
It aims to make everything simple.

## Main features

1. Custom styles
2. Attractive tables
3. Fast
4. Automatically resizable cells

## Where to get it

The source code is currently available on [github](https://www.sololearn.com/Profile/23547751/?ref=app)

## Installation from sources

To install it using PIP use the following command
```
pip install PandasPretty
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
import PandasPretty as pp
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
import PandasPretty as pp 
```

### Parameters :

- **<ins>data</ins>** : Accepts a dataframe object.

- **<ins>corner</ins>** : Accepts character to be shown on corner points _(default value is "+")_.

- **<ins>separator</ins>** : Accepts character to be shown in place to the line separating two values _(default value is "|")_.

- **<ins>joins</ins>** : Accepts character to be shown in place to the line joining two rows _(default value is "-")_.

#### Passing parameter

```python
[...]
prettyfied = pp.pretty(data = df, corner='%', separator=';', joins='=')
print(prettyfied)
```

#### Output :

```
%================%=========%===========%===========%
;           Name ;   Class ;   Roll_no ;   Section ;
%================%=========%===========%===========%
;    Ayush kumar ;      12 ;         8 ;         A ;
%================%=========%===========%===========%
;   Prince kumar ;      12 ;        23 ;         A ;
%================%=========%===========%===========%
;   Khushi singh ;      12 ;        18 ;         B ;
%================%=========%===========%===========%
;      Prathisha ;      12 ;        23 ;         B ;
%================%=========%===========%===========%
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
#----------------#---------#-----------#-----------#
|           Name |   Class |   Roll_no |   Section |
#----------------#---------#-----------#-----------#
|    Ayush kumar |      12 |         8 |         A |
#----------------#---------#-----------#-----------#
|   Prince kumar |      12 |        23 |         A |
#----------------#---------#-----------#-----------#
|   Khushi singh |      12 |        18 |         B |
#----------------#---------#-----------#-----------#
|      Prathisha |      12 |        23 |         B |
#----------------#---------#-----------#-----------#
```
----
### Example 2:

#### Code
```python
[...]
prettyfied = pp.pretty(data = df, separator='!')
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
prettyfied = pp.pretty(data = df, joins='~')
print(prettyfied)
```

#### Output

```
+~~~~~~~~~~~~~~~~+~~~~~~~~~+~~~~~~~~~~~+~~~~~~~~~~~+
|           Name |   Class |   Roll_no |   Section |
+~~~~~~~~~~~~~~~~+~~~~~~~~~+~~~~~~~~~~~+~~~~~~~~~~~+
|    Ayush kumar |      12 |         8 |         A |
+~~~~~~~~~~~~~~~~+~~~~~~~~~+~~~~~~~~~~~+~~~~~~~~~~~+
|   Prince kumar |      12 |        23 |         A |
+~~~~~~~~~~~~~~~~+~~~~~~~~~+~~~~~~~~~~~+~~~~~~~~~~~+
|   Khushi singh |      12 |        18 |         B |
+~~~~~~~~~~~~~~~~+~~~~~~~~~+~~~~~~~~~~~+~~~~~~~~~~~+
|      Prathisha |      12 |        23 |         B |
+~~~~~~~~~~~~~~~~+~~~~~~~~~+~~~~~~~~~~~+~~~~~~~~~~~+
```
----
> Contacts : [github](https://github.com/ayushkumarsingh2422005) | [sololearn](https://www.sololearn.com/Profile/16882555/?ref=app) | [instagram](https://instagram.com/ayush_the_dev?utm_medium=copy_link) | [stackoverflow](https://stackoverflow.com/users/13060979/ayush-kumar)
----
