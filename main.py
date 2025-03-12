import streamlit as st
from components.input_form import render_input_form
from components.results_display import display_results
from utils.statistical_calculator import calculate_ab_test_results

def get_translation(lang):
    translations = {
        "English": {
            "title": "A/B Test Statistical Significance Calculator",
            "description": """
            This calculator helps you determine if your A/B test results are statistically significant.
            Enter the data from your control (A) and test (B) groups to analyze the results.
            """,
            "calculate_button": "Calculate Results",
            "fill_warning": "Please fill in all fields with valid numbers.",
            "error_msg": "Error calculating results: ",
            "understanding_stats": "Understanding Statistical Terms",
            "stats_explanation": """
            - **P-value**: The probability that the observed difference between variants occurred by chance.
            - **Confidence Interval**: A range of values that we can be confident contains the true value.
            - **Statistical Significance**: Typically achieved when p-value < 0.05 (95% confidence level).
            - **Conversion Rate**: The percentage of users who completed the desired action.
            """
        },
        "Türkçe": {
            "title": "A/B Test İstatistiksel Anlamlılık Hesaplayıcı",
            "description": """
            Bu hesaplayıcı, A/B test sonuçlarınızın istatistiksel olarak anlamlı olup olmadığını belirlemenize yardımcı olur.
            Sonuçları analiz etmek için kontrol (A) ve test (B) gruplarınızdan elde edilen verileri girin.
            """,
            "calculate_button": "Sonuçları Hesapla",
            "fill_warning": "Lütfen tüm alanları geçerli sayılarla doldurun.",
            "error_msg": "Sonuçlar hesaplanırken hata oluştu: ",
            "understanding_stats": "İstatistiksel Terimleri Anlama",
            "stats_explanation": """
            - **P-değeri**: Varyantlar arasında gözlemlenen farkın şans eseri ortaya çıkma olasılığı.
            - **Güven Aralığı**: Gerçek değeri içerdiğinden emin olduğumuz değer aralığı.
            - **İstatistiksel Anlamlılık**: Genellikle p-değeri < 0.05 (95% güven düzeyi) olduğunda elde edilir.
            - **Dönüşüm Oranı**: İstenen eylemi tamamlayan kullanıcıların yüzdesi.
            """
        }
    }
    return translations[lang]

def main():
    st.set_page_config(
        page_title="A/B Test Calculator",
        page_icon="📊",
        layout="wide"
    )

    # Dil seçimi
    lang = st.sidebar.selectbox(
        "Language / Dil",
        ["English", "Türkçe"]
    )
    
    # Dil seçimini session state'e kaydet
    st.session_state['language'] = lang
    
    # Çevirileri al
    t = get_translation(lang)

    st.title(t["title"])
    st.markdown(t["description"])

    # Render input form and get values
    control_size, control_conv, test_size, test_conv = render_input_form()

    if st.button(t["calculate_button"]):
        if control_size and control_conv and test_size and test_conv:
            try:
                # Calculate statistical results
                results = calculate_ab_test_results(
                    control_size, control_conv,
                    test_size, test_conv
                )
                
                # Display results
                display_results(results)
                
            except Exception as e:
                st.error(t["error_msg"] + str(e))
        else:
            st.warning(t["fill_warning"])

    # Add explanatory section
    with st.expander(t["understanding_stats"]):
        st.markdown(t["stats_explanation"])

if __name__ == "__main__":
    main()
