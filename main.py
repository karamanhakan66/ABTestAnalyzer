import streamlit as st
from components.input_form import render_input_form
from components.results_display import display_results
from utils.statistical_calculator import calculate_ab_test_results

def main():
    st.set_page_config(
        page_title="A/B Test Calculator",
        page_icon="📊",
        layout="wide"
    )

    st.title("A/B Test Statistical Significance Calculator")
    
    st.markdown("""
    This calculator helps you determine if your A/B test results are statistically significant.
    Enter the data from your control (A) and test (B) groups to analyze the results.
    """)

    # Render input form and get values
    control_size, control_conv, test_size, test_conv = render_input_form()

    if st.button("Calculate Results"):
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
                st.error(f"Error calculating results: {str(e)}")
        else:
            st.warning("Please fill in all fields with valid numbers.")

    # Add explanatory section
    with st.expander("Understanding Statistical Terms"):
        st.markdown("""
        - **P-value**: The probability that the observed difference between variants occurred by chance.
        - **Confidence Interval**: A range of values that we can be confident contains the true value.
        - **Statistical Significance**: Typically achieved when p-value < 0.05 (95% confidence level).
        - **Conversion Rate**: The percentage of users who completed the desired action.
        """)

if __name__ == "__main__":
    main()
