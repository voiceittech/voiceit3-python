from voiceit2 import *
import unittest
import os
import urllib

class TestVoiceIt2(unittest.TestCase):
    def setUp(self):
        urllib.request.urlretrieve('https://s3.amazonaws.com/voiceit-api2-testing-files/test-data/videoEnrollmentArmaan1.mov', 'videoEnrollmentArmaan1.mov')
        urllib.request.urlretrieve('https://s3.amazonaws.com/voiceit-api2-testing-files/test-data/videoEnrollmentArmaan2.mov', 'videoEnrollmentArmaan2.mov')
        urllib.request.urlretrieve('https://s3.amazonaws.com/voiceit-api2-testing-files/test-data/videoEnrollmentArmaan3.mov', 'videoEnrollmentArmaan3.mov')
        urllib.request.urlretrieve('https://s3.amazonaws.com/voiceit-api2-testing-files/test-data/videoVerificationArmaan1.mov', 'videoVerificationArmaan1.mov')
        urllib.request.urlretrieve('https://s3.amazonaws.com/voiceit-api2-testing-files/test-data/videoEnrollmentStephen1.mov', 'videoEnrollmentStephen1.mov')
        urllib.request.urlretrieve('https://s3.amazonaws.com/voiceit-api2-testing-files/test-data/videoEnrollmentStephen2.mov', 'videoEnrollmentStephen2.mov')
        urllib.request.urlretrieve('https://s3.amazonaws.com/voiceit-api2-testing-files/test-data/videoEnrollmentStephen3.mov', 'videoEnrollmentStephen3.mov')
        urllib.request.urlretrieve('https://s3.amazonaws.com/voiceit-api2-testing-files/test-data/enrollmentArmaan1.wav', 'enrollmentArmaan1.wav')
        urllib.request.urlretrieve('https://s3.amazonaws.com/voiceit-api2-testing-files/test-data/enrollmentArmaan2.wav', 'enrollmentArmaan2.wav')
        urllib.request.urlretrieve('https://s3.amazonaws.com/voiceit-api2-testing-files/test-data/enrollmentArmaan3.wav', 'enrollmentArmaan3.wav')
        urllib.request.urlretrieve('https://s3.amazonaws.com/voiceit-api2-testing-files/test-data/verificationArmaan1.wav', 'verificationArmaan1.wav')
        urllib.request.urlretrieve('https://s3.amazonaws.com/voiceit-api2-testing-files/test-data/enrollmentStephen1.wav', 'enrollmentStephen1.wav')
        urllib.request.urlretrieve('https://s3.amazonaws.com/voiceit-api2-testing-files/test-data/enrollmentStephen2.wav', 'enrollmentStephen2.wav')
        urllib.request.urlretrieve('https://s3.amazonaws.com/voiceit-api2-testing-files/test-data/enrollmentStephen3.wav', 'enrollmentStephen3.wav')
        urllib.request.urlretrieve('https://s3.amazonaws.com/voiceit-api2-testing-files/test-data/faceEnrollmentArmaan1.mp4', 'faceEnrollmentArmaan1.mp4')
        urllib.request.urlretrieve('https://s3.amazonaws.com/voiceit-api2-testing-files/test-data/faceEnrollmentArmaan2.mp4', 'faceEnrollmentArmaan2.mp4')
        urllib.request.urlretrieve('https://s3.amazonaws.com/voiceit-api2-testing-files/test-data/faceEnrollmentArmaan3.mp4', 'faceEnrollmentArmaan3.mp4')
        urllib.request.urlretrieve('https://s3.amazonaws.com/voiceit-api2-testing-files/test-data/faceVerificationArmaan1.mp4', 'faceVerificationArmaan1.mp4')


    def tearDown(self):
        os.remove('./videoEnrollmentArmaan1.mov')
        os.remove('./videoEnrollmentArmaan2.mov')
        os.remove('./videoEnrollmentArmaan3.mov')
        os.remove('./videoVerificationArmaan1.mov')
        os.remove('./videoEnrollmentStephen1.mov')
        os.remove('./videoEnrollmentStephen2.mov')
        os.remove('./videoEnrollmentStephen3.mov')
        os.remove('./enrollmentArmaan1.wav')
        os.remove('./enrollmentArmaan2.wav')
        os.remove('./enrollmentArmaan3.wav')
        os.remove('./verificationArmaan1.wav')
        os.remove('./enrollmentStephen1.wav')
        os.remove('./enrollmentStephen2.wav')
        os.remove('./enrollmentStephen3.wav')

    def test_key_token(self): # Check if api key and token can be found in the environment variables
        vikey = os.environ['VIAPIKEY']
        vitoken = os.environ['VIAPITOKEN']
        self.assertNotEqual(vikey, '')
        self.assertNotEqual(vitoken, '')

    def test_basics(self): # Get all users, Get all groups, Add User to Group, Remove User from Group, Delete User, Delete Group
        vikey = os.environ['VIAPIKEY']
        vitoken = os.environ['VIAPITOKEN']
        my_voiceit = VoiceIt2(vikey, vitoken)
        ret = my_voiceit.create_user()
        self.assertEqual(201, ret['status'])
        self.assertEqual('SUCC', ret['responseCode'])
        user_id1 = ret['userId']
        ret = my_voiceit.create_user()
        user_id2 = ret['userId']
        ret = my_voiceit.create_user()
        user_id3 = ret['userId']
        ret = my_voiceit.create_group('Sample Group Description')
        self.assertEqual(201, ret['status'])
        self.assertEqual('SUCC', ret['responseCode'])
        group_id = ret['groupId']
        ret = my_voiceit.add_user_to_group(group_id, user_id1)
        self.assertEqual(200, ret['status'])
        self.assertEqual('SUCC', ret['responseCode'])
        ret = my_voiceit.add_user_to_group(group_id, user_id2)
        self.assertEqual(200, ret['status'])
        self.assertEqual('SUCC', ret['responseCode'])
        ret = my_voiceit.add_user_to_group(group_id, user_id3)
        self.assertEqual(200, ret['status'])
        self.assertEqual('SUCC', ret['responseCode'])
        self.assertEqual(1, len(my_voiceit.get_groups_for_user(user_id1)['groups']))
        self.assertEqual(1, len(my_voiceit.get_groups_for_user(user_id2)['groups']))
        self.assertEqual(1, len(my_voiceit.get_groups_for_user(user_id3)['groups']))
        self.assertEqual(group_id, my_voiceit.get_groups_for_user(user_id1)['groups'][0])
        self.assertEqual(group_id, my_voiceit.get_groups_for_user(user_id2)['groups'][0])
        self.assertEqual(group_id, my_voiceit.get_groups_for_user(user_id3)['groups'][0])
        ret = my_voiceit.remove_user_from_group(group_id, user_id1)
        self.assertEqual(200, ret['status'])
        self.assertEqual('SUCC', ret['responseCode'])
        ret = my_voiceit.remove_user_from_group(group_id, user_id2)
        self.assertEqual(200, ret['status'])
        self.assertEqual('SUCC', ret['responseCode'])
        ret = my_voiceit.remove_user_from_group(group_id, user_id3)
        self.assertEqual(200, ret['status'])
        self.assertEqual('SUCC', ret['responseCode'])
        ret = my_voiceit.delete_group(group_id)
        self.assertEqual(200, ret['status'])
        self.assertEqual('SUCC', ret['responseCode'])
        ret = my_voiceit.delete_user(user_id1)
        self.assertEqual(200, ret['status'])
        self.assertEqual('SUCC', ret['responseCode'])
        ret = my_voiceit.delete_user(user_id2)
        self.assertEqual(200, ret['status'])
        self.assertEqual('SUCC', ret['responseCode'])
        ret = my_voiceit.delete_user(user_id3)
        self.assertEqual(200, ret['status'])
        self.assertEqual('SUCC', ret['responseCode'])

    def test_video(self): # Create video enrollment, verify, identify (repeat for by URL)
        #  Create users, groups, and add users to group
        vikey = os.environ['VIAPIKEY']
        vitoken = os.environ['VIAPITOKEN']
        my_voiceit = VoiceIt2(vikey, vitoken)
        ret = my_voiceit.create_user()
        user_id1 = my_voiceit.create_user()['userId']
        user_id2 = my_voiceit.create_user()['userId']
        group_id = my_voiceit.create_group('Sample Group Description')['groupId']
        my_voiceit.add_user_to_group(group_id, user_id1)
        my_voiceit.add_user_to_group(group_id, user_id2)
        
        #  Check video enrollments
        ret = my_voiceit.create_video_enrollment(user_id1, 'en-US', './videoEnrollmentArmaan1.mov')
        self.assertEqual(201, ret['status'])
        self.assertEqual('SUCC', ret['responseCode'])
        enrollment1 = ret['id']
        ret = my_voiceit.create_video_enrollment(user_id1, 'en-US', './videoEnrollmentArmaan2.mov')
        self.assertEqual(201, ret['status'])
        self.assertEqual('SUCC', ret['responseCode'])
        enrollment2 = ret['id']
        ret = my_voiceit.create_video_enrollment(user_id1, 'en-US', './videoEnrollmentArmaan3.mov')
        self.assertEqual(201, ret['status'])
        self.assertEqual('SUCC', ret['responseCode'])
        enrollment3 = ret['id']
        ret = my_voiceit.create_video_enrollment(user_id2, 'en-US', './videoEnrollmentStephen1.mov')
        self.assertEqual(201, ret['status'])
        self.assertEqual('SUCC', ret['responseCode'])
        ret = my_voiceit.create_video_enrollment(user_id2, 'en-US', './videoEnrollmentStephen2.mov')
        self.assertEqual(201, ret['status'])
        self.assertEqual('SUCC', ret['responseCode'])
        ret = my_voiceit.create_video_enrollment(user_id2, 'en-US', './videoEnrollmentStephen3.mov')
        self.assertEqual(201, ret['status'])
        self.assertEqual('SUCC', ret['responseCode'])

        #  Verification
        ret = my_voiceit.video_verification(user_id1, 'en-US', './videoVerificationArmaan1.mov')
        self.assertEqual(200, ret['status'])
        self.assertEqual('SUCC', ret['responseCode'])

        #  Identification
        ret = my_voiceit.video_identification(group_id, 'en-US', './videoVerificationArmaan1.mov')
        self.assertEqual(200, ret['status'])
        self.assertEqual('SUCC', ret['responseCode'])
        self.assertEqual(user_id1, ret['userId'])

        #  Delete enrollment
        ret = my_voiceit.delete_enrollment_for_user(user_id1, enrollment1)
        self.assertEqual(200, ret['status'])
        self.assertEqual('SUCC', ret['responseCode'])
        ret = my_voiceit.delete_enrollment_for_user(user_id1, enrollment2)
        self.assertEqual(200, ret['status'])
        self.assertEqual('SUCC', ret['responseCode'])
        ret = my_voiceit.delete_enrollment_for_user(user_id1, enrollment3)
        self.assertEqual(200, ret['status'])
        self.assertEqual('SUCC', ret['responseCode'])
        my_voiceit.delete_all_enrollments_for_user(user_id2)

        #  Check video enrollments by URL
        ret = my_voiceit.create_video_enrollment_by_url(user_id1, 'en-US', 'https://s3.amazonaws.com/voiceit-api2-testing-files/test-data/videoEnrollmentArmaan1.mov')
        self.assertEqual(201, ret['status'])
        self.assertEqual('SUCC', ret['responseCode'])
        ret = my_voiceit.create_video_enrollment_by_url(user_id1, 'en-US', 'https://s3.amazonaws.com/voiceit-api2-testing-files/test-data/videoEnrollmentArmaan2.mov')
        self.assertEqual(201, ret['status'])
        self.assertEqual('SUCC', ret['responseCode'])
        ret = my_voiceit.create_video_enrollment_by_url(user_id1, 'en-US', 'https://s3.amazonaws.com/voiceit-api2-testing-files/test-data/videoEnrollmentArmaan3.mov')
        self.assertEqual(201, ret['status'])
        self.assertEqual('SUCC', ret['responseCode'])
        ret = my_voiceit.create_video_enrollment_by_url(user_id2, 'en-US', 'https://s3.amazonaws.com/voiceit-api2-testing-files/test-data/videoEnrollmentStephen1.mov')
        self.assertEqual(201, ret['status'])
        self.assertEqual('SUCC', ret['responseCode'])
        ret = my_voiceit.create_video_enrollment_by_url(user_id2, 'en-US', 'https://s3.amazonaws.com/voiceit-api2-testing-files/test-data/videoEnrollmentStephen2.mov')
        self.assertEqual(201, ret['status'])
        self.assertEqual('SUCC', ret['responseCode'])
        ret = my_voiceit.create_video_enrollment_by_url(user_id2, 'en-US', 'https://s3.amazonaws.com/voiceit-api2-testing-files/test-data/videoEnrollmentStephen3.mov')
        self.assertEqual(201, ret['status'])
        self.assertEqual('SUCC', ret['responseCode'])

        #  Verification by URL
        ret = my_voiceit.video_verification_by_url(user_id1, 'en-US', 'https://s3.amazonaws.com/voiceit-api2-testing-files/test-data/videoVerificationArmaan1.mov')
        self.assertEqual(200, ret['status'])
        self.assertEqual('SUCC', ret['responseCode'])

        #  Identification by URL
        ret = my_voiceit.video_identification_by_url(group_id, 'en-US', 'https://s3.amazonaws.com/voiceit-api2-testing-files/test-data/videoVerificationArmaan1.mov')
        self.assertEqual(200, ret['status'])
        self.assertEqual('SUCC', ret['responseCode'])
        self.assertEqual(user_id1, ret['userId'])


        my_voiceit.delete_all_enrollments_for_user(user_id1)
        my_voiceit.delete_all_enrollments_for_user(user_id2)
        my_voiceit.delete_group(group_id)
        my_voiceit.delete_user(user_id1)
        my_voiceit.delete_user(user_id2)

        


    def test_voice(self): # Create voice enrollment, verify, identify (repeat for by URL)
        vikey = os.environ['VIAPIKEY']
        vitoken = os.environ['VIAPITOKEN']
        my_voiceit = VoiceIt2(vikey, vitoken)
        #  Create users and groups
        ret = my_voiceit.create_user()
        self.assertEqual(201, ret['status'])
        self.assertEqual('SUCC', ret['responseCode'])
        user_id1 = ret['userId']
        ret = my_voiceit.create_user()
        self.assertEqual(201, ret['status'])
        self.assertEqual('SUCC', ret['responseCode'])
        user_id2 = ret['userId']
        ret = my_voiceit.create_group('Sample Group Description')
        self.assertEqual(201, ret['status'])
        self.assertEqual('SUCC', ret['responseCode'])
        group_id = ret['groupId']

        #  Test Voice Enrollments
        ret = my_voiceit.create_voice_enrollment(user_id1, 'en-US', './enrollmentArmaan1.wav')
        self.assertEqual(201, ret['status'])
        self.assertEqual('SUCC', ret['responseCode'])
        enrollment1 = ret['id']
        ret = my_voiceit.create_voice_enrollment(user_id1, 'en-US', './enrollmentArmaan2.wav')
        self.assertEqual(201, ret['status'])
        self.assertEqual('SUCC', ret['responseCode'])
        enrollment2 = ret['id']
        ret = my_voiceit.create_voice_enrollment(user_id1, 'en-US', './enrollmentArmaan3.wav')
        self.assertEqual(201, ret['status'])
        self.assertEqual('SUCC', ret['responseCode'])
        enrollment3 = ret['id']
        ret = my_voiceit.create_voice_enrollment(user_id2, 'en-US', './videoEnrollmentStephen1.mov')
        self.assertEqual(201, ret['status'])
        self.assertEqual('SUCC', ret['responseCode'])
        ret = my_voiceit.create_voice_enrollment(user_id2, 'en-US', './videoEnrollmentStephen2.mov')
        self.assertEqual(201, ret['status'])
        self.assertEqual('SUCC', ret['responseCode'])
        ret = my_voiceit.create_voice_enrollment(user_id2, 'en-US', './videoEnrollmentStephen3.mov')
        self.assertEqual(201, ret['status'])
        self.assertEqual('SUCC', ret['responseCode'])

        my_voiceit.add_user_to_group(group_id, user_id1)
        my_voiceit.add_user_to_group(group_id, user_id2)
        
        #  Test Voice Verification
        ret = my_voiceit.voice_verification(user_id1, 'en-US', './verificationArmaan1.wav')
        self.assertEqual(200, ret['status'])
        self.assertEqual('SUCC', ret['responseCode'])
        
        #  Test Voice Identification
        ret = my_voiceit.voice_identification(group_id, 'en-US', './verificationArmaan1.wav')
        self.assertEqual(200, ret['status'])
        self.assertEqual('SUCC', ret['responseCode'])
        self.assertEqual(user_id1, ret['userId'])

        #  Delete enrollment
        ret = my_voiceit.delete_enrollment_for_user(user_id1, enrollment1)
        self.assertEqual(200, ret['status'])
        self.assertEqual('SUCC', ret['responseCode'])
        ret = my_voiceit.delete_enrollment_for_user(user_id1, enrollment2)
        self.assertEqual(200, ret['status'])
        self.assertEqual('SUCC', ret['responseCode'])
        ret = my_voiceit.delete_enrollment_for_user(user_id1, enrollment3)
        self.assertEqual(200, ret['status'])
        self.assertEqual('SUCC', ret['responseCode'])
        my_voiceit.delete_all_enrollments_for_user(user_id2)


        #  Test Voice Enrollments by URL
        ret = my_voiceit.create_voice_enrollment_by_url(user_id1, 'en-US', 'https://s3.amazonaws.com/voiceit-api2-testing-files/test-data/enrollmentArmaan1.wav')
        self.assertEqual(201, ret['status'])
        self.assertEqual('SUCC', ret['responseCode'])
        ret = my_voiceit.create_voice_enrollment_by_url(user_id1, 'en-US', 'https://s3.amazonaws.com/voiceit-api2-testing-files/test-data/enrollmentArmaan2.wav')
        self.assertEqual(201, ret['status'])
        self.assertEqual('SUCC', ret['responseCode'])
        ret = my_voiceit.create_voice_enrollment_by_url(user_id1, 'en-US', 'https://s3.amazonaws.com/voiceit-api2-testing-files/test-data/enrollmentArmaan3.wav')
        self.assertEqual(201, ret['status'])
        self.assertEqual('SUCC', ret['responseCode'])
        ret = my_voiceit.create_voice_enrollment_by_url(user_id2, 'en-US', 'https://s3.amazonaws.com/voiceit-api2-testing-files/test-data/enrollmentStephen1.wav')
        self.assertEqual(201, ret['status'])
        self.assertEqual('SUCC', ret['responseCode'])
        ret = my_voiceit.create_voice_enrollment_by_url(user_id2, 'en-US', 'https://s3.amazonaws.com/voiceit-api2-testing-files/test-data/enrollmentStephen2.wav')
        self.assertEqual(201, ret['status'])
        self.assertEqual('SUCC', ret['responseCode'])
        ret = my_voiceit.create_voice_enrollment_by_url(user_id2, 'en-US', 'https://s3.amazonaws.com/voiceit-api2-testing-files/test-data/enrollmentStephen3.wav')
        self.assertEqual(201, ret['status'])
        self.assertEqual('SUCC', ret['responseCode'])
        
        #  Test Voice Verification by URL
        ret = my_voiceit.voice_verification_by_url(user_id1, 'en-US', 'https://s3.amazonaws.com/voiceit-api2-testing-files/test-data/verificationArmaan1.wav')
        self.assertEqual(200, ret['status'])
        self.assertEqual('SUCC', ret['responseCode'])
        
        #  Test Voice Identification by URL
        ret = my_voiceit.voice_identification_by_url(group_id, 'en-US', 'https://s3.amazonaws.com/voiceit-api2-testing-files/test-data/verificationArmaan1.wav')
        self.assertEqual(200, ret['status'])
        self.assertEqual('SUCC', ret['responseCode'])
        self.assertEqual(user_id1, ret['userId'])

        my_voiceit.delete_all_enrollments_for_user(user_id1)
        my_voiceit.delete_all_enrollments_for_user(user_id2)
        my_voiceit.delete_user(user_id1)
        my_voiceit.delete_user(user_id2)
        my_voiceit.delete_group(group_id)

    def face(self): # Create face enrollment, verify, identify
        vikey = os.environ['VIAPIKEY']
        vitoken = os.environ['VIAPITOKEN']
        my_voiceit = VoiceIt2(vikey, vitoken)

        #  Create users and groups
        ret = my_voiceit.create_user('Sample Group Description')
        self.assertEqual(201, ret['status'])
        self.assertEqual('SUCC', ret['responseCode'])
        user_id = ret['userId']

        #  Test Face Enrollments
        ret = my_voiceit.create_face_enrollment(user_id, './https://s3.amazonaws.com/voiceit-api2-testing-files/test-data/faceEnrollmentArmaan1.mp4')
        self.assertEqual(201, ret['status'])
        self.assertEqual('SUCC', ret['responseCode'])
        faceId1 = ret['faceEnrollmentId']
        ret = my_voiceit.create_face_enrollment(user_id, 'https://s3.amazonaws.com/voiceit-api2-testing-files/test-data/faceEnrollmentArmaan2.mp4')
        self.assertEqual(201, ret['status'])
        self.assertEqual('SUCC', ret['responseCode'])
        faceId2 = ret['faceEnrollmentId']
        ret = my_voiceit.create_face_enrollment(user_id, 'https://s3.amazonaws.com/voiceit-api2-testing-files/test-data/faceEnrollmentArmaan3.mp4')
        self.assertEqual(201, ret['status'])
        self.assertEqual('SUCC', ret['responseCode'])
        faceId3 = ret['faceEnrollmentId']

        #  Test Face Verification
        ret = my_voiceit.face_verification(user_id, 'https://s3.amazonaws.com/voiceit-api2-testing-files/test-data/faceVerificationArmaan1.mp4')
        self.assertEqual(200, ret['status'])
        self.assertEqual('SUCC', ret['responseCode'])

        #  Test delete enrollments
        ret = my_voiceit.delete_face_enrollment(user_id, faceId1)
        self.assertEqual(200, ret['status'])
        self.assertEqual('SUCC', ret['responseCode'])
        ret = my_voiceit.delete_face_enrollment(user_id, faceId2)
        self.assertEqual(200, ret['status'])
        self.assertEqual('SUCC', ret['responseCode'])
        ret = my_voiceit.delete_face_enrollment(user_id, faceId3)
        self.assertEqual(200, ret['status'])
        self.assertEqual('SUCC', ret['responseCode'])

        os.remove('./faceEnrollmentArmaan1.mp4')
        os.remove('./faceEnrollmentArmaan2.mp4')
        os.remove('./faceEnrollmentArmaan3.mp4')
        os.remove('./faceVerificationArmaan1.mp4')
        my_voiceit.delete_user(user_id)
        my_voiceit.delete_group(group_id)

if __name__ == '__main__':
    unittest.main()
