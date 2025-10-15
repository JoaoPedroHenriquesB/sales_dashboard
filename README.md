# Intelligent Dashboard

![Full Dashboard View](/imgs/img1.png)

## 📖 About The Project

This project is an **Intelligent Dashboard** created for data analysis studies. It's a web application built with Python, Streamlit, Pandas, and Plotly that allows users to upload their sales data in a CSV format and instantly visualize key business metrics and trends through interactive charts.

The main goal is to provide a hands-on example of how to build a simple, yet powerful, data visualization tool.

---

## ✨ Features

*   **Dynamic CSV Upload**: Easily upload your sales data via a user-friendly sidebar.
*   **Key Performance Indicators (KPIs)**: Get a quick overview of your business with metrics like:
    *   Total Revenue
    *   Total Units Sold
    *   Best Selling Product
    *   Top Performing City
    *   Most Used Payment Method
*   **Interactive Charts**: Dive deeper into your data with several interactive charts:
    *   Best Selling Products (Bar Chart)
    *   Sales by City (Line Chart)
    *   Sales Over Time (Bar Chart)
    *   Payment Method Distribution (Pie Chart)

![KPI Section](/imgs/kpi.png)

---

## 🚀 How to Run

1.  **Clone the repository:**
    ```sh
    git clone https://github.com/JoaoPedroHenriquesB/sales_dashboard.git
    cd inteligent-dashboard
    ```

2.  **Install the dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

3.  **Run the Streamlit app:**
    ```sh
    streamlit run src/main.py
    ```

4.  Open your browser and navigate to the local URL provided by Streamlit. Use the sidebar to upload your CSV file.

![File Uploader](/imgs/sidebar.png)

---

## ⚠️ Important: CSV Column Name Limitation

This application is designed for study purposes and has a specific requirement for the column names in the uploaded CSV file. The script expects the following column names to be present:

*   `Product`
*   `Quantity`
*   `Total ($)`
*   `Payment Method`
*   `City`
*   `Sale Date`

If your CSV file uses different names for these columns, the application will fail to process the data and will display an error message.

!Error Message

**To fix this, you must ensure your CSV file's header matches these names exactly.** Future versions could include a feature to map columns dynamically, but for now, the names are fixed.

---

## 🛠️ Tech Stack

*   **Python**: Core programming language.
*   **Streamlit**: For building the interactive web application.
*   **Pandas**: For data manipulation and analysis.
*   **Plotly**: For creating interactive and beautiful charts.

!Charts Example

---

![Cities](/imgs/img2.png)
![Months](/imgs/img4.png)
![Payment Methods](/imgs/img5.png)

This project serves as a practical exercise in data analysis and visualization with Python. Feel free to fork it, experiment with it, and expand its capabilities!
