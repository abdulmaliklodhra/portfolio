
import streamlit as st
import pandas as pd
import plotly.express as px
from PIL import Image

# --- Page Config ---
st.set_page_config(
    page_title="Abdul Malik - CRVS Specialist & Portfolio",
    page_icon="📋",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --- Custom Styling ---
st.markdown("""
<style>
    /* Main Background & Font */
    body {
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
        color: #334155;
    }
    
    /* Headers */
    h1, h2, h3 {
        color: #0F172A; /* Deep Navy */
    }
    h1 {
        font-weight: 800;
        border-bottom: 2px solid #D4AF37; /* Gold */
        padding-bottom: 10px;
    }
    h2 {
        margin-top: 30px;
        border-left: 5px solid #D4AF37;
        padding-left: 10px;
    }
    
    /* Metrics */
    [data-testid="stMetricValue"] {
        font-size: 2rem;
        color: #1E3A8A;
    }
    
    /* Sidebar */
    [data-testid="stSidebar"] {
        background-color: #F8FAFC;
        border-right: 1px solid #ddd;
    }
    
    /* Custom Card */
    .card {
        background-color: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        margin-bottom: 20px;
        border: 1px solid #e2e8f0;
    }
    .card-title {
        font-weight: bold;
        color: #0F172A;
        font-size: 1.3rem;
    }
    .card-subtitle {
        color: #D4AF37;
        font-size: 0.95rem;
        margin-bottom: 10px;
        font-weight: 600;
    }
    
    /* Contact Links */
    .contact-link {
        text-decoration: none;
        color: #1E3A8A;
        font-weight: bold;
        font-size: 1.1rem;
        display: block;
        margin: 5px 0;
    }
    .contact-link:hover {
        color: #D4AF37;
    }
</style>
""", unsafe_allow_html=True)

# --- Header Section ---
col1, col2 = st.columns([1, 4])

with col1:
    st.markdown("<div style='text-align: center; font-size: 80px;'>👤</div>", unsafe_allow_html=True)

with col2:
    st.title("Abdul Malik")
    st.markdown("**CRVS Regional Focal Person & District Superintendent CRMS | NADRA Regional Head Office Multan**")
    st.markdown("📍 Multan, Pakistan | 🛂 Pakistani (Golden Visa Eligible - UAE Relocation Ready)")
    st.write("22-year NADRA veteran leading United Nations-funded Civil Registration & Vital Statistics (CRVS) Projects.")

# --- Sidebar ---
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to:", ["Home & Summary", "Experience", "Skills & Achievements", "Contact"])

st.sidebar.markdown("---")
st.sidebar.subheader("Quick Connect")
st.sidebar.markdown("[LinkedIn](https://www.linkedin.com/in/abdul-malik-42b5a8254/)", unsafe_allow_html=True)
st.sidebar.markdown("[GitHub](https://github.com/abdulmaliklodhra)", unsafe_allow_html=True)
st.sidebar.markdown("[Kaggle](https://www.kaggle.com/abdulmaliklodhra)", unsafe_allow_html=True)
st.sidebar.markdown("📧 **abdulmaliklodhra77@gmail.com**")
st.sidebar.markdown("📞 **+92-03023575410**")


# --- Page: Home & Summary ---
if page == "Home & Summary":
    st.header("Professional Summary")
    st.markdown("""
    <div class="card">
        <p>
        I am a <b>Strategy & Operations Leader</b> with over <b>22 years of experience</b> at NADRA. 
        As the <b>only officer in Multan Region</b> selected to lead the <b>UN-funded CRVS Project</b>, 
        I have pioneered every major digital transformation in civil registration for South Punjab since 2006.
        </p>
        <p>
        My expertise bridges the gap between field operations, government policy, and modern technology. 
        I am now seeking to bring this specialized experience to the UAE's next-generation identity and registry systems.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.header("Key Metrics (Career)")
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Experience", "22+ Years", "NADRA Veteran")
    m2.metric("Revenue Impact", "10M+ PKR", "Top District 2022")
    m3.metric("Sites Managed", "1,577+", "Across 196 UCs")
    m4.metric("Uptime", "99.9%", "Service Reliability")
    
    st.subheader("Core Competencies")
    competencies = [
        "Civil Registration (CRVS)", "UN Standards Compliance", "Technical & Financial Audits",
        "Large-Scale Deployment", "Govt Liaison", "Fraud Prevention", 
        "Revenue Maximisation", "Stakeholder Management"
    ]
    st.write(" | ".join([f"**{c}**" for c in competencies]))

# --- Page: Experience ---
elif page == "Experience":
    st.header("Professional Experience")
    
    # Career Timeline (Data)
    experience_data = [
        {
            "Role": "CRVS Regional Focal Person (South Punjab)",
            "Company": "NADRA Regional Head Office",
            "Period": "Dec 2025 – Present",
            "Highlights": [
                "<b>Leading UN-funded projects (CRVS).</b>",
                "Launched first hospital-integrated BNRT/DNRT at Doctors Care Hospital.",
                "Rolled out CRMS Mobile Application across entire Multan Region (14 districts).",
                "<b>Master Trainer:</b> Certified by Punjab Focal Person. Trained UC Secretaries & Assistant Directors Local Govt in Multan.",
                "<b>Liaised with local government authorities, from Union Council officials to the Divisional Director, to support effective technical and administrative implementation.</b>",
                "<b>Provided audit support to the CRMS Branch, RHO Multan.</b>"
            ]
        },
        {
            "Role": "District Superintendent CRMS",
            "Company": "NADRA Multan",
            "Period": "2010 – Present",
            "Highlights": [
                "Full P&L and operational responsibility for 196 Union Councils (1,577 sites).",
                "Delivered 10+ million PKR revenue in 2022 alone – highest performing district in Pakistan.",
                "<b>Conducted Technical and Financial Audits of Union Councils.</b>",
                "Daily monitoring of vital events, revenue reconciliation, fraud prevention and field audits."
            ]
        },
        {
            "Role": "Project Lead (Mobile App Rollout)",
            "Company": "NADRA Multan Region",
            "Period": "2024 – Dec 2025",
            "Highlights": [
                "End-to-end deployment of vital events registration app across 14 districts.",
                "Pioneered adoption across entire region."
            ]
        },
        {
            "Role": "Pioneer & Inaugurator – CRMS Web App",
            "Company": "NADRA Multan",
            "Period": "Jan 2022",
            "Highlights": [
                "<b>Inaugurated by Director General NADRA Multan Region Major (R) Imran Ali Khan.</b>",
                "Personally inaugurated the first web-based CRMS site in Pakistan.",
                "Multan became #1 revenue generating region."
            ],
            "Images": ["images/plaque_1.jpg", "images/group_photo.jpg", "images/ribbon_cutting.jpg"]
        },
        {
            "Role": "System Administrator (CBRC Project)",
            "Company": "NADRA Multan",
            "Period": "2006 – 2015",
            "Highlights": [
                "Led the rollout of the first Computerized Birth Registration Certificate project.",
                "Liaison with local government at divisional level."
            ]
        },
    ]
    
    # Display as Cards
    for role in experience_data:
        points = "".join([f"<li>{h}</li>" for h in role['Highlights']])
        st.markdown(f"""
        <div class="card">
            <div class="card-title">{role['Role']}</div>
            <div class="card-subtitle">{role['Company']} | {role['Period']}</div>
            <ul>{points}</ul>
        </div>
        """, unsafe_allow_html=True)
        
        # Display Images if they exist for the role
        if "Images" in role:
            cols = st.columns(len(role['Images']))
            for idx, img_path in enumerate(role['Images']):
                try:
                    cols[idx].image(img_path, use_container_width=True)
                except:
                    pass

# --- Page: Skills & Achievements ---
elif page == "Skills & Achievements":
    st.header("Key Achievements")
    
    achievements = [
        "🏆 **#1 Revenue District:** Made Multan the highest revenue-generating CRMS region in Pakistan (2022 & 2025).",
        "🚀 **First Web App:** Inaugurated Pakistan's first CRMS Web Application (Jan 2022).",
        "📱 **Mobile Rollout:** Successfully deployed mobile registration across 14 districts (Dec 2025).",
        "🏥 **Hospital Integration:** Launched first BNRT/DNRT site at Doctors Care Hospital (Dec 2025).",
        "🔎 **Audit & Compliance:** Conducted extensive technical and financial audits of Union Councils."
    ]
    
    for ach in achievements:
        st.info(ach)

    st.header("Education & Continuous Learning")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class="card" style="border-left: 5px solid #1E3A8A; height: 100%;">
            <div class="card-title">MSc Economics</div>
            <div class="card-subtitle">Bahauddin Zakariya University, Multan | 2001</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="card" style="border-left: 5px solid #3B82F6; height: 100%;">
            <div class="card-title">Data Science & AI</div>
            <div class="card-subtitle">Professional Development | Currently Enrolled</div>
            <p style="font-size: 0.9rem;">Enhancing skills in Machine Learning, Python, and AI for advanced data analytics.</p>
        </div>
        """, unsafe_allow_html=True)
        
    st.header("Technical & Operational Skills")
    
    # Skill Bars using Streamlit Progress
    col_a, col_b = st.columns(2)
    with col_a:
        st.subheader("Domain Expertise")
        st.markdown("**CRVS & Civil Registration**")
        st.progress(100)
        st.markdown("**Audit & Compliance**")
        st.progress(95)
        st.markdown("**Govt Liaison**")
        st.progress(100)
        
    with col_b:
        st.subheader("Management & Tech")
        st.markdown("**Team Leadership**")
        st.progress(95)
        st.markdown("**Data Analytics (Kaggle/Python)**")
        st.progress(85)
        st.markdown("**Project Management**")
        st.progress(90)

# --- Page: Contact ---
elif page == "Contact":
    st.header("Get In Touch")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="card">
            <h3>Contact Details</h3>
            <p>I am available for immediate joining and relocation to Dubai/Abu Dhabi.</p>
            <a class="contact-link" href="tel:+9203023575410">📞 +92-03023575410</a>
            <a class="contact-link" href="mailto:abdulmaliklodhra77@gmail.com">📧 abdulmaliklodhra77@gmail.com</a>
        </div>
        """, unsafe_allow_html=True)
        
        st.subheader("Social & Coding Profiles")
        st.markdown("""
        - [LinkedIn Profile](https://www.linkedin.com/in/abdul-malik-42b5a8254/)
        - [GitHub Profile (abdulmaliklodhra)](https://github.com/abdulmaliklodhra)
        - [Kaggle Profile (abdulmaliklodhra)](https://www.kaggle.com/abdulmaliklodhra)
        """)
    
    with col2:
        st.markdown("### Message Me")
        with st.form("contact_form"):
            st.text_input("Name")
            st.text_input("Email")
            st.text_area("Message")
            st.form_submit_button("Send Message")

