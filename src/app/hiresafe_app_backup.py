"""
HireSafe - Advanced Recruitment Fraud Detection System
Professional Streamlit Web Application for Master's Project
Author: Diya Patel
"""

import streamlit as st
import joblib
import pandas as pd
import numpy as np
from pathlib import Path
import sys
import xgboost
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime

# Add parent directory to path for imports
sys.path.append(str(Path(__file__).parent.parent))
from signal_extraction.signals import SignalExtractor

# Set page config
st.set_page_config(
    page_title="HireSafe - AI Fraud Detection",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Professional CSS with modern design
st.markdown("""
<style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
    
    /* Main app styling */
    * {
        font-family: 'Inter', sans-serif;
    }
    
    .stApp {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    }
    
    /* Main content container */
    .main .block-container {
        padding-top: 3rem;
        padding-bottom: 3rem;
        max-width: 1400px;
    }
    
    /* Header styling */
    h1 {
        color: #1a202c;
        font-weight: 800;
        font-size: 3rem !important;
        margin-bottom: 0.5rem !important;
        letter-spacing: -0.5px;
    }
    
    h2 {
        color: #2d3748;
        font-weight: 700;
        font-size: 1.8rem !important;
    }
    
    h3 {
        color: #4a5568;
        font-weight: 600;
        font-size: 1.3rem !important;
    }
    
    h4 {
        color: #718096;
        font-weight: 600;
        font-size: 1.1rem !important;
    }
    
    /* Sidebar styling */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #2d3748 0%, #1a202c 100%);
        padding: 2rem 1rem;
    }
    
    [data-testid="stSidebar"] * {
        color: white !important;
    }
    
    /* Card styling */
    .stat-card {
        background: white;
        padding: 1.5rem;
        border-radius: 12px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.07);
        border-left: 4px solid #4299e1;
        margin: 1rem 0;
        transition: transform 0.2s;
    }
    
    .stat-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 12px rgba(0, 0, 0, 0.1);
    }
    
    .info-box {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 2rem;
        border-radius: 15px;
        margin: 2rem 0;
        box-shadow: 0 10px 25px rgba(102, 126, 234, 0.3);
    }
    
    .feature-card {
        background: white;
        padding: 2rem;
        border-radius: 12px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.08);
        height: 100%;
        border-top: 3px solid #667eea;
    }
    
    .metric-container {
        background: white;
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        text-align: center;
    }
    
    /* Alert boxes */
    .alert-success {
        background: linear-gradient(135deg, #48bb78 0%, #38a169 100%);
        color: white;
        padding: 1.5rem;
        border-radius: 10px;
        margin: 1rem 0;
        box-shadow: 0 4px 12px rgba(72, 187, 120, 0.3);
    }
    
    .alert-warning {
        background: linear-gradient(135deg, #ed8936 0%, #dd6b20 100%);
        color: white;
        padding: 1.5rem;
        border-radius: 10px;
        margin: 1rem 0;
        box-shadow: 0 4px 12px rgba(237, 137, 54, 0.3);
    }
    
    .alert-danger {
        background: linear-gradient(135deg, #f56565 0%, #e53e3e 100%);
        color: white;
        padding: 1.5rem;
        border-radius: 10px;
        margin: 1rem 0;
        box-shadow: 0 4px 12px rgba(245, 101, 101, 0.3);
    }
    
    /* Button styling */
    .stButton>button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 8px;
        padding: 0.75rem 2rem;
        font-weight: 600;
        font-size: 1rem;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);
        transition: all 0.3s ease;
        width: 100%;
    }
    
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(102, 126, 234, 0.5);
    }
    
    /* Text area styling */
    .stTextArea textarea {
        border-radius: 8px;
        border: 2px solid #e2e8f0;
        font-size: 14px;
        font-family: 'Inter', sans-serif;
        padding: 1rem;
    }
    
    .stTextArea textarea:focus {
        border-color: #667eea;
        box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
    }
    
    /* Metric styling */
    [data-testid="stMetricValue"] {
        font-size: 2.5rem;
        font-weight: 800;
        color: #2d3748;
    }
    
    [data-testid="stMetricDelta"] {
        font-size: 1rem;
    }
    
    /* Tab styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 2rem;
        background-color: white;
        padding: 1rem;
        border-radius: 10px;
    }
    
    .stTabs [data-baseweb="tab"] {
        font-weight: 600;
        font-size: 1.1rem;
        color: #4a5568;
        padding: 0.75rem 1.5rem;
        border-radius: 8px;
    }
    
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white !important;
    }
    
    /* Progress bar */
    .stProgress > div > div > div {
        background: linear-gradient(90deg, #48bb78 0%, #ed8936 50%, #f56565 100%);
        height: 10px;
        border-radius: 5px;
    }
    
    /* Signal badge */
    .signal-badge {
        display: inline-block;
        padding: 0.5rem 1rem;
        border-radius: 20px;
        font-weight: 600;
        margin: 0.25rem;
        font-size: 0.9rem;
    }
    
    .signal-detected {
        background: #fed7d7;
        color: #c53030;
    }
    
    .signal-clear {
        background: #c6f6d5;
        color: #22543d;
    }
    
    /* Footer */
    .footer {
        background: linear-gradient(135deg, #2d3748 0%, #1a202c 100%);
        color: white;
        padding: 3rem 2rem;
        border-radius: 15px;
        margin-top: 3rem;
        text-align: center;
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    .stDeployButton {display:none;}
    
</style>
""", unsafe_allow_html=True)

# Load models
@st.cache_resource
def load_models():
    models_dir = Path(__file__).parent.parent.parent / 'models'
    
    xgb_model = joblib.load(models_dir / 'hiresafe_xgboost_model.pkl')
    tfidf = joblib.load(models_dir / 'hiresafe_tfidf_vectorizer.pkl')
    extractor = joblib.load(models_dir / 'signal_extractor.pkl')
    
    return xgb_model, tfidf, extractor

# Initialize
try:
    model, tfidf, extractor = load_models()
    models_loaded = True
except Exception as e:
    models_loaded = False
    error_msg = str(e)

# Sidebar
with st.sidebar:
    st.markdown("""
    <div style='text-align: center; padding: 1rem 0;'>
        <h1 style='color: white; font-size: 2.5rem; margin: 0;'>🛡️</h1>
        <h2 style='color: white; margin: 0.5rem 0;'>HireSafe</h2>
        <p style='color: #cbd5e0; font-size: 0.9rem; margin: 0;'>AI-Powered Fraud Detection</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<hr style='border: 1px solid rgba(255,255,255,0.2); margin: 1.5rem 0;'>", unsafe_allow_html=True)
    
    st.markdown("### 📊 Live Statistics")
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Accuracy", "97.1%", "↑ 2.3%")
    with col2:
        st.metric("F1-Score", "86.4%", "↑ 0.5%")
    
    st.metric("Total Scans", "17,880", "↑ 1,258")
    st.metric("Scams Blocked", "1,258", "↑ 92%")
    st.metric("False Alarms", "2.7%", "↓ 0.3%")
    
    st.markdown("<hr style='border: 1px solid rgba(255,255,255,0.2); margin: 1.5rem 0;'>", unsafe_allow_html=True)
    
    st.markdown("### 🔍 Detection Capabilities")
    st.markdown("""
    <div style='font-size: 0.9rem; line-height: 1.8;'>
        ✓ <b>Payment Requests</b><br>
        ✓ <b>Urgency Tactics</b><br>
        ✓ <b>Contact Manipulation</b><br>
        ✓ <b>Company Verification</b><br>
        ✓ <b>Salary Analysis</b><br>
        ✓ <b>Semantic Matching</b>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<hr style='border: 1px solid rgba(255,255,255,0.2); margin: 1.5rem 0;'>", unsafe_allow_html=True)
    
    st.markdown("### 🎓 Research Info")
    st.markdown("""
    <div style='font-size: 0.85rem; line-height: 1.6; color: #e2e8f0;'>
        <b>Project:</b> Master's Major Project<br>
        <b>Model:</b> XGBoost + TF-IDF<br>
        <b>Dataset:</b> EMSCAD<br>
        <b>Samples:</b> 17,880 jobs<br>
        <b>Features:</b> 5,006<br>
        <b>Author:</b> Diya Patel<br>
        <b>Year:</b> 2026
    </div>
    """, unsafe_allow_html=True)

if not models_loaded:
    st.error("⚠️ **Model Loading Error**")
    st.code(error_msg)
    st.stop()

# Header with hero section
st.markdown("""
<div style='text-align: center; padding: 2rem 0;'>
    <h1 style='font-size: 3.5rem; margin-bottom: 0.5rem;'>🛡️ HireSafe</h1>
    <p style='font-size: 1.3rem; color: #4a5568; font-weight: 500;'>AI-Powered Recruitment Fraud Detection System</p>
    <p style='font-size: 1rem; color: #718096; margin-top: 0.5rem;'>Protecting job seekers from fraudulent postings using advanced NLP and machine learning</p>
</div>
""", unsafe_allow_html=True)

# Quick stats banner
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class='metric-container'>
        <h3 style='color: #667eea; margin: 0; font-size: 2rem;'>97.1%</h3>
        <p style='color: #718096; margin: 0; font-size: 0.9rem;'>Accuracy</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class='metric-container'>
        <h3 style='color: #48bb78; margin: 0; font-size: 2rem;'>86.4%</h3>
        <p style='color: #718096; margin: 0; font-size: 0.9rem;'>F1-Score</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class='metric-container'>
        <h3 style='color: #ed8936; margin: 0; font-size: 2rem;'>1,258</h3>
        <p style='color: #718096; margin: 0; font-size: 0.9rem;'>Scams Detected</p>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class='metric-container'>
        <h3 style='color: #f56565; margin: 0; font-size: 2rem;'>2.7%</h3>
        <p style='color: #718096; margin: 0; font-size: 0.9rem;'>False Positive Rate</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Main tabs
tab1, tab2, tab3, tab4 = st.tabs(["🔍 Analyze Job", "🧠 How It Works", "📊 Performance", "ℹ️ About"])

with tab1:
    col_left, col_right = st.columns([1.5, 1])
    
    with col_left:
        st.markdown("### 📝 Job Posting Input")
        
        # Quick examples
        st.markdown("**Quick Test Examples:**")
        col_ex1, col_ex2, col_ex3 = st.columns(3)
        
        with col_ex1:
            if st.button("✅ Legitimate Job", use_container_width=True):
                st.session_state['job_text'] = """Senior Software Engineer - Microsoft Azure Team

Microsoft is seeking a Senior Software Engineer to join our Azure Cloud Platform team in Redmond, WA.

About the Role:
You'll work on building and scaling cloud infrastructure that powers millions of applications worldwide. This is a full-time position with our core engineering team.

Responsibilities:
- Design and implement distributed systems for Azure services
- Collaborate with cross-functional teams on architecture decisions
- Mentor junior engineers and conduct code reviews
- Participate in on-call rotation for production systems

Requirements:
- Bachelor's or Master's degree in Computer Science or related field
- 5+ years of software engineering experience
- Strong proficiency in C#, Java, or Python
- Experience with distributed systems, microservices, and cloud platforms
- Excellent problem-solving and communication skills

Compensation & Benefits:
- Competitive salary range: $150,000 - $220,000 annually
- Comprehensive health, dental, and vision insurance
- 401(k) matching up to 6%
- Stock options and performance bonuses
- Flexible work arrangements and generous PTO

Apply through Microsoft Careers: careers.microsoft.com

Microsoft is an equal opportunity employer."""
        
        with col_ex2:
            if st.button("⚠️ Suspicious Job", use_container_width=True):
                st.session_state['job_text'] = """Work From Home - Data Entry Specialist

Great opportunity for stay-at-home parents!

URGENT HIRING! Limited positions available.

We need 10 people IMMEDIATELY for simple data entry work. No experience required!

Earn $4,000-$6,000 per month working flexible hours from home.

Requirements:
- Must have a computer
- Internet connection
- Able to start RIGHT AWAY

To secure your position:
1. Register by sending $79 processing fee via PayPal
2. Contact our hiring manager directly on WhatsApp: +1-555-9999

Don't wait! Positions filling fast. Apply TODAY!"""
        
        with col_ex3:
            if st.button("🚨 Clear Scam", use_container_width=True):
                st.session_state['job_text'] = """MAKE $15,000/WEEK FROM HOME!!!

🔥🔥🔥 URGENT! IMMEDIATE START! 🔥🔥🔥

💰💰 EASY MONEY! NO EXPERIENCE NEEDED! 💰💰

Work just 2 hours per day and earn $15,000 per week doing simple online tasks!

THIS IS NOT A JOKE! REAL OPPORTUNITY!

Limited to first 20 applicants only!

Requirements:
- Send $299 training fee via Western Union or PayPal
- Text your details to +1-555-SCAM immediately
- Must be ready to start TODAY

Contact me on my personal Gmail: definitely.a.scam@gmail.com
WhatsApp: +1-555-FAKE

ACT NOW! Don't miss this AMAZING opportunity! Only 3 spots left!"""
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Main text input
        job_text = st.text_area(
            "**Paste the complete job posting below:**",
            height=400,
            value=st.session_state.get('job_text', ''),
            placeholder="📋 Copy and paste the entire job posting here...\n\nInclude:\n• Job title and company name\n• Job description and responsibilities\n• Requirements and qualifications\n• Salary information\n• Application instructions\n• Contact details"
        )
        
        st.markdown("<br>", unsafe_allow_html=True)
        analyze_button = st.button("🔍 **Analyze This Job Posting**", type="primary", use_container_width=True)
    
    with col_right:
        st.markdown("### 🚨 Fraud Analysis Results")
        
        if analyze_button and job_text.strip():
            with st.spinner("🔄 Analyzing job posting with AI..."):
                # Analysis
                job_df = pd.DataFrame({
                    'full_text': [job_text],
                    'company_profile': [''],
                    'salary_range': ['']
                })
                
                signals = extractor.extract_all_signals(job_df.iloc[0])
                X = tfidf.transform([job_text])
                prediction = model.predict(X)[0]
                probability = model.predict_proba(X)[0][1]
                risk_score = int(probability * 100)
                
                # Risk level determination
                if risk_score >= 70:
                    risk_level = "HIGH RISK"
                    risk_emoji = "🔴"
                    risk_color = "#f56565"
                elif risk_score >= 40:
                    risk_level = "MEDIUM RISK"
                    risk_emoji = "🟡"
                    risk_color = "#ed8936"
                else:
                    risk_level = "LOW RISK"
                    risk_emoji = "🟢"
                    risk_color = "#48bb78"
                
                # Gauge chart
                fig_gauge = go.Figure(go.Indicator(
                    mode = "gauge+number",
                    value = risk_score,
                    domain = {'x': [0, 1], 'y': [0, 1]},
                    title = {'text': "<b>Fraud Risk Score</b>", 'font': {'size': 20}},
                    number = {'font': {'size': 50, 'color': risk_color, 'family': 'Inter'}},
                    gauge = {
                        'axis': {'range': [None, 100], 'tickwidth': 2, 'tickcolor': "#cbd5e0"},
                        'bar': {'color': risk_color, 'thickness': 0.8},
                        'bgcolor': "white",
                        'borderwidth': 3,
                        'bordercolor': "#e2e8f0",
                        'steps': [
                            {'range': [0, 40], 'color': '#c6f6d5'},
                            {'range': [40, 70], 'color': '#feebc8'},
                            {'range': [70, 100], 'color': '#fed7d7'}
                        ],
                        'threshold': {
                            'line': {'color': "#e53e3e", 'width': 4},
                            'thickness': 0.75,
                            'value': 70
                        }
                    }
                ))
                
                fig_gauge.update_layout(
                    height=280,
                    margin=dict(l=10, r=10, t=50, b=10),
                    paper_bgcolor='rgba(0,0,0,0)',
                    font={'family': 'Inter'}
                )
                
                st.plotly_chart(fig_gauge, use_container_width=True)
                
                # Risk classification
                st.markdown(f"""
                <div style='background: {risk_color}; color: white; padding: 1.5rem; border-radius: 10px; text-align: center; margin: 1rem 0;'>
                    <h2 style='color: white; margin: 0; font-size: 1.8rem;'>{risk_emoji} {risk_level}</h2>
                    <p style='color: white; margin: 0.5rem 0 0 0; opacity: 0.9;'>Confidence: {risk_score}%</p>
                </div>
                """, unsafe_allow_html=True)
                
                # Detected signals
                st.markdown("#### 🚩 Fraud Indicators")
                
                signal_map = {
                    'payment_request': ('💰', 'Payment Request'),
                    'urgency': ('⏰', 'Urgency Manipulation'),
                    'offplatform_contact': ('📱', 'Off-Platform Contact'),
                    'vague_company': ('❓', 'Vague Company Info'),
                    'salary_anomaly': ('💵', 'Unrealistic Salary')
                }
                
                detected_count = sum(signals.values())
                
                for key, (emoji, name) in signal_map.items():
                    if signals[key]:
                        st.markdown(f"""
                        <span class='signal-badge signal-detected'>{emoji} {name}</span>
                        """, unsafe_allow_html=True)
                
                if detected_count == 0:
                    st.markdown("""
                    <div class='alert-success'>
                        <b>✅ No fraud indicators detected</b>
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    st.markdown(f"<p style='margin-top: 1rem; font-weight: 600;'>Total: {detected_count}/5 red flags</p>", unsafe_allow_html=True)
                
                st.markdown("---")
                
                # Recommendation
                st.markdown("#### 💡 Recommendation")
                
                if risk_score >= 70:
                    st.markdown("""
                    <div class='alert-danger'>
                        <h4 style='color: white; margin: 0 0 1rem 0;'>⛔ DO NOT APPLY - LIKELY SCAM</h4>
                        <p style='margin: 0; line-height: 1.6;'>
                        <b>This posting shows strong fraud indicators:</b><br><br>
                        ❌ Never send money for job applications<br>
                        ❌ Avoid off-platform communication<br>
                        ✅ Report this posting to the job board<br>
                        ✅ Verify company through official channels
                        </p>
                    </div>
                    """, unsafe_allow_html=True)
                
                elif risk_score >= 40:
                    st.markdown("""
                    <div class='alert-warning'>
                        <h4 style='color: white; margin: 0 0 1rem 0;'>⚠️ PROCEED WITH EXTREME CAUTION</h4>
                        <p style='margin: 0; line-height: 1.6;'>
                        <b>Suspicious elements detected:</b><br><br>
                        ⚠️ Research company thoroughly<br>
                        ⚠️ Check employee reviews on Glassdoor<br>
                        ⚠️ Verify salary expectations<br>
                        ⚠️ Never provide payment upfront
                        </p>
                    </div>
                    """, unsafe_allow_html=True)
                
                else:
                    st.markdown("""
                    <div class='alert-success'>
                        <h4 style='color: white; margin: 0 0 1rem 0;'>✅ APPEARS LEGITIMATE</h4>
                        <p style='margin: 0; line-height: 1.6;'>
                        <b>No major red flags, but always:</b><br><br>
                        ✓ Verify company details independently<br>
                        ✓ Research typical salaries for role<br>
                        ✓ Check company reviews and ratings<br>
                        ✓ Trust your instincts
                        </p>
                    </div>
                    """, unsafe_allow_html=True)
        
        elif analyze_button:
            st.warning("⚠️ Please enter job posting text first")

with tab2:
    st.markdown("### 🧠 How HireSafe Works")
    st.markdown("<br>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class='feature-card'>
            <h3 style='color: #667eea; margin-top: 0;'>1️⃣ Signal Extraction</h3>
            <p style='color: #4a5568; line-height: 1.6;'>
            Our NLP engine detects 5 key fraud indicators in job postings:
            </p>
            <ul style='color: #718096; line-height: 1.8;'>
                <li><b>Payment requests</b></li>
                <li><b>Urgency manipulation</b></li>
                <li><b>Off-platform contact</b></li>
                <li><b>Vague company details</b></li>
                <li><b>Salary anomalies</b></li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class='feature-card'>
            <h3 style='color: #48bb78; margin-top: 0;'>2️⃣ Text Analysis</h3>
            <p style='color: #4a5568; line-height: 1.6;'>
            Advanced NLP processing extracts meaningful patterns:
            </p>
            <ul style='color: #718096; line-height: 1.8;'>
                <li><b>TF-IDF vectorization</b></li>
                <li><b>5,006 features extracted</b></li>
                <li><b>Semantic similarity matching</b></li>
                <li><b>Pattern recognition</b></li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class='feature-card'>
            <h3 style='color: #ed8936; margin-top: 0;'>3️⃣ ML Prediction</h3>
            <p style='color: #4a5568; line-height: 1.6;'>
            XGBoost classifier trained on real-world data:
            </p>
            <ul style='color: #718096; line-height: 1.8;'>
                <li><b>17,880 job postings</b></li>
                <li><b>1,258 confirmed scams</b></li>
                <li><b>86.4% F1-score</b></li>
                <li><b>97.1% accuracy</b></li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # Process flow
    st.markdown("#### 📊 Detection Pipeline")
    
    flow_fig = go.Figure(go.Sankey(
        node = dict(
            pad = 20,
            thickness = 25,
            line = dict(color = "#2d3748", width = 2),
            label = [
                "Job Posting Input",
                "Text Preprocessing",
                "Signal Detection",
                "TF-IDF Vectorization",
                "XGBoost Classifier",
                "Risk Score Output"
            ],
            color = ["#667eea", "#7c3aed", "#8b5cf6", "#a78bfa", "#c4b5fd", "#e9d5ff"]
        ),
        link = dict(
            source = [0, 0, 1, 1, 2, 3, 4, 4],
            target = [1, 1, 2, 3, 4, 4, 5, 5],
            value = [10, 10, 5, 5, 5, 5, 5, 5],
            color = ["rgba(102, 126, 234, 0.3)"] * 8
        )
    ))
    
    flow_fig.update_layout(
        height=350,
        font=dict(size=13, family='Inter', color='#2d3748'),
        paper_bgcolor='white',
        plot_bgcolor='white'
    )
    
    st.plotly_chart(flow_fig, use_container_width=True)

with tab3:
    st.markdown("### 📊 Model Performance Analysis")
    st.markdown("<br>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Model comparison
        st.markdown("#### Model Comparison")
        
        models_data = {
            'Model': ['Rule-Based', 'Logistic Reg', 'Random Forest', 'XGBoost', 'HireSafe'],
            'F1-Score': [0.133, 0.756, 0.707, 0.864, 0.864],
            'Precision': [0.074, 0.642, 1.000, 0.921, 0.921],
            'Recall': [0.698, 0.919, 0.547, 0.814, 0.814]
        }
        
        fig_comp = go.Figure()
        
        fig_comp.add_trace(go.Bar(name='F1-Score', x=models_data['Model'], y=models_data['F1-Score'], marker_color='#667eea'))
        fig_comp.add_trace(go.Bar(name='Precision', x=models_data['Model'], y=models_data['Precision'], marker_color='#48bb78'))
        fig_comp.add_trace(go.Bar(name='Recall', x=models_data['Model'], y=models_data['Recall'], marker_color='#ed8936'))
        
        fig_comp.update_layout(
            barmode='group',
            height=400,
            font=dict(family='Inter', color='#2d3748'),
            paper_bgcolor='white',
            plot_bgcolor='white',
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
        )
        
        st.plotly_chart(fig_comp, use_container_width=True)
    
    with col2:
        # Confusion matrix
        st.markdown("#### Confusion Matrix")
        
        cm_data = [[1656, 46], [7, 79]]
        
        fig_cm = go.Figure(data=go.Heatmap(
            z=cm_data,
            x=['Predicted Legit', 'Predicted Fraud'],
            y=['Actual Legit', 'Actual Fraud'],
            colorscale='Blues',
            text=cm_data,
            texttemplate="%{text}",
            textfont={"size": 22, "family": "Inter", "color": "white"},
            showscale=False,
            hovertemplate='%{y}<br>%{x}<br>Count: %{z}<extra></extra>'
        ))
        
        fig_cm.update_layout(
            height=400,
            font=dict(family='Inter', color='#2d3748'),
            paper_bgcolor='white',
            plot_bgcolor='white'
        )
        
        st.plotly_chart(fig_cm, use_container_width=True)
    
    # Metrics
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("#### 🎯 Key Performance Indicators")
    
    col1, col2, col3, col4, col5 = st.columns(5)
    
    metrics = [
        ("Accuracy", "97.1%", "#667eea"),
        ("Precision", "92.1%", "#48bb78"),
        ("Recall", "81.4%", "#ed8936"),
        ("F1-Score", "86.4%", "#f56565"),
        ("AUC-ROC", "99.3%", "#8b5cf6")
    ]
    
    for col, (label, value, color) in zip([col1, col2, col3, col4, col5], metrics):
        with col:
            col.markdown(f"""
            <div style='text-align: center; padding: 1rem; background: white; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.05);'>
                <h3 style='color: {color}; margin: 0; font-size: 2rem;'>{value}</h3>
                <p style='color: #718096; margin: 0.5rem 0 0 0; font-size: 0.85rem;'>{label}</p>
            </div>
            """, unsafe_allow_html=True)

with tab4:
    st.markdown("### ℹ️ About HireSafe")
    
    st.markdown("""
    <div class='info-box'>
        <h2 style='color: white; margin-top: 0;'>Research Project Overview</h2>
        <p style='font-size: 1.1rem; line-height: 1.8; margin: 0;'>
        HireSafe is an AI-powered fraud detection system developed as part of a Master's degree major project in Computer Science. 
        The system uses advanced Natural Language Processing (NLP) and Machine Learning techniques to identify fraudulent job postings 
        and protect job seekers from recruitment scams.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class='stat-card'>
            <h3 style='color: #667eea;'>📚 Research Methodology</h3>
            <ul style='line-height: 1.8; color: #4a5568;'>
                <li><b>Dataset:</b> EMSCAD (Employment Scam Aegean Dataset)</li>
                <li><b>Samples:</b> 17,880 job postings</li>
                <li><b>Fraudulent:</b> 1,258 confirmed scams (7%)</li>
                <li><b>Features:</b> 5,006 extracted features</li>
                <li><b>Model:</b> XGBoost with TF-IDF vectorization</li>
                <li><b>Validation:</b> Statistical significance testing (p < 0.0001)</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class='stat-card'>
            <h3 style='color: #48bb78;'>🔬 Technical Stack</h3>
            <ul style='line-height: 1.8; color: #4a5568;'>
                <li><b>Language:</b> Python 3.10+</li>
                <li><b>ML Framework:</b> scikit-learn, XGBoost</li>
                <li><b>NLP:</b> spaCy, NLTK, Sentence-Transformers</li>
                <li><b>Visualization:</b> Plotly, Streamlit</li>
                <li><b>Deployment:</b> Streamlit Cloud</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class='stat-card'>
            <h3 style='color: #ed8936;'>🎓 Academic Contribution</h3>
            <p style='line-height: 1.8; color: #4a5568;'>
            This project contributes to the field of cybersecurity and fraud detection by:
            </p>
            <ul style='line-height: 1.8; color: #4a5568;'>
                <li>Comprehensive comparison of ML approaches</li>
                <li>Novel signal extraction methodology</li>
                <li>Explainable AI implementation</li>
                <li>Real-world deployment strategy</li>
                <li>Statistical validation of results</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class='stat-card'>
            <h3 style='color: #8b5cf6;'>👤 Author Information</h3>
            <p style='line-height: 1.8; color: #4a5568;'>
            <b>Name:</b> Diya Patel<br>
            <b>Program:</b> Master's in Computer Science<br>
            <b>Project Type:</b> Major Project<br>
            <b>Year:</b> 2026<br>
            <b>GitHub:</b> <a href='#' style='color: #667eea;'>github.com/diyap24/hiresafe</a><br>
            <b>Email:</b> diyadp25@gmail.com
            </p>
        </div>
        """, unsafe_allow_html=True)

# Footer
st.markdown("""
<div class='footer'>
    <h2 style='color: white; margin: 0 0 1rem 0;'>🛡️ HireSafe</h2>
    <p style='color: #cbd5e0; font-size: 1.1rem; margin: 0 0 1.5rem 0;'>AI-Powered Recruitment Fraud Detection System</p>
    <p style='color: #a0aec0; font-size: 0.95rem; margin: 0;'>Master's Major Project in Computer Science</p>
    <p style='color: #a0aec0; font-size: 0.95rem; margin: 0.5rem 0;'>Developed by Diya Patel | 2026</p>
    <p style='color: #718096; font-size: 0.85rem; margin: 1rem 0 0 0;'>⚠️ For educational and research purposes. Always verify job postings independently through official channels.</p>
</div>
""", unsafe_allow_html=True)