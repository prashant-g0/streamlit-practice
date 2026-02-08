import streamlit as st

def main():
    st.title("This is a BMI Calculator")
    weight = st.number_input("Enter your weight in KGs", min_value=0.0, placeholder="Type weight")
    height = st.number_input("Enter your height in Meters", min_value=1.0, placeholder="Type height")

    if st.button("Calculate BMI"):
        bmi = weight/(height**2)
        st.success(f"Your BMI Score is {bmi:.2f}")
    
        if bmi < 18.5: 
            st.info("Hawa tez ho toh sambhal ke chalna!")
            st.image("img/patlu.jpg", caption="You lack vitamin me ;)", width=250)
        elif 18.5 <= bmi <= 24.9: 
            st.success("Body bhi khush, doctor bhi khush!")
            st.image("img/inspector.jpg", caption="Let's meet tonight :3", width=250)
        elif 25 <= bmi <= 29.9: 
            st.error("Abbey mote, gym ja gym!")
            st.image("img/motu.jpg", caption="Seems like you're the matress tonight X)", width=250)
        elif bmi > 29.9: 
            st.error("Dharti pr bhoj, gende!")
            st.image("img/hippo.jpg", caption="You're literally a Hippo!", width=250)


if __name__ == "__main__":
    main()
