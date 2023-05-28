#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import pickle
import streamlit as st
from PIL import Image

# In[2]:


# Load the saved model
loaded_model = pickle.load(open('Praktikum/trained_model.sav', 'rb'))


# In[ ]:
page_bg_color = """
<style> 
[data-testid="stAppViewContainer"]{
  background-color: #A79AFF;

</style>

"""

st.markdown(page_bg_color, unsafe_allow_html=True)




# Create a function for Prediction
def deathevent_prediction(input_data):

    # Change the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # Reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
    
    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
      return 'Pasien Diprediksi Tidak Meninggal'
    else:
      return 'Pasien Diprediksi Meninggal'

def main():
    
    # Give a title
    st.title('Death Event Prediction Web App')
        
    img = Image.open("images (2).png")
    st.image(img, width=250)
    st.subheader('Selamat datang di Aplikasi Prediksi Kemungkinan Kematian Pasien Gagal Jantung')
    st.caption("Aplikasi ini merupakan sebuah aplikasi yang dapat digunakan untuk memprediksi kemungkinan kematian dari pasien gagal jantung dari hasil klasifikasi variabel - variabel pada dataset Death Event oleh Tanvir Ahmad, Assia Munir, Sajjad Haider Bhatti, Muhammad Aftab, and Muhammad Ali Raza (Government College University, Faisalabad, Pakistan)")
    st.caption("Pada aplikasi ini digunakan K-Nearest Neighbour sebagai algoritma klasifikasi")
    
    # To get the input data from the user
    age = st.number_input('Age of the person')
    anaemia = st.number_input('decrease of red blood cells or hemoglobin ')
    creatinine_phosphokinase = st.number_input('level of the CPK ')
    diabetes = st.number_input('if the patient has diabetes ')
    ejection_fraction = st.number_input('percentage of blood leaving the heart at each contraction')
    high_blood_pressure = st.number_input('if the patient has hypertension ')
    platelets = st.number_input('platelets in the blood value')
    serum_creatinine = st.number_input('level of serum creatinine in the blood ')
    serum_sodium = st.number_input('level of serum sodium in the blood')
    sex = st.number_input('woman or man ')
    smoking = st.number_input('if the patient smokes or not ')
    time = st.number_input('follow-up period- days')
    
    # Code for Prediction
    diagnosis = ''
    
    # Create a button for Prediction
    
    if st.button('Death Event Test Result'):
        diagnosis = deathevent_prediction([age, anaemia, creatinine_phosphokinase, diabetes, ejection_fraction, high_blood_pressure, platelets, serum_creatinine, serum_sodium, sex, smoking, time])
        
    st.info(diagnosis)



if __name__ == '__main__':
    main()
  
with st.sidebar:
        st.title('Death Event Prediction Web App')
        st.write("Nama Anggota Kelompok 9 : ")
        st.caption('- Ayu Anggraini (20051214001)')
        st.caption('- Bunga Meilita (20051214001)')
        st.caption('- Devi Yanti (200512140019)')
        st.caption('- Faalih Hibban (20051214001)')
        st.caption('- Fauza Wayah   (20051214029)')
        st.caption('- Darell Timotius (20051214067)')
        
# In[ ]:




