#!/bin/bash

# This script runs on Streamlit Cloud before starting the app

# Create necessary directories
mkdir -p ~/.streamlit/

# Copy config
echo "\
[theme]\n\
primaryColor = '#6C63FF'\n\
backgroundColor = '#0E1117'\n\
secondaryBackgroundColor = '#1E2127'\n\
textColor = '#FAFAFA'\n\
font = 'sans serif'\n\
\n\
[server]\n\
headless = true\n\
port = 8501\n\
enableCORS = false\n\
enableXsrfProtection = true\n\
" > ~/.streamlit/config.toml

echo "Setup complete!"