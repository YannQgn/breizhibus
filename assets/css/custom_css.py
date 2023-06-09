import streamlit as st

# CSS personnalisé
def load_css():
    css = st.markdown('''
    <style>
    h1 {
        color: rgb(255 255 255);
    }

    img {
        -webkit-box-shadow: 1px 2px 23px -2px #000000; 
        box-shadow: 1px 2px 23px -2px #000000;
    }

    .css-17b7mgn {
        -webkit-box-shadow: 1px 2px 23px -2px #000000;
        box-shadow: 1px 2px 23px -2px #000000;
    }

    .css-16idsys p {
        font-size: 20px;
    }

    .css-1b0udgb {
        font-size: 20px;
        color: rgb(255 255 255);
    }

    .css-81oif8 {
        font-size: 20px;
        color: rgb(255 255 255)
    }
    
    .css-fg4pbf {
        background-image: url('https://a-static.besthdwallpaper.com/abstract-color-waves-crafted-in-dark-tones-wallpaper-3840x1080-96552_75.jpg');
        background-size: cover;
    }

    .st-bw { 
        background-color: rgb(225 241 161); 
    }

    .css-vk3wp9 {
        -webkit-box-shadow: 7px 2px 15px -6px #00000059;
        box-shadow: 7px 2px 15px -6px #00000059;
    }
    </style>''', unsafe_allow_html=True)

    return css