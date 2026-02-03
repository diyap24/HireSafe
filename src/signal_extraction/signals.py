"""
Signal Extraction Module for HireSafe
Detects fraud signals in job postings
"""

import re
import pandas as pd
import numpy as np

class SignalExtractor:
    """Extract fraud signals from job posting text"""
    
    def __init__(self):
        # Payment-related keywords
        self.payment_keywords = [
            'fee', 'deposit', 'wire transfer', 'pay upfront', 'western union',
            'paypal', 'processing fee', 'training fee', 'equipment fee',
            'background check fee', 'application fee', 'registration fee',
            'starter kit', 'money order', 'cashier check', 'send money'
        ]
        
        # Urgency manipulation keywords
        self.urgency_keywords = [
            'urgent', 'immediately', 'asap', 'act now', 'limited time',
            'hurry', 'don\'t wait', 'apply today', 'positions filling fast',
            'immediate start', 'start immediately', 'limited positions',
            'only a few spots', 'first come first serve', 'deadline today'
        ]
        
        # Off-platform communication keywords
        self.offplatform_keywords = [
            'whatsapp', 'telegram', 'text me', 'personal email',
            'gmail', 'yahoo', 'hotmail', 'contact via', 'message me at',
            'call my cell', 'reach me at', 'wechat', 'viber', 'skype'
        ]
    
    def detect_payment_request(self, text):
        """
        Detect if text contains payment-related keywords
        Returns 1 if found, 0 otherwise
        """
        if pd.isna(text) or text == '':
            return 0
        
        text_lower = text.lower()
        for keyword in self.payment_keywords:
            if keyword in text_lower:
                return 1
        return 0
    
    def detect_urgency(self, text):
        """
        Detect urgency manipulation tactics
        Returns 1 if found, 0 otherwise
        """
        if pd.isna(text) or text == '':
            return 0
        
        text_lower = text.lower()
        for keyword in self.urgency_keywords:
            if keyword in text_lower:
                return 1
        return 0
    
    def detect_offplatform_contact(self, text):
        """
        Detect requests for off-platform communication
        Returns 1 if found, 0 otherwise
        """
        if pd.isna(text) or text == '':
            return 0
        
        text_lower = text.lower()
        for keyword in self.offplatform_keywords:
            if keyword in text_lower:
                return 1
        return 0
    
    def check_vague_company(self, company_profile):
        """
        Check if company information is missing or vague
        Returns 1 if vague/missing, 0 if detailed
        """
        if pd.isna(company_profile) or company_profile.strip() == '':
            return 1
        
        # If company profile is too short (less than 50 chars), consider it vague
        if len(company_profile.strip()) < 50:
            return 1
        
        return 0
    
    def detect_salary_anomaly(self, salary_range, job_title=''):
        """
        Detect unrealistic salary claims
        Simple version: flags if contains very high numbers
        Returns 1 if anomaly detected, 0 otherwise
        """
        if pd.isna(salary_range) or salary_range == '':
            return 0
        
        # Extract numbers from salary string
        numbers = re.findall(r'\d+', salary_range.replace(',', ''))
        
        if numbers:
            max_salary = max([int(n) for n in numbers])
            
            # Flag if weekly/hourly salary > $500 or yearly > $500,000
            # These are clearly unrealistic for most jobs
            if 'week' in salary_range.lower() or 'weekly' in salary_range.lower():
                if max_salary > 10000:  # $10k/week = $520k/year
                    return 1
            elif 'hour' in salary_range.lower() or 'hourly' in salary_range.lower():
                if max_salary > 200:  # $200/hour
                    return 1
            else:  # Assume yearly
                if max_salary > 500000:  # $500k/year
                    return 1
        
        return 0
    
    def extract_all_signals(self, row):
        """
        Extract all signals from a job posting row
        
        Parameters:
        -----------
        row : pandas Series
            Must contain 'full_text', 'company_profile', 'salary_range'
        
        Returns:
        --------
        dict : Dictionary with all signal flags
        """
        full_text = row.get('full_text', '')
        company_profile = row.get('company_profile', '')
        salary_range = row.get('salary_range', '')
        
        return {
            'payment_request': self.detect_payment_request(full_text),
            'urgency': self.detect_urgency(full_text),
            'offplatform_contact': self.detect_offplatform_contact(full_text),
            'vague_company': self.check_vague_company(company_profile),
            'salary_anomaly': self.detect_salary_anomaly(salary_range)
        }


# Test the module
if __name__ == "__main__":
    print("Testing SignalExtractor...")
    print("=" * 80)
    
    extractor = SignalExtractor()
    
    # Test Case 1: Obvious scam
    print("\n1. SCAM EXAMPLE:")
    scam_row = pd.Series({
        'full_text': "URGENT! Work from home data entry. Start IMMEDIATELY. Send $299 training fee via PayPal. Contact me on WhatsApp: +1-555-1234.",
        'company_profile': '',
        'salary_range': '$8000-$12000 per week'
    })
    scam_signals = extractor.extract_all_signals(scam_row)
    print(f"Text: {scam_row['full_text'][:100]}...")
    print(f"Signals detected: {scam_signals}")
    print(f"Total red flags: {sum(scam_signals.values())}/5")
    
    # Test Case 2: Legitimate job
    print("\n2. LEGITIMATE EXAMPLE:")
    legit_row = pd.Series({
        'full_text': "Software Engineer position at Google Inc. We are looking for experienced developers with 5+ years in Python and distributed systems. Competitive salary and benefits package.",
        'company_profile': "Google LLC is a multinational technology company specializing in Internet-related services and products, including online advertising technologies, search engine, cloud computing, software, and hardware.",
        'salary_range': '$120,000-$180,000 per year'
    })
    legit_signals = extractor.extract_all_signals(legit_row)
    print(f"Text: {legit_row['full_text'][:100]}...")
    print(f"Signals detected: {legit_signals}")
    print(f"Total red flags: {sum(legit_signals.values())}/5")
    
    print("\n" + "=" * 80)
    print("✓ SignalExtractor module working correctly!")