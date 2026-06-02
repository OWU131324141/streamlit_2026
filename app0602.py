import streamlit as st

# if "count" not in st.session_state:
#     st.session_state["count"] = 1

if "kibun_history" not in st.session_state:
    st.session_state["kibun_history"] = []

col1,col2,col3,col4 = st.columns(4)

with col1:
    if st.button("😊 嬉しい"):
        st.session_state["kibun_history"].append("😊 嬉しい")

with col2:
    if st.button("😢 悲しい"):
        st.session_state["kibun_history"].append("😢 悲しい")

with col3:
    if st.button("😴 眠い"):
        st.session_state["kibun_history"].append("😴 眠い")

with col4:
    if st.button("🍕 お腹すいた"):
        st.session_state["kibun_history"].append("🍕 お腹すいた")

for kibun in st.session_state["kibun_history"]:
    st.write(kibun)

# if st.button("カウンター"):
#     st.session_state["count"] = st.session_state["count"] + 1

# st.write(st.session_state["count"])


# st.write("メイン画面")

# st.header("自己紹介")
# st.write("名前；小池")

# with st.expander("詳細"):
#     st.write("生年月日：2006年1月18日")
    
#     col1,col2,col3 = st.columns(3)
    
#     with col1:
#         st.header("Cat") 
#         st.image("https://static.streamlit.io/examples/cat.jpg")

#     with col2:
#         st.header("Dog") 
#         st.image("https://static.streamlit.io/examples/dog.jpg")

#     with col3: 
#         st.header("Owl") 
#         st.image("https://static.streamlit.io/examples/owl.jpg")


# st.sidebar.write("サイドバー")
# name = st.sidebar.text_input(
#     "お名前"
# )

# student_id = st.sidebar.text_input(
#     "学籍番号"
# )

# if name and student_id:
#     st.sidebar.write(name)
#     st.sidebar.write("学籍番号は"+student_id+"です。")