#sys path -- python adds only user end to the path, not llm_api so it can't find that.
import sys
sys.path.insert(0, '/project/DBchat')

from encryption import encrypt
from LLM_API.call_llm import call
from query_exec import execute 

def run():
    query=input("Enter the query : ").strip()
    tables=input("table names for encryption: ").split(" ")

    prompt,maped=encrypt(prompt=query,tables=tables)

    query=call(prompt)
    #print("llm response : ",query)
    query=query.split(" ")

    #print(maped)
    #print(query)
    index=0
    for i in query:
        if i in maped:
            query[index]=maped[i]
        index+=1
    query=" ".join(query)
    result=execute(query)
    print(result)


if __name__=='__main__':
    run()



 