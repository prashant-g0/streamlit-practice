import streamlit as st

def main():
    st.title("This is an Age Calculator.")
    st.header("Remember: Age is just a number!")

    name = st.text_input("Enter your name:", max_chars=50, placeholder="Prash")
    if st.button("Enter"): 
        st.session_state["Name"] = name
    
    if "Name" in st.session_state:
        st.subheader(f"Hello, {st.session_state["Name"]}!")
    
        year = st.number_input("Enter your age:(1947-2026)", min_value=1947, max_value=2026, placeholder="2005")
        if st.button("Calculate"):
            age = 2026 - year
            st.success(f"You are/will be {age} years old in 2026.")
    else:
        st.error("Please enter your name first.")


if __name__ == "__main__":
    main()
