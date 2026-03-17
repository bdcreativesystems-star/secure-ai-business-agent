# 🔐 Secure AI Business Insights Agent

An AI-powered business intelligence dashboard that simulates secure, role-based access to insights and recommendations.

Built for the **Auth0 for AI Agents Hackathon**.

---

## 🚀 Overview

This project demonstrates how an AI system can deliver different levels of insights based on user roles, simulating secure access patterns similar to Auth0.

Users can switch between roles:
- **Admin** → Full access to insights and data
- **Manager** → Partial insights and restricted data
- **Viewer** → Limited, high-level summaries only

---

## 🧠 Key Features

- 📊 Real-time KPI dashboard (Revenue, Orders, Conversion)
- 📈 Trend analysis with charts
- 🌍 Regional performance breakdown
- 🤖 AI-generated business insights
- 🔐 Role-based access control simulation
- ⚡ Streamlit-powered interactive UI

---

## 🔐 Security Concept

This project simulates how **Auth0 for AI Agents** can:
- Manage user identity
- Control access to AI-generated insights
- Restrict sensitive data based on permissions

---

## 🛠️ Tech Stack

- Python
- Streamlit
- Pandas
- NumPy

---

## ▶️ How to Run

```bash
git clone <your-repo-link>
cd secure-ai-business-agent

python -m venv venv
.\venv\Scripts\activate

pip install -r requirements.txt
python run.py