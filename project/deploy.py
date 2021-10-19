import translator
import streamlit as st

lang_list = translator.a

lang_list_select = []
lang_list_select = translator.df.name.unique()
lang_list_select.sort()

def main():       

    st.set_page_config(
        page_title="Text Translator",
        page_icon=":whale:",
        initial_sidebar_state="auto"
        ) 

    st.header("Text Translator")
    st.markdown("""
    #### By: [Phanindra](https://www.linkedin.com/in/palisetty-phanindra-sai/)    
    """)
    colFrom, colempty, colTo = st.columns(3)
      
    # following lines create boxes in which user can enter data required 
    with colFrom:
        st.subheader("From Language")
        from_language = st.selectbox('Known',lang_list_select, 18)
    
    with colTo: 
        st.subheader("To Lanuage")
        to_language = st.selectbox('Foreign',lang_list_select, 29)
        
    with colempty:
        st.empty()
    
    
    st.subheader("Text to be translated")
    text = st.text_area('Enter the Text')

    # when 'Translate' is clicked, make the translation and store it 
    st.text("")
    st.text("")
    id = lang_list[from_language][0]+'-'+lang_list[to_language][0]
    if st.button("Translate") : 
        result = translator.translateText(text, id)
        st.header(result)
    st.write("Note: If you don't see the sidebar, please press the `>` icon on the top left side of your screen.")
    
    st.sidebar.header("About")
    
    st.sidebar.markdown("""
    This application uses IBM Watson® Language Translator-r7 to translate text from one language to another.\
    Learn about API implementation [here](https://cloud.ibm.com/apidocs/language-translator).

    It essentially supports over 60 languages and scroll through the dropdown to go through the sorted list of languages available. 

    Deployment is done using Streamlit package library. And the page icon "Spouting Whale" is by [Twemoji](https://github.com/twitter/twemoji) open-source.
    
    **Source Code**: [GitHub](https://github.com/phanindrapalisetty/Text-Translator)    
    """)
    
               
if __name__=='__main__': 
    main()