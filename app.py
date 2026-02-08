import streamlit as st
import pandas as pd
import joblib
from streamlit_extras.let_it_rain import rain

model = joblib.load('lg_model.plk')
scale = joblib.load('scale.plk')

st.set_page_config(page_title='Penguin Classification', page_icon= '🐧', layout= 'wide')

page_bg = '''
    <style>
        [data-testid="stAppViewContainer"] {
        background: linear-gradient(180deg, #090909 0%, #271033 50%, #1e3c72 100%);
        background-attachment: fixed;
        background-position: center;
}
        }
    </style>
'''
st.markdown(page_bg, unsafe_allow_html=True)

st.title('PENGUIN CLASSIFIER')

col1, col2, col3, col4 = st.columns(4)

with col1 :
    
    st.subheader('Culmen Length')
    c_len = st.number_input('',30,60,43)
    
with col2 :
    
    st.subheader('Culmen Depth')
    c_dpt = st.number_input('',10,25,17)
    
with col3 :
    
    st.subheader('Flipper Length')
    f_len = st.slider('',170,235,201)
    
with col4 :
    
    st.subheader('Body Mass')
    mass = st.slider('',2600,6400,4202)

btn = st.button('Find')

if btn :
    st.snow()
    
    input_row = {
        'culmen_length_mm' : [c_len],
        'culmen_depth_mm' : [c_dpt],
        'flipper_length_mm' : [f_len],
        'body_mass_g' : [mass]
    }

    input_df = pd.DataFrame(input_row)
    scaled_df = scale.transform(input_df)
    pred_df = model.predict(scaled_df)[0]

    match (pred_df[0]) :
        case 0 :
            species = 'Adelie'
        case 1 :
            species = 'Chinstrap'
        case 2 :
            species = 'Gentoo'
    
    match (pred_df[1]) :
        case 0 :
            island = 'Biscoe'
        case 1 :
            island = 'Dream'
        case 2 :
            island = 'Torgersen'
    
    st.success(f'It is a {species} penguin. This is from {island} island')
    rain(
        emoji="🐧",
        font_size=75,
        falling_speed= 5,
        animation_length= 'short'
    )
    
    
    
    
    