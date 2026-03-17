import pandas as pd
import streamlit as st

st.set_page_config(page_title="Secure AI Business Insights Agent", layout="wide")

# -----------------------------
# Demo users for hackathon demo
# -----------------------------
USERS = {
    "admin@demo.com": {"password": "admin123", "role": "Admin"},
    "manager@demo.com": {"password": "manager123", "role": "Manager"},
    "viewer@demo.com": {"password": "viewer123", "role": "Viewer"},
}

# -----------------------------
# Session state setup
# -----------------------------
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if "user_email" not in st.session_state:
    st.session_state.user_email = ""

if "user_role" not in st.session_state:
    st.session_state.user_role = ""

# -----------------------------
# Helpers
# -----------------------------
def login_user(email: str, password: str) -> bool:
    user = USERS.get(email)
    if user and user["password"] == password:
        st.session_state.authenticated = True
        st.session_state.user_email = email
        st.session_state.user_role = user["role"]
        return True
    return False

def logout_user() -> None:
    st.session_state.authenticated = False
    st.session_state.user_email = ""
    st.session_state.user_role = ""

# -----------------------------
# Login screen
# -----------------------------
if not st.session_state.authenticated:
    st.title("Secure AI Business Insights Agent")
    st.caption("Sign in to access protected insights, tasks, and recommendations.")

    st.subheader("Demo Sign In")

    with st.form("login_form"):
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        submitted = st.form_submit_button("Sign In")

    with st.expander("Demo credentials"):
        st.write("Admin: admin@demo.com / admin123")
        st.write("Manager: manager@demo.com / manager123")
        st.write("Viewer: viewer@demo.com / viewer123")

    if submitted:
        if login_user(email.strip().lower(), password):
            st.success("Login successful. Loading dashboard...")
            st.rerun()
        else:
            st.error("Invalid email or password.")

    st.stop()

# -----------------------------
# Protected dashboard
# -----------------------------
role = st.session_state.user_role
user_email = st.session_state.user_email

top_left, top_right = st.columns([4, 1])

with top_left:
    st.title("Secure AI Business Insights Agent")
    st.caption("Protected AI dashboard with role-based access and task visibility.")

with top_right:
    st.write("")
    st.write(f"**{role}**")
    if st.button("Logout"):
        logout_user()
        st.rerun()

st.write(f"Signed in as: **{user_email}**")

st.subheader("Access Status")
if role == "Admin":
    st.success("Full access granted")
elif role == "Manager":
    st.warning("Limited access granted")
else:
    st.info("View-only access granted")

# -----------------------------
# KPI section
# -----------------------------
revenue = 128450
orders = 842
conversion_rate = 4.8
forecast_growth = 12.4

c1, c2, c3, c4 = st.columns(4)
c1.metric("Monthly Revenue", f"${revenue:,.0f}")
c2.metric("Orders", f"{orders}")
c3.metric("Conversion Rate", f"{conversion_rate}%")
c4.metric("Forecast Growth", f"{forecast_growth}%")

st.divider()

# -----------------------------
# Trend charts
# -----------------------------
df_trend = pd.DataFrame({
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "Revenue": [72000, 81000, 86500, 94000, 108000, 128450],
    "Orders": [510, 560, 590, 645, 730, 842],
})

left, right = st.columns(2)

with left:
    st.subheader("Revenue Trend")
    st.line_chart(df_trend.set_index("Month")[["Revenue"]])

with right:
    st.subheader("Order Volume")
    st.bar_chart(df_trend.set_index("Month")[["Orders"]])

st.divider()

# -----------------------------
# Protected task area
# -----------------------------
st.subheader("Agent Tasks")

admin_tasks = [
    "Approve regional budget increases",
    "Review full revenue forecast",
    "Unlock detailed market-level analysis",
]

manager_tasks = [
    "Review team performance trends",
    "Monitor conversion rate changes",
    "Escalate access request for full forecast controls",
]

viewer_tasks = [
    "Review summary KPI trends",
    "Read limited performance snapshot",
]

if role == "Admin":
    for task in admin_tasks:
        st.checkbox(task, value=False)
elif role == "Manager":
    for task in manager_tasks:
        st.checkbox(task, value=False)
else:
    for task in viewer_tasks:
        st.checkbox(task, value=False)

st.divider()

# -----------------------------
# Regional data
# -----------------------------
st.subheader("Regional Performance")
df_regions = pd.DataFrame({
    "Region": ["South", "West", "Midwest", "Northeast"],
    "Revenue": [40200, 31500, 28750, 28000],
    "Growth %": [15.2, 10.8, 9.1, 8.7],
})

if role in ["Admin", "Manager"]:
    st.dataframe(df_regions, use_container_width=True)
else:
    st.info("Regional performance details are restricted for Viewer access.")

st.divider()

# -----------------------------
# AI insights
# -----------------------------
st.subheader("AI-Generated Insights")

if role == "Admin":
    st.info(
        """
        Revenue is trending upward month-over-month, with the strongest acceleration in May and June.
        The South region is the top-performing market by both revenue and growth.
        Current demand patterns suggest continued double-digit growth if acquisition efficiency holds.
        """
    )
elif role == "Manager":
    st.info(
        """
        Revenue is trending upward and high-performing regions should receive additional budget attention.
        Detailed regional breakdown is partially restricted at this access level.
        """
    )
else:
    st.info(
        """
        Limited insights available. Viewer mode can access summary trends only.
        Upgrade access for deeper business analysis and recommendations.
        """
    )

st.subheader("Recommended Actions")
if role == "Admin":
    st.write(
        """
        1. Increase investment in top-performing regions.
        2. Monitor conversion rate as order volume scales.
        3. Expand forecasting with channel-level and customer-level features.
        """
    )
elif role == "Manager":
    st.write(
        """
        1. Focus on maintaining growth momentum.
        2. Review conversion efficiency weekly.
        3. Request admin access for deeper forecasting controls.
        """
    )
else:
    st.write(
        """
        1. Review summary performance trends.
        2. Request elevated access for detailed insights.
        """
    )

st.divider()

st.subheader("Security Concept")
st.write(
    """
    This prototype uses a sign-in gate plus role-based visibility to simulate protected AI agent workflows.
    In a production version, Auth0 for AI Agents could manage authentication, identity, permissions,
    and secure task execution on behalf of authenticated users.
    """
)