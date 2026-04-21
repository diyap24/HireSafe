import matplotlib
matplotlib.use('Agg')  # non-GUI backend
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle
import numpy as np
import seaborn as sns

sns.set_style("whitegrid")
import os
os.makedirs('figures', exist_ok=True)

# ============================================================================
# FIGURE: Future Research Roadmap (Chapter 6)
# ============================================================================
print("Generating Chapter 6 Figure: Research Roadmap...")

fig, ax = plt.subplots(figsize=(14, 10))
ax.set_xlim(0, 14)
ax.set_ylim(0, 12)
ax.axis('off')

ax.text(7, 11.5, 'HireSafe Future Research and Development Roadmap', 
        fontsize=15, fontweight='bold', ha='center')

# Timeline
timeline_y = 10.5
ax.plot([1, 13], [timeline_y, timeline_y], 'k-', linewidth=3)

phases = [
    ('Short-term\n(6 months)', 2, '#3498db'),
    ('Medium-term\n(1-2 years)', 5.5, '#f39c12'),
    ('Long-term\n(3+ years)', 10, '#27ae60')
]

for label, x, color in phases:
    circle = plt.Circle((x, timeline_y), 0.3, facecolor=color, edgecolor='black', linewidth=2)
    ax.add_patch(circle)
    ax.text(x, timeline_y + 0.8, label, fontsize=9, ha='center', fontweight='bold')

# Short-term initiatives
short_term = [
    'API Development',
    'Browser Extension',
    'Mobile Apps',
    'Enhanced Signals'
]

y_start = 8.5
for i, item in enumerate(short_term):
    box = FancyBboxPatch((0.5, y_start - i*0.7), 3, 0.5, 
                         boxstyle="round,pad=0.05",
                         edgecolor='#3498db', facecolor='#d6eaf8', linewidth=2)
    ax.add_patch(box)
    ax.text(2, y_start - i*0.7 + 0.25, item, fontsize=9, ha='center', va='center', fontweight='bold')

# Medium-term initiatives
medium_term = [
    'Advanced NLP (BERT)',
    'Multi-modal Detection',
    'Active Learning',
    'Fairness Auditing'
]

for i, item in enumerate(medium_term):
    box = FancyBboxPatch((4.5, y_start - i*0.7), 3, 0.5,
                         boxstyle="round,pad=0.05",
                         edgecolor='#f39c12', facecolor='#fef5e7', linewidth=2)
    ax.add_patch(box)
    ax.text(6, y_start - i*0.7 + 0.25, item, fontsize=9, ha='center', va='center', fontweight='bold')

# Long-term initiatives
long_term = [
    'Adversarial Robustness',
    'Temporal Analysis',
    'Ecosystem Integration',
    'Real-time Intelligence'
]

for i, item in enumerate(long_term):
    box = FancyBboxPatch((9, y_start - i*0.7), 3.5, 0.5,
                         boxstyle="round,pad=0.05",
                         edgecolor='#27ae60', facecolor='#d5f4e6', linewidth=2)
    ax.add_patch(box)
    ax.text(10.75, y_start - i*0.7 + 0.25, item, fontsize=9, ha='center', va='center', fontweight='bold')

# Key challenges
challenges = Rectangle((1, 3.5), 12, 1.8, facecolor='#ffe6e6', edgecolor='#e74c3c', linewidth=2.5)
ax.add_patch(challenges)
ax.text(7, 5, 'Key Challenges to Address', fontsize=11, ha='center', fontweight='bold')

challenge_text = [
    '• Dataset limitations (temporal, geographic)',
    '• Adversarial evasion techniques',
    '• Fairness and bias mitigation',
    '• Real-world deployment scalability'
]

for i, text in enumerate(challenge_text):
    ax.text(1.5, 4.6 - i*0.3, text, fontsize=8, va='top')

# Success metrics
metrics = Rectangle((1, 1.2), 12, 1.8, facecolor='#e6f7ff', edgecolor='#3498db', linewidth=2.5)
ax.add_patch(metrics)
ax.text(7, 2.7, 'Success Metrics', fontsize=11, ha='center', fontweight='bold')

metric_text = [
    '• >90% F1-Score on diverse datasets',
    '• <3% False Positive Rate',
    '• Real-time processing (<100ms per posting)',
    '• Deployment on 3+ major job platforms'
]

for i, text in enumerate(metric_text):
    ax.text(1.5, 2.3 - i*0.3, text, fontsize=8, va='top')

plt.tight_layout()
plt.savefig('figures/research_roadmap.png', dpi=300, bbox_inches='tight', facecolor='white')
plt.close()
print("✓ Generated")

# ============================================================================
# FIGURE: Impact Summary (Chapter 7)
# ============================================================================
print("Generating Chapter 7 Figure: Research Impact...")

fig, ax = plt.subplots(figsize=(13, 9))
ax.set_xlim(0, 13)
ax.set_ylim(0, 10)
ax.axis('off')

ax.text(6.5, 9.5, 'HireSafe Research Contributions and Impact', 
        fontsize=15, fontweight='bold', ha='center')

# Four quadrants
quadrants = [
    ('Technical\nContributions', 1, 6, 5, 2.8, '#3498db'),
    ('Methodological\nInsights', 7.5, 6, 5, 2.8, '#e74c3c'),
    ('Practical\nApplications', 1, 2.5, 5, 2.8, '#27ae60'),
    ('Future\nDirections', 7.5, 2.5, 5, 2.8, '#f39c12')
]

for title, x, y, w, h, color in quadrants:
    box = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.1",
                         edgecolor=color, facecolor=color, alpha=0.2, linewidth=3)
    ax.add_patch(box)
    ax.text(x + w/2, y + h - 0.3, title, fontsize=11, fontweight='bold', ha='center')

# Technical contributions
tech_items = [
    '• 5-signal detection framework',
    '• 97.1% accuracy XGBoost model',
    '• End-to-end web application',
    '• Comprehensive evaluation'
]
for i, item in enumerate(tech_items):
    ax.text(1.3, 7.8 - i*0.4, item, fontsize=8)

# Methodological insights
method_items = [
    '• Domain + ML hybrid approach',
    '• Class imbalance techniques',
    '• Interpretability-performance balance',
    '• Computational efficiency focus'
]
for i, item in enumerate(method_items):
    ax.text(7.8, 7.8 - i*0.4, item, fontsize=8)

# Practical applications
practical_items = [
    '• Job seeker fraud protection',
    '• Platform moderation assistance',
    '• Real-time deployment ready',
    '• Open-source availability'
]
for i, item in enumerate(practical_items):
    ax.text(1.3, 4.3 - i*0.4, item, fontsize=8)

# Future directions
future_items = [
    '• Advanced NLP integration',
    '• Adversarial robustness',
    '• Multi-modal analysis',
    '• Ecosystem collaboration'
]
for i, item in enumerate(future_items):
    ax.text(7.8, 4.3 - i*0.4, item, fontsize=8)

# Central achievement
achievement = plt.Circle((6.5, 5.5), 1.2, facecolor='#fff3cd', edgecolor='#f39c12', linewidth=3)
ax.add_patch(achievement)
ax.text(6.5, 5.8, '86.4%', fontsize=20, ha='center', fontweight='bold', color='#f39c12')
ax.text(6.5, 5.2, 'F1-Score', fontsize=11, ha='center', fontweight='bold')

# Bottom banner
banner = Rectangle((1, 0.3), 11, 1.5, facecolor='#f0f0f0', edgecolor='#2c3e50', linewidth=2)
ax.add_patch(banner)
ax.text(6.5, 1.4, 'Validated Solution for Real-World Recruitment Fraud Detection', 
        fontsize=10, ha='center', fontweight='bold')
ax.text(6.5, 0.9, 'Combining Domain Expertise with Machine Learning', 
        fontsize=9, ha='center', style='italic')
ax.text(6.5, 0.5, 'Accessible • Effective • Deployable', 
        fontsize=9, ha='center', color='#27ae60', fontweight='bold')

plt.tight_layout()
plt.savefig('figures/research_impact.png', dpi=300, bbox_inches='tight', facecolor='white')
plt.close()
print("✓ Generated")

print("\n" + "="*60)
print("CHAPTER 6 & 7 FIGURES GENERATED!")
print("="*60)
print("\nFiles created:")
print("1. research_roadmap.png (Chapter 6)")
print("2. research_impact.png (Chapter 7)")