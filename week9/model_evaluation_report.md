 Car Price Prediction Model Evaluation Report
1. Model Overview
- Model Type: Linear Regression
- Target Variable: Price
- Feature Used: Year of manufacture
- Dataset: df20 (subset of car listings)
3. Interpretation
- The model performs reasonably well, with an R² of 0.80, indicating strong explanatory power using just the year of manufacture.
- MAE and RMSE suggest moderate prediction errors, which may be acceptable depending on the price range of vehicles in the dataset.
- MSE is high due to squaring large errors, which is typical in regression tasks with wide price ranges.
4. Limitations
- Single Feature: Using only Year of manufacture limits the model’s ability to capture other influential factors like brand, mileage, engine size, etc.
- Linear Assumption: The model assumes a linear relationship, which may not hold across all vehicle types or price segments.
- Feature Expansion: Include additional predictors such as Engine size, Mileage, Brand, and Fuel type.
- Model Comparison: Try other models like Random Forest or XGBoost for potentially better performance.
- Residual Analysis: Plot residuals to check for patterns or heteroscedasticity.
- Cross-Validation: Use k-fold cross-validation to ensure robustness across different data splits.




