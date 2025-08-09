# 📊 Telco Customer Churn Analysis

## 📌 Project Overview
This project analyzes the **Telco Customer Churn** dataset to identify patterns and factors that influence customer attrition.  
Using **Python (Pandas, Matplotlib, Seaborn)**, we explore how contract type, tenure, internet service, and payment method affect churn.

---

## 📂 Dataset Information
**Rows:** 7,043 customers  
**Columns:** 21 (Demographics, services, contracts, payment methods, churn status)  

---

## 🛠 Tools & Libraries Used
- **Python:** Pandas, NumPy  
- **Visualization:** Matplotlib, Seaborn  
- **IDE:** VS Code 

---

## 📊 Churn Distribution
| Status     | Count | Percentage |
|------------|-------|------------|
| Retained   | 5,174 | 73.5%      |
| Churned    | 1,869 | 26.5%      |

**Visualization:**  
![Churn Distribution](images/churn_distribution.png)

---

## 📈 Key Visuals

### Gender vs Churn
![Churn by Gender](images/churn_by_gender.png)

### Senior Citizen vs Churn
![Churn by Senior Citizen](images/churn_by_senior.png)

### Tenure vs Churn
![Tenure vs Churn](images/tenure_vs_churn.png)

### Contract Type vs Churn
![Contract vs Churn](images/contract_vs_churn.png)

### Internet Service vs Churn
![Internet Service vs Churn](images/internet_vs_churn.png)

### Online Security vs Churn
![Online Security vs Churn](images/onlinesecurity_vs_churn.png)

### Tech Support vs Churn
![Tech Support vs Churn](images/techsupport_vs_churn.png)

### Payment Method vs Churn
![Payment Method vs Churn](images/payment_vs_churn.png)

---

## 📌 Key Insights
- **Month-to-month** contract customers churn the most (~43%).  
- **Fiber optic** internet customers churn more (~42%) than DSL users (~19%).  
- Customers without **online security** or **tech support** churn ~3x more.  
- **Electronic check** users have the highest churn rate (~45%).  

---

## 💡 Recommendations
1. Promote **long-term contracts** to reduce churn.  
2. Bundle **security & tech support** with internet plans.  
3. Offer incentives for switching from **electronic check** to auto-pay methods.  
4. Target **fiber optic customers** with loyalty rewards.

---

## 🚀 How to Run This Project
1. Install Python 3.8+ and required libraries:
   ```bash
   pip install pandas matplotlib seaborn