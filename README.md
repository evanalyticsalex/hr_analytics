
# 📊 HR Attrition Analysis | evanalytics.Corp

This project was created for evanalytics. Corp as a showcase of how HR attrition data can be used to support financial forecasting, workforce planning, and scenario modeling — all critical to modern FP&A (Financial Planning & Analysis) roles.

---

## 🎯 Goal

Use HR data to simulate real-world challenges a financial analyst may face:
- Modeling the cost of employee attrition ()
- Identifying retention bottlenecks
- Proposing data-driven recommendations

---

## 🧠 Working Hypotheses

1. Employees with **low income, high overtime, and low satisfaction** are more likely to leave — affecting hiring and training budgets.
2. **Departments with high attrition** also show high variance in tenure and performance scores — suggesting inefficiencies.
3. **Younger employees** leave more often — which lowers ROI on onboarding investment.

---

## 🧰 Tools Used

- Python (pandas, seaborn, matplotlib, plotly)
- Jupyter Notebook
- Git & GitHub
- VS Code (with Git Bash)
- Tableau or Power BI (optional)

---

## 📁 Folder Structure

```
HR_analytics_evCorp/
│
├── data/
│   └── WA_Fn-UseC_-HR-Employee-Attrition.csv
│
├── notebooks/
│   └── explore_hr_attrition.ipynb
│
├── dashboards/
│   └── hr_attrition_dashboard.html  # Optional
│
├── scripts/
│   └── attrition_model.py          # Optional
│
├── requirements.txt
└── README.md
```

---

## 📈 Key Insights

- Built correlation heatmaps and attrition risk visuals
- Simulated retention-improvement scenarios using statistical logic
- Developed a dashboard with actionable KPIs:
  - Attrition Rate
  - Avg. Income of Leavers
  - Tenure Distribution
  - Overtime % vs Attrition Rate

---

## 📌 Business Value

- Supports forecasting and scenario planning
- Helps HR & Finance collaborate on retention strategy
- Demonstrates the strategic value of data analytics in cost control

IMPORTANT NOTES 

📊 Attrition Cost Modeling
This project estimates the financial impact of employee attrition using a basic cost model.

🔍 What It Does:
Loads employee data from data/WA_Fn-UseC_-HR-Employee-Attrition.csv

Flags employees who left the company (Attrition = 'Yes')

Assigns a fixed cost of $50,000 per leaver (customizable)

Calculates:

Total number of leavers

Total estimated attrition cost

Cost breakdown by department

📂 Output Files:
Saved automatically in the /outputs folder after running the script:

outputs/attrition_leavers.csv
→ Detailed records of employees who left

outputs/attrition_cost_by_department.csv
→ Summary of attrition cost per department

🧠 Script Location:
You can find the full implementation in:
scripts/model_attrition_cost.py