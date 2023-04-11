import streamlit as st
from streamlit_elements import media, elements

st.title(":gift: Feliz aniversário Paula Kintschev :cake:")


st.markdown("![Alt Text](https://media2.giphy.com/media/g5R9dok94mrIvplmZd/giphy.gif)")


st.balloons()


with elements("media_player"):
    media.Player(
        url="https://www.youtube.com/watch?v=P52crWWUnOw", 
        playing = True,
        loop = True,
        controls=True
    )