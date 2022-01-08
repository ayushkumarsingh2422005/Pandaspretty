"""
PandasPretty is a python package which provides you feature to convert your DataFrame in a good looking table, just in few steps. It aims to make everything simple.
"""

def pretty(data, corner = '+', separator='|', joins='-'):
    """
    Parameters :
    
    ~ data : Accepts a dataframe object.
    ~ corner : Accepts character to be shown on corner points (default value is "+").
    ~ separator : Accepts character to be shown in place to the line separating two values (default value is "|").
    ~ joins : Accepts character to be shown in place to the line joining two rows (default value is "-").
    
    
    Example : PandasPretty.pretty(data = df, corner='%', separator=';', joins='=')
    Output :
    
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
    """
    max_len = []
    data_t = data.T
    data_t_columns = data_t.index.tolist()
    data_t = data.T.values.tolist()
    
    for i,j in zip(data_t, data_t_columns):
        i.insert(0,j)
    
    for i in data_t:
        len_lst = map(lambda x : len(str(x)), i)
        max_len.append(max(list(len_lst)))
    
    data_columns = data.columns.tolist()
    data = data.values.tolist()
    data.insert(0, data_columns)
    
    def line_simple(lst, corner, joins):
        string = ''
        for i in lst:
            string += (i+4)*joins+corner
        return corner+string
        
    def line_advans(lst, max_len, separator):
        string = ''
        def white_spc(word, max_ln, separator):
            return separator+((max_ln+4) - len(str(word))-1)*' '+str(word)+' '
            
            
        for i, j in zip(lst, max_len):
            string += white_spc(i, j, separator)
        return(string)
        
            
    main_str = ''
    for i in data:
        main_str += line_simple(max_len, corner, joins)+'\n'
        main_str += line_advans(i, max_len, separator)+separator+'\n'
    main_str += line_simple(max_len, corner, joins)
    return main_str
