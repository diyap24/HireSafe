import matplotlib
matplotlib.use('Agg')  # non-GUI backend

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np
import seaborn as sns
from matplotlib.patches import Rectangle, Circle, Arrow
import matplotlib.lines as mlines
import matplotlib


# Set style
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("husl")

# Create output directory
import os
os.makedirs('figures', exist_ok=True)

# ============================================================================
# FIGURE 1: Research Framework
# ============================================================================

fig, ax = plt.subplots(figsize=(14, 10))
ax.set_xlim(0, 10)
ax.set_ylim(0, 12)
ax.axis('off')

# Define colors
color_data = '#3498db'
color_preprocess = '#9b59b6'
color_feature = '#e74c3c'
color_model = '#f39c12'
color_eval = '#2ecc71'

# Phase 1: Data Collection
box1 = FancyBboxPatch((0.5, 10), 9, 1.5, boxstyle="round,pad=0.1", 
                       edgecolor=color_data, facecolor=color_data, alpha=0.3, linewidth=3)
ax.add_patch(box1)
ax.text(5, 10.75, 'Phase 1: Data Collection & Preparation', 
        fontsize=14, fontweight='bold', ha='center', va='center')
ax.text(5, 10.3, 'EMSCAD Dataset: 17,880 job postings\n1,258 Fraudulent (7.04%) | 16,622 Legitimate (92.96%)', 
        fontsize=11, ha='center', va='center')

# Arrow
arrow1 = FancyArrowPatch((5, 10), (5, 8.8), arrowstyle='->', mutation_scale=30, 
                         linewidth=3, color='black')
ax.add_patch(arrow1)

# Phase 2: Exploratory Data Analysis
box2 = FancyBboxPatch((0.5, 7.5), 9, 1.2, boxstyle="round,pad=0.1", 
                       edgecolor=color_preprocess, facecolor=color_preprocess, alpha=0.3, linewidth=3)
ax.add_patch(box2)
ax.text(5, 8.4, 'Phase 2: Exploratory Data Analysis', 
        fontsize=14, fontweight='bold', ha='center', va='center')
ax.text(5, 7.95, 'Missing value analysis | Class distribution | Text quality assessment', 
        fontsize=10, ha='center', va='center')

# Arrow
arrow2 = FancyArrowPatch((5, 7.5), (5, 6.3), arrowstyle='->', mutation_scale=30, 
                         linewidth=3, color='black')
ax.add_patch(arrow2)

# Phase 3: Feature Engineering - Split into two branches
box3 = FancyBboxPatch((0.5, 4.5), 9, 1.7, boxstyle="round,pad=0.1", 
                       edgecolor=color_feature, facecolor=color_feature, alpha=0.3, linewidth=3)
ax.add_patch(box3)
ax.text(5, 5.9, 'Phase 3: Feature Engineering & Signal Extraction', 
        fontsize=14, fontweight='bold', ha='center', va='center')

# Left branch - Signals
box3a = FancyBboxPatch((0.7, 4.7), 4, 1, boxstyle="round,pad=0.05", 
                        edgecolor='darkred', facecolor='lightcoral', alpha=0.5, linewidth=2)
ax.add_patch(box3a)
ax.text(2.7, 5.45, 'Signal Extraction', fontsize=11, fontweight='bold', ha='center', va='center')
ax.text(2.7, 5.05, '5 Fraud Signals:\nPayment | Urgency | Off-Platform\nVague Company | Salary Anomaly', 
        fontsize=9, ha='center', va='center')

# Right branch - TF-IDF
box3b = FancyBboxPatch((5.3, 4.7), 4, 1, boxstyle="round,pad=0.05", 
                        edgecolor='darkblue', facecolor='lightblue', alpha=0.5, linewidth=2)
ax.add_patch(box3b)
ax.text(7.3, 5.45, 'TF-IDF Vectorization', fontsize=11, fontweight='bold', ha='center', va='center')
ax.text(7.3, 5.05, '5,006 Features:\nUnigrams + Bigrams\nmax_features=5000', 
        fontsize=9, ha='center', va='center')

# Merge arrow
arrow3a = FancyArrowPatch((2.7, 4.7), (5, 3.8), arrowstyle='->', mutation_scale=25, 
                          linewidth=2.5, color='black')
ax.add_patch(arrow3a)
arrow3b = FancyArrowPatch((7.3, 4.7), (5, 3.8), arrowstyle='->', mutation_scale=25, 
                          linewidth=2.5, color='black')
ax.add_patch(arrow3b)

# Phase 4: Model Development
box4 = FancyBboxPatch((0.5, 2.0), 9, 1.6, boxstyle="round,pad=0.1", 
                       edgecolor=color_model, facecolor=color_model, alpha=0.3, linewidth=3)
ax.add_patch(box4)
ax.text(5, 3.3, 'Phase 4: Model Development & Training', 
        fontsize=14, fontweight='bold', ha='center', va='center')

# Model boxes
models = ['Rule-Based', 'Logistic\nRegression', 'Random\nForest', 'XGBoost']
x_positions = [1.5, 3.5, 5.5, 7.5]
for i, (model, x) in enumerate(zip(models, x_positions)):
    box_model = FancyBboxPatch((x-0.7, 2.2), 1.4, 0.8, boxstyle="round,pad=0.05", 
                                edgecolor='darkorange', facecolor='wheat', alpha=0.7, linewidth=1.5)
    ax.add_patch(box_model)
    ax.text(x, 2.6, model, fontsize=9, fontweight='bold', ha='center', va='center')

# Arrow
arrow4 = FancyArrowPatch((5, 2.0), (5, 0.8), arrowstyle='->', mutation_scale=30, 
                         linewidth=3, color='black')
ax.add_patch(arrow4)

# Phase 5: Evaluation
box5 = FancyBboxPatch((0.5, -0.5), 9, 1.2, boxstyle="round,pad=0.1", 
                       edgecolor=color_eval, facecolor=color_eval, alpha=0.3, linewidth=3)
ax.add_patch(box5)
ax.text(5, 0.4, 'Phase 5: Evaluation & Validation', 
        fontsize=14, fontweight='bold', ha='center', va='center')
ax.text(5, -0.05, 'Cross-validation | Statistical testing | Performance metrics (F1, Precision, Recall, AUC)', 
        fontsize=10, ha='center', va='center')

plt.title('HireSafe Research Framework and Methodology', fontsize=18, fontweight='bold', pad=20)
plt.tight_layout()
plt.savefig('figures/research_framework.png', dpi=300, bbox_inches='tight', facecolor='white')
plt.close()

print("✓ Figure 1: Research Framework generated")

# ============================================================================
# FIGURE 2: Methodology Pipeline - End-to-End
# ============================================================================

fig, ax = plt.subplots(figsize=(16, 12))
ax.set_xlim(0, 10)
ax.set_ylim(0, 14)
ax.axis('off')

def add_process_box(ax, x, y, width, height, text, color, fontsize=10):
    box = FancyBboxPatch((x, y), width, height, boxstyle="round,pad=0.08", 
                         edgecolor=color, facecolor=color, alpha=0.25, linewidth=2.5)
    ax.add_patch(box)
    ax.text(x + width/2, y + height/2, text, fontsize=fontsize, 
            fontweight='bold', ha='center', va='center')

def add_arrow(ax, x1, y1, x2, y2):
    arrow = FancyArrowPatch((x1, y1), (x2, y2), arrowstyle='->', mutation_scale=25, 
                            linewidth=2.5, color='black')
    ax.add_patch(arrow)

# START
ax.text(5, 13.5, 'START', fontsize=14, fontweight='bold', ha='center', 
        bbox=dict(boxstyle='round', facecolor='lightgreen', edgecolor='darkgreen', linewidth=2))
add_arrow(ax, 5, 13.3, 5, 12.8)

# Step 1: Load Data
add_process_box(ax, 2, 12, 6, 0.7, 'Load EMSCAD Dataset\n17,880 job postings', '#3498db', 11)
add_arrow(ax, 5, 12, 5, 11.4)

# Step 2: Data Splitting
add_process_box(ax, 2, 10.6, 6, 0.7, 'Train/Val/Test Split\n80% / 10% / 10% (Stratified)', '#9b59b6', 11)
add_arrow(ax, 5, 10.6, 5, 10.0)

# Step 3: Text Preprocessing
add_process_box(ax, 2, 9.2, 6, 0.7, 'Text Preprocessing\nLowercase | HTML removal | Tokenization', '#e74c3c', 11)
add_arrow(ax, 5, 9.2, 5, 8.6)

# Split into two parallel paths
add_arrow(ax, 5, 8.6, 2.5, 7.9)
add_arrow(ax, 5, 8.6, 7.5, 7.9)

# Left path: Signal Extraction
add_process_box(ax, 0.5, 7.0, 4, 0.8, 'Signal Extraction Module', '#c0392b', 10)
ax.text(2.5, 6.5, '1. Payment Request\n2. Urgency\n3. Off-Platform Contact\n4. Vague Company\n5. Salary Anomaly', 
        fontsize=8, ha='center', va='top')
add_arrow(ax, 2.5, 6.2, 2.5, 5.5)
add_process_box(ax, 0.5, 4.8, 4, 0.6, '5 Binary Signals', '#c0392b', 10)

# Right path: TF-IDF
add_process_box(ax, 5.5, 7.0, 4, 0.8, 'TF-IDF Vectorization', '#2980b9', 10)
ax.text(7.5, 6.5, 'Parameters:\n• max_features: 5,000\n• ngram_range: (1,2)\n• min_df: 2, max_df: 0.95', 
        fontsize=8, ha='center', va='top')
add_arrow(ax, 7.5, 6.2, 7.5, 5.5)
add_process_box(ax, 5.5, 4.8, 4, 0.6, '5,000 TF-IDF Features', '#2980b9', 10)

# Merge paths
add_arrow(ax, 2.5, 4.8, 5, 4.3)
add_arrow(ax, 7.5, 4.8, 5, 4.3)

# Step 4: Feature Concatenation
add_process_box(ax, 2, 3.5, 6, 0.7, 'Feature Concatenation\n5,005 Total Features (5 Signals + 5,000 TF-IDF)', '#f39c12', 11)
add_arrow(ax, 5, 3.5, 5, 2.9)

# Step 5: Model Training
add_process_box(ax, 2, 2.1, 6, 0.7, 'XGBoost Model Training\nGradient Boosting with Early Stopping', '#16a085', 11)
add_arrow(ax, 5, 2.1, 5, 1.5)

# Step 6: Prediction
add_process_box(ax, 2, 0.7, 6, 0.7, 'Fraud Prediction & Risk Assessment\nProbability | Risk Level | Confidence', '#27ae60', 11)
add_arrow(ax, 5, 0.7, 5, 0.1)

# END
ax.text(5, -0.3, 'END', fontsize=14, fontweight='bold', ha='center', 
        bbox=dict(boxstyle='round', facecolor='lightcoral', edgecolor='darkred', linewidth=2))

plt.title('End-to-End Methodology Pipeline', fontsize=18, fontweight='bold', pad=20)
plt.tight_layout()
plt.savefig('figures/methodology_pipeline.png', dpi=300, bbox_inches='tight', facecolor='white')
plt.close()

print("✓ Figure 2: Methodology Pipeline generated")

# ============================================================================
# FIGURE 3: Signal Extraction Flowchart
# ============================================================================

fig, ax = plt.subplots(figsize=(14, 16))
ax.set_xlim(0, 10)
ax.set_ylim(0, 20)
ax.axis('off')

def add_decision_box(ax, x, y, width, height, text):
    # Diamond shape for decision
    points = np.array([[x+width/2, y+height], [x+width, y+height/2], 
                       [x+width/2, y], [x, y+height/2]])
    polygon = plt.Polygon(points, facecolor='#ffe6e6', edgecolor='#c0392b', linewidth=2)
    ax.add_patch(polygon)
    ax.text(x+width/2, y+height/2, text, fontsize=9, ha='center', va='center', fontweight='bold')

# Input
ax.text(5, 19.5, 'INPUT: Job Posting J', fontsize=12, fontweight='bold', ha='center',
        bbox=dict(boxstyle='round', facecolor='lightblue', edgecolor='blue', linewidth=2))
ax.text(5, 18.9, 'Text T, Company Profile C, Salary S', fontsize=10, ha='center')
add_arrow(ax, 5, 18.7, 5, 18.2)

# Initialize
add_process_box(ax, 2, 17.5, 6, 0.6, 'Initialize Signal Vector\nv = {s₁:0, s₂:0, s₃:0, s₄:0, s₅:0}', '#3498db', 10)
add_arrow(ax, 5, 17.5, 5, 16.8)

# Signal 1: Payment
add_process_box(ax, 1.5, 16.0, 7, 0.7, 'Signal 1: Search for Payment Keywords in T\n(fee, payment, deposit, wire transfer, etc.)', '#e74c3c', 9)
add_arrow(ax, 5, 16.0, 5, 15.2)

add_decision_box(ax, 4, 14.2, 2, 0.9, 'Match\nFound?')
add_arrow(ax, 6, 14.65, 7.5, 14.65)
ax.text(7.7, 14.65, 's₁ = 1', fontsize=10, ha='left', va='center',
        bbox=dict(boxstyle='round', facecolor='#ffcccc', alpha=0.7))
add_arrow(ax, 5, 14.2, 5, 13.4)

# Signal 2: Urgency
add_process_box(ax, 1.5, 12.6, 7, 0.7, 'Signal 2: Search for Urgency Keywords in T\n(urgent, immediately, ASAP, limited time, etc.)', '#f39c12', 9)
add_arrow(ax, 5, 12.6, 5, 11.8)

add_decision_box(ax, 4, 10.8, 2, 0.9, 'Match\nFound?')
add_arrow(ax, 6, 11.25, 7.5, 11.25)
ax.text(7.7, 11.25, 's₂ = 1', fontsize=10, ha='left', va='center',
        bbox=dict(boxstyle='round', facecolor='#ffe6cc', alpha=0.7))
add_arrow(ax, 5, 10.8, 5, 10.0)

# Signal 3: Off-Platform
add_process_box(ax, 1.5, 9.2, 7, 0.7, 'Signal 3: Search for Off-Platform Contact in T\n(WhatsApp, Telegram, Gmail, personal email, etc.)', '#9b59b6', 9)
add_arrow(ax, 5, 9.2, 5, 8.4)

add_decision_box(ax, 4, 7.4, 2, 0.9, 'Match\nFound?')
add_arrow(ax, 6, 7.85, 7.5, 7.85)
ax.text(7.7, 7.85, 's₃ = 1', fontsize=10, ha='left', va='center',
        bbox=dict(boxstyle='round', facecolor='#e6ccff', alpha=0.7))
add_arrow(ax, 5, 7.4, 5, 6.6)

# Signal 4: Vague Company
add_process_box(ax, 1.5, 5.8, 7, 0.7, 'Signal 4: Analyze Company Profile C\nCheck length < 20 OR generic descriptors ≥ 2', '#1abc9c', 9)
add_arrow(ax, 5, 5.8, 5, 5.0)

add_decision_box(ax, 4, 4.0, 2, 0.9, 'Vague\nInfo?')
add_arrow(ax, 6, 4.45, 7.5, 4.45)
ax.text(7.7, 4.45, 's₄ = 1', fontsize=10, ha='left', va='center',
        bbox=dict(boxstyle='round', facecolor='#ccffe6', alpha=0.7))
add_arrow(ax, 5, 4.0, 5, 3.2)

# Signal 5: Salary Anomaly
add_process_box(ax, 1.5, 2.4, 7, 0.7, 'Signal 5: Analyze Salary Range S\nCheck if max(S) > $500k OR min(S) > max(S)', '#e67e22', 9)
add_arrow(ax, 5, 2.4, 5, 1.6)

add_decision_box(ax, 4, 0.6, 2, 0.9, 'Anomaly\nDetected?')
add_arrow(ax, 6, 1.05, 7.5, 1.05)
ax.text(7.7, 1.05, 's₅ = 1', fontsize=10, ha='left', va='center',
        bbox=dict(boxstyle='round', facecolor='#ffe6cc', alpha=0.7))
add_arrow(ax, 5, 0.6, 5, -0.2)

# Output
ax.text(5, -0.7, 'OUTPUT: Signal Vector v = {s₁, s₂, s₃, s₄, s₅}', fontsize=12, fontweight='bold', ha='center',
        bbox=dict(boxstyle='round', facecolor='lightgreen', edgecolor='darkgreen', linewidth=2))

plt.title('Signal Extraction Flowchart', fontsize=18, fontweight='bold', pad=20)
plt.tight_layout()
plt.savefig('figures/signal_extraction_flowchart.png', dpi=300, bbox_inches='tight', facecolor='white')
plt.close()

print("✓ Figure 3: Signal Extraction Flowchart generated")

# ============================================================================
# FIGURE 4: Training Pipeline Flowchart
# ============================================================================

fig, ax = plt.subplots(figsize=(12, 16))
ax.set_xlim(0, 10)
ax.set_ylim(0, 18)
ax.axis('off')

y_pos = 17.5

# START
ax.text(5, y_pos, 'START', fontsize=12, fontweight='bold', ha='center',
        bbox=dict(boxstyle='round', facecolor='lightgreen', edgecolor='darkgreen', linewidth=2))
y_pos -= 0.5
add_arrow(ax, 5, y_pos+0.2, 5, y_pos-0.2)
y_pos -= 0.6

# Load Dataset
add_process_box(ax, 2, y_pos, 6, 0.6, 'Load EMSCAD Dataset\n17,880 job postings', '#3498db', 10)
y_pos -= 0.6
add_arrow(ax, 5, y_pos+0.6, 5, y_pos)
y_pos -= 0.6

# Preprocessing
add_process_box(ax, 2, y_pos, 6, 0.6, 'Data Preprocessing\nClean text | Handle missing data', '#9b59b6', 10)
y_pos -= 0.6
add_arrow(ax, 5, y_pos+0.6, 5, y_pos)
y_pos -= 0.6

# Split Data
add_process_box(ax, 2, y_pos, 6, 0.7, 'Train/Val/Test Split\nTrain: 80% | Val: 10% | Test: 10%', '#e74c3c', 10)
y_pos -= 0.7
add_arrow(ax, 5, y_pos+0.7, 5, y_pos)
y_pos -= 0.6

# Feature Engineering
add_process_box(ax, 2, y_pos, 6, 0.8, 'Feature Engineering\n• Extract 5 signals\n• Create TF-IDF (5006)\n• Concatenate features', '#f39c12', 9)
y_pos -= 0.8
add_arrow(ax, 5, y_pos+0.8, 5, y_pos)
y_pos -= 0.6

# Train Baselines
add_process_box(ax, 2, y_pos, 6, 0.7, 'Train Baseline Models\nRule-based | Logistic Regression | Random Forest', '#1abc9c', 9)
y_pos -= 0.7
add_arrow(ax, 5, y_pos+0.7, 5, y_pos)
y_pos -= 0.6

# Hyperparameter Tuning
add_process_box(ax, 2, y_pos, 6, 0.6, 'Hyperparameter Tuning\nGrid search | Cross-validation', '#e67e22', 10)
y_pos -= 0.6
add_arrow(ax, 5, y_pos+0.6, 5, y_pos)
y_pos -= 0.6

# Train XGBoost
add_process_box(ax, 2, y_pos, 6, 0.6, 'Train XGBoost Model\nwith optimal parameters', '#c0392b', 10)
y_pos -= 0.6
add_arrow(ax, 5, y_pos+0.6, 5, y_pos)
y_pos -= 0.6

# Evaluate
add_process_box(ax, 2, y_pos, 6, 0.7, 'Evaluate on Test Set\nCalculate metrics | Generate reports', '#16a085', 10)
y_pos -= 0.7
add_arrow(ax, 5, y_pos+0.7, 5, y_pos)
y_pos -= 0.6

# Statistical Validation
add_process_box(ax, 2, y_pos, 6, 0.6, 'Statistical Validation\nPaired t-test | Significance testing', '#8e44ad', 10)
y_pos -= 0.6
add_arrow(ax, 5, y_pos+0.6, 5, y_pos)
y_pos -= 0.6

# Save Models
add_process_box(ax, 2, y_pos, 6, 0.7, 'Save Models & Results\nXGBoost.pkl | TF-IDF.pkl | Extractor.pkl', '#2c3e50', 10)
y_pos -= 0.7
add_arrow(ax, 5, y_pos+0.7, 5, y_pos)
y_pos -= 0.4

# END
ax.text(5, y_pos, 'END', fontsize=12, fontweight='bold', ha='center',
        bbox=dict(boxstyle='round', facecolor='lightcoral', edgecolor='darkred', linewidth=2))

plt.title('Complete Training Pipeline Flowchart', fontsize=18, fontweight='bold', pad=20)
plt.tight_layout()
plt.savefig('figures/training_pipeline.png', dpi=300, bbox_inches='tight', facecolor='white')
plt.close()

print("✓ Figure 4: Training Pipeline generated")

# ============================================================================
# FIGURE 5: Data Flow Diagram
# ============================================================================

fig, ax = plt.subplots(figsize=(14, 10))
ax.set_xlim(0, 10)
ax.set_ylim(0, 12)
ax.axis('off')

# Input
ax.text(5, 11.5, 'INPUT: Job Posting Text', fontsize=14, fontweight='bold', ha='center',
        bbox=dict(boxstyle='round', facecolor='#e8f4f8', edgecolor='#3498db', linewidth=3))
add_arrow(ax, 5, 11.2, 5, 10.5)

# Preprocessing
add_process_box(ax, 2, 9.7, 6, 0.7, 'Text Preprocessing\nLowercase | HTML Clean | Tokenization', '#9b59b6', 11)
add_arrow(ax, 5, 9.7, 3, 8.8)
add_arrow(ax, 5, 9.7, 7, 8.8)

# Split into two paths
# Left: Signal Extraction
box_left = FancyBboxPatch((0.5, 6.5), 4.5, 2.2, boxstyle="round,pad=0.1", 
                          edgecolor='#c0392b', facecolor='#fadbd8', alpha=0.5, linewidth=2.5)
ax.add_patch(box_left)
ax.text(2.75, 8.4, 'Signal Extraction Module', fontsize=12, fontweight='bold', ha='center')
ax.text(2.75, 7.9, '📊 5 Binary Signals', fontsize=11, ha='center')

signals = ['💰 Payment Request', '⏰ Urgency', '📱 Off-Platform', '❓ Vague Company', '💵 Salary Anomaly']
for i, sig in enumerate(signals):
    ax.text(2.75, 7.5 - i*0.3, sig, fontsize=9, ha='center')

add_arrow(ax, 2.75, 6.5, 2.75, 5.5)
add_process_box(ax, 1, 4.9, 3.5, 0.5, '5 Signal Features', '#c0392b', 10)

# Right: TF-IDF
box_right = FancyBboxPatch((5, 6.5), 4.5, 2.2, boxstyle="round,pad=0.1", 
                           edgecolor='#2980b9', facecolor='#d6eaf8', alpha=0.5, linewidth=2.5)
ax.add_patch(box_right)
ax.text(7.25, 8.4, 'TF-IDF Vectorization', fontsize=12, fontweight='bold', ha='center')
ax.text(7.25, 7.9, '📝 Text Features', fontsize=11, ha='center')

tfidf_params = ['max_features: 5,000', 'ngram_range: (1,2)', 'min_df: 2', 'max_df: 0.95', 'stop_words: english']
for i, param in enumerate(tfidf_params):
    ax.text(7.25, 7.5 - i*0.3, param, fontsize=9, ha='center')

add_arrow(ax, 7.25, 6.5, 7.25, 5.5)
add_process_box(ax, 5.5, 4.9, 3.5, 0.5, '5,000 TF-IDF Features', '#2980b9', 10)

# Merge
add_arrow(ax, 2.75, 4.9, 5, 4.2)
add_arrow(ax, 7.25, 4.9, 5, 4.2)

add_process_box(ax, 2, 3.4, 6, 0.7, 'Feature Concatenation\n5,005 Total Features', '#f39c12', 11)
add_arrow(ax, 5, 3.4, 5, 2.6)

# XGBoost
add_process_box(ax, 2, 1.8, 6, 0.7, 'XGBoost Classifier\nGradient Boosting', '#16a085', 11)
add_arrow(ax, 5, 1.8, 5, 1.0)

# Output
box_output = FancyBboxPatch((2, 0.2), 6, 0.7, boxstyle="round,pad=0.1", 
                            edgecolor='#27ae60', facecolor='#d5f4e6', linewidth=3)
ax.add_patch(box_output)
ax.text(5, 0.8, 'Risk Assessment Output', fontsize=12, fontweight='bold', ha='center')
ax.text(5, 0.4, '🎯 Risk Score | 🔴/🟡/🟢 Risk Level | 🤖 Confidence', fontsize=10, ha='center')

plt.title('Data Flow Architecture', fontsize=18, fontweight='bold', pad=20)
plt.tight_layout()
plt.savefig('figures/data_flow.png', dpi=300, bbox_inches='tight', facecolor='white')
plt.close()

print("✓ Figure 5: Data Flow Diagram generated")

print("\n" + "="*60)
print("ALL CHAPTER 3 FIGURES GENERATED SUCCESSFULLY!")
print("="*60)
print("\nGenerated files:")
print("1. figures/research_framework.png")
print("2. figures/methodology_pipeline.png")
print("3. figures/signal_extraction_flowchart.png")
print("4. figures/training_pipeline.png")
print("5. figures/data_flow.png")
print("\nAll figures saved in 'figures/' directory at 300 DPI")