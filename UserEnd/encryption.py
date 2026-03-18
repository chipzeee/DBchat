dummy_tables=['ab','cd','xy','zh']

def replace_substring(text, old, new):
    arr=text.split(" ")

    ptr=0
    for i in arr:
        if i==old:
            arr[ptr]=new
        ptr+=1
    text=" ".join(arr)
    return text
    
 
def encrypt(prompt,tables):
    index=0
    maped={}
    for i in tables:
        prompt=replace_substring(prompt,i,dummy_tables[index])
        maped[dummy_tables[index]]=i
        index+=1
        if index==4:
            print("Table limit extend, in encryption.")
            return -1

    return (prompt,maped)

if __name__ == '__main__':
    prompt="table is the key of table2 and table3 is the good table of table2 and table3"
    print("OG: ",prompt)
    tables=['table','table2','table3']
    prompt,maped=encrypt(prompt=prompt,tables=tables)
    
    print("NEW : ",prompt)
    print("Maping ",maped)


 
