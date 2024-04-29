import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor
from sklearn.metrics import mean_squared_error, accuracy_score
from joblib import dump

# 加载数据
file_path = "/Users/huasongwen/PycharmProjects/JobRecNew/venv/dataset.csv"
data = pd.read_csv(file_path)

# 使用OneHotEncoder对分类特征进行编码
encoder = OneHotEncoder(handle_unknown='ignore')
encoded_features = encoder.fit_transform(data[['PastJobTitles', 'Degree', 'Major', 'ProfessionalCertification']])
encoded_features_df = pd.DataFrame(encoded_features.toarray(), columns=encoder.get_feature_names_out())

# 组合编码特征和原始数据集
features = pd.concat([data[['Salary']], encoded_features_df], axis=1)

# 定义目标变量
target_jobs = data['BestFitJob']
target_skills = data['SkillsNeeded']
target_salary = data['PotentialSalary']

# 划分训练集和测试集
X_train, X_test, y_train_jobs, y_test_jobs = train_test_split(features, target_jobs, test_size=0.2, random_state=42)
X_train_skills, X_test_skills, y_train_skills, y_test_skills = train_test_split(features, target_skills, test_size=0.2, random_state=42)
X_train_salary, X_test_salary, y_train_salary, y_test_salary = train_test_split(features, target_salary, test_size=0.2, random_state=42)

# 初始化模型，这里可能需要不同的模型来预测不同的输出
# 对于分类任务使用决策树分类器
model_jobs = DecisionTreeClassifier(random_state=42)
model_skills = DecisionTreeClassifier(random_state=42)
# 对于连续目标变量使用决策树回归器
model_salary = DecisionTreeRegressor(random_state=42)

# 训练模型
model_jobs.fit(X_train, y_train_jobs)
model_skills.fit(X_train_skills, y_train_skills)
model_salary.fit(X_train_salary, y_train_salary)

# 在训练集上进行预测
y_train_pred_jobs = model_jobs.predict(X_train)
y_train_pred_skills = model_skills.predict(X_train_skills)
y_train_pred_salary = model_salary.predict(X_train_salary)

# 在测试集上进行预测
y_pred_jobs = model_jobs.predict(X_test)
y_pred_skills = model_skills.predict(X_test_skills)
y_pred_salary = model_salary.predict(X_test_salary)

# 计算分类任务的训练集和测试集准确率
accuracy_train_jobs = accuracy_score(y_train_jobs, y_train_pred_jobs)
accuracy_test_jobs = accuracy_score(y_test_jobs, y_pred_jobs)

accuracy_train_skills = accuracy_score(y_train_skills, y_train_pred_skills)
accuracy_test_skills = accuracy_score(y_test_skills, y_pred_skills)

# 计算回归任务的训练集和测试集MSE
mse_train_salary = mean_squared_error(y_train_salary, y_train_pred_salary)
mse_test_salary = mean_squared_error(y_test_salary, y_pred_salary)

# 打印训练集和测试集的准确率和MSE
print(f"Training Accuracy for BestFitJob: {accuracy_train_jobs}")
print(f"Test Accuracy for BestFitJob: {accuracy_test_jobs}")

print(f"Training Accuracy for SkillsNeeded: {accuracy_train_skills}")
print(f"Test Accuracy for SkillsNeeded: {accuracy_test_skills}")

print(f"Training MSE for PotentialSalary: {mse_train_salary}")
print(f"Test MSE for PotentialSalary: {mse_test_salary}")

# 保存模型和编码器
dump(model_jobs, 'model_jobs.joblib')
dump(model_skills, 'model_skills.joblib')
dump(model_salary, 'model_salary.joblib')
dump(encoder, 'one_hot_encoder.joblib')

# Paths for download (relative to your current working directory)
model_paths = {
    "model_jobs": 'model_jobs.joblib',
    "model_skills": 'model_skills.joblib',
    "model_salary": 'model_salary.joblib',
    "encoder": 'one_hot_encoder.joblib'
}


model_paths
