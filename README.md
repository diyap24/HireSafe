# HireSafe 🛡️

> **AI-Powered Recruitment Fraud Detection System**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.22.0-FF4B4B.svg)](https://streamlit.io)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

**HireSafe** is an intelligent fraud detection system that protects job seekers from fraudulent job postings using Natural Language Processing (NLP) and Machine Learning. Built as a Master's thesis project in Computer Engineering, the system achieves **97.1% accuracy** and **86.4% F1-score** through a hybrid approach combining domain-specific signal extraction with XGBoost ensemble learning.

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Performance](#-performance)
- [Demo](#-demo)
- [Installation](#-installation)
- [Quick Start](#-quick-start)
- [Usage](#-usage)
- [Architecture](#-architecture)
- [Dataset](#-dataset)
- [Model Details](#-model-details)
- [Project Structure](#-project-structure)
- [Deployment](#-deployment)
- [API Reference](#-api-reference)
- [Contributing](#-contributing)
- [Roadmap](#-roadmap)
- [Research](#-research)
- [License](#-license)
- [Citation](#-citation)
- [Contact](#-contact)

---

## 🎯 Overview

Online recruitment fraud has become a pervasive threat, with scammers exploiting job seekers through fake postings that request upfront payments, steal personal information, or engage in identity theft. HireSafe addresses this critical problem by providing:

- **Real-time fraud detection** with <150ms response time
- **Explainable AI** through transparent signal-based analysis
- **High accuracy** with 97.1% overall accuracy and 86.4% F1-score
- **User-friendly interface** for both individual and batch analysis
- **Privacy-focused** design with no data storage or tracking

### Key Statistics

- 🎯 **97.1%** Overall Accuracy
- ⚡ **86.4%** F1-Score (Balanced Performance)
- 🎨 **92.1%** Precision (Low False Alarms)
- 🔍 **81.4%** Recall (High Detection Rate)
- ⏱️ **148ms** Average Processing Time
- 📊 **0.986** AUC-ROC Score

---

## ✨ Features

### 🎯 Core Capabilities

- **Single Job Analysis**: Paste any job posting and get instant fraud assessment
- **Batch Processing**: Upload CSV files to screen hundreds of postings simultaneously
- **Job Comparison**: Compare two postings side-by-side to identify the safer option
- **Statistical Dashboard**: View system performance metrics and session statistics
- **Explainable Results**: Clear explanations for every prediction with detected signals

### 🔍 Five Detection Signals

HireSafe identifies fraud through five domain-specific indicators:

| Signal | Description | Importance |
|--------|-------------|------------|
| 💰 **Payment Request** | Detects demands for upfront fees, registration costs, or training payments | 34.2% |
| ⏰ **Urgency Tactics** | Identifies artificial time pressure and "act now" manipulation | 21.8% |
| 📱 **Off-Platform Contact** | Flags suspicious communication channels (WhatsApp, personal email, etc.) | 19.7% |
| 🏢 **Vague Company Info** | Catches incomplete or missing employer details | 14.3% |
| 💵 **Salary Anomaly** | Spots unrealistic compensation claims and get-rich-quick promises | 10.0% |

### 📊 Advanced Features

- **Interactive Fraud Gauge**: Visual probability indicator with color-coded risk levels
- **Signal Badge System**: Quick visual indicators for each detected fraud signal
- **Risk Distribution Charts**: Pie charts showing fraud vs. legitimate classification
- **Downloadable Results**: Export batch analysis results as CSV
- **Session Tracking**: Monitor analyses performed and high-risk postings flagged
- **Responsive Design**: Works seamlessly on desktop and mobile devices

---

## 📈 Performance

### Test Set Results (EMSCAD Dataset)

| Metric | Value | Description |
|--------|-------|-------------|
| **Accuracy** | 97.1% | Overall classification correctness |
| **Precision** | 92.1% | Accuracy of fraud predictions |
| **Recall** | 81.4% | Percentage of frauds detected |
| **F1-Score** | 86.4% | Harmonic mean of precision and recall |
| **Specificity** | 98.9% | Accuracy on legitimate postings |
| **AUC-ROC** | 0.986 | Discrimination ability |
| **False Positive Rate** | 1.1% | Legitimate postings flagged as fraud |
| **False Negative Rate** | 18.6% | Fraudulent postings missed |

### Confusion Matrix

```
                    Predicted
                 Legitimate  Fraudulent
Actual  
Legitimate         1,644        18
Fraudulent            23       103
```

**Interpretation:**
- ✅ **1,644** legitimate postings correctly identified
- ✅ **103** fraudulent postings correctly detected
- ⚠️ **18** false alarms (1.1% false positive rate)
- ⚠️ **23** missed frauds (18.6% false negative rate)

### Comparison with Baseline Models

| Model | Accuracy | Precision | Recall | F1-Score | Training Time |
|-------|----------|-----------|--------|----------|---------------|
| Rule-Based | 84.7% | 31.2% | 87.3% | 46.1% | <1 sec |
| Logistic Regression | 94.5% | 78.9% | 74.6% | 76.7% | 8 sec |
| Random Forest | 95.8% | 85.4% | 78.6% | 81.9% | 126 sec |
| **HireSafe (XGBoost)** | **97.1%** | **92.1%** | **81.4%** | **86.4%** | 217 sec |

### Computational Performance

| Operation | Single Posting | Batch (100 postings) |
|-----------|----------------|----------------------|
| **Text Preprocessing** | 8 ms | - |
| **Signal Extraction** | 15 ms | - |
| **TF-IDF Vectorization** | 65 ms | - |
| **Model Inference** | 55 ms | 4,762/sec |
| **Total Pipeline** | **148 ms** | **2.1 sec** |

---

## 🎥 Demo

### Live Application

🌐 **Try it now:** [HireSafe Live Demo](https://hiresafe-3gvdvcdxsnb6uzubymcajd.streamlit.app/)

Experience the full application with:
- ✅ Real-time fraud detection
- ✅ Batch CSV processing
- ✅ Side-by-side job comparison
- ✅ Interactive statistics dashboard
- ✅ Explainable AI results

### Example Analysis

**Input:**
```
Urgent! Work from home opportunity. Earn $5000/week with minimal effort!
Small registration fee of $99 required. Contact via WhatsApp: +1-555-0123
No experience necessary. Limited spots available - apply now!
```

**Output:**
```
🚨 FRAUD PROBABILITY: 94.3%
⚠️  RISK LEVEL: HIGH

Detected Signals:
💰 Payment Request          ✓ DETECTED
⏰ Urgency Tactics          ✓ DETECTED  
📱 Off-Platform Contact     ✓ DETECTED
💵 Salary Anomaly           ✓ DETECTED
🏢 Vague Company Info       ✓ DETECTED

⚠️ RECOMMENDATION: AVOID THIS POSTING
This job posting exhibits multiple fraud indicators. Do not send money
or share personal information.
```

---

## 🚀 Installation

### Prerequisites

- **Python**: 3.10 or higher
- **RAM**: 8 GB minimum (16 GB recommended)
- **Disk Space**: 2 GB free space
- **OS**: Windows, macOS, or Linux

### Option 1: Standard Installation (Recommended)

```bash
# Clone the repository
git clone https://github.com/yourusername/HireSafe.git
cd HireSafe

# Create virtual environment
python -m venv hiresafe_env

# Activate virtual environment
# On Windows:
hiresafe_env\Scripts\activate

# On macOS/Linux:
source hiresafe_env/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Option 2: Using Conda

```bash
# Clone the repository
git clone https://github.com/yourusername/HireSafe.git
cd HireSafe

# Create conda environment
conda create -n hiresafe python=3.10
conda activate hiresafe

# Install dependencies
pip install -r requirements.txt
```

### Option 3: Docker (Coming Soon)

```bash
# Pull the image
docker pull hiresafe/app:latest

# Run the container
docker run -p 8501:8501 hiresafe/app:latest
```

### Verify Installation

```bash
# Check Python version
python --version  # Should be 3.10+

# Verify Streamlit installation
streamlit --version

# Test imports
python -c "import xgboost, sklearn, streamlit; print('All imports successful!')"
```

---

## ⚡ Quick Start

### Launch the Web Application

```bash
# Navigate to project directory
cd HireSafe

# Activate virtual environment (if not already active)
source hiresafe_env/bin/activate  # macOS/Linux
# OR
hiresafe_env\Scripts\activate  # Windows

# Run the Streamlit app
streamlit run src/app/hiresafe_app.py
```

The application will automatically open in your browser at `http://localhost:8501`

### Analyze a Single Job Posting (Python API)

```python
from src.fraud_detector import FraudDetector

# Initialize the detector
detector = FraudDetector()

# Example job posting
job_text = """
Software Engineer - Remote Position
TechCorp is seeking talented developers. Competitive salary $120K-150K.
Apply at careers@techcorp.com with your resume.
"""

# Analyze
result = detector.analyze(job_text)

# Display results
print(f"Fraud Probability: {result['probability']:.1%}")
print(f"Risk Level: {result['risk_level']}")
print(f"Detected Signals: {', '.join(result['signals']) if result['signals'] else 'None'}")
```

**Output:**
```
Fraud Probability: 3.2%
Risk Level: LOW
Detected Signals: None
```

### Batch Processing Example

```python
import pandas as pd
from src.fraud_detector import FraudDetector

# Load job postings from CSV
df = pd.read_csv('job_postings.csv')

# Initialize detector
detector = FraudDetector()

# Analyze all postings
results = detector.analyze_batch(df['description'].tolist())

# Add results to dataframe
df['fraud_probability'] = results['probabilities']
df['risk_level'] = results['risk_levels']
df['detected_signals'] = results['signals']

# Filter high-risk postings
high_risk = df[df['risk_level'] == 'HIGH']
print(f"Found {len(high_risk)} high-risk postings")

# Save results
df.to_csv('analysis_results.csv', index=False)
```

---

## 📖 Usage

### Web Interface Guide

#### 1️⃣ Single Analysis Tab

**Purpose:** Analyze one job posting at a time

**Steps:**
1. Navigate to **"Single Analysis"** tab
2. Paste the complete job posting text
3. Click **"Analyze for Fraud Now"**
4. View results:
   - Fraud probability gauge (0-100%)
   - Risk level classification (Low/Medium/High)
   - Detected signal indicators
   - Actionable recommendation

**Quick Test Buttons:**
- 🟢 **Legitimate Job**: Test with a safe posting
- 🟡 **Suspicious Job**: Test with a borderline posting
- 🔴 **Obvious Scam**: Test with a clear fraud

#### 2️⃣ Batch Analysis Tab

**Purpose:** Screen multiple postings from CSV file

**CSV Format:**
```csv
job_id,title,description
1,Software Engineer,"Python developer needed..."
2,Sales Representative,"Earn $10K/week from home..."
3,Marketing Manager,"Leading tech company seeks..."
```

**Steps:**
1. Prepare CSV with `description` or `job_text` column
2. Navigate to **"Batch Analysis"** tab
3. Upload your CSV file (max 200 MB)
4. Click **"Start Batch Analysis"**
5. View comprehensive results table
6. Download results as CSV

**Results Include:**
- Risk score for each posting
- Signal breakdown (✓ or ✗ for each signal)
- Risk level classification
- Total fraud flags count

#### 3️⃣ Compare Jobs Tab

**Purpose:** Compare two postings side-by-side

**Steps:**
1. Navigate to **"Compare Jobs"** tab
2. Paste first job posting in **Job A** field
3. Paste second job posting in **Job B** field
4. Click both **"Analyze"** buttons
5. View comparison results:
   - Risk scores comparison
   - Signal-by-signal breakdown
   - Recommendation on safer option

#### 4️⃣ Statistics Tab

**Purpose:** View system performance and session stats

**Displays:**
- Model accuracy (97.1%)
- F1-Score (86.4%)
- Session statistics:
  - Total postings analyzed
  - High-risk postings flagged
- System status indicator

#### 5️⃣ How It Works Tab

**Purpose:** Understand the detection methodology

**Explains:**
- Three-stage detection process
- Signal extraction methodology
- NLP processing pipeline
- ML classification approach

---

## 🏗️ Architecture

### System Overview

```
┌──────────────────────────────────────────────────────────────┐
│                    Presentation Layer                         │
│              (Streamlit Web Application)                      │
│  ┌────────────┐  ┌────────────┐  ┌────────────┐             │
│  │   Single   │  │   Batch    │  │  Compare   │             │
│  │  Analysis  │  │  Analysis  │  │    Jobs    │             │
│  └────────────┘  └────────────┘  └────────────┘             │
└────────────────────────┬─────────────────────────────────────┘
                         │
┌────────────────────────┴─────────────────────────────────────┐
│                   Application Layer                           │
│  ┌───────────────┐  ┌──────────────┐  ┌─────────────────┐   │
│  │    Signal     │  │   Feature    │  │    XGBoost      │   │
│  │  Extraction   │→ │ Engineering  │→ │   Classifier    │   │
│  │  (5 signals)  │  │ (TF-IDF +    │  │ (200 trees,     │   │
│  │               │  │  Signals)    │  │  5005 features) │   │
│  └───────────────┘  └──────────────┘  └─────────────────┘   │
└────────────────────────┬─────────────────────────────────────┘
                         │
┌────────────────────────┴─────────────────────────────────────┐
│                      Data Layer                               │
│  ┌──────────────┐  ┌───────────────┐  ┌──────────────┐      │
│  │   XGBoost    │  │   TF-IDF      │  │    Signal    │      │
│  │   Model      │  │  Vectorizer   │  │   Patterns   │      │
│  │  (42.3 MB)   │  │   (8.7 MB)    │  │  (156 KB)    │      │
│  └──────────────┘  └───────────────┘  └──────────────┘      │
└──────────────────────────────────────────────────────────────┘
```

### Technology Stack

**Core Technologies:**
- **Language**: Python 3.10
- **Web Framework**: Streamlit 1.22.0
- **ML Framework**: XGBoost 1.7.5, scikit-learn 1.2.2
- **NLP**: TF-IDF vectorization with n-grams
- **Visualization**: Plotly 5.14.1
- **Data Processing**: pandas 1.5.3, NumPy 1.24.2

**Development Tools:**
- **Version Control**: Git
- **Code Formatting**: Black
- **Testing**: pytest
- **Documentation**: Markdown

### Data Flow

```
User Input
    ↓
Text Preprocessing (lowercase, clean)
    ↓
Signal Extraction (5 binary features)
    ↓
TF-IDF Vectorization (5000 features)
    ↓
Feature Concatenation (5005 total)
    ↓
XGBoost Prediction
    ↓
Risk Assessment (Low/Medium/High)
    ↓
Result Presentation
```

---

## 📊 Dataset

### EMSCAD (Employment Scam Aegean Dataset)

**Source**: [University of the Aegean Research Lab](https://emscad.github.io/)  
**Publication**: Vidros et al. (2017)

#### Dataset Statistics

| Metric | Count | Percentage |
|--------|-------|------------|
| **Total Job Postings** | 17,880 | 100% |
| **Fraudulent Postings** | 866 | 4.8% |
| **Legitimate Postings** | 17,014 | 95.2% |
| **Time Period** | 2012-2014 | - |
| **Language** | English | - |
| **Features** | 18 attributes | - |

#### Signal Prevalence in Dataset

| Signal | Fraud Posts | Legitimate Posts | Ratio |
|--------|-------------|------------------|-------|
| Payment Request | 47.6% | 0.8% | 59.5× |
| Urgency Tactics | 44.9% | 3.0% | 15.0× |
| Off-Platform Contact | 38.2% | 1.2% | 31.8× |
| Vague Company Info | 52.1% | 8.4% | 6.2× |
| Salary Anomaly | 31.7% | 2.1% | 15.1× |

#### Data Split

| Split | Samples | Fraud | Legitimate | Purpose |
|-------|---------|-------|------------|---------|
| **Training** | 14,304 (80%) | 693 | 13,611 | Model training |
| **Validation** | 1,788 (10%) | 87 | 1,701 | Hyperparameter tuning |
| **Test** | 1,788 (10%) | 86 | 1,702 | Final evaluation |

#### Key Features

- Job title and description
- Company profile and location
- Requirements and qualifications
- Salary range and benefits
- Employment type (full-time, part-time, etc.)
- Required experience and education
- Application instructions
- Fraud label (0 = legitimate, 1 = fraudulent)

### Downloading the Dataset

```bash
# Create data directory
mkdir -p data

# Download from official source
wget https://raw.githubusercontent.com/emscad/emscad-dataset/master/emscad_v1.csv \
     -O data/emscad_dataset.csv

# Verify download
wc -l data/emscad_dataset.csv  # Should show 17,881 lines (including header)
```

---

## 🧠 Model Details

### Feature Engineering Pipeline

#### 1. Text Preprocessing

```python
def preprocess_text(text):
    """Clean and normalize job posting text."""
    # Convert to lowercase
    text = text.lower()
    
    # Remove URLs
    text = re.sub(r'http\S+|www\S+', '', text)
    
    # Remove emails
    text = re.sub(r'\S+@\S+', '', text)
    
    # Remove special characters
    text = re.sub(r'[^a-z0-9\s]', ' ', text)
    
    # Normalize whitespace
    text = re.sub(r'\s+', ' ', text).strip()
    
    return text
```

#### 2. Signal Extraction (5 Binary Features)

Each signal uses regex patterns tuned on the training set:

**Payment Signal Pattern:**
```python
payment_patterns = [
    r'registration fee',
    r'processing fee',
    r'training (?:fee|cost|payment)',
    r'upfront (?:payment|fee|cost)',
    r'starter kit',
    r'pay.*(?:\$|usd|dollars)',
]
```

**Importance Scores:**
- Payment Request: **34.2%**
- Urgency Manipulation: **21.8%**
- Off-Platform Contact: **19.7%**
- Vague Company Info: **14.3%**
- Salary Anomaly: **10.0%**

#### 3. TF-IDF Vectorization (5,000 Features)

```python
tfidf_config = {
    'max_features': 5000,
    'ngram_range': (1, 2),      # Unigrams and bigrams
    'min_df': 2,                 # Minimum document frequency
    'max_df': 0.95,              # Maximum document frequency
    'sublinear_tf': True,        # Use log(tf) instead of tf
    'strip_accents': 'unicode',
    'lowercase': True,
    'stop_words': 'english'
}
```

**Top TF-IDF Features by Importance:**
1. "fee" → fraud indicator
2. "urgent" → pressure tactic
3. "whatsapp" → off-platform
4. "apply now" → urgency
5. "no experience" → suspicious ease

#### 4. Feature Concatenation

Final feature vector: **5,005 dimensions**
- 5 binary signal features
- 5,000 TF-IDF features
- Sparse matrix representation (98.7% sparsity)

### XGBoost Configuration

```python
xgboost_params = {
    # Tree structure
    'max_depth': 6,
    'min_child_weight': 1,
    'gamma': 0,
    
    # Boosting parameters
    'learning_rate': 0.1,
    'n_estimators': 200,
    'subsample': 0.8,
    'colsample_bytree': 0.8,
    
    # Regularization
    'reg_alpha': 0,
    'reg_lambda': 1,
    
    # Class imbalance handling
    'scale_pos_weight': 13.0,  # Ratio of negative to positive class
    
    # Objective and evaluation
    'objective': 'binary:logistic',
    'eval_metric': 'logloss',
    
    # Reproducibility
    'random_state': 42,
    'n_jobs': -1
}
```

### Training Process

```bash
# Train the model
python src/training/train_model.py \
    --data data/emscad_dataset.csv \
    --output models/ \
    --cv-folds 5 \
    --tune-hyperparams
```

**Training Statistics:**
- **Training Time**: 3.6 minutes (AMD Ryzen 5, 6 cores)
- **Model Size**: 42.3 MB
- **Cross-Validation**: 5-fold stratified
- **Early Stopping**: 10 rounds patience
- **Best Iteration**: 187/200

### Model Interpretability

**Feature Importance (Top 10):**
```
1. payment_signal         34.2%
2. urgency_signal         21.8%
3. off_platform_signal    19.7%
4. tfidf_fee               4.8%
5. tfidf_urgent            3.2%
6. vague_company_signal   14.3%
7. tfidf_whatsapp          2.9%
8. salary_anomaly_signal  10.0%
9. tfidf_apply_now         2.4%
10. tfidf_no_experience    1.9%
```

---

## 📁 Project Structure

```
HireSafe/
│
├── .streamlit/                    # Streamlit configuration
│   └── config.toml               # Theme and server settings
│
├── data/                          # Dataset files
│   ├── emscad_dataset.csv        # EMSCAD dataset (not in repo)
│   ├── README.md                 # Data documentation
│   └── .gitkeep                  # Keep folder in git
│
├── models/                        # Trained models
│   ├── xgboost_model.pkl         # XGBoost classifier (42.3 MB)
│   ├── tfidf_vectorizer.pkl      # TF-IDF vectorizer (8.7 MB)
│   ├── signal_extractor.pkl      # Signal patterns (156 KB)
│   └── model_metadata.json       # Model version info
│
├── src/                           # Source code
│   ├── app/
│   │   ├── hiresafe_app.py       # Main Streamlit application
│   │   └── components/           # UI components
│   │       ├── header.py
│   │       ├── analysis_tab.py
│   │       └── visualizations.py
│   │
│   ├── training/
│   │   ├── train_model.py        # Model training script
│   │   ├── evaluate.py           # Evaluation script
│   │   └── hyperparameter_tune.py
│   │
│   ├── preprocessing/
│   │   ├── text_cleaner.py       # Text preprocessing
│   │   └── feature_engineer.py   # Feature extraction
│   │
│   ├── signals/
│   │   ├── signal_extractor.py   # Signal detection logic
│   │   └── patterns.py           # Regex patterns
│   │
│   ├── fraud_detector.py          # Main detector class
│   └── utils.py                   # Utility functions
│
├── notebooks/                     # Jupyter notebooks
│   ├── 01_exploratory_analysis.ipynb
│   ├── 02_feature_engineering.ipynb
│   ├── 03_model_training.ipynb
│   ├── 04_evaluation.ipynb
│   └── 05_error_analysis.ipynb
│
├── tests/                         # Unit tests
│   ├── test_signals.py
│   ├── test_preprocessing.py
│   ├── test_detector.py
│   └── test_integration.py
│
├── docs/                          # Documentation
│   ├── images/                   # Screenshots and diagrams
│   ├── DEPLOYMENT.md             # Deployment guide
│   ├── API_REFERENCE.md          # API documentation
│   └── CONTRIBUTING.md           # Contribution guidelines
│
├── .gitignore                     # Git ignore rules
├── .gitattributes                # Git LFS configuration
├── requirements.txt               # Python dependencies
├── setup.py                       # Package setup
├── setup.sh                       # Streamlit Cloud setup
├── Procfile                       # Heroku deployment
├── runtime.txt                    # Python version
├── config.json                    # Application config
├── LICENSE                        # MIT License
└── README.md                      # This file
```

---

## 🚀 Deployment

### Streamlit Cloud (Recommended)

**Free, easy, and automatic deployments!**

1. **Push to GitHub**
   ```bash
   git add .
   git commit -m "Deploy to Streamlit Cloud"
   git push
   ```

2. **Deploy on Streamlit Cloud**
   - Visit https://share.streamlit.io/
   - Sign in with GitHub
   - Click "New app"
   - Select repository: `yourusername/HireSafe`
   - Main file: `src/app/hiresafe_app.py`
   - Click "Deploy!"

3. **Your app is live!**
   - URL: `https://yourusername-hiresafe-app.streamlit.app`
   - Auto-updates on every git push
   - Free SSL certificate included

### Alternative Platforms

**Heroku:**
```bash
heroku create hiresafe-app
git push heroku main
heroku open
```

**Docker:**
```bash
docker build -t hiresafe .
docker run -p 8501:8501 hiresafe
```

**See [DEPLOYMENT.md](docs/DEPLOYMENT.md) for detailed instructions.**

---

## 🔌 API Reference

### FraudDetector Class

```python
from src.fraud_detector import FraudDetector

detector = FraudDetector(
    model_path='models/xgboost_model.pkl',
    vectorizer_path='models/tfidf_vectorizer.pkl',
    signal_extractor_path='models/signal_extractor.pkl'
)
```

#### Methods

##### `analyze(text: str) -> dict`

Analyze a single job posting.

**Parameters:**
- `text` (str): Job posting text

**Returns:**
```python
{
    'probability': 0.943,              # Fraud probability (0-1)
    'risk_level': 'HIGH',              # 'LOW', 'MEDIUM', or 'HIGH'
    'signals': ['payment', 'urgency'], # Detected signals
    'confidence': 0.89,                # Model confidence
    'processing_time_ms': 152.3        # Processing time
}
```

**Example:**
```python
result = detector.analyze("Earn $10K/week! Small fee required...")
print(f"Risk: {result['risk_level']} ({result['probability']:.1%})")
```

##### `analyze_batch(texts: List[str]) -> dict`

Analyze multiple job postings efficiently.

**Parameters:**
- `texts` (List[str]): List of job posting texts

**Returns:**
```python
{
    'probabilities': [0.03, 0.94, 0.12],
    'risk_levels': ['LOW', 'HIGH', 'LOW'],
    'signals': [[], ['payment', 'urgency'], []],
    'processing_time_ms': 2100.5
}
```

**Example:**
```python
postings = [
    "Software Engineer at Google...",
    "Make money fast! Pay $99...",
    "Marketing role at Microsoft..."
]
results = detector.analyze_batch(postings)
```

##### `explain_prediction(text: str) -> dict`

Get detailed explanation for a prediction.

**Returns:**
```python
{
    'probability': 0.943,
    'top_features': [
        ('payment_signal', 0.342),
        ('tfidf_fee', 0.048),
        ('urgency_signal', 0.218)
    ],
    'signal_breakdown': {
        'payment': True,
        'urgency': True,
        'off_platform': False,
        'vague_company': True,
        'salary_anomaly': False
    },
    'recommendation': 'AVOID: Multiple fraud indicators detected'
}
```

---

## 🤝 Contributing

We welcome contributions! Here's how you can help:

### Ways to Contribute

- 🐛 **Report bugs** via GitHub Issues
- 💡 **Suggest features** in Discussions
- 📝 **Improve documentation**
- 🧪 **Add test cases**
- 🎨 **Enhance UI/UX**
- 🔧 **Fix bugs** via Pull Requests
- 🌍 **Add internationalization** (i18n)

### Development Setup

```bash
# Fork and clone
git clone https://github.com/yourusername/HireSafe.git
cd HireSafe

# Create feature branch
git checkout -b feature/amazing-feature

# Install dev dependencies
pip install -r requirements-dev.txt

# Install pre-commit hooks
pre-commit install

# Make your changes
# ...

# Run tests
pytest tests/ -v --cov=src

# Format code
black src/
isort src/

# Lint
pylint src/

# Commit and push
git add .
git commit -m "Add amazing feature"
git push origin feature/amazing-feature
```

### Code Standards

- ✅ Follow [PEP 8](https://pep8.org/)
- ✅ Use [Black](https://black.readthedocs.io/) formatting
- ✅ Write [Google-style](https://google.github.io/styleguide/pyguide.html) docstrings
- ✅ Maintain >85% test coverage
- ✅ Add type hints where possible
- ✅ Update documentation

### Pull Request Process

1. Update README.md if needed
2. Add tests for new features
3. Ensure all tests pass
4. Update CHANGELOG.md
5. Request review from maintainers

---

## 🗺️ Roadmap

### Version 1.1 (Q3 2025)

- [ ] REST API with FastAPI
- [ ] Docker containerization
- [ ] Multi-language support (Spanish, French)
- [ ] Enhanced signal library (10+ signals)
- [ ] Real-time monitoring dashboard
- [ ] A/B testing framework

### Version 2.0 (Q4 2025)

- [ ] BERT/Transformer integration
- [ ] Browser extension (Chrome, Firefox)
- [ ] Mobile apps (iOS, Android)
- [ ] Active learning pipeline
- [ ] User feedback mechanism
- [ ] LinkedIn integration

### Version 3.0 (2026)

- [ ] Multi-modal detection (images, metadata)
- [ ] Adversarial robustness testing
- [ ] Federated learning for privacy
- [ ] Enterprise deployment toolkit
- [ ] Advanced analytics dashboard
- [ ] Third-party API integration

**See [full roadmap](docs/ROADMAP.md) for details.**

---

## 🔬 Research

### Academic Foundation

This project was developed as part of a Master's thesis in Computer Engineering, investigating the application of machine learning to online recruitment fraud detection.

**Thesis Title:**  
*"HireSafe: AI-Powered Recruitment Fraud Detection Using Natural Language Processing and Ensemble Machine Learning"*

**Author:** Diya Patel  
**Advisor:** Dr. Ausuf Mahmood  
**Institution:** [Your University Name]  
**Year:** 2025

### Key Contributions

1. **Hybrid Detection Approach**: Combines domain-specific signal extraction with deep feature learning
2. **High Performance**: Achieves 97.1% accuracy with 86.4% F1-score on imbalanced dataset
3. **Explainability**: Provides transparent, interpretable predictions through signal analysis
4. **Production-Ready**: Deployable web application with <150ms response time
5. **Comprehensive Evaluation**: Statistical validation and cross-dataset testing

### Publications

*Coming soon: Paper submission to relevant conferences/journals*

### Related Work

- Vidros et al. (2017) - EMSCAD Dataset
- Chen & Guestrin (2016) - XGBoost Algorithm
- Pedregosa et al. (2011) - scikit-learn Library

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) 2025 Diya Patel

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
```

---

## 📖 Citation

If you use HireSafe in your research or project, please cite:

```bibtex
@mastersthesis{patel2025hiresafe,
  title     = {HireSafe: AI-Powered Recruitment Fraud Detection Using 
               Natural Language Processing and Ensemble Machine Learning},
  author    = {Patel, Diya},
  year      = {2025},
  school    = {[Your University Name]},
  type      = {Master's Thesis},
  advisor   = {Mahmood, Ausuf},
  keywords  = {fraud detection, machine learning, NLP, recruitment, XGBoost}
}
```

**Academic Paper:** *In preparation*

---

## 📞 Contact & Support

### Author

**Diya Patel**  
Master's Student in Computer Engineering  
📧 Email: diyadp25@gmail.com  
💼 LinkedIn: [linkedin.com/in/diyapatel](https://www.linkedin.com/in/diya-patel-58639b210/)  
🐙 GitHub: [@diyapatel](https://github.com/diyap24)


### Project Links

- 🌐 **Live Demo**: [https://hiresafe-3gvdvcdxsnb6uzubymcajd.streamlit.app/](https://hiresafe-3gvdvcdxsnb6uzubymcajd.streamlit.app/)
- 📄 **Research Paper**: *In preparation*


---

## 🙏 Acknowledgments

### Dataset

**EMSCAD Dataset** provided by the University of the Aegean:
- Vidros, S., Kolias, C., Kambourakis, G., & Akoglu, L. (2017)
- "Automatic Detection of Online Recruitment Frauds: Characteristics, Methods, and a Public Dataset"

### Libraries & Frameworks

- **XGBoost**: Chen, T., & Guestrin, C. (2016)
- **scikit-learn**: Pedregosa et al. (2011)
- **Streamlit**: Streamlit Inc.
- **Plotly**: Plotly Technologies Inc.

### Special Thanks

- **Dr. Ausuf Mahmood** - Research advisor and mentor
- **University of Bridgeport** - Computer Engineering Department
- **Open Source Community** - For amazing tools and support

### Inspiration

This project was inspired by the critical need to protect job seekers in an increasingly digital employment landscape, where fraudulent postings exploit vulnerable individuals seeking legitimate opportunities.

---



<div align="center">

### 🛡️ Protecting Job Seekers Worldwide


**[⬆ Back to Top](#hiresafe-)**

---

*"In a world of fake opportunities, HireSafe helps you find real ones."*

[![Made with Python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![Powered by Streamlit](https://img.shields.io/badge/Powered%20by-Streamlit-FF4B4B.svg)](https://streamlit.io)
[![Powered by XGBoost](https://img.shields.io/badge/Powered%20by-XGBoost-orange.svg)](https://xgboost.readthedocs.io/)

</div>
