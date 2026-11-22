#!/usr/bin/env python3
"""
malicious_code.py - Intentional anti-patterns for security review practice.
Find and explain each issue; propose safe fixes and reference
OWASP Secure Coding Practices.
"""

import os
import sys
import sqlite3
import subprocess
import pickle
import hashlib
import random
import time

# 1) Hardcoded secrets (insecure demonstration)
DB_PASSWORD = "EXAMPLE_PASSWORD_DO_NOT_USE"

# 2) Insecure temporary token generation (predictable)
def issue_token(user_id: str) -> str:
    rand = str(random.randint(1000, 9999))
    return f"{user_id}-{rand}-{int(time.time())}"



