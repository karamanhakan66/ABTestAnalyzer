import streamlit as st

def get_form_translations(lang):
    translations = {
        "English": {
            "control_group": "Control Group (A)",
            "test_group": "Test Group (B)",
            "total_visitors_control": "Total visitors in Control Group",
            "total_visitors_control_help": "Enter the total number of visitors in your control group",
            "conversions_control": "Conversions in Control Group",
            "conversions_control_help": "Enter the number of conversions in your control group",
            "total_visitors_test": "Total visitors in Test Group",
            "total_visitors_test_help": "Enter the total number of visitors in your test group",
            "conversions_test": "Conversions in Test Group",
            "conversions_test_help": "Enter the number of conversions in your test group"
        },
        "Türkçe": {
            "control_group": "Kontrol Grubu (A)",
            "test_group": "Test Grubu (B)",
            "total_visitors_control": "Kontrol Grubundaki Toplam Ziyaretçi",
            "total_visitors_control_help": "Kontrol grubunuzdaki toplam ziyaretçi sayısını girin",
            "conversions_control": "Kontrol Grubundaki Dönüşümler",
            "conversions_control_help": "Kontrol grubunuzdaki dönüşüm sayısını girin",
            "total_visitors_test": "Test Grubundaki Toplam Ziyaretçi",
            "total_visitors_test_help": "Test grubunuzdaki toplam ziyaretçi sayısını girin",
            "conversions_test": "Test Grubundaki Dönüşümler",
            "conversions_test_help": "Test grubunuzdaki dönüşüm sayısını girin"
        }
    }
    return translations[lang]

def render_input_form():
    """
    Render the input form for A/B test data
    
    Returns:
        tuple: (control_size, control_conv, test_size, test_conv)
    """
    # Get current language from session state
    lang = st.session_state.get('language', 'English')
    t = get_form_translations(lang)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader(t["control_group"])
        control_size = st.number_input(
            t["total_visitors_control"],
            min_value=1,
            value=1000,
            step=1,
            help=t["total_visitors_control_help"]
        )
        
        control_conv = st.number_input(
            t["conversions_control"],
            min_value=0,
            max_value=int(control_size),
            value=100,
            step=1,
            help=t["conversions_control_help"]
        )

    with col2:
        st.subheader(t["test_group"])
        test_size = st.number_input(
            t["total_visitors_test"],
            min_value=1,
            value=1000,
            step=1,
            help=t["total_visitors_test_help"]
        )
        
        test_conv = st.number_input(
            t["conversions_test"],
            min_value=0,
            max_value=int(test_size),
            value=120,
            step=1,
            help=t["conversions_test_help"]
        )
    
    return control_size, control_conv, test_size, test_conv
