import pandas as pd
from joblib import load


model_jobs = load("./model_jobs.joblib")
model_skills = load("./model_skills.joblib")
model_salary = load("./model_salary.joblib")
encoder = load("./one_hot_encoder.joblib")


new_data = pd.DataFrame({
    # 'PastJobTitles', 'Salary', 'Degree', 'Major', 'ProfessionalCertification' are the features used for training
    'PastJobTitles': ['Software Developer', 'Software Developer'],
    'Salary': [75000, 65000],
    'Degree': ['Bachelors', 'Masters'],
    'Major': ['Computer Science', 'Business Administration'],
    'ProfessionalCertification': ['None', 'PMP']
})

# Apply one-hot encoding using the loaded encoder
encoded_features_new = encoder.transform(new_data[['PastJobTitles', 'Degree', 'Major', 'ProfessionalCertification']])
encoded_features_new_df = pd.DataFrame(encoded_features_new.toarray(), columns=encoder.get_feature_names_out())

# Combine encoded features with other features.
# Assuming 'Salary' was a numeric feature that did not require encoding and was used directly in training.
features_new = pd.concat([new_data[['Salary']], encoded_features_new_df], axis=1)

# Make predictions using the loaded models
predictions_jobs = model_jobs.predict(features_new)
predictions_skills = model_skills.predict(features_new)
predictions_salary = model_salary.predict(features_new)

# Print the predictions
print("Predictions for BestFitJob:")
print(predictions_jobs)

print("Predictions for SkillsNeeded:")
print(predictions_skills)

print("Predictions for PotentialSalary:")
print(predictions_salary)
