import streamlit as st

def get_response(user_input):
    user_input = user_input.lower()

    imagem = "https://sdmntprsouthcentralus.oaiusercontent.com/files/00000000-3930-61f7-b1bb-bd04b77b2094/raw?se=2025-04-30T03%3A16%3A51Z&sp=r&sv=2024-08-04&sr=b&scid=c80d804c-ba1d-512e-b1c9-d575c3b247a8&skoid=dfdaf859-26f6-4fed-affc-1befb5ac1ac2&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2025-04-29T22%3A33%3A06Z&ske=2025-04-30T22%3A33%3A06Z&sks=b&skv=2024-08-04&sig=5XsMyerOZ9CZrWsKYqLaHkTRBStZjB9VHaQnvE8cdAY%3D"

    if "remédio" in user_input or "medicamento" in user_input:
        resposta = "Temos uma grande variedade de medicamentos. Você está procurando algo com receita ou sem receita médica?"
        imagem = "https://sdmntprsouthcentralus.oaiusercontent.com/files/00000000-da54-61f7-9503-f8e4ddaaa94e/raw?se=2025-04-30T03%3A08%3A29Z&sp=r&sv=2024-08-04&sr=b&scid=eca5f987-b790-5206-aef9-ee0f0213f639&skoid=dfdaf859-26f6-4fed-affc-1befb5ac1ac2&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2025-04-29T22%3A33%3A41Z&ske=2025-04-30T22%3A33%3A41Z&sks=b&skv=2024-08-04&sig=ni79f3ZNOlb%2BT5f0s9ZcJth1iT5B/vJbDBmmxlU6QEs%3D"
    elif "horário" in user_input or "funcionamento" in user_input:
        resposta = "Estamos disponíveis para atendimento online 24 horas por dia, todos os dias da semana."
        imagem = "https://cdn-icons-png.flaticon.com/512/151/151770.png"
    elif "entrega" in user_input:
        resposta = "Fazemos entregas em até 2 horas nas principais regiões da cidade. Você pode consultar o prazo informando seu CEP."
        imagem = "https://e7.pngegg.com/pngimages/748/33/png-clipart-package-delivery-cargo-van-others-angle-van-thumbnail.png"
    elif "promoção" in user_input or "oferta" in user_input:
        resposta = "Estamos com descontos em medicamentos genéricos e produtos de cuidados pessoais. Aproveite!"
        imagem = "https://cdn-icons-png.flaticon.com/512/2878/2878556.png"
    elif "vacina" in user_input:
        resposta = "Oferecemos vacinação contra gripe, COVID-19 e outras doenças. É necessário agendar com antecedência."
        imagem = "https://cdn-icons-png.flaticon.com/512/808/808999.png"
    else:
        resposta = "Desculpe, não entendi sua pergunta. Pode reformular?"

    return resposta, imagem

st.title("Assistente Virtual da Farmácia Saúde+")
st.write("Olá! Sou o assistente virtual da Farmácia Saúde+. Como posso ajudar você hoje?")

user_input = st.text_input("Digite sua pergunta:")

if user_input:
    response, image = get_response(user_input)
    st.write("Chatbot: " + response)
    st.image(image, caption="Imagem relacionada", use_container_width=True)