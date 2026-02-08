import streamlit as st
import requests as re

def main():
    st.title("World Currency Converter!")
    st.subheader("Convert X currency to Y currency")

    url = "https://api.exchangerate-api.com/v4/latest/INR"
    response = re.get(url)
    
    if response.status_code == 200:
        data = response.json()
        available_conversions = [rates for rates in data["rates"].keys()]

        user_currency = st.selectbox("Enter your currency:", available_conversions)
        amount = st.number_input("Enter amount: ", min_value=1, placeholder="100")
        target_currency = st.selectbox("Enter target currency:", available_conversions)

        if st.button("Convert"):
            converted_value = (amount / data["rates"][user_currency]) * data["rates"][target_currency]
            st.success(f"{amount} {user_currency} =  {converted_value:.2f} {target_currency}")
    else:
        st.error("⚠️ Failed to fetch conversion rate. Try later")
    
    st.subheader("Quick FAQs")
    with st.expander("What is the logic of conversion ? ", ):
        st.write('''The source currency is first converted to USD (base) and then that amount is converted to target currency.''')
    



if __name__ == "__main__":
    main()
