#!/usr/bin/env python3
"""Full API test: create user, video enroll x3, video verify, cleanup"""
import os, sys
from voiceit3 import VoiceIt3

api_key = os.environ.get("VOICEIT_API_KEY", "")
api_token = os.environ.get("VOICEIT_API_TOKEN", "")
if not api_key or not api_token:
    print("Set VOICEIT_API_KEY and VOICEIT_API_TOKEN"); sys.exit(1)

vi = VoiceIt3(api_key, api_token)
phrase = "Never forget tomorrow is a new day"
td = "test-data"
errors = 0

def check(step, r, expected="SUCC"):
    global errors
    code = r.get("responseCode", "?")
    ok = code == expected
    print(f"{'PASS' if ok else 'FAIL'}: {step} ({code})")
    if not ok: errors += 1
    return r

# 1. Create user
r = check("CreateUser", vi.create_user())
user_id = r.get("userId", "")

# 2. Video enrollment x3
for i in range(1, 4):
    check(f"VideoEnrollment{i}", vi.create_video_enrollment(user_id, "en-US", phrase, f"{td}/videoEnrollmentA{i}.mov"))

# 3. Video verification (tests both voice + face)
r = check("VideoVerification", vi.video_verification(user_id, "en-US", phrase, f"{td}/videoVerificationA1.mov"))
print(f"  Voice confidence: {r.get('voiceConfidence', 0)}, Face confidence: {r.get('faceConfidence', 0)}")

# 4. Cleanup
check("DeleteEnrollments", vi.delete_all_enrollments(user_id))
check("DeleteUser", vi.delete_user(user_id))

if errors > 0:
    print(f"\n{errors} FAILURES"); sys.exit(1)
print("\nAll tests passed!")
