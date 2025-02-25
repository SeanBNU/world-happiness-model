import pandas as pd
import numpy as np
from scipy import interpolate

# THIS IS HOW CLAUDE IMPUTED

# Load your data
df = pd.read_csv('your_data.csv')

# Make sure Year is numeric
df['Year'] = pd.to_numeric(df['Year'])

# Function to impute using time trajectory for each country
def impute_by_time_trajectory(dataframe, country_col='Country', year_col='Year'):
    # Create a copy to avoid modifying the original
    df_imputed = dataframe.copy()
    
    # Get list of all columns that might need imputation (exclude Country, Code, Year)
    value_columns = [col for col in df_imputed.columns if col not in [country_col, 'Code', year_col]]
    
    # Iterate through each country
    for country in df_imputed[country_col].unique():
        # Get data for this country
        country_data = df_imputed[df_imputed[country_col] == country].sort_values(by=year_col)
        
        # For each value column
        for col in value_columns:
            # Check if there are any missing values for this country and column
            if country_data[col].isna().any():
                # Get non-missing data points
                existing_years = country_data[~country_data[col].isna()][year_col].values
                existing_values = country_data[~country_data[col].isna()][col].values
                
                # If enough data points exist for interpolation (at least 2)
                if len(existing_years) >= 2:
                    # Create interpolation function
                    f = interpolate.interp1d(existing_years, existing_values, 
                                            bounds_error=False, 
                                            fill_value=(existing_values[0], existing_values[-1]),
                                            kind='linear')
                    
                    # Get years with missing values
                    missing_years = country_data[country_data[col].isna()][year_col].values
                    
                    # Interpolate those values and update the dataframe
                    for year in missing_years:
                        interpolated_value = f(year)
                        mask = (df_imputed[country_col] == country) & (df_imputed[year_col] == year)
                        df_imputed.loc[mask, col] = interpolated_value
                
                # If not enough data points, use forward/backward fill
                else:
                    # Get country indices for this column
                    country_indices = df_imputed[df_imputed[country_col] == country].index
                    # Use forward fill then backward fill for remaining NAs
                    df_imputed.loc[country_indices, col] = df_imputed.loc[country_indices, col].ffill().bfill()
    
    return df_imputed

# Apply the imputation
df_imputed = impute_by_time_trajectory(df)

# Check if there are any remaining missing values
missing_after = df_imputed.isna().sum().sum()
print(f"Missing values after imputation: {missing_after}")