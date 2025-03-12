import numpy as np
from scipy import stats
import pandas as pd

def calculate_ab_test_results(control_size, control_conv, test_size, test_conv):
    """
    Calculate statistical significance and related metrics for A/B test results.
    
    Args:
        control_size (int): Size of control group
        control_conv (int): Number of conversions in control group
        test_size (int): Size of test group
        test_conv (int): Number of conversions in test group
        
    Returns:
        dict: Dictionary containing all calculated metrics
    """
    # Input validation
    if any(x <= 0 for x in [control_size, test_size]):
        raise ValueError("Group sizes must be positive numbers")
    if control_conv > control_size or test_conv > test_size:
        raise ValueError("Conversions cannot exceed group size")

    # Calculate conversion rates
    control_rate = control_conv / control_size
    test_rate = test_conv / test_size
    
    # Calculate absolute difference
    absolute_difference = test_rate - control_rate
    relative_difference = (test_rate - control_rate) / control_rate * 100

    # Calculate standard errors
    control_se = np.sqrt((control_rate * (1 - control_rate)) / control_size)
    test_se = np.sqrt((test_rate * (1 - test_rate)) / test_size)
    
    # Calculate pooled standard error
    pooled_se = np.sqrt(control_se**2 + test_se**2)
    
    # Calculate z-score
    z_score = absolute_difference / pooled_se
    
    # Calculate two-tailed p-value
    p_value = 2 * (1 - stats.norm.cdf(abs(z_score)))
    
    # Calculate confidence intervals (95%)
    ci_margin = 1.96 * pooled_se
    ci_lower = absolute_difference - ci_margin
    ci_upper = absolute_difference + ci_margin
    
    return {
        'control_rate': control_rate,
        'test_rate': test_rate,
        'absolute_difference': absolute_difference,
        'relative_difference': relative_difference,
        'p_value': p_value,
        'ci_lower': ci_lower,
        'ci_upper': ci_upper,
        'is_significant': p_value < 0.05,
        'control_size': control_size,
        'control_conv': control_conv,
        'test_size': test_size,
        'test_conv': test_conv
    }
