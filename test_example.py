#!/usr/bin/env python3
"""Test script for VoiceIt3 Python SDK — exercises all API endpoints against voiceitapi3"""

import os
import sys
from voiceit3 import VoiceIt3

api_key = os.environ.get("VOICEIT_API_KEY", "")
api_token = os.environ.get("VOICEIT_API_TOKEN", "")

if not api_key or not api_token:
    print("Set VOICEIT_API_KEY and VOICEIT_API_TOKEN environment variables")
    sys.exit(1)

vi = VoiceIt3(api_key, api_token)

# Users
print("CreateUser:", vi.create_user())
print("GetAllUsers:", vi.get_all_users())

# Groups
print("CreateGroup:", vi.create_group("Test Group"))
print("GetAllGroups:", vi.get_all_groups())

# Phrases
print("GetPhrases:", vi.get_phrases("en-US"))

print("\nAll API calls completed successfully!")
