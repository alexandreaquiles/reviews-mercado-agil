import os
from dotenv import load_dotenv

import pandas as pd # csv

import google.generativeai as genai # genai

load_dotenv()

genai.configure(api_key=os.getenv('GEMINI_API_KEY'))

generation_config = {
  "temperature": 0,
  "response_mime_type": "text/plain"
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config
)

# ler o csv e percorrer os itens

reviews = pd.read_csv('reviews-entrega-MercadoAgil-imagens.csv')
for index, review in reviews.iterrows():
  reviewer_id = review['reviewer_id']
  reviewer_email = review['reviewer_email']
  review_image = review['review_image']
  
  path_image = f'image/{review_image}'
  
  image_file = genai.upload_file(path=path_image)
  
  prompt = 'Transcreva a imagem em anexo'
  response = model.generate_content([prompt, image_file])

  transcricao = response.text

  print(reviewer_email)
  print(transcricao)
  print('\n')