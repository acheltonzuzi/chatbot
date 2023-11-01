import openai
api_key='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'
openai.api_key=api_key

def enviar_msg(texto,lista_mesg=[]):
    lista_mesg=[
        {"role": "system", "content": texto},
    ]
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=lista_mesg
    )
    return response['choices'][0]['message']['content']
lista_mesg=[]
while True:
    texto=input('user: ')
    if(texto=='exit'):
        break
    else:
        resposta=enviar_msg(texto)
        lista_mesg.append(resposta)
        print('Chatbot: '+resposta)