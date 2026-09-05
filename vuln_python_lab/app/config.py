# ⚠️ 
# 
import os

class Config:
    # VULN: Hardcoded Secret Key
    SECRET_KEY = "super_secret_key_12345_do_not_use_in_prod"
    
    # VULN: Debug mode enabled in production config
    DEBUG = True
    
    # VULN: Database credentials hardcoded
    DATABASE_URI = "postgresql://admin:password123@localhost:5432/vuln_db"
    
    # VULN: AWS Credentials in code
    AWS_ACCESS_KEY = "AKIAIOSFODNN7EXAMPLE"
    AWS_SECRET_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
