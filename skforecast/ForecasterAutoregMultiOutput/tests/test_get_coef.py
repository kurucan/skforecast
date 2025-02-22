# Test method get_coef()
# ==============================================================================

import numpy as np
import pandas as pd
from skforecast.ForecasterAutoregMultiOutput import ForecasterAutoregMultiOutput
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor


def test_get_coef_when_regressor_is_LinearRegression_lags_3_step_1():
    '''
    Test output of get_coef for step 1, when regressor is LinearRegression with lags=3
    and it is trained with y=pd.Series(np.arange(5)).
    '''
    forecaster = ForecasterAutoregMultiOutput(LinearRegression(), lags=3, steps=1)
    forecaster.fit(y=pd.Series(np.arange(5)))
    results = forecaster.get_coef(step=1)
    expected = pd.DataFrame({
                    'feature': ['lag_1', 'lag_2', 'lag_3'],
                    'coef': np.array([0.33333333, 0.33333333, 0.33333333])
                })
    pd.testing.assert_frame_equal(results, expected)

    
def test_output_get_coef_when_regressor_is_RandomForest():
    '''
    Test output of get_coef when regressor is RandomForestRegressor with lags=3
    and it is trained with y=pd.Series(np.arange(5)).
    '''
    forecaster = ForecasterAutoregMultiOutput(RandomForestRegressor(), lags=3, steps=1)
    forecaster.fit(y=pd.Series(np.arange(5)))
    expected = None
    results = forecaster.get_coef(step=1)
    assert results is expected
    