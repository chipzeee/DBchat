from google import genai


with open('LLM_API/api_key.txt','r') as file:
    api_key=file.readline()

client= genai.Client(api_key=api_key)
def call(text):
     
    default_prompt='''Just give the sql code as response, 
    nothing else not even a single extra word or sign. 
    with the proper syntax error free query, so i can directly pass your entire response as a query
    and one more thing add space after and before every table and column name in query. 
    description : '''

    #call api with final prompt
    prompt=default_prompt+text

    response = client.models.generate_content(
    model="gemini-3-flash-preview", contents=prompt)
    return response.text




if __name__=='__main__':
    #text="create table name of student with info of its id with integer and primary key, its name and marks."
    text="fetch data fromt the student info table of there name, passport number and there salary"
    call(text)

