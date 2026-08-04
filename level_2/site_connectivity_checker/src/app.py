import streamlit as st
import requests
import pandas as pd
from concurrent.futures import ThreadPoolExecutor, as_completed


def check_site_availability(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
        }

        response = requests.get(
            url,
            timeout=5,
            headers=headers
        )

        return url, response.status_code == 200

    except requests.exceptions.RequestException:
        return url, False

def main():

    st.set_page_config(
        page_title="Website Availability Checker",
    )

    st.title("Website Availability Checker")

    st.write("Enter multiple websites, one URL per line.")

    websites = st.text_area("Websites")

    if st.button("Check Websites"):

        if not websites.strip():
            st.warning("Please enter at least one website.")

        else:
            urls = [
                url.strip()
                for url in websites.splitlines()
                if url.strip()
            ]

            urls = [
                url if url.startswith(("http://", "https://")) else "https://" + url
                for url in urls
            ]

            results = {}

            with st.spinner("Checking websites..."):
                with ThreadPoolExecutor(max_workers=20) as executor:
                    futures = [executor.submit(check_site_availability, url) for url in urls]

                    for future in as_completed(futures):
                        url, is_available = future.result()
                        results[url] = is_available

            df = pd.DataFrame([
                {"Website": url, "Status": "Available" if results[url] else "Unavailable"}
                for url in urls
            ])

            st.subheader("Results")
            st.dataframe(
                df,
                use_container_width=True,
                hide_index=True
            )

if __name__ == '__main__':
    main()