from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
from joblib import load

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

# 加载模型和编码器
model_jobs = load("./model_jobs.joblib")
model_skills = load("./model_skills.joblib")
model_salary = load("./model_salary.joblib")
encoder = load("./one_hot_encoder.joblib")

@app.route('/predict', methods=['POST'])
def predict():
    """
    Expecting JSON in format:
    {
      "PastJobTitles": ["Software Developer", "Project Manager", "Data Analyst"],
      "Salary": [75000, 65000, 70000],
      "Degree": ["Bachelors", "Masters", "None"],
      "Major": ["Computer Science", "Business Administration", "None"],
      "ProfessionalCertification": ["None", "PMP", "None"]
    }
    """
    # 从请求中获取JSON数据
    data = request.json

    # 将JSON数据转换为Pandas DataFrame
    try:
        new_data = pd.DataFrame(data)
    except Exception as e:
        return jsonify({'error': 'Bad request', 'message': str(e)}), 400

    # 应用One-Hot编码
    try:
        encoded_features_new = encoder.transform(new_data[['PastJobTitles', 'Degree', 'Major', 'ProfessionalCertification']])
        encoded_features_new_df = pd.DataFrame(encoded_features_new.toarray(), columns=encoder.get_feature_names_out())

        # Combine encoded features with other features
        features_new = pd.concat([new_data[['Salary']], encoded_features_new_df], axis=1)

        # 使用模型进行预测
        predictions_jobs = model_jobs.predict(features_new)
        predictions_skills = model_skills.predict(features_new)
        predictions_salary = model_salary.predict(features_new)

        # Prepare the predictions to be returned as JSON
        response = {
            "BestFitJob": predictions_jobs.tolist(),
            "SkillsNeeded": predictions_skills.tolist(),
            "PotentialSalary": predictions_salary.tolist()
        }
    except Exception as e:
        return jsonify({'error': 'Error during prediction', 'message': str(e)}), 500

    # 将预测结果转换为JSON响应
    return jsonify(response)

@app.route('/')
def hello():
    return 'Hello, Flask!'

if __name__ == "__main__":
    app.run(port=8000, debug=True)
