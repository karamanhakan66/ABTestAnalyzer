import streamlit as st
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def get_results_translations(lang):
    translations = {
        "English": {
            "test_results": "Test Results",
            "significant": "🎉 The test results are statistically significant!",
            "not_significant": "The test results are not statistically significant.",
            "control_rate": "Control Conversion Rate",
            "test_rate": "Test Conversion Rate",
            "relative_improvement": "Relative Improvement",
            "conversion_rates": "Conversion Rates Comparison",
            "confidence_interval": "Confidence Interval",
            "control": "Control",
            "test": "Test",
            "difference": "Difference",
            "visualization_title": "A/B Test Results Visualization",
            "detailed_stats": "Detailed Statistics",
            "p_value": "P-value",
            "absolute_difference": "Absolute difference",
            "confidence_interval_range": "Confidence Interval"
        },
        "Türkçe": {
            "test_results": "Test Sonuçları",
            "significant": "🎉 Test sonuçları istatistiksel olarak anlamlıdır!",
            "not_significant": "Test sonuçları istatistiksel olarak anlamlı değildir.",
            "control_rate": "Kontrol Dönüşüm Oranı",
            "test_rate": "Test Dönüşüm Oranı",
            "relative_improvement": "Göreceli İyileştirme",
            "conversion_rates": "Dönüşüm Oranları Karşılaştırması",
            "confidence_interval": "Güven Aralığı",
            "control": "Kontrol",
            "test": "Test",
            "difference": "Fark",
            "visualization_title": "A/B Test Sonuçları Görselleştirmesi",
            "detailed_stats": "Detaylı İstatistikler",
            "p_value": "P-değeri",
            "absolute_difference": "Mutlak fark",
            "confidence_interval_range": "Güven Aralığı"
        }
    }
    return translations[lang]

def display_results(results):
    """
    Display the A/B test results using various visualizations and metrics
    
    Args:
        results (dict): Dictionary containing calculated metrics
    """
    # Get current language from session state
    lang = st.session_state.get('language', 'English')
    t = get_results_translations(lang)
    
    # Display significance verdict
    st.header(t["test_results"])
    
    if results['is_significant']:
        st.success(t["significant"])
    else:
        st.warning(t["not_significant"])

    # Display key metrics
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric(
            t["control_rate"],
            f"{results['control_rate']:.2%}"
        )
    
    with col2:
        st.metric(
            t["test_rate"],
            f"{results['test_rate']:.2%}"
        )
    
    with col3:
        st.metric(
            t["relative_improvement"],
            f"{results['relative_difference']:+.2f}%"
        )

    # Create visualization
    fig = make_subplots(
        rows=1, cols=2,
        subplot_titles=(t["conversion_rates"], t["confidence_interval"])
    )

    # Bar chart for conversion rates
    fig.add_trace(
        go.Bar(
            name=t["control"],
            x=[t["control"]],
            y=[results['control_rate']],
            text=[f"{results['control_rate']:.2%}"],
            textposition='auto',
        ),
        row=1, col=1
    )

    fig.add_trace(
        go.Bar(
            name=t["test"],
            x=[t["test"]],
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
            name=t["difference"],
            marker=dict(size=10)
        ),
        row=1, col=2
    )

    fig.update_layout(
        height=400,
        showlegend=True,
        title_text=t["visualization_title"]
    )

    st.plotly_chart(fig, use_container_width=True)

    # Display detailed statistics
    st.subheader(t["detailed_stats"])
    st.markdown(f"""
    - **{t["p_value"]}**: {results['p_value']:.4f}
    - **{t["absolute_difference"]}**: {results['absolute_difference']:.4f}
    - **{t["confidence_interval_range"]}**: ({results['ci_lower']:.4f}, {results['ci_upper']:.4f})
    """)
