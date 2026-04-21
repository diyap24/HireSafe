import matplotlib
matplotlib.use('Agg')  # disable GUI backend
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Rectangle, Polygon, Circle
import numpy as np
import seaborn as sns

sns.set_style("whitegrid")
plt.rcParams['font.size'] = 10
plt.rcParams['font.family'] = 'sans-serif'

import os
os.makedirs('figures', exist_ok=True)

def add_box(ax, x, y, w, h, text, color, fontsize=10):
    """Helper to add styled box"""
    box = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.08", 
                         edgecolor=color, facecolor=color, alpha=0.25, linewidth=2.5)
    ax.add_patch(box)
    ax.text(x + w/2, y + h/2, text, fontsize=fontsize, 
            fontweight='bold', ha='center', va='center')

def add_arrow(ax, x1, y1, x2, y2, color='black', width=2.5):
    """Helper to add arrow"""
    arrow = FancyArrowPatch((x1, y1), (x2, y2), arrowstyle='->', 
                            mutation_scale=25, linewidth=width, color=color)
    ax.add_patch(arrow)

# ============================================================================
# FIGURE 1: System Architecture
# ============================================================================
print("Generating Figure 1: System Architecture...")

fig, ax = plt.subplots(figsize=(14, 11))
ax.set_xlim(0, 10)
ax.set_ylim(0, 13)
ax.axis('off')

ax.text(5, 12.5, 'HireSafe System Architecture', fontsize=16, 
        fontweight='bold', ha='center')

# Presentation Layer
layer1 = FancyBboxPatch((0.5, 10), 9, 2, boxstyle="round,pad=0.1", 
                        edgecolor='#3498db', facecolor='#ebf5fb', linewidth=3)
ax.add_patch(layer1)
ax.text(5, 11.7, 'PRESENTATION LAYER', fontsize=13, fontweight='bold', ha='center')
ax.text(5, 11.3, 'Streamlit Web Interface', fontsize=10, ha='center', style='italic')

# UI tabs
tabs = ['Single', 'Batch', 'Compare', 'Stats', 'Method', 'About']
for i, tab in enumerate(tabs):
    x = 1 + i * 1.3
    tab_box = Rectangle((x, 10.3), 1.1, 0.5, facecolor='#d6eaf8', 
                        edgecolor='#2980b9', linewidth=1.5)
    ax.add_patch(tab_box)
    ax.text(x + 0.55, 10.55, tab, fontsize=7, ha='center', va='center')

add_arrow(ax, 5, 10, 5, 9.3)

# Application Layer
layer2 = FancyBboxPatch((0.5, 6.5), 9, 2.5, boxstyle="round,pad=0.1", 
                        edgecolor='#e74c3c', facecolor='#fadbd8', linewidth=3)
ax.add_patch(layer2)
ax.text(5, 8.7, 'APPLICATION LAYER', fontsize=13, fontweight='bold', ha='center')

modules = [
    ('Signal\nExtract', 1, 7, 1.5, 1, '#c0392b'),
    ('Feature\nEngineer', 3, 7, 1.5, 1, '#9b59b6'),
    ('Model\nInference', 5, 7, 1.5, 1, '#f39c12'),
    ('Risk\nAssess', 7.5, 7, 1.5, 1, '#16a085')
]

for name, x, y, w, h, color in modules:
    add_box(ax, x, y, w, h, name, color, 9)

for i in range(3):
    add_arrow(ax, 2.5 + i*2, 7.5, 3 + i*2, 7.5, '#7f8c8d', 2)

add_arrow(ax, 5, 6.5, 5, 5.8)

# Data Layer
layer3 = FancyBboxPatch((0.5, 3.5), 9, 2, boxstyle="round,pad=0.1", 
                        edgecolor='#27ae60', facecolor='#d5f4e6', linewidth=3)
ax.add_patch(layer3)
ax.text(5, 5.2, 'DATA LAYER', fontsize=13, fontweight='bold', ha='center')

files = [
    ('XGBoost\n42MB', 1.2, 3.8),
    ('TF-IDF\n8.7MB', 3.2, 3.8),
    ('Signals\n156KB', 5.2, 3.8),
    ('Config\n4KB', 7.2, 3.8)
]

for name, x, y in files:
    file_box = Rectangle((x, y), 1.4, 0.9, facecolor='#abebc6', 
                         edgecolor='#229954', linewidth=1.5)
    ax.add_patch(file_box)
    ax.text(x + 0.7, y + 0.45, name, fontsize=7, ha='center', va='center')

# Infrastructure
infra = Rectangle((1, 1.8), 8, 1.2, facecolor='#ecf0f1', 
                  edgecolor='#95a5a6', linewidth=2, linestyle='dashed')
ax.add_patch(infra)
ax.text(5, 2.9, 'Infrastructure: Python 3.10 | Streamlit | File System', 
        fontsize=9, ha='center', fontweight='bold')

plt.tight_layout()
plt.savefig('figures/system_architecture.png', dpi=300, bbox_inches='tight', facecolor='white')
plt.close()
print("✓ Generated")

# ============================================================================
# FIGURE 2: Component Diagram
# ============================================================================
print("Generating Figure 2: Component Diagram...")

fig, ax = plt.subplots(figsize=(13, 9))
ax.set_xlim(0, 13)
ax.set_ylim(0, 9)
ax.axis('off')

ax.text(6.5, 8.5, 'Application Layer Components', fontsize=15, 
        fontweight='bold', ha='center')

components = {
    'UI Control': (1, 6.5, 2.3, 1, '#3498db'),
    'Signal Extract': (1, 4, 2.3, 1, '#e74c3c'),
    'Feature Eng': (4.5, 4, 2.3, 1, '#9b59b6'),
    'TF-IDF': (4.5, 2.2, 2.3, 1, '#f39c12'),
    'Inference': (8, 4, 2.3, 1, '#16a085'),
    'Risk Assess': (8, 6.5, 2.3, 1, '#c0392b'),
    'Formatter': (4.5, 6.5, 2.3, 1, '#8e44ad')
}

for name, (x, y, w, h, color) in components.items():
    add_box(ax, x, y, w, h, name, color, 10)

# Arrows showing data flow
flows = [
    (2.15, 7, 4.5, 7),
    (2.15, 4.5, 4.5, 4.5),
    (3.15, 4, 3.15, 5),
    (5.65, 3.2, 5.65, 4),
    (6.8, 4.5, 8, 4.5),
    (9.15, 5, 9.15, 6.5),
    (8, 7, 6.8, 7),
]

for x1, y1, x2, y2 in flows:
    add_arrow(ax, x1, y1, x2, y2, '#34495e', 2)

plt.tight_layout()
plt.savefig('figures/component_diagram.png', dpi=300, bbox_inches='tight', facecolor='white')
plt.close()
print("✓ Generated")

# ============================================================================
# FIGURE 3: UI Mockups
# ============================================================================
print("Generating Figure 3: UI Mockups...")

fig = plt.figure(figsize=(15, 9))
gs = fig.add_gridspec(2, 2, hspace=0.3, wspace=0.25)

# Mockup 1: Main Interface
ax1 = fig.add_subplot(gs[0, :])
ax1.set_xlim(0, 10)
ax1.set_ylim(0, 5)
ax1.axis('off')
ax1.text(5, 4.7, 'Single Analysis Interface', fontsize=12, fontweight='bold', ha='center')

# Browser chrome - FIXED
chrome = Rectangle((0.2, 4.2), 9.6, 0.35, facecolor='#34495e', edgecolor='black')
ax1.add_patch(chrome)
ax1.text(5, 4.37, '🌐 HireSafe - Fraud Detection', fontsize=9, ha='center', color='white')

# Page - FIXED
page = Rectangle((0.2, 0.3), 9.6, 3.9, facecolor='#0f172a', edgecolor='#2c3e50', linewidth=2)
ax1.add_patch(page)

# Input area - FIXED
input_area = Rectangle((0.5, 2), 4.5, 1.8, facecolor='#1e293b', edgecolor='#3b82f6', linewidth=2)
ax1.add_patch(input_area)
ax1.text(2.75, 3.5, 'Job Posting Input', fontsize=9, ha='center', color='white', fontweight='bold')
ax1.text(2.75, 2.5, '[Text area]', fontsize=8, ha='center', color='#94a3b8')

# Button - FIXED
btn = Rectangle((1.5, 2.1), 2.5, 0.3, facecolor='#3b82f6', edgecolor='none')
ax1.add_patch(btn)
ax1.text(2.75, 2.25, 'ANALYZE', fontsize=8, ha='center', color='white', fontweight='bold')

# Results area - FIXED
result_area = Rectangle((5.5, 2), 4, 1.8, facecolor='#1e293b', edgecolor='#3b82f6', linewidth=2)
ax1.add_patch(result_area)
ax1.text(7.5, 3.5, 'Analysis Results', fontsize=9, ha='center', color='white', fontweight='bold')

# Gauge
gauge = Circle((7.5, 2.8), 0.5, facecolor='#0f172a', edgecolor='#ef4444', linewidth=3)
ax1.add_patch(gauge)
ax1.text(7.5, 2.8, '78%', fontsize=12, ha='center', color='#ef4444', fontweight='bold')

# Mockup 2: Batch Analysis
ax2 = fig.add_subplot(gs[1, 0])
ax2.set_xlim(0, 5)
ax2.set_ylim(0, 4)
ax2.axis('off')
ax2.text(2.5, 3.7, 'Batch Analysis', fontsize=11, fontweight='bold', ha='center')

# FIXED
batch_bg = Rectangle((0.3, 0.5), 4.4, 3, facecolor='#0f172a', edgecolor='#3b82f6', linewidth=2)
ax2.add_patch(batch_bg)

# FIXED
upload = Rectangle((0.8, 2), 3.4, 1, facecolor='#1e293b', edgecolor='#3b82f6', 
                   linewidth=1.5, linestyle='dashed')
ax2.add_patch(upload)
ax2.text(2.5, 2.5, '📂 Upload CSV', fontsize=9, ha='center', color='#cbd5e0')

# Mockup 3: Statistics
ax3 = fig.add_subplot(gs[1, 1])
ax3.set_xlim(0, 5)
ax3.set_ylim(0, 4)
ax3.axis('off')
ax3.text(2.5, 3.7, 'Statistics Dashboard', fontsize=11, fontweight='bold', ha='center')

# FIXED
stats_bg = Rectangle((0.3, 0.5), 4.4, 3, facecolor='#0f172a', edgecolor='#3b82f6', linewidth=2)
ax3.add_patch(stats_bg)

# Metric cards - FIXED
metrics = [('248', 0.6, 2.5), ('42', 1.8, 2.5), ('89', 3, 2.5)]
for val, x, y in metrics:
    card = Rectangle((x, y), 1, 0.6, facecolor='#1e293b', edgecolor='#3b82f6', linewidth=1.5)
    ax3.add_patch(card)
    ax3.text(x + 0.5, y + 0.3, val, fontsize=10, ha='center', color='#60a5fa', fontweight='bold')

plt.suptitle('HireSafe User Interface Mockups', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('figures/ui_mockups.png', dpi=300, bbox_inches='tight', facecolor='white')
plt.close()
print("✓ Generated")

# ============================================================================
# FIGURE 4: Deployment Architecture
# ============================================================================
print("Generating Figure 4: Deployment Architecture...")

fig, ax = plt.subplots(figsize=(13, 9))
ax.set_xlim(0, 13)
ax.set_ylim(0, 11)
ax.axis('off')

ax.text(6.5, 10.5, 'Cloud Deployment Architecture', fontsize=15, fontweight='bold', ha='center')

# Users
for x in [1, 2, 3]:
    user = Circle((x, 9.5), 0.25, facecolor='#3498db', edgecolor='#2c3e50', linewidth=2)
    ax.add_patch(user)
    ax.text(x, 9.5, '👤', fontsize=12, ha='center', va='center')

ax.text(2, 8.9, 'End Users', fontsize=9, ha='center', fontweight='bold')

# Internet cloud
cloud_pts = np.array([[5.5, 9.5], [7, 10], [8.5, 9.5], [8, 8.8], [6, 8.8]])
cloud = Polygon(cloud_pts, facecolor='#ecf0f1', edgecolor='#95a5a6', linewidth=2)
ax.add_patch(cloud)
ax.text(7, 9.3, '☁ Internet', fontsize=10, ha='center', fontweight='bold')

add_arrow(ax, 3.5, 9.5, 5.5, 9.3)

# Load Balancer
lb = FancyBboxPatch((5.5, 7.5), 2.5, 0.8, boxstyle="round,pad=0.08", 
                    edgecolor='#e74c3c', facecolor='#fadbd8', linewidth=2.5)
ax.add_patch(lb)
ax.text(6.75, 7.9, '⚖ Load Balancer', fontsize=9, fontweight='bold', ha='center')

add_arrow(ax, 6.75, 8.8, 6.75, 8.3)

# Containers
containers = [(1.5, 5.5, '🐳 App 1'), (5.5, 5.5, '🐳 App 2'), (9.5, 5.5, '🐳 App 3')]

for x, y, label in containers:
    cont = FancyBboxPatch((x, y), 2, 1.2, boxstyle="round,pad=0.08", 
                          edgecolor='#3498db', facecolor='#d6eaf8', linewidth=2)
    ax.add_patch(cont)
    ax.text(x + 1, y + 0.6, label, fontsize=8, ha='center', va='center', fontweight='bold')
    add_arrow(ax, 6.75, 7.5, x + 1, 6.7, '#7f8c8d', 1.5)

# Storage
storage = FancyBboxPatch((4, 3.2), 4.5, 1, boxstyle="round,pad=0.08", 
                         edgecolor='#27ae60', facecolor='#d5f4e6', linewidth=2.5)
ax.add_patch(storage)
ax.text(6.25, 3.9, '💾 Cloud Object Storage', fontsize=9, fontweight='bold', ha='center')
ax.text(6.25, 3.5, 'Models | Config', fontsize=7, ha='center', style='italic')

for x, _, _ in containers:
    add_arrow(ax, x + 1, 5.5, 6.25, 4.2, '#16a085', 1.5)

# Monitoring
monitor = FancyBboxPatch((0.5, 1.5), 2.5, 1.2, boxstyle="round,pad=0.08", 
                         edgecolor='#f39c12', facecolor='#fef5e7', linewidth=2)
ax.add_patch(monitor)
ax.text(1.75, 2.3, '📊 Logging', fontsize=8, fontweight='bold', ha='center')
ax.text(1.75, 1.9, 'CloudWatch', fontsize=7, ha='center', style='italic')

# Database
db = FancyBboxPatch((10, 1.5), 2.5, 1.2, boxstyle="round,pad=0.08", 
                    edgecolor='#8e44ad', facecolor='#f4ecf7', linewidth=2, linestyle='dashed')
ax.add_patch(db)
ax.text(11.25, 2.3, '🗄 Database', fontsize=8, fontweight='bold', ha='center')
ax.text(11.25, 1.9, '(Optional)', fontsize=7, ha='center', style='italic')

plt.tight_layout()
plt.savefig('figures/deployment_architecture.png', dpi=300, bbox_inches='tight', facecolor='white')
plt.close()
print("✓ Generated")

# ============================================================================
# FIGURE 5: Request Flow
# ============================================================================
print("Generating Figure 5: Request Flow...")

fig, ax = plt.subplots(figsize=(9, 13))
ax.set_xlim(0, 9)
ax.set_ylim(0, 15)
ax.axis('off')

ax.text(4.5, 14.5, 'Request Processing Workflow', fontsize=14, fontweight='bold', ha='center')

steps = [
    (13.5, '1. User submits job posting', '#3498db'),
    (12.7, '2. Input validation', '#9b59b6'),
    (11.9, '3. Text preprocessing', '#e74c3c'),
    (11.1, '4. Signal extraction (15ms)', '#c0392b'),
    (10.3, '5. TF-IDF transform (65ms)', '#2980b9'),
    (9.5, '6. Feature concatenation', '#f39c12'),
    (8.7, '7. XGBoost inference (55ms)', '#16a085'),
    (7.9, '8. Risk assessment', '#8e44ad'),
    (7.1, '9. Format & display results', '#27ae60'),
]

for y, text, color in steps:
    add_box(ax, 2, y, 5, 0.6, text, color, 9)
    if y > 7.1:
        add_arrow(ax, 4.5, y, 4.5, y - 0.7)

# Total time
ax.text(4.5, 0.8, 'Total: ~150ms per posting', fontsize=11, ha='center', fontweight='bold',
        bbox=dict(boxstyle='round', facecolor='#fff3cd', edgecolor='#f39c12', linewidth=2))

plt.tight_layout()
plt.savefig('figures/request_flow.png', dpi=300, bbox_inches='tight', facecolor='white')
plt.close()
print("✓ Generated")

# ============================================================================
# FIGURE 6: UI Screenshots
# ============================================================================
print("Generating Figure 6: UI Screenshots...")

fig = plt.figure(figsize=(15, 11))
gs = fig.add_gridspec(3, 2, hspace=0.3, wspace=0.2)

# Screenshot 1: Dashboard
ax1 = fig.add_subplot(gs[0, :])
ax1.set_xlim(0, 15)
ax1.set_ylim(0, 3.5)
ax1.axis('off')

# FIXED
page_bg = Rectangle((0.2, 0.2), 14.6, 3.1, facecolor='#0a0e27', edgecolor='#2c3e50', linewidth=2)
ax1.add_patch(page_bg)

# FIXED
header = Rectangle((0.5, 2.9), 14, 0.25, facecolor='#1e293b', edgecolor='none')
ax1.add_patch(header)
ax1.text(7.5, 3.02, '🛡 HireSafe - AI Fraud Detection', fontsize=10, 
         ha='center', color='#60a5fa', fontweight='bold')

# Tabs - FIXED
tabs = ['🔍 Single', '📦 Batch', '⚖ Compare', '📊 Stats', '🧠 Method', 'ℹ About']
for i, tab in enumerate(tabs):
    tab_color = '#3b82f6' if i == 0 else '#334155'
    tab_box = Rectangle((1 + i*2.3, 2.55), 2.1, 0.12, facecolor=tab_color, edgecolor='#475569')
    ax1.add_patch(tab_box)
    ax1.text(2.05 + i*2.3, 2.61, tab, fontsize=7, ha='center', color='white')

ax1.text(7.5, 1.5, 'Job Posting Analysis Interface', fontsize=9, ha='center', color='#cbd5e0')

# Screenshot 2: Results
ax2 = fig.add_subplot(gs[1, 0])
ax2.set_xlim(0, 7.5)
ax2.set_ylim(0, 3.5)
ax2.axis('off')

# FIXED
result_bg = Rectangle((0.2, 0.2), 7.1, 3.1, facecolor='#0f172a', edgecolor='#334155', linewidth=2)
ax2.add_patch(result_bg)
ax2.text(3.75, 3, 'Fraud Analysis Results', fontsize=9, ha='center', color='#f1f5f9', fontweight='bold')

gauge_bg = Circle((3.75, 1.8), 0.65, facecolor='#1e293b', edgecolor='#3b82f6', linewidth=3)
ax2.add_patch(gauge_bg)
ax2.text(3.75, 1.8, '78%', fontsize=16, ha='center', color='#ef4444', fontweight='bold')
ax2.text(3.75, 1.2, '🔴 HIGH RISK', fontsize=10, ha='center', color='#ef4444', fontweight='bold')

# Screenshot 3: Batch
ax3 = fig.add_subplot(gs[1, 1])
ax3.set_xlim(0, 7.5)
ax3.set_ylim(0, 3.5)
ax3.axis('off')

# FIXED
batch_bg = Rectangle((0.2, 0.2), 7.1, 3.1, facecolor='#0f172a', edgecolor='#334155', linewidth=2)
ax3.add_patch(batch_bg)
ax3.text(3.75, 3, 'Batch Analysis Results', fontsize=9, ha='center', color='#f1f5f9', fontweight='bold')

# FIXED
table_bg = Rectangle((0.5, 0.7), 6.5, 2, facecolor='#1e293b', edgecolor='#475569', linewidth=1.5)
ax3.add_patch(table_bg)
ax3.text(3.75, 2.3, '[Results Table]', fontsize=8, ha='center', color='#94a3b8')

# Screenshot 4: Stats
ax4 = fig.add_subplot(gs[2, :])
ax4.set_xlim(0, 15)
ax4.set_ylim(0, 3.5)
ax4.axis('off')

# FIXED
stats_bg = Rectangle((0.2, 0.2), 14.6, 3.1, facecolor='#0f172a', edgecolor='#334155', linewidth=2)
ax4.add_patch(stats_bg)
ax4.text(7.5, 3, 'Statistics Dashboard', fontsize=9, ha='center', color='#f1f5f9', fontweight='bold')

# Metric cards - FIXED
metrics_display = [('248', 1.5), ('42', 5), ('89', 8.5), ('117', 12)]
for val, x in metrics_display:
    card = Rectangle((x, 2.3), 2.3, 0.5, facecolor='#1e293b', edgecolor='#3b82f6', linewidth=1.5)
    ax4.add_patch(card)
    ax4.text(x + 1.15, 2.55, val, fontsize=10, ha='center', color='#60a5fa', fontweight='bold')

plt.suptitle('HireSafe User Interface Screenshots', fontsize=13, fontweight='bold')
plt.tight_layout()
plt.savefig('figures/ui_screenshots.png', dpi=300, bbox_inches='tight', facecolor='white')
plt.close()
print("✓ Generated")

print("\n" + "="*60)
print("ALL CHAPTER 4 FIGURES GENERATED SUCCESSFULLY!")
print("="*60)
print("\nGenerated files:")
print("1. figures/system_architecture.png")
print("2. figures/component_diagram.png")
print("3. figures/ui_mockups.png")
print("4. figures/deployment_architecture.png")
print("5. figures/request_flow.png")
print("6. figures/ui_screenshots.png")
print("\nAll figures saved at 300 DPI")