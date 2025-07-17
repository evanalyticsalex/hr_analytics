# 📊 HR Attrition Analysis | *evanalytics.Corp*

This project simulates how a Financial Analyst can leverage HR attrition data to support **forecasting**, **cost modeling**, and **retention strategy** — all essential to **modern FP\&A functions**.

---

## 🎯 Objective

To explore how data-driven HR insights can inform financial decisions, we:

* Model the **cost of employee attrition**
* Detect potential **retention bottlenecks**
* Simulate **real-world FP\&A use cases**

---

## 🧪 Hypotheses

1. **Low income**, **frequent overtime**, and **low satisfaction** are predictors of attrition.
2. **Departments with high attrition** also show high **variance in tenure and performance**.
3. **Younger employees** tend to leave earlier, reducing ROI on onboarding.

---

## 🛠️ Tech Stack

| Category      | Tools                                        |
| ------------- | -------------------------------------------- |
| Analysis      | Python (Pandas, Seaborn, Matplotlib, Plotly) |
| Interface     | Jupyter Notebook                             |
| Automation    | Scripts & GitHub                             |
| IDE           | VS Code with Git Bash                        |
| Visualization | Tableau / Power BI (optional)                |

---

## 🗂️ Project Structure

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
│   └── hr_attrition_dashboard.html  # (optional)
│
├── scripts/
│   └── model_attrition_cost.py      # (attrition cost modeling)
│
├── outputs/
│   ├── attrition_leavers.csv
│   └── attrition_cost_by_department.csv
│
├── requirements.txt
└── README.md
```

---

## 🔍 Attrition Cost Modeling

The script `scripts/model_attrition_cost.py` loads the dataset and calculates financial impact using the following steps:

### What it does:

1. **Loads data** from `/data/WA_Fn-UseC_-HR-Employee-Attrition.csv`
2. Flags records where `Attrition == 'Yes'`
3. Assigns a **fixed cost of \$50,000 per leaver** *(editable in script)*
4. Computes:

   * 🔻 Total number of leavers
   * 💸 Total estimated cost of attrition
   * 🏢 Department-wise cost breakdown
5. Saves results to `/outputs` folder as CSV files
6. Plots a **horizontal bar chart** showing departmental attrition cost

### Output Files:

| File                                       | Description                   |
| ------------------------------------------ | ----------------------------- |
| `outputs/attrition_leavers.csv`            | Records of employees who left |
| `outputs/attrition_cost_by_department.csv` | Cost breakdown per department |

---

## 📊 Sample Insights

* Correlation heatmaps revealed patterns in satisfaction, income, and overtime
* Attrition rates were highest in **Sales** and **R\&D**
* Simulated savings by improving retention in high-cost departments

---

## 💡 Business Value

* Helps HR & Finance **align on cost-saving goals**
* Aids in **budgeting** and **strategic workforce planning**
* Demonstrates how **analytics supports cost control**


