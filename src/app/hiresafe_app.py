"""
HireSafe - Advanced Recruitment Fraud Detection System
Complete Enhanced Version with All Features - FIXED
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
import json
from io import StringIO, BytesIO
import time

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

# Enhanced Professional Dark Theme CSS
st.markdown("""
<style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700;800&family=Inter:wght@300;400;500;600;700;800;900&display=swap');
    
    /* Advanced Animations */
    @keyframes gradientShift {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    @keyframes float {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-15px); }
    }
    
    @keyframes glow {
        0%, 100% { box-shadow: 0 0 20px rgba(59, 130, 246, 0.3); }
        50% { box-shadow: 0 0 40px rgba(59, 130, 246, 0.6); }
    }
    
    @keyframes pulse {
        0%, 100% { opacity: 1; transform: scale(1); }
        50% { opacity: 0.8; transform: scale(1.05); }
    }
    
    @keyframes slideInLeft {
        from { transform: translateX(-30px); opacity: 0; }
        to { transform: translateX(0); opacity: 1; }
    }
    
    @keyframes slideInRight {
        from { transform: translateX(30px); opacity: 0; }
        to { transform: translateX(0); opacity: 1; }
    }
    
    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }
    
    @keyframes rotate {
        from { transform: rotate(0deg); }
        to { transform: rotate(360deg); }
    }
    
    @keyframes shimmer {
        0% { background-position: -1000px 0; }
        100% { background-position: 1000px 0; }
    }
    
    @keyframes bounce {
        0%, 100% { transform: translateY(0); }
        50% { transform: translateY(-8px); }
    }
    
    /* Particle effect overlay */
    .stApp::before {
        content: '';
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-image: 
            radial-gradient(circle at 15% 40%, rgba(59, 130, 246, 0.08) 0%, transparent 50%),
            radial-gradient(circle at 85% 60%, rgba(147, 51, 234, 0.08) 0%, transparent 50%),
            radial-gradient(circle at 50% 80%, rgba(16, 185, 129, 0.05) 0%, transparent 50%),
            radial-gradient(circle at 30% 20%, rgba(245, 158, 11, 0.05) 0%, transparent 50%);
        pointer-events: none;
        z-index: 0;
        animation: float 20s ease-in-out infinite;
    }
    
    /* Main app background */
    * {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    }
    
    .stApp {
        background: linear-gradient(-45deg, #0a0e27, #16213e, #1a1f3a, #0f1419, #1e293b);
        background-size: 400% 400%;
        animation: gradientShift 20s ease infinite;
        color: #e2e8f0;
    }
    
    /* Content container with glassmorphism */
    .main .block-container {
        padding: 3rem 2.5rem;
        max-width: 1600px;
        background: rgba(10, 14, 39, 0.75);
        backdrop-filter: blur(25px);
        border-radius: 30px;
        border: 2px solid rgba(59, 130, 246, 0.2);
        box-shadow: 0 10px 50px rgba(0, 0, 0, 0.6);
        animation: fadeIn 0.8s ease-in;
    }
    
    /* Typography with enhanced visibility */
    h1 {
        color: #ffffff !important;
        font-family: 'Space Grotesk', sans-serif !important;
        font-weight: 900 !important;
        font-size: 4rem !important;
        margin-bottom: 1rem !important;
        letter-spacing: -2px !important;
        text-shadow: 0 0 50px rgba(59, 130, 246, 1),
                     0 0 100px rgba(147, 51, 234, 0.6),
                     0 5px 20px rgba(0, 0, 0, 0.8);
        animation: glow 3s ease-in-out infinite, fadeIn 1s ease-in;
        background: linear-gradient(135deg, #60a5fa 0%, #a78bfa 50%, #f472b6 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    
    h2 {
        color: #f1f5f9 !important;
        font-weight: 800 !important;
        font-size: 2.2rem !important;
        text-shadow: 0 2px 15px rgba(59, 130, 246, 0.4);
        animation: slideInLeft 0.6s ease-out;
    }
    
    h3 {
        color: #e2e8f0 !important;
        font-weight: 700 !important;
        font-size: 1.6rem !important;
        animation: slideInRight 0.6s ease-out;
    }
    
    h4 {
        color: #cbd5e0 !important;
        font-weight: 600 !important;
        font-size: 1.3rem !important;
    }
    
    p, span, div {
        color: #cbd5e0 !important;
    }
    
    /* Sidebar with enhanced styling */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0f172a 0%, #1e293b 40%, #1a1f3a 70%, #0f172a 100%);
        padding: 2rem 1rem;
        border-right: 3px solid;
        border-image: linear-gradient(180deg, #3b82f6, #8b5cf6, #3b82f6) 1;
        box-shadow: 5px 0 30px rgba(0, 0, 0, 0.6);
        position: relative;
        overflow: hidden;
    }
    
    [data-testid="stSidebar"]::before {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: radial-gradient(circle, rgba(59, 130, 246, 0.05) 0%, transparent 70%);
        animation: rotate 30s linear infinite;
    }
    
    [data-testid="stSidebar"] * {
        color: #f1f5f9 !important;
        position: relative;
        z-index: 1;
    }
    
    [data-testid="stSidebar"] hr {
        border-color: rgba(59, 130, 246, 0.3) !important;
        box-shadow: 0 1px 10px rgba(59, 130, 246, 0.2);
    }
    
    /* Enhanced cards */
    .stat-card {
        background: linear-gradient(135deg, rgba(15, 23, 42, 0.98) 0%, rgba(30, 41, 59, 0.98) 100%);
        padding: 2rem;
        border-radius: 18px;
        border: 2px solid rgba(59, 130, 246, 0.3);
        box-shadow: 0 10px 40px rgba(0, 0, 0, 0.7), inset 0 1px 0 rgba(255, 255, 255, 0.1);
        margin: 1.2rem 0;
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        position: relative;
        overflow: hidden;
        animation: slideInLeft 0.6s ease-out;
    }
    
    .stat-card::before {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: linear-gradient(45deg, transparent, rgba(59, 130, 246, 0.1), transparent);
        transform: rotate(45deg);
        animation: shimmer 3s infinite;
    }
    
    .stat-card:hover {
        transform: translateY(-8px) scale(1.02);
        border-color: rgba(59, 130, 246, 0.7);
        box-shadow: 0 15px 60px rgba(59, 130, 246, 0.5), inset 0 1px 0 rgba(255, 255, 255, 0.15);
    }
    
    .metric-container {
        background: linear-gradient(135deg, rgba(15, 23, 42, 0.95) 0%, rgba(30, 41, 59, 0.95) 100%);
        padding: 2.5rem 2rem;
        border-radius: 18px;
        border: 2px solid rgba(59, 130, 246, 0.3);
        box-shadow: 0 8px 30px rgba(0, 0, 0, 0.5);
        text-align: center;
        transition: all 0.4s ease;
        position: relative;
        overflow: hidden;
        animation: bounce 2s ease-in-out infinite;
    }
    
    .metric-container::after {
        content: '●';
        position: absolute;
        top: 15px;
        right: 15px;
        color: #10b981;
        font-size: 12px;
        animation: pulse 2s infinite;
    }
    
    .metric-container:hover {
        transform: translateY(-6px) scale(1.05);
        border-color: rgba(59, 130, 246, 0.6);
        box-shadow: 0 12px 40px rgba(59, 130, 246, 0.4);
    }
    
    .metric-container h3 {
        font-size: 3rem !important;
        font-weight: 900 !important;
        margin: 0 !important;
        background: linear-gradient(135deg, #60a5fa 0%, #a78bfa 50%, #f472b6 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        text-shadow: none !important;
        animation: pulse 3s ease-in-out infinite;
    }
    
    .feature-card {
        background: linear-gradient(135deg, rgba(15, 23, 42, 0.98) 0%, rgba(30, 41, 59, 0.98) 100%);
        padding: 3rem;
        border-radius: 20px;
        border: 2px solid rgba(59, 130, 246, 0.3);
        box-shadow: 0 8px 35px rgba(0, 0, 0, 0.6);
        height: 100%;
        transition: all 0.4s ease;
        position: relative;
        overflow: hidden;
    }
    
    .feature-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 5px;
        background: linear-gradient(90deg, #3b82f6, #8b5cf6, #f472b6);
        transform: scaleX(0);
        transition: transform 0.4s ease;
    }
    
    .feature-card:hover::before {
        transform: scaleX(1);
    }
    
    .feature-card:hover {
        border-color: rgba(59, 130, 246, 0.7);
        box-shadow: 0 12px 50px rgba(59, 130, 246, 0.4);
        transform: translateY(-5px);
    }
    
    /* Alert boxes */
    .alert-success {
        background: linear-gradient(135deg, rgba(16, 185, 129, 0.18) 0%, rgba(5, 150, 105, 0.18) 100%);
        color: #6ee7b7 !important;
        padding: 2rem;
        border-radius: 16px;
        border: 2px solid rgba(16, 185, 129, 0.6);
        box-shadow: 0 0 40px rgba(16, 185, 129, 0.3), inset 0 1px 0 rgba(255, 255, 255, 0.1);
        margin: 1.5rem 0;
        position: relative;
        animation: slideInRight 0.5s ease-out;
    }
    
    .alert-success::before {
        content: '✓';
        position: absolute;
        top: 20px;
        left: 20px;
        font-size: 2rem;
        color: #10b981;
        animation: bounce 2s ease-in-out infinite;
    }
    
    .alert-success h4, .alert-success p, .alert-success b {
        color: #d1fae5 !important;
        padding-left: 3rem;
    }
    
    .alert-warning {
        background: linear-gradient(135deg, rgba(245, 158, 11, 0.18) 0%, rgba(217, 119, 6, 0.18) 100%);
        color: #fcd34d !important;
        padding: 2rem;
        border-radius: 16px;
        border: 2px solid rgba(245, 158, 11, 0.6);
        box-shadow: 0 0 40px rgba(245, 158, 11, 0.3), inset 0 1px 0 rgba(255, 255, 255, 0.1);
        margin: 1.5rem 0;
        position: relative;
        animation: slideInRight 0.5s ease-out;
    }
    
    .alert-warning::before {
        content: '⚠';
        position: absolute;
        top: 20px;
        left: 20px;
        font-size: 2rem;
        color: #f59e0b;
        animation: pulse 2s ease-in-out infinite;
    }
    
    .alert-warning h4, .alert-warning p, .alert-warning b {
        color: #fef3c7 !important;
        padding-left: 3rem;
    }
    
    .alert-danger {
        background: linear-gradient(135deg, rgba(239, 68, 68, 0.18) 0%, rgba(220, 38, 38, 0.18) 100%);
        color: #fca5a5 !important;
        padding: 2rem;
        border-radius: 16px;
        border: 2px solid rgba(239, 68, 68, 0.6);
        box-shadow: 0 0 40px rgba(239, 68, 68, 0.3), inset 0 1px 0 rgba(255, 255, 255, 0.1);
        margin: 1.5rem 0;
        position: relative;
        animation: slideInRight 0.5s ease-out;
    }
    
    .alert-danger::before {
        content: '⛔';
        position: absolute;
        top: 20px;
        left: 20px;
        font-size: 2rem;
        animation: pulse 1.5s ease-in-out infinite;
    }
    
    .alert-danger h4, .alert-danger p, .alert-danger b {
        color: #fecaca !important;
        padding-left: 3rem;
    }
    
    .alert-info {
        background: linear-gradient(135deg, rgba(59, 130, 246, 0.18) 0%, rgba(37, 99, 235, 0.18) 100%);
        color: #93c5fd !important;
        padding: 2rem;
        border-radius: 16px;
        border: 2px solid rgba(59, 130, 246, 0.6);
        box-shadow: 0 0 40px rgba(59, 130, 246, 0.3), inset 0 1px 0 rgba(255, 255, 255, 0.1);
        margin: 1.5rem 0;
        position: relative;
    }
    
    .alert-info::before {
        content: 'ℹ';
        position: absolute;
        top: 20px;
        left: 20px;
        font-size: 2rem;
        color: #3b82f6;
    }
    
    .alert-info h4, .alert-info p, .alert-info b {
        color: #dbeafe !important;
        padding-left: 3rem;
    }
    
    /* Enhanced buttons */
    .stButton>button {
        background: linear-gradient(135deg, #3b82f6 0%, #8b5cf6 100%);
        color: white !important;
        border: none;
        border-radius: 14px;
        padding: 1rem 3rem;
        font-weight: 800;
        font-size: 1.1rem;
        box-shadow: 0 6px 25px rgba(59, 130, 246, 0.5);
        transition: all 0.3s ease;
        width: 100%;
        text-transform: uppercase;
        letter-spacing: 1px;
        position: relative;
        overflow: hidden;
    }
    
    .stButton>button::before {
        content: '';
        position: absolute;
        top: 50%;
        left: 50%;
        width: 0;
        height: 0;
        border-radius: 50%;
        background: rgba(255, 255, 255, 0.3);
        transform: translate(-50%, -50%);
        transition: width 0.6s, height 0.6s;
    }
    
    .stButton>button:hover::before {
        width: 300px;
        height: 300px;
    }
    
    .stButton>button:hover {
        transform: translateY(-4px);
        box-shadow: 0 10px 40px rgba(59, 130, 246, 0.7);
        background: linear-gradient(135deg, #2563eb 0%, #7c3aed 100%);
    }
    
    /* Text area */
    .stTextArea textarea {
        background: rgba(15, 23, 42, 0.9) !important;
        border: 3px solid rgba(59, 130, 246, 0.4) !important;
        border-radius: 14px !important;
        color: #e2e8f0 !important;
        font-size: 16px !important;
        padding: 1.5rem !important;
        font-family: 'Inter', monospace !important;
        box-shadow: inset 0 2px 10px rgba(0, 0, 0, 0.3);
        transition: all 0.3s ease;
    }
    
    .stTextArea textarea:focus {
        border-color: rgba(59, 130, 246, 1) !important;
        box-shadow: 0 0 30px rgba(59, 130, 246, 0.5), inset 0 2px 10px rgba(0, 0, 0, 0.3) !important;
    }
    
    .stTextArea textarea::placeholder {
        color: #64748b !important;
    }
    
    /* Enhanced metrics */
    [data-testid="stMetricValue"] {
        font-size: 3.2rem !important;
        font-weight: 900 !important;
        background: linear-gradient(135deg, #60a5fa 0%, #a78bfa 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        text-shadow: none !important;
        animation: pulse 2s ease-in-out infinite;
    }
    
    [data-testid="stMetricDelta"] {
        font-size: 1.2rem !important;
        color: #6ee7b7 !important;
        font-weight: 700 !important;
    }
    
    /* Tabs */
    .stTabs [data-baseweb="tab-list"] {
        gap: 1.5rem;
        background: rgba(15, 23, 42, 0.8);
        padding: 1.5rem;
        border-radius: 16px;
        border: 2px solid rgba(59, 130, 246, 0.25);
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.4);
    }
    
    .stTabs [data-baseweb="tab"] {
        font-weight: 700;
        font-size: 1.15rem;
        color: #94a3b8 !important;
        padding: 1.2rem 2.5rem;
        border-radius: 12px;
        border: 2px solid transparent;
        transition: all 0.3s ease;
        position: relative;
    }
    
    .stTabs [data-baseweb="tab"]::before {
        content: '';
        position: absolute;
        bottom: 0;
        left: 50%;
        width: 0;
        height: 3px;
        background: linear-gradient(90deg, #3b82f6, #8b5cf6);
        transform: translateX(-50%);
        transition: width 0.3s ease;
    }
    
    .stTabs [data-baseweb="tab"]:hover {
        background: rgba(59, 130, 246, 0.15);
        border-color: rgba(59, 130, 246, 0.4);
    }
    
    .stTabs [data-baseweb="tab"]:hover::before {
        width: 80%;
    }
    
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #3b82f6 0%, #8b5cf6 100%) !important;
        color: white !important;
        border-color: rgba(59, 130, 246, 0.6) !important;
        box-shadow: 0 6px 25px rgba(59, 130, 246, 0.5);
    }
    
    .stTabs [aria-selected="true"]::before {
        width: 100%;
    }
    
    /* Progress bar */
    .stProgress > div > div > div {
        background: linear-gradient(90deg, #10b981 0%, #f59e0b 50%, #ef4444 100%);
        height: 14px;
        border-radius: 7px;
        box-shadow: 0 2px 10px rgba(59, 130, 246, 0.4);
    }
    
    /* Signal badges */
    .signal-badge {
        display: inline-block;
        padding: 0.8rem 1.5rem;
        border-radius: 30px;
        font-weight: 800;
        margin: 0.5rem;
        font-size: 1rem;
        border: 3px solid;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3);
        animation: fadeIn 0.5s ease-in;
    }
    
    .signal-detected {
        background: rgba(239, 68, 68, 0.25);
        color: #fca5a5 !important;
        border-color: rgba(239, 68, 68, 0.7);
        box-shadow: 0 0 20px rgba(239, 68, 68, 0.4);
    }
    
    .signal-detected:hover {
        transform: scale(1.1);
        box-shadow: 0 0 30px rgba(239, 68, 68, 0.6);
    }
    
    .signal-clear {
        background: rgba(16, 185, 129, 0.25);
        color: #6ee7b7 !important;
        border-color: rgba(16, 185, 129, 0.7);
        box-shadow: 0 0 20px rgba(16, 185, 129, 0.4);
    }
    
    .signal-clear:hover {
        transform: scale(1.1);
        box-shadow: 0 0 30px rgba(16, 185, 129, 0.6);
    }
    
    /* Info box */
    .info-box {
        background: linear-gradient(135deg, rgba(59, 130, 246, 0.2) 0%, rgba(147, 51, 234, 0.2) 100%);
        color: #e2e8f0 !important;
        padding: 3.5rem;
        border-radius: 25px;
        margin: 2.5rem 0;
        border: 3px solid;
        border-image: linear-gradient(135deg, #3b82f6, #8b5cf6, #f472b6) 1;
        box-shadow: 0 0 60px rgba(59, 130, 246, 0.3);
        position: relative;
        overflow: hidden;
        animation: fadeIn 1s ease-in;
    }
    
    .info-box::before {
        content: '';
        position: absolute;
        top: -50%;
        right: -50%;
        width: 200%;
        height: 200%;
        background: radial-gradient(circle, rgba(147, 51, 234, 0.1) 0%, transparent 70%);
        animation: rotate 25s linear infinite;
    }
    
    .info-box h2, .info-box p {
        color: #f1f5f9 !important;
        position: relative;
        z-index: 1;
    }
    
    /* Footer */
    .footer {
        background: linear-gradient(135deg, rgba(15, 23, 42, 0.98) 0%, rgba(30, 41, 59, 0.98) 100%);
        color: #cbd5e0 !important;
        padding: 4rem 3rem;
        border-radius: 25px;
        margin-top: 4rem;
        text-align: center;
        border: 3px solid;
        border-image: linear-gradient(135deg, #3b82f6, #8b5cf6) 1;
        box-shadow: 0 -8px 40px rgba(0, 0, 0, 0.5);
        position: relative;
        overflow: hidden;
    }
    
    .footer::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: radial-gradient(circle at 50% 50%, rgba(59, 130, 246, 0.05) 0%, transparent 70%);
    }
    
    .footer h2, .footer p {
        color: #e2e8f0 !important;
        position: relative;
        z-index: 1;
    }
    
    /* Expander styling */
    .streamlit-expanderHeader {
        background: rgba(30, 41, 59, 0.8) !important;
        border: 2px solid rgba(59, 130, 246, 0.3) !important;
        border-radius: 12px !important;
        color: #e2e8f0 !important;
        font-weight: 700 !important;
        font-size: 1.1rem !important;
    }
    
    .streamlit-expanderHeader:hover {
        background: rgba(30, 41, 59, 1) !important;
        border-color: rgba(59, 130, 246, 0.6) !important;
    }
    
    /* Download button */
    .stDownloadButton>button {
        background: linear-gradient(135deg, #10b981 0%, #059669 100%);
        color: white !important;
        font-weight: 700;
        padding: 0.8rem 2rem;
    }
    
    .stDownloadButton>button:hover {
        background: linear-gradient(135deg, #059669 0%, #047857 100%);
        transform: translateY(-2px);
    }
    
    /* File uploader */
    [data-testid="stFileUploader"] {
        background: rgba(15, 23, 42, 0.8);
        border: 2px dashed rgba(59, 130, 246, 0.5);
        border-radius: 12px;
        padding: 2rem;
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    .stDeployButton {display:none;}
    header {visibility: hidden;}
    
    /* Custom scrollbar */
    ::-webkit-scrollbar {
        width: 14px;
        height: 14px;
    }
    
    ::-webkit-scrollbar-track {
        background: rgba(15, 23, 42, 0.8);
        border-radius: 7px;
    }
    
    ::-webkit-scrollbar-thumb {
        background: linear-gradient(180deg, #3b82f6, #8b5cf6);
        border-radius: 7px;
        border: 2px solid rgba(15, 23, 42, 0.8);
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: linear-gradient(180deg, #2563eb, #7c3aed);
    }
    
    /* Decorative elements */
    .divider-glow {
        width: 100%;
        height: 2px;
        background: linear-gradient(90deg, transparent, #3b82f6, transparent);
        margin: 2rem 0;
        box-shadow: 0 0 10px rgba(59, 130, 246, 0.5);
    }
    
    /* Tip box */
    .tip-box {
        background: linear-gradient(135deg, rgba(139, 92, 246, 0.15) 0%, rgba(59, 130, 246, 0.15) 100%);
        border-left: 5px solid #8b5cf6;
        padding: 1.5rem;
        border-radius: 12px;
        margin: 1.5rem 0;
        box-shadow: 0 4px 20px rgba(139, 92, 246, 0.2);
    }
    
    .tip-box h4 {
        color: #c4b5fd !important;
        margin: 0 0 1rem 0;
    }
    
    .tip-box p {
        color: #ddd6fe !important;
        margin: 0;
        line-height: 1.8;
    }
    
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

# Helper functions
def analyze_job_posting(job_text, model, tfidf, extractor):
    """Analyze a single job posting and return results"""
    try:
        if not job_text or not job_text.strip():
            return None, "Empty job posting text"
        
        # Create dataframe
        job_df = pd.DataFrame({
            'full_text': [job_text],
            'company_profile': [''],
            'salary_range': ['']
        })
        
        # Extract signals
        signals = extractor.extract_all_signals(job_df.iloc[0])
        
        # Transform text
        X = tfidf.transform([job_text])
        
        # Get predictions
        prediction = model.predict(X)[0]
        probability = model.predict_proba(X)[0]
        
        # Calculate risk score and confidence
        risk_score = int(probability[1] * 100)
        confidence = float(max(probability) * 100)  # Convert to Python float
        
        # Determine risk level
        if risk_score >= 70:
            risk_level = "HIGH RISK"
            risk_emoji = "🔴"
            risk_color = "#ef4444"
            risk_status = "DANGER"
        elif risk_score >= 40:
            risk_level = "MEDIUM RISK"
            risk_emoji = "🟡"
            risk_color = "#f59e0b"
            risk_status = "WARNING"
        else:
            risk_level = "LOW RISK"
            risk_emoji = "🟢"
            risk_color = "#10b981"
            risk_status = "SAFE"
        
        # Convert all numpy types to Python native types for JSON serialization
        result = {
            'prediction': int(prediction),
            'probability': [float(p) for p in probability],  # Convert numpy array to list of floats
            'risk_score': int(risk_score),
            'confidence': float(confidence),
            'risk_level': str(risk_level),
            'risk_emoji': str(risk_emoji),
            'risk_color': str(risk_color),
            'risk_status': str(risk_status),
            'signals': {k: bool(v) for k, v in signals.items()},  # Convert to Python bool
            'job_text': str(job_text)
        }
        
        return result, None
        
    except Exception as e:
        return None, str(e)

def generate_fraud_tips(risk_score, signals):
    """Generate context-sensitive fraud prevention tips"""
    tips = []
    
    # Risk-based tips
    if risk_score >= 70:
        tips.append("🚨 **CRITICAL:** This posting shows strong fraud indicators. Do NOT apply or provide any information.")
        tips.append("⛔ **Never send money** for job applications, training materials, or equipment - legitimate employers never ask for upfront payment.")
    elif risk_score >= 40:
        tips.append("⚠️ **CAUTION:** Several suspicious elements detected. Research thoroughly before proceeding.")
        tips.append("🔍 **Verify independently** - Check company registration, reviews, and official website before engaging.")
    else:
        tips.append("✅ **Appears legitimate** but always practice due diligence when job hunting.")
    
    # Signal-specific tips
    if signals.get('payment_request'):
        tips.append("💰 **Payment Request Detected:** Legitimate employers NEVER ask for money during hiring. Report this immediately.")
    
    if signals.get('urgency'):
        tips.append("⏰ **Urgency Tactics Detected:** Scammers create false urgency to prevent careful consideration. Take your time to research.")
    
    if signals.get('offplatform_contact'):
        tips.append("📱 **Off-Platform Contact:** Avoid WhatsApp, Telegram, or personal emails. Use official company channels only.")
    
    if signals.get('vague_company'):
        tips.append("❓ **Vague Company Info:** Missing company details are a major red flag. Research the employer thoroughly.")
    
    if signals.get('salary_anomaly'):
        tips.append("💵 **Unrealistic Salary:** Claims of unusually high pay for minimal work are common scam tactics.")
    
    # General tips
    tips.append("🔐 **Protect Your Identity:** Never share SSN, bank details, or copies of ID documents before a verified job offer.")
    tips.append("📧 **Email Verification:** Check if the recruiter's email domain matches the company's official website.")
    tips.append("🏢 **Company Research:** Use LinkedIn, Glassdoor, and Google to verify the company's legitimacy and reputation.")
    
    return tips

def generate_report_text(analysis_record, analysis_id):
    """Generate formatted text report"""
    signal_map = {
        'payment_request': ('💰', 'Payment Request Detected'),
        'urgency': ('⏰', 'Urgency Manipulation Tactics'),
        'offplatform_contact': ('📱', 'Off-Platform Communication'),
        'vague_company': ('❓', 'Vague Company Information'),
        'salary_anomaly': ('💵', 'Unrealistic Salary Claims')
    }
    
    report_lines = [
        "="*80,
        "HIRESAFE - FRAUD DETECTION ANALYSIS REPORT",
        "="*80,
        f"\nAnalysis Date: {analysis_record['timestamp']}",
        f"Analysis ID: #{analysis_id}",
        "\n" + "="*80,
        "RISK ASSESSMENT",
        "="*80,
        f"\nRisk Level: {analysis_record['risk_level']}",
        f"Risk Score: {analysis_record['risk_score']}/100",
        f"Model Confidence: {analysis_record.get('confidence', 0):.1f}%",
        f"Status: {analysis_record['risk_status']}",
        f"\n{'='*80}",
        "FRAUD INDICATORS DETECTED",
        "="*80,
    ]
    
    detected_count = sum(analysis_record['signals'].values())
    
    if detected_count > 0:
        for key, (emoji, name) in signal_map.items():
            if analysis_record['signals'][key]:
                report_lines.append(f"\n[X] {name}")
    else:
        report_lines.append("\n[✓] No fraud indicators detected")
    
    report_lines.append(f"\nTotal Red Flags: {detected_count}/5")
    
    report_lines.extend([
        f"\n{'='*80}",
        "RECOMMENDATION",
        "="*80
    ])
    
    risk_score = analysis_record['risk_score']
    
    if risk_score >= 70:
        report_lines.extend([
            "\n⛔ DO NOT APPLY - LIKELY FRAUD",
            "\nThis posting exhibits strong fraud indicators:",
            "• Never send money for job applications or training",
            "• Avoid communicating through personal messaging apps",
            "• Report this posting to the job board immediately",
            "• Verify company legitimacy through official business registries"
        ])
    elif risk_score >= 40:
        report_lines.extend([
            "\n⚠️ PROCEED WITH EXTREME CAUTION",
            "\nSeveral suspicious elements detected:",
            "• Research the company thoroughly using multiple sources",
            "• Check employee reviews on Glassdoor and Indeed",
            "• Verify salary expectations match industry standards",
            "• Never provide payment or sensitive financial information upfront"
        ])
    else:
        report_lines.extend([
            "\n✅ APPEARS LEGITIMATE",
            "\nNo major fraud indicators, but always practice due diligence:",
            "• Independently verify company details through official channels",
            "• Research typical salaries for this role and experience level",
            "• Check company reviews and ratings on multiple platforms",
            "• Trust your professional judgment and intuition"
        ])
    
    report_lines.extend([
        f"\n{'='*80}",
        "JOB POSTING ANALYZED",
        "="*80,
        f"\n{analysis_record['full_text']}",
        f"\n{'='*80}",
        "DISCLAIMER",
        "="*80,
        "\nThis analysis is provided for informational purposes only.",
        "Always verify job postings independently through official channels.",
        "HireSafe is an educational AI system and does not guarantee accuracy.",
        "\nGenerated by HireSafe - AI-Powered Recruitment Fraud Detection",
        "Master's Project by Diya Patel",
        "="*80
    ])
    
    return "\n".join(report_lines)

# Initialize
try:
    model, tfidf, extractor = load_models()
    models_loaded = True
except Exception as e:
    models_loaded = False
    error_msg = str(e)

# Initialize session state
if 'analysis_history' not in st.session_state:
    st.session_state.analysis_history = []

if 'analysis_count' not in st.session_state:
    st.session_state.analysis_count = 0

if 'comparison_slot_1' not in st.session_state:
    st.session_state.comparison_slot_1 = None

if 'comparison_slot_2' not in st.session_state:
    st.session_state.comparison_slot_2 = None

if 'total_analyses' not in st.session_state:
    st.session_state.total_analyses = 0

if 'total_high_risk' not in st.session_state:
    st.session_state.total_high_risk = 0

if 'total_medium_risk' not in st.session_state:
    st.session_state.total_medium_risk = 0

if 'total_low_risk' not in st.session_state:
    st.session_state.total_low_risk = 0

# Enhanced Sidebar
with st.sidebar:
    st.markdown("""
    <div style='text-align: center; padding: 2rem 0; animation: float 4s ease-in-out infinite;'>
        <div style='font-size: 4.5rem; margin-bottom: 1rem; filter: drop-shadow(0 0 20px rgba(96, 165, 250, 0.8));'>🛡️</div>
        <h2 style='color: #f1f5f9; margin: 0.5rem 0; font-size: 2.5rem; font-family: "Space Grotesk", sans-serif; text-shadow: 0 0 20px rgba(96, 165, 250, 0.6);'>HireSafe</h2>
        <p style='color: #94a3b8; font-size: 1rem; margin: 0.5rem 0; font-weight: 600;'>🤖 AI-Powered Security</p>
        <div style='margin-top: 1rem; padding: 0.5rem 1rem; background: rgba(16, 185, 129, 0.2); border-radius: 20px; border: 2px solid rgba(16, 185, 129, 0.5); display: inline-block;'>
            <span style='color: #6ee7b7; font-size: 0.85rem; font-weight: 700;'>● SYSTEM ONLINE</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<div class='divider-glow'></div>", unsafe_allow_html=True)
    
    st.markdown("### 📊 Session Statistics")
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric("🔍 Analyzed", st.session_state.total_analyses)
    with col2:
        st.metric("🚨 High Risk", st.session_state.total_high_risk)
    
    st.metric("⚠️ Medium Risk", st.session_state.total_medium_risk)
    st.metric("✅ Low Risk", st.session_state.total_low_risk)
    
    st.markdown("<div class='divider-glow'></div>", unsafe_allow_html=True)
    
    st.markdown("### 📈 Model Performance")
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric("🎯 Accuracy", "97.1%", "↑ 2.3%")
    with col2:
        st.metric("⚡ F1-Score", "86.4%", "↑ 0.5%")
    
    st.metric("✓ Precision", "92.1%", "↑ 1.1%")
    st.metric("🔍 Recall", "81.4%", "↑ 0.8%")
    
    st.markdown("<div class='divider-glow'></div>", unsafe_allow_html=True)
    
    st.markdown("### 🔬 Detection Capabilities")
    st.markdown("""
    <div style='font-size: 1rem; line-height: 2.2; color: #cbd5e0;'>
        <div style='padding: 0.5rem 0;'>
            <span style='color: #6ee7b7; font-size: 1.2rem;'>✓</span> 
            <b style='color: #f1f5f9;'>Payment Detection</b>
            <span style='float: right; color: #10b981; font-size: 0.85rem;'>●</span>
        </div>
        <div style='padding: 0.5rem 0;'>
            <span style='color: #6ee7b7; font-size: 1.2rem;'>✓</span> 
            <b style='color: #f1f5f9;'>Urgency Analysis</b>
            <span style='float: right; color: #10b981; font-size: 0.85rem;'>●</span>
        </div>
        <div style='padding: 0.5rem 0;'>
            <span style='color: #6ee7b7; font-size: 1.2rem;'>✓</span> 
            <b style='color: #f1f5f9;'>Contact Verification</b>
            <span style='float: right; color: #10b981; font-size: 0.85rem;'>●</span>
        </div>
        <div style='padding: 0.5rem 0;'>
            <span style='color: #6ee7b7; font-size: 1.2rem;'>✓</span> 
            <b style='color: #f1f5f9;'>Company Validation</b>
            <span style='float: right; color: #10b981; font-size: 0.85rem;'>●</span>
        </div>
        <div style='padding: 0.5rem 0;'>
            <span style='color: #6ee7b7; font-size: 1.2rem;'>✓</span> 
            <b style='color: #f1f5f9;'>Salary Intelligence</b>
            <span style='float: right; color: #10b981; font-size: 0.85rem;'>●</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

if not models_loaded:
    st.error("⚠️ **System Error: Models Not Loaded**")
    st.code(error_msg)
    st.stop()

# Enhanced Hero Header
st.markdown("""
<div style='text-align: center; padding: 3rem 0 4rem 0; position: relative;'>
    <div style='font-size: 6rem; margin-bottom: 1.5rem; animation: float 5s ease-in-out infinite; filter: drop-shadow(0 0 30px rgba(96, 165, 250, 1));'>
        🛡️
    </div>
    <h1 style='font-size: 5rem; margin-bottom: 1.5rem;'>HireSafe</h1>
    <div style='width: 200px; height: 4px; background: linear-gradient(90deg, transparent, #3b82f6, #8b5cf6, #f472b6, transparent); margin: 1.5rem auto; box-shadow: 0 0 20px rgba(59, 130, 246, 0.8);'></div>
    <p style='font-size: 1.8rem; color: #f1f5f9; font-weight: 700; text-shadow: 0 2px 20px rgba(0,0,0,0.8); margin: 1.5rem 0; letter-spacing: 1px;'>
        🤖 AI-Powered Recruitment Fraud Detection System
    </p>
    <p style='font-size: 1.15rem; color: #94a3b8; max-width: 900px; margin: 1.5rem auto; line-height: 2;'>
        🔍 Protecting job seekers worldwide from fraudulent postings using advanced Natural Language Processing, 
        Machine Learning algorithms, and real-time threat intelligence
    </p>
</div>
""", unsafe_allow_html=True)

# Quick Stats Banner
col1, col2, col3, col4 = st.columns(4)

metrics_data = [
    ("97.1%", "🎯 Accuracy Rate", "#3b82f6"),
    ("86.4%", "⚡ F1-Score", "#10b981"),
    (f"{st.session_state.total_analyses}", "🔍 Analyzed", "#f59e0b"),
    (f"{st.session_state.total_high_risk}", "🚨 High Risk", "#ef4444")
]

for col, (value, label, color) in zip([col1, col2, col3, col4], metrics_data):
    with col:
        col.markdown(f"""
        <div class='metric-container'>
            <h3 style='color: {color};'>{value}</h3>
            <p style='color: #94a3b8; margin: 0.8rem 0 0 0; font-size: 1rem; font-weight: 600;'>{label}</p>
        </div>
        """, unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# Analysis History Section
if len(st.session_state.analysis_history) > 0:
    st.markdown("<br>", unsafe_allow_html=True)
    
    with st.expander(f"📊 Analysis History ({len(st.session_state.analysis_history)} analyses)", expanded=False):
        st.markdown("### Recent Fraud Detection Analyses")
        
        for idx, record in enumerate(st.session_state.analysis_history):
            risk_color_map = {
                "HIGH RISK": "#ef4444",
                "MEDIUM RISK": "#f59e0b",
                "LOW RISK": "#10b981"
            }
            
            bg_color = risk_color_map.get(record['risk_level'], "#64748b")
            
            col_hist1, col_hist2, col_hist3, col_hist4 = st.columns([3, 1, 1, 1])
            
            with col_hist1:
                st.markdown(f"""
                <div style='background: rgba(30, 41, 59, 0.6); padding: 1rem; border-radius: 10px; border-left: 4px solid {bg_color}; margin-bottom: 1rem;'>
                    <p style='margin: 0; color: #cbd5e0; font-size: 0.9rem;'><b>🕐 {record['timestamp']}</b></p>
                    <p style='margin: 0.5rem 0 0 0; color: #94a3b8; font-size: 0.85rem;'>{record['job_text_preview']}</p>
                </div>
                """, unsafe_allow_html=True)
            
            with col_hist2:
                st.markdown(f"""
                <div style='text-align: center; padding: 0.8rem; background: rgba(30, 41, 59, 0.6); border-radius: 10px; margin-bottom: 1rem;'>
                    <p style='margin: 0; color: {bg_color}; font-size: 1.3rem; font-weight: 800;'>{record['risk_score']}%</p>
                    <p style='margin: 0; color: #94a3b8; font-size: 0.75rem;'>{record['risk_level']}</p>
                </div>
                """, unsafe_allow_html=True)
            
            with col_hist3:
                flags_count = sum(record['signals'].values())
                st.markdown(f"""
                <div style='text-align: center; padding: 0.8rem; background: rgba(30, 41, 59, 0.6); border-radius: 10px; margin-bottom: 1rem;'>
                    <p style='margin: 0; color: #f59e0b; font-size: 1.3rem; font-weight: 800;'>{flags_count}/5</p>
                    <p style='margin: 0; color: #94a3b8; font-size: 0.75rem;'>Red Flags</p>
                </div>
                """, unsafe_allow_html=True)
            
            with col_hist4:
                confidence = record.get('confidence', 0)
                st.markdown(f"""
                <div style='text-align: center; padding: 0.8rem; background: rgba(30, 41, 59, 0.6); border-radius: 10px; margin-bottom: 1rem;'>
                    <p style='margin: 0; color: #3b82f6; font-size: 1.3rem; font-weight: 800;'>{confidence:.0f}%</p>
                    <p style='margin: 0; color: #94a3b8; font-size: 0.75rem;'>Confidence</p>
                </div>
                """, unsafe_allow_html=True)
        
        if st.button("🗑️ Clear History", use_container_width=True):
            st.session_state.analysis_history = []
            st.session_state.analysis_count = 0
            st.rerun()

st.markdown("<br>", unsafe_allow_html=True)

# Main tabs
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "🔍 Single Analysis", 
    "📦 Batch Analysis",
    "⚖️ Compare Jobs",
    "📊 Statistics",
    "🧠 How It Works", 
    "ℹ️ About"
])

# TAB 1: Single Analysis
with tab1:
    col_left, col_right = st.columns([1.6, 1])
    
    with col_left:
        st.markdown("### 📝 Job Posting Input Center")
        
        # Quick examples
        st.markdown("**⚡ Quick Test Examples:**")
        col_ex1, col_ex2, col_ex3 = st.columns(3)
        
        with col_ex1:
            if st.button("✅ Legitimate Job", use_container_width=True):
                st.session_state['job_text'] = """Senior Software Engineer - Microsoft Azure

Microsoft Corporation is seeking an experienced Senior Software Engineer to join our Azure Cloud Platform team in Redmond, Washington.

About the Role:
You will be responsible for designing, developing, and maintaining large-scale distributed systems that power Microsoft Azure. This is a full-time position working with cutting-edge cloud technologies.

Responsibilities:
- Design and implement scalable microservices for Azure infrastructure
- Collaborate with product managers and designers on feature development
- Conduct thorough code reviews and mentor junior engineers

Requirements:
- Bachelor's or Master's degree in Computer Science or related technical field
- 5+ years of professional software development experience
- Strong proficiency in C#, Java, Python, or similar languages

Compensation & Benefits:
- Competitive base salary: $150,000 - $220,000 annually
- Comprehensive health, dental, and vision insurance
- 401(k) retirement plan with company matching

How to Apply:
Please submit your application through the official Microsoft Careers portal at careers.microsoft.com."""
        
        with col_ex2:
            if st.button("⚠️ Suspicious Job", use_container_width=True):
                st.session_state['job_text'] = """Data Entry Specialist - Work From Home

URGENT HIRING! Great opportunity for those looking to work from home!

We are immediately seeking motivated individuals for our remote data entry team. This is a LIMITED TIME opportunity with only a few positions available.

What You'll Do:
- Simple data entry tasks
- Processing information
- No experience required!

Pay: $4,000-$6,000 per month

To Secure Your Position:
1. Register by sending $79 processing fee via PayPal
2. Contact our hiring manager directly on WhatsApp: +1-555-9876

Contact: hiring.manager2024@gmail.com"""
        
        with col_ex3:
            if st.button("🚨 Obvious Scam", use_container_width=True):
                st.session_state['job_text'] = """🔥🔥 MAKE $15,000/WEEK FROM HOME!!! 🔥🔥

💰💰💰 URGENT! IMMEDIATE START REQUIRED! 💰💰💰

EASY MONEY! NO EXPERIENCE! NO SKILLS NEEDED!

Work just 2 HOURS per day and earn $15,000 PER WEEK!

THIS IS 100% REAL! NOT A SCAM! LIMITED TO FIRST 20 APPLICANTS ONLY!!!

Requirements:
- Send $299 training fee IMMEDIATELY via Western Union
- Text your details to +1-555-SCAM right now
- Must be ready to start TODAY

ACT NOW!!! Only 3 spots left!!!

Contact: definitelynotascam@gmail.com"""

        st.markdown("<br>", unsafe_allow_html=True)
        
        # Text input
        job_text = st.text_area(
            "**📋 Paste complete job posting below:**",
            height=440,
            value=st.session_state.get('job_text', ''),
            placeholder="📄 Paste the entire job posting here for AI analysis...\n\n✓ Include job title and company name\n✓ Complete job description\n✓ Requirements and qualifications\n✓ Salary and benefits\n✓ Application instructions"
        )
        
        st.markdown("<br>", unsafe_allow_html=True)
        analyze_button = st.button("🔍 **ANALYZE FOR FRAUD NOW**", type="primary", use_container_width=True)
    
    with col_right:
        st.markdown("### 🚨 Fraud Analysis Dashboard")
        
        if analyze_button and job_text.strip():
            with st.spinner("🔄 Running advanced AI fraud detection..."):
                result, error = analyze_job_posting(job_text, model, tfidf, extractor)
                
                if error:
                    st.error(f"❌ **Analysis Error:** {error}")
                    st.info("💡 **Tip:** Make sure the job posting text is complete and properly formatted.")
                else:
                    # Update statistics
                    st.session_state.total_analyses += 1
                    if result['risk_level'] == "HIGH RISK":
                        st.session_state.total_high_risk += 1
                    elif result['risk_level'] == "MEDIUM RISK":
                        st.session_state.total_medium_risk += 1
                    else:
                        st.session_state.total_low_risk += 1
                    
                    # Store in history
                    analysis_record = {
                        'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                        'job_text_preview': job_text[:100] + "..." if len(job_text) > 100 else job_text,
                        'risk_score': result['risk_score'],
                        'confidence': result['confidence'],
                        'risk_level': result['risk_level'],
                        'risk_status': result['risk_status'],
                        'signals': result['signals'].copy(),
                        'full_text': job_text
                    }
                    st.session_state.analysis_history.insert(0, analysis_record)
                    st.session_state.analysis_count += 1
                    
                    # Keep only last 20 analyses
                    if len(st.session_state.analysis_history) > 20:
                        st.session_state.analysis_history = st.session_state.analysis_history[:20]
                    
                    # Gauge Chart
                    fig_gauge = go.Figure(go.Indicator(
                        mode = "gauge+number+delta",
                        value = result['risk_score'],
                        domain = {'x': [0, 1], 'y': [0, 1]},
                        title = {
                            'text': "<b>🎯 Fraud Probability</b>", 
                            'font': {'size': 20, 'color': '#e2e8f0', 'family': 'Space Grotesk'}
                        },
                        number = {
                            'font': {'size': 64, 'color': result['risk_color'], 'family': 'Space Grotesk'},
                            'suffix': '%'
                        },
                        delta = {'reference': 50, 'increasing': {'color': "#ef4444"}},
                        gauge = {
                            'axis': {'range': [None, 100], 'tickcolor': "#475569"},
                            'bar': {'color': result['risk_color'], 'thickness': 0.8},
                            'bgcolor': "rgba(15, 23, 42, 0.6)",
                            'steps': [
                                {'range': [0, 40], 'color': 'rgba(16, 185, 129, 0.25)'},
                                {'range': [40, 70], 'color': 'rgba(245, 158, 11, 0.25)'},
                                {'range': [70, 100], 'color': 'rgba(239, 68, 68, 0.25)'}
                            ],
                            'threshold': {'line': {'color': "#dc2626", 'width': 6}, 'value': 70}
                        }
                    ))
                    
                    fig_gauge.update_layout(
                        height=320,
                        margin=dict(l=20, r=20, t=70, b=20),
                        paper_bgcolor='rgba(0,0,0,0)',
                        plot_bgcolor='rgba(0,0,0,0)'
                    )
                    
                    st.plotly_chart(fig_gauge, use_container_width=True)
                    
                    # Risk Display with Confidence
                    st.markdown(f"""
                    <div style='background: linear-gradient(135deg, {result['risk_color']} 0%, rgba(0,0,0,0.3) 100%); color: white; padding: 2rem; border-radius: 15px; text-align: center; margin: 2rem 0; box-shadow: 0 0 40px {result['risk_color']}70; border: 3px solid {result['risk_color']};'>
                        <div style='font-size: 3rem; margin-bottom: 0.5rem; animation: pulse 2s ease-in-out infinite;'>{result['risk_emoji']}</div>
                        <h2 style='color: white; margin: 0; font-size: 2.2rem; font-weight: 900;'>{result['risk_level']}</h2>
                        <p style='color: white; margin: 1rem 0 0 0; font-size: 1.15rem;'>🎯 Risk: {result['risk_score']}% | 🤖 Confidence: {result['confidence']:.1f}%</p>
                        <p style='color: white; margin: 0.5rem 0 0 0; font-size: 0.9rem; opacity: 0.8;'>📅 {analysis_record['timestamp']}</p>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    # Download Reports (FIXED JSON SERIALIZATION)
                    st.markdown("#### 📥 Download Analysis Report")
                    
                    report_text = generate_report_text(analysis_record, st.session_state.analysis_count)
                    
                    col_download1, col_download2 = st.columns(2)
                    
                    with col_download1:
                        st.download_button(
                            label="📄 Text Report",
                            data=report_text,
                            file_name=f"HireSafe_Analysis_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
                            mime="text/plain",
                            use_container_width=True
                        )
                    
                    with col_download2:
                        # Convert all values to JSON-serializable Python types
                        report_json = {
                            'analysis_id': int(st.session_state.analysis_count),
                            'timestamp': str(analysis_record['timestamp']),
                            'risk_assessment': {
                                'risk_level': str(result['risk_level']),
                                'risk_score': int(result['risk_score']),
                                'confidence': float(result['confidence']),
                                'status': str(result['risk_status'])
                            },
                            'fraud_indicators': {
                                str(k): bool(v) for k, v in result['signals'].items()
                            },
                            'total_red_flags': int(sum(result['signals'].values())),
                            'job_posting_text': str(job_text)
                        }
                        
                        st.download_button(
                            label="📊 JSON Data",
                            data=json.dumps(report_json, indent=2),
                            file_name=f"HireSafe_Analysis_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json",
                            mime="application/json",
                            use_container_width=True
                        )
                    
                    st.markdown("<div class='divider-glow'></div>", unsafe_allow_html=True)
                    
                    # Fraud Indicators
                    st.markdown("#### 🚩 Detected Fraud Indicators")
                    
                    signal_map = {
                        'payment_request': ('💰', 'Payment Request'),
                        'urgency': ('⏰', 'Urgency Tactics'),
                        'offplatform_contact': ('📱', 'Off-Platform Contact'),
                        'vague_company': ('❓', 'Vague Company Info'),
                        'salary_anomaly': ('💵', 'Salary Anomaly')
                    }
                    
                    detected_count = sum(result['signals'].values())
                    
                    if detected_count > 0:
                        for key, (emoji, name) in signal_map.items():
                            if result['signals'][key]:
                                st.markdown(f"""
                                <span class='signal-badge signal-detected'>{emoji} {name}</span>
                                """, unsafe_allow_html=True)
                        
                        st.markdown(f"""
                        <div style='margin-top: 1.5rem; padding: 1rem; background: rgba(239, 68, 68, 0.15); border-radius: 12px; border-left: 5px solid #ef4444;'>
                            <p style='margin: 0; font-weight: 800; font-size: 1.15rem; color: #fca5a5;'>
                                ⚠️ <b>{detected_count}/5</b> critical red flags identified
                            </p>
                        </div>
                        """, unsafe_allow_html=True)
                    else:
                        st.markdown("""
                        <div class='alert-success' style='padding: 1.5rem;'>
                            <p style='margin: 0; font-size: 1.1rem; font-weight: 700; text-align: center;'>
                                ✅ No fraud indicators detected
                            </p>
                        </div>
                        """, unsafe_allow_html=True)
                    
                    st.markdown("<div class='divider-glow'></div>", unsafe_allow_html=True)
                    
                    # Educational Tips
                    st.markdown("#### 💡 Fraud Prevention Tips")
                    
                    tips = generate_fraud_tips(result['risk_score'], result['signals'])
                    
                    for tip in tips[:5]:  # Show first 5 tips
                        st.markdown(f"""
                        <div class='tip-box'>
                            <p>{tip}</p>
                        </div>
                        """, unsafe_allow_html=True)
        
        elif analyze_button:
            st.warning("⚠️ **Please enter job posting text**")
            st.info("💡 Paste the complete job posting in the text area to the left")

# TAB 2: Batch Analysis
with tab2:
    st.markdown("### 📦 Batch Job Posting Analysis")
    st.markdown("""
    <div class='alert-info'>
        <p><b>Upload a CSV file containing multiple job postings for bulk fraud detection analysis.</b></p>
        <p>Required column: <b>'job_text'</b> or <b>'description'</b> containing the full job posting text.</p>
    </div>
    """, unsafe_allow_html=True)
    
    uploaded_file = st.file_uploader(
        "📂 Upload CSV file with job postings",
        type=['csv'],
        help="CSV must contain a 'job_text' or 'description' column"
    )
    
    if uploaded_file is not None:
        try:
            df = pd.read_csv(uploaded_file)
            
            # Detect text column
            text_col = None
            if 'job_text' in df.columns:
                text_col = 'job_text'
            elif 'description' in df.columns:
                text_col = 'description'
            elif 'text' in df.columns:
                text_col = 'text'
            
            if text_col is None:
                st.error("❌ **Error:** CSV must contain 'job_text', 'description', or 'text' column")
            else:
                st.success(f"✅ **File uploaded successfully!** Found {len(df)} job postings")
                st.info(f"📊 **Using column:** `{text_col}`")
                
                if st.button("🚀 **Start Batch Analysis**", type="primary"):
                    results = []
                    progress_bar = st.progress(0)
                    status_text = st.empty()
                    
                    for idx, row in df.iterrows():
                        job_text = str(row[text_col])
                        
                        status_text.text(f"Analyzing job {idx+1} of {len(df)}...")
                        progress_bar.progress((idx + 1) / len(df))
                        
                        result, error = analyze_job_posting(job_text, model, tfidf, extractor)
                        
                        if result:
                            results.append({
                                'Job_ID': idx + 1,
                                'Risk_Level': result['risk_level'],
                                'Risk_Score': result['risk_score'],
                                'Confidence': f"{result['confidence']:.1f}%",
                                'Payment_Request': '✓' if result['signals']['payment_request'] else '✗',
                                'Urgency': '✓' if result['signals']['urgency'] else '✗',
                                'Off_Platform': '✓' if result['signals']['offplatform_contact'] else '✗',
                                'Vague_Company': '✓' if result['signals']['vague_company'] else '✗',
                                'Salary_Anomaly': '✓' if result['signals']['salary_anomaly'] else '✗',
                                'Total_Flags': sum(result['signals'].values())
                            })
                        else:
                            results.append({
                                'Job_ID': idx + 1,
                                'Risk_Level': 'ERROR',
                                'Risk_Score': 0,
                                'Confidence': '0%',
                                'Error': error
                            })
                    
                    status_text.text("✅ Analysis complete!")
                    progress_bar.empty()
                    
                    results_df = pd.DataFrame(results)
                    
                    st.markdown("### 📊 Batch Analysis Results")
                    
                    # Summary statistics
                    col1, col2, col3, col4 = st.columns(4)
                    
                    high_risk_count = len(results_df[results_df['Risk_Level'] == 'HIGH RISK'])
                    medium_risk_count = len(results_df[results_df['Risk_Level'] == 'MEDIUM RISK'])
                    low_risk_count = len(results_df[results_df['Risk_Level'] == 'LOW RISK'])
                    
                    with col1:
                        st.metric("📝 Total Analyzed", len(results_df))
                    with col2:
                        st.metric("🔴 High Risk", high_risk_count)
                    with col3:
                        st.metric("🟡 Medium Risk", medium_risk_count)
                    with col4:
                        st.metric("🟢 Low Risk", low_risk_count)
                    
                    # Display results table
                    st.dataframe(results_df, use_container_width=True)
                    
                    # Download results
                    csv = results_df.to_csv(index=False)
                    st.download_button(
                        label="📥 Download Results CSV",
                        data=csv,
                        file_name=f"HireSafe_Batch_Results_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
                        mime="text/csv",
                        use_container_width=True
                    )
                    
                    # Visualization
                    st.markdown("### 📈 Risk Distribution")
                    
                    risk_counts = results_df['Risk_Level'].value_counts()
                    
                    fig_pie = go.Figure(data=[go.Pie(
                        labels=risk_counts.index,
                        values=risk_counts.values,
                        marker=dict(colors=['#ef4444', '#f59e0b', '#10b981']),
                        hole=0.4
                    )])
                    
                    fig_pie.update_layout(
                        height=400,
                        paper_bgcolor='rgba(0,0,0,0)',
                        plot_bgcolor='rgba(0,0,0,0)',
                        font=dict(color='#e2e8f0', size=14)
                    )
                    
                    st.plotly_chart(fig_pie, use_container_width=True)
        
        except Exception as e:
            st.error(f"❌ **Error processing file:** {str(e)}")
            st.info("💡 **Tip:** Make sure your CSV is properly formatted with a 'job_text' or 'description' column")

# TAB 3: Compare Jobs
with tab3:
    st.markdown("### ⚖️ Side-by-Side Job Comparison")
    st.markdown("""
    <div class='alert-info'>
        <p><b>Compare two job postings to identify differences in fraud risk and signals.</b></p>
    </div>
    """, unsafe_allow_html=True)
    
    col_compare1, col_compare2 = st.columns(2)
    
    with col_compare1:
        st.markdown("#### 📋 Job Posting A")
        job_a = st.text_area(
            "Paste first job posting:",
            height=300,
            key="job_a",
            placeholder="Paste first job posting here..."
        )
        
        if st.button("🔍 Analyze Job A", use_container_width=True):
            if job_a.strip():
                result, error = analyze_job_posting(job_a, model, tfidf, extractor)
                if result:
                    st.session_state.comparison_slot_1 = result
                    st.success("✅ Job A analyzed!")
                else:
                    st.error(f"❌ Error: {error}")
            else:
                st.warning("⚠️ Please enter job posting text")
    
    with col_compare2:
        st.markdown("#### 📋 Job Posting B")
        job_b = st.text_area(
            "Paste second job posting:",
            height=300,
            key="job_b",
            placeholder="Paste second job posting here..."
        )
        
        if st.button("🔍 Analyze Job B", use_container_width=True):
            if job_b.strip():
                result, error = analyze_job_posting(job_b, model, tfidf, extractor)
                if result:
                    st.session_state.comparison_slot_2 = result
                    st.success("✅ Job B analyzed!")
                else:
                    st.error(f"❌ Error: {error}")
            else:
                st.warning("⚠️ Please enter job posting text")
    
    # Display comparison
    if st.session_state.comparison_slot_1 and st.session_state.comparison_slot_2:
        st.markdown("<div class='divider-glow'></div>", unsafe_allow_html=True)
        st.markdown("### 📊 Comparison Results")
        
        result_a = st.session_state.comparison_slot_1
        result_b = st.session_state.comparison_slot_2
        
        # Comparison metrics
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("""
            <div style='text-align: center; padding: 1.5rem; background: rgba(30, 41, 59, 0.8); border-radius: 12px;'>
                <h4 style='color: #cbd5e0; margin: 0 0 1rem 0;'>Risk Score</h4>
            </div>
            """, unsafe_allow_html=True)
            
            subcol1, subcol2 = st.columns(2)
            with subcol1:
                st.metric("Job A", f"{result_a['risk_score']}%")
            with subcol2:
                st.metric("Job B", f"{result_b['risk_score']}%")
        
        with col2:
            st.markdown("""
            <div style='text-align: center; padding: 1.5rem; background: rgba(30, 41, 59, 0.8); border-radius: 12px;'>
                <h4 style='color: #cbd5e0; margin: 0 0 1rem 0;'>Confidence</h4>
            </div>
            """, unsafe_allow_html=True)
            
            subcol1, subcol2 = st.columns(2)
            with subcol1:
                st.metric("Job A", f"{result_a['confidence']:.1f}%")
            with subcol2:
                st.metric("Job B", f"{result_b['confidence']:.1f}%")
        
        with col3:
            st.markdown("""
            <div style='text-align: center; padding: 1.5rem; background: rgba(30, 41, 59, 0.8); border-radius: 12px;'>
                <h4 style='color: #cbd5e0; margin: 0 0 1rem 0;'>Red Flags</h4>
            </div>
            """, unsafe_allow_html=True)
            
            subcol1, subcol2 = st.columns(2)
            with subcol1:
                flags_a = sum(result_a['signals'].values())
                st.metric("Job A", f"{flags_a}/5")
            with subcol2:
                flags_b = sum(result_b['signals'].values())
                st.metric("Job B", f"{flags_b}/5")
        
        # Signal comparison
        st.markdown("### 🚩 Signal Comparison")
        
        signal_names = {
            'payment_request': '💰 Payment Request',
            'urgency': '⏰ Urgency Tactics',
            'offplatform_contact': '📱 Off-Platform Contact',
            'vague_company': '❓ Vague Company',
            'salary_anomaly': '💵 Salary Anomaly'
        }
        
        comparison_data = []
        for key, name in signal_names.items():
            comparison_data.append({
                'Signal': name,
                'Job A': '✓' if result_a['signals'][key] else '✗',
                'Job B': '✓' if result_b['signals'][key] else '✗'
            })
        
        comparison_df = pd.DataFrame(comparison_data)
        st.dataframe(comparison_df, use_container_width=True, hide_index=True)
        
        # Recommendation
        st.markdown("### 💡 Comparison Recommendation")
        
        if result_a['risk_score'] < result_b['risk_score']:
            st.markdown(f"""
            <div class='alert-success'>
                <h4>Job A appears safer than Job B</h4>
                <p>Job A has a lower fraud risk score ({result_a['risk_score']}% vs {result_b['risk_score']}%) and fewer red flags ({flags_a} vs {flags_b}).</p>
            </div>
            """, unsafe_allow_html=True)
        elif result_a['risk_score'] > result_b['risk_score']:
            st.markdown(f"""
            <div class='alert-success'>
                <h4>Job B appears safer than Job A</h4>
                <p>Job B has a lower fraud risk score ({result_b['risk_score']}% vs {result_a['risk_score']}%) and fewer red flags ({flags_b} vs {flags_a}).</p>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div class='alert-info'>
                <h4>Both jobs have similar risk levels</h4>
                <p>Both postings show similar fraud risk scores ({result_a['risk_score']}%). Review other factors like company reputation.</p>
            </div>
            """, unsafe_allow_html=True)

# TAB 4: Statistics Dashboard
with tab4:
    st.markdown("### 📊 Usage Statistics Dashboard")
    
    if st.session_state.total_analyses == 0:
        st.info("📈 **No analyses yet.** Start analyzing job postings to see statistics here!")
    else:
        # Summary cards
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric(
                "🔍 Total Analyses",
                st.session_state.total_analyses,
                delta=None
            )
        
        with col2:
            high_pct = (st.session_state.total_high_risk / st.session_state.total_analyses * 100) if st.session_state.total_analyses > 0 else 0
            st.metric(
                "🔴 High Risk",
                st.session_state.total_high_risk,
                delta=f"{high_pct:.1f}%"
            )
        
        with col3:
            medium_pct = (st.session_state.total_medium_risk / st.session_state.total_analyses * 100) if st.session_state.total_analyses > 0 else 0
            st.metric(
                "🟡 Medium Risk",
                st.session_state.total_medium_risk,
                delta=f"{medium_pct:.1f}%"
            )
        
        with col4:
            low_pct = (st.session_state.total_low_risk / st.session_state.total_analyses * 100) if st.session_state.total_analyses > 0 else 0
            st.metric(
                "🟢 Low Risk",
                st.session_state.total_low_risk,
                delta=f"{low_pct:.1f}%"
            )
        
        st.markdown("<div class='divider-glow'></div>", unsafe_allow_html=True)
        
        # Charts
        col_chart1, col_chart2 = st.columns(2)
        
        with col_chart1:
            st.markdown("#### 📈 Risk Distribution")
            
            fig_dist = go.Figure(data=[go.Pie(
                labels=['High Risk', 'Medium Risk', 'Low Risk'],
                values=[st.session_state.total_high_risk, st.session_state.total_medium_risk, st.session_state.total_low_risk],
                marker=dict(colors=['#ef4444', '#f59e0b', '#10b981']),
                hole=0.4
            )])
            
            fig_dist.update_layout(
                height=400,
                paper_bgcolor='rgba(0,0,0,0)',
                font=dict(color='#e2e8f0', size=14)
            )
            
            st.plotly_chart(fig_dist, use_container_width=True)
        
        with col_chart2:
            st.markdown("#### 📊 Analysis Trend")
            
            if len(st.session_state.analysis_history) > 1:
                # Get risk scores over time
                risk_scores = [record['risk_score'] for record in reversed(st.session_state.analysis_history)]
                analysis_nums = list(range(1, len(risk_scores) + 1))
                
                fig_trend = go.Figure()
                fig_trend.add_trace(go.Scatter(
                    x=analysis_nums,
                    y=risk_scores,
                    mode='lines+markers',
                    line=dict(color='#3b82f6', width=3),
                    marker=dict(size=8, color='#60a5fa'),
                    fill='tozeroy',
                    fillcolor='rgba(59, 130, 246, 0.2)'
                ))
                
                fig_trend.update_layout(
                    height=400,
                    xaxis_title="Analysis Number",
                    yaxis_title="Risk Score (%)",
                    paper_bgcolor='rgba(0,0,0,0)',
                    plot_bgcolor='rgba(15, 23, 42, 0.6)',
                    font=dict(color='#e2e8f0'),
                    xaxis=dict(showgrid=False),
                    yaxis=dict(showgrid=True, gridcolor='rgba(148, 163, 184, 0.15)')
                )
                
                st.plotly_chart(fig_trend, use_container_width=True)
            else:
                st.info("📊 Analyze more jobs to see trend analysis")
        
        # Signal frequency
        if len(st.session_state.analysis_history) > 0:
            st.markdown("<div class='divider-glow'></div>", unsafe_allow_html=True)
            st.markdown("#### 🚩 Most Common Fraud Signals")
            
            signal_counts = {
                'Payment Request': 0,
                'Urgency Tactics': 0,
                'Off-Platform Contact': 0,
                'Vague Company': 0,
                'Salary Anomaly': 0
            }
            
            for record in st.session_state.analysis_history:
                if record['signals']['payment_request']:
                    signal_counts['Payment Request'] += 1
                if record['signals']['urgency']:
                    signal_counts['Urgency Tactics'] += 1
                if record['signals']['offplatform_contact']:
                    signal_counts['Off-Platform Contact'] += 1
                if record['signals']['vague_company']:
                    signal_counts['Vague Company'] += 1
                if record['signals']['salary_anomaly']:
                    signal_counts['Salary Anomaly'] += 1
            
            fig_signals = go.Figure(data=[go.Bar(
                x=list(signal_counts.keys()),
                y=list(signal_counts.values()),
                marker_color=['#ef4444', '#f59e0b', '#3b82f6', '#8b5cf6', '#10b981'],
                text=list(signal_counts.values()),
                textposition='outside'
            )])
            
            fig_signals.update_layout(
                height=400,
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(15, 23, 42, 0.6)',
                font=dict(color='#e2e8f0'),
                xaxis=dict(showgrid=False),
                yaxis=dict(showgrid=True, gridcolor='rgba(148, 163, 184, 0.15)', title="Count")
            )
            
            st.plotly_chart(fig_signals, use_container_width=True)

# TAB 5: How It Works
with tab5:
    st.markdown("### 🧠 Advanced Fraud Detection Methodology")
    st.markdown("<div class='divider-glow'></div>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class='feature-card'>
            <div style='text-align: center; font-size: 3.5rem; margin-bottom: 1.5rem;'>1️⃣</div>
            <h3 style='color: #60a5fa; text-align: center;'>🔍 Signal Extraction</h3>
            <p style='color: #cbd5e0; line-height: 2; text-align: center;'>
            Multi-layer NLP engine detects 5 critical fraud indicators
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class='feature-card'>
            <div style='text-align: center; font-size: 3.5rem; margin-bottom: 1.5rem;'>2️⃣</div>
            <h3 style='color: #a78bfa; text-align: center;'>🤖 NLP Processing</h3>
            <p style='color: #cbd5e0; line-height: 2; text-align: center;'>
            Sophisticated text analysis extracts semantic patterns
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class='feature-card'>
            <div style='text-align: center; font-size: 3.5rem; margin-bottom: 1.5rem;'>3️⃣</div>
            <h3 style='color: #f472b6; text-align: center;'>⚡ ML Classification</h3>
            <p style='color: #cbd5e0; line-height: 2; text-align: center;'>
            XGBoost ensemble model trained on validated data
            </p>
        </div>
        """, unsafe_allow_html=True)

# TAB 6: About
with tab6:
    st.markdown("### ℹ️ About HireSafe Research Project")
    
    st.markdown("""
    <div class='info-box'>
        <div style='text-align: center; font-size: 3.5rem; margin-bottom: 1.5rem;'>🎓</div>
        <h2 style='margin-top: 0; font-size: 2.5rem; text-align: center;'>Academic Research & Development</h2>
        <p style='font-size: 1.2rem; line-height: 2.2; margin: 2rem 0 0 0; text-align: justify;'>
        HireSafe is a comprehensive AI-powered fraud detection system developed as a Master's degree major project in Computer Engineering. 
        This research project leverages cutting-edge Natural Language Processing techniques and Machine Learning algorithms to protect job seekers worldwide.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class='stat-card'>
        <h3 style='color: #60a5fa; font-size: 1.8rem;'>👤 Project Information</h3>
        <div style='margin-top: 1.5rem; background: rgba(30, 41, 59, 0.6); padding: 2rem; border-radius: 15px;'>
            <table style='width: 100%; color: #cbd5e0; line-height: 2.8; font-size: 1.1rem;'>
                <tr>
                    <td style='width: 40%;'><b style='color: #f1f5f9;'>👤 Student:</b></td>
                    <td style='color: #f59e0b; font-weight: 700;'>Diya Patel</td>
                </tr>
                <tr>
                    <td><b style='color: #f1f5f9;'>🎓 Program:</b></td>
                    <td style='color: #10b981; font-weight: 700;'>Master's in Computer Engineering</td>
                </tr>
                <tr>
                    <td><b style='color: #f1f5f9;'>📅 Year:</b></td>
                    <td style='color: #60a5fa; font-weight: 700;'>2025-2026</td>
                </tr>
            </table>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("""
<div class='footer'>
    <div style='font-size: 5rem; margin-bottom: 1.5rem;'>🛡️</div>
    <h2 style='margin: 0 0 1.5rem 0; font-size: 3rem;'>HireSafe</h2>
    <p style='font-size: 1.4rem; margin: 1.5rem 0;'>🤖 AI-Powered Recruitment Fraud Detection System</p>
    <p style='font-size: 1.1rem; margin: 1rem 0;'>🎓 Master's Major Project in Computer Engineering</p>
    <p style='font-size: 1.05rem;'>Developed by <b style='color: #60a5fa;'>Diya Patel</b> | 2025-2026</p>
</div>
""", unsafe_allow_html=True)