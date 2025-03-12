import streamlit as st

def render_input_form():
    """
    Render the input form for A/B test data
    
    Returns:
        tuple: (control_size, control_conv, test_size, test_conv)
    """
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Control Group (A)")
        control_size = st.number_input(
            "Total visitors in Control Group",
            min_value=1,
            value=1000,
            step=1,
            help="Enter the total number of visitors in your control group"
        )
        
        control_conv = st.number_input(
            "Conversions in Control Group",
            min_value=0,
            max_value=int(control_size),
            value=100,
            step=1,
            help="Enter the number of conversions in your control group"
        )

    with col2:
        st.subheader("Test Group (B)")
        test_size = st.number_input(
            "Total visitors in Test Group",
            min_value=1,
            value=1000,
            step=1,
            help="Enter the total number of visitors in your test group"
        )
        
        test_conv = st.number_input(
            "Conversions in Test Group",
            min_value=0,
            max_value=int(test_size),
            value=120,
            step=1,
            help="Enter the number of conversions in your test group"
        )
    
    return control_size, control_conv, test_size, test_conv
