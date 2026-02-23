import streamlit as st
from constants import CURRENCIES
from currency_conventor import get_exchange_rate, conventor_currency

st.image("/home/mary/project_based_python/projects/level_2/currency_conventor/src/Money Currency Pixel Pattern Design Vector Download.jpg", width = 1500)
st.title(":dollar: Currency Conventor")
st.markdown("""This tool allows you to instantly convert amounts between different currencies :earth_africa:

Enter the amount and choose the currencies to see the result.""")

base_currency = st.selectbox("From currency (Base): ", CURRENCIES)
target_currency = st.selectbox("To currency (Target): ", CURRENCIES)
amount = st.number_input("Enter amount: ", min_value = 0)

if amount > 0 and base_currency and target_currency:
    exchange_rate = get_exchange_rate(base_currency, target_currency)

    if exchange_rate:
        converted_amount = conventor_currency(amount, exchange_rate)
        st.success(f"✅ Exchange Rate: {exchange_rate:.3f}")
        col1, col2, col3 = st.columns(3)
        col1.metric(label="Base Currency", value = f"{amount} {base_currency}")
        col2.markdown("<h1 style='text-align: center; margin: 0; color: red;'>&#8594;</h1>", unsafe_allow_html=True)
        col3.metric(label="Target Currency", value=f"{converted_amount:.2f} {target_currency}")

    else:
        st.error("Error fetching exchange rate.")

st.markdown("---")
st.markdown("### ℹ️ About This Tool")
st.markdown("""
This currency converter uses real-time exchange rates provided by the ExchangeRate-API.
- The conversion updates automatically as you input the amount or change the currency.
- Enjoy seamless currency conversion without the need to press a button!
""")