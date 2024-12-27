# **Car Price Prediction System**

### **📊 Project Overview**
The Car Price Prediction System is a web application that estimates the resale price of a car based on key attributes provided by the user. It leverages a Linear Regression Model trained on historical car price data and uses Streamlit for an interactive user interface.

---
### **💡Motive of the Project**:
The primary motive of this project is to simplify the process of evaluating car resale prices, enabling users to make informed decisions when buying or selling used cars. It aims to eliminate guesswork and provide reliable price estimates based on historical data and machine learning techniques.

---
### **🏆Achievements**:
- Successfully implemented a Linear Regression Model with high prediction accuracy.
- Built an interactive and user-friendly web application using Streamlit.
- Provided a seamless user experience for input and output handling.
- Enabled instant predictions with real-time feedback.
- Developed a modular and scalable codebase for future enhancements.

### **🛠️ Features**

1. **User-Friendly Interface**: Allows users to input car details such as company, model, year of purchase, fuel type, and kilometers driven.
2. **Accurate Price Prediction**: Uses a pre-trained Linear Regression model to predict car prices.
3. **Interactive Widgets**:Sliders, dropdowns, and buttons make the input process simple and intuitive.
4. **Real-Time Results**:  Displays predictions instantly upon user input.


---

### **💻 Technologies Used**
- **Programming Language:** Python
- **Libraries:**
   - Pandas
   - NumPy
   - Streamlit
   - Pickle
- Model Type: Linear Regression
- Dataset: Cleaned data file (cleaned_car.csv) for training the model.
- GitHub (for version control)

---
## **📁Project Structure**:
![image](https://github.com/user-attachments/assets/14574675-92c1-40fc-8322-741860f3031d)

- app.py: Contains the Streamlit application code.

- helper.py: Loads the pre-trained model for predictions.

- LinearRegressionModel.pkl: Serialized Linear Regression model.

- cleaned_car.csv: Dataset used for training.

- requirements.txt: Dependencies needed for running the application.

## **Example Prediction**:
![image](https://github.com/user-attachments/assets/1ac502cf-529f-4e40-81c4-05009bc82e69)
---

## 📚 **How to Run the Project**

1. Clone the Repository:

```bash
   git clone https://github.com/yourusername/Car_price_prediction.git
```
2. Install Dependencies:
```bash
 pip install -r requirements.txt
```
3. Run the Application:
```bash
streamlit run app.py
```
4. Open the App in Browser:
```bash
 http://localhost:8501
```

## 🔄Future Enhancements:

- Add more features like transmission type and owner history.

- Include multiple model options (e.g., Decision Trees, Random Forest).

- Enhance UI with additional styling and charts.

##  **👨‍💻 Author**
- Sai Vamsi Sistu

- Email: 2100080214ai.ds@gmail.com

- LinkedIn: www.linkedin.com/in/saivasmisistu
