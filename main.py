import streamlit as st
import numpy as np
import pandas as pd

st.title('テスト')
st.write('DataFrame')

df = pd.DataFrame(
    np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
    columns=['lat', 'lon']
)
if st.checkbox('Show Map'):
    st.map(df)

condition = st.slider('あなたの今の調子は？', 0, 100, 50)
'コンディション:', condition

