import streamlit as st
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def display_results(results):
    """
    Display the A/B test results using various visualizations and metrics
    
    Args:
        results (dict): Dictionary containing calculated metrics
    """
    # Display significance verdict
    st.header("Test Results")
    
    if results['is_significant']:
        st.success("🎉 The test results are statistically significant!")
    else:
        st.warning("The test results are not statistically significant.")

    # Display key metrics
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric(
            "Control Conversion Rate",
            f"{results['control_rate']:.2%}"
        )
    
    with col2:
        st.metric(
            "Test Conversion Rate",
            f"{results['test_rate']:.2%}"
        )
    
    with col3:
        st.metric(
            "Relative Improvement",
            f"{results['relative_difference']:+.2f}%"
        )

    # Create visualization
    fig = make_subplots(
        rows=1, cols=2,
        subplot_titles=("Conversion Rates Comparison", "Confidence Interval")
    )

    # Bar chart for conversion rates
    fig.add_trace(
        go.Bar(
            name="Control",
            x=["Control"],
            y=[results['control_rate']],
            text=[f"{results['control_rate']:.2%}"],
            textposition='auto',
        ),
        row=1, col=1
    )

    fig.add_trace(
        go.Bar(
            name="Test",
            x=["Test"],
            y=[results['test_rate']],
            text=[f"{results['test_rate']:.2%}"],
            textposition='auto',
        ),
        row=1, col=1
    )

    # Confidence interval plot
    fig.add_trace(
        go.Scatter(
            x=[0],
            y=[results['absolute_difference']],
            error_y=dict(
                type='data',
                symmetric=True,
                array=[1.96 * (results['ci_upper'] - results['ci_lower']) / 4],
                color="rgba(0,0,0,0.5)"
            ),
            mode='markers',
            name='Difference',
            marker=dict(size=10)
        ),
        row=1, col=2
    )

    fig.update_layout(
        height=400,
        showlegend=True,
        title_text="A/B Test Results Visualization"
    )

    st.plotly_chart(fig, use_container_width=True)

    # Display detailed statistics
    st.subheader("Detailed Statistics")
    st.markdown(f"""
    - **P-value**: {results['p_value']:.4f}
    - **Absolute difference**: {results['absolute_difference']:.4f}
    - **Confidence Interval**: ({results['ci_lower']:.4f}, {results['ci_upper']:.4f})
    """)
