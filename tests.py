from voiceit2 import VoiceIt2
import os
import shutil
import unittest
import urllib

users_to_delete = []
groups_to_delete = []
VI_KEY = os.environ['VIAPIKEY']
VI_TOKEN = os.environ['VIAPITOKEN']
S3_URL = 'https://s3.amazonaws.com/voiceit-api2-testing-files/'
PHRASE = 'never forget tomorrow is a new day'
CONTENT_LANGUAGE = 'en-US'

def downloadS3File(fileName):
    urllib.request.urlretrieve(S3_URL + fileName, fileName)

class TestVoiceIt2(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('Started Downloading Test Files ...')
        os.mkdir('test-data')
        downloadS3File('test-data/enrollmentArmaanMyFaceAndVoice.m4a')
        downloadS3File('test-data/enrollmentNoel1.wav')
        downloadS3File('test-data/enrollmentNoel2.wav')
        downloadS3File('test-data/enrollmentNoel3.wav')
        downloadS3File('test-data/verificationNoel1.wav')
        downloadS3File('test-data/enrollmentStephen1.wav')
        downloadS3File('test-data/enrollmentStephen2.wav')
        downloadS3File('test-data/enrollmentStephen3.wav')
        downloadS3File('test-data/videoEnrollmentArmaan1.mov')
        downloadS3File('test-data/videoEnrollmentArmaan2.mov')
        downloadS3File('test-data/videoEnrollmentArmaan3.mov')
        downloadS3File('test-data/videoVerificationArmaan1.mov')
        downloadS3File('test-data/videoEnrollmentStephen1.mov')
        downloadS3File('test-data/videoEnrollmentStephen2.mov')
        downloadS3File('test-data/videoEnrollmentStephen3.mov')
        downloadS3File('test-data/faceEnrollmentArmaan1.mp4')
        downloadS3File('test-data/faceEnrollmentArmaan2.mp4')
        downloadS3File('test-data/faceEnrollmentArmaan3.mp4')
        downloadS3File('test-data/faceVerificationArmaan1.mp4')
        downloadS3File('test-data/faceVerificationStephen1.mp4')
        print('Done Downloading Test Files')

    # Method called once at the end of all tests
    @classmethod
    def tearDownClass(cls):
        global groups_to_delete,users_to_delete
        my_voiceit = VoiceIt2(VI_KEY, VI_TOKEN)
        for user_id in users_to_delete:
            my_voiceit.delete_user(user_id)
        for group_id in groups_to_delete:
            my_voiceit.delete_group(group_id)
        shutil.rmtree('test-data')

    # Check if api key and token can be found in the environment variables
    def test_webhooks(self):
        print('Testing Notification URL')
        my_voiceit = VoiceIt2(VI_KEY, VI_TOKEN)
        if os.environ['BOXFUSE_ENV'] == 'voiceittest':
            text_file = open(os.environ['HOME'] + '/platformVersion', "w")
            text_file.write(my_voiceit.version)
            text_file.close()
        my_voiceit.addNotificationUrl('https://voiceit.io')
        self.assertEqual(my_voiceit.notificationUrl, '?notificationURL=https%3A%2F%2Fvoiceit.io')
        my_voiceit.removeNotificationUrl()
        self.assertEqual(my_voiceit.notificationUrl, '')


    # Check if api key and token can be found in the environment variables
    def test_api_key_token(self):
        print('Testing Key/Token Environment Variables')
        self.assertNotEqual(VI_KEY, '')
        self.assertNotEqual(VI_TOKEN, '')

    def test_file_not_found(self):
        my_voiceit = VoiceIt2(VI_KEY, VI_TOKEN)
        print('Testing File Not Found')
        print('   Testing File Not Found Enrollment')
        try:
            my_voiceit.create_voice_enrollment('', CONTENT_LANGUAGE, PHRASE, 'test-data/nonexistent.wav')
            self.assertTrue(False)
        except IOError:
            self.assertTrue(True)

        try:
            my_voiceit.create_face_enrollment('', 'test-data/nonexistent.mov')
            self.assertTrue(False)
        except IOError:
            self.assertTrue(True)

        try:
            my_voiceit.create_video_enrollment('', CONTENT_LANGUAGE, PHRASE, 'test-data/nonexistent.mov')
            self.assertTrue(False)
        except IOError:
            self.assertTrue(True)

        print('   Testing File Not Found Verification')
        try:
            my_voiceit.voice_verification('', CONTENT_LANGUAGE, PHRASE, 'test-data/nonexistent.wav')
            self.assertTrue(False)
        except IOError:
            self.assertTrue(True)

        try:
            my_voiceit.face_verification('', 'test-data/nonexistent.mov')
            self.assertTrue(False)
        except IOError:
            self.assertTrue(True)

        try:
            my_voiceit.video_verification('', CONTENT_LANGUAGE, PHRASE, 'test-data/nonexistent.mov')
            self.assertTrue(False)
        except IOError:
            self.assertTrue(True)

        print('   Testing File Not Found Identification')
        try:
            my_voiceit.voice_identification('', CONTENT_LANGUAGE, PHRASE, 'test-data/nonexistent.wav')
            self.assertTrue(False)
        except IOError:
            self.assertTrue(True)

        try:
            my_voiceit.face_identification('', 'test-data/nonexistent.mov')
            self.assertTrue(False)
        except IOError:
            self.assertTrue(True)

        try:
            my_voiceit.video_identification('', CONTENT_LANGUAGE, PHRASE, 'test-data/nonexistent.mov')
            self.assertTrue(False)
        except IOError:
            self.assertTrue(True)

    def test_users(self):
        my_voiceit = VoiceIt2(VI_KEY, VI_TOKEN)
        global users_to_delete
        print('Testing User API Calls')

        print('   Testing Get All Users')
        ret = my_voiceit.get_all_users()
        self.assertEqual(200, ret['status'])
        self.assertEqual('SUCC', ret['responseCode'])
        self.assertGreaterEqual(len(ret['users']), 0)

        print('   Testing Create User')
        ret = my_voiceit.create_user()
        self.assertEqual(201, ret['status'])
        self.assertEqual('SUCC', ret['responseCode'])
        user_id = ret['userId']
        users_to_delete.append(user_id)

        print('   Testing Check User Exists')
        ret = my_voiceit.check_user_exists(user_id)
        self.assertEqual(200, ret['status'])
        self.assertEqual('SUCC', ret['responseCode'])

        print('   Testing Get Groups For User')
        ret = my_voiceit.get_groups_for_user(user_id)
        self.assertEqual(200, ret['status'])
        self.assertEqual('SUCC', ret['responseCode'])
        self.assertEqual(0, len(my_voiceit.get_groups_for_user(user_id)['groups']))

        print('   Testing Create User Token')
        ret = my_voiceit.create_user_token(user_id, 5)
        self.assertEqual(201, ret['status'])
        self.assertEqual('SUCC', ret['responseCode'])

        print('   Testing Delete User')
        ret = my_voiceit.delete_user(user_id)
        self.assertEqual(200, ret['status'])
        self.assertEqual('SUCC', ret['responseCode'])

    def test_phrases(self):
        my_voiceit = VoiceIt2(VI_KEY, VI_TOKEN)
        print('Testing Phrase API Calls')

        print('   Testing Get Phrases')
        ret = my_voiceit.get_phrases('en-US')
        self.assertEqual(200, ret['status'])
        self.assertEqual('SUCC', ret['responseCode'])
        self.assertGreaterEqual(len(ret['phrases']), 0)

    def test_groups(self):
        my_voiceit = VoiceIt2(VI_KEY, VI_TOKEN)
        global groups_to_delete,users_to_delete
        print('Test Group API Calls')

        print('   Test Create Group')
        ret = my_voiceit.create_group('Sample Group Description')
        self.assertEqual(201, ret['status'])
        self.assertEqual('SUCC', ret['responseCode'])
        group_id = ret['groupId']
        groups_to_delete.append(group_id)

        print('   Test Get Group')
        ret = my_voiceit.get_group(group_id)
        self.assertEqual(200, ret['status'])
        self.assertEqual('SUCC', ret['responseCode'])

        print('   Test Get All Groups')
        ret = my_voiceit.get_all_groups()
        self.assertEqual(200, ret['status'])
        self.assertEqual('SUCC', ret['responseCode'])
        self.assertGreaterEqual(len(ret['groups']), 0)

        print('   Test Group Exists')
        ret = my_voiceit.group_exists(group_id)
        self.assertEqual(200, ret['status'])
        self.assertEqual('SUCC', ret['responseCode'])
        self.assertEqual(True, ret['exists'])

        user_id = my_voiceit.create_user()['userId']
        users_to_delete.append(user_id)

        print('   Test Add User to Group')
        ret = my_voiceit.add_user_to_group(group_id, user_id)
        self.assertEqual(200, ret['status'])
        self.assertEqual('SUCC', ret['responseCode'])

        print('   Test Remove User from Group')
        ret = my_voiceit.remove_user_from_group(group_id, user_id)
        self.assertEqual(200, ret['status'])
        self.assertEqual('SUCC', ret['responseCode'])

        print('   Test Delete Group')
        ret = my_voiceit.delete_group(group_id)
        self.assertEqual(200, ret['status'])
        self.assertEqual('SUCC', ret['responseCode'])

    def test_enrollments(self):
        my_voiceit = VoiceIt2(VI_KEY, VI_TOKEN)
        ret = my_voiceit.create_user()
        user_id = my_voiceit.create_user()['userId']
        users_to_delete.append(user_id)
        print('Test Enrollment API Calls')

        print('   Test Get All Face Enrollments')
        ret = my_voiceit.get_all_face_enrollments(user_id)
        self.assertEqual(200, ret['status'])
        self.assertEqual('SUCC', ret['responseCode'])
        self.assertGreaterEqual(len(ret['faceEnrollments']), 0)

        print('   Test Get All Voice Enrollments')
        ret = my_voiceit.get_all_voice_enrollments(user_id)
        self.assertEqual(200, ret['status'])
        self.assertEqual('SUCC', ret['responseCode'])
        self.assertGreaterEqual(len(ret['voiceEnrollments']), 0)

        print('   Test Get All Video Enrollments')
        ret = my_voiceit.get_all_video_enrollments(user_id)
        self.assertEqual(200, ret['status'])
        self.assertEqual('SUCC', ret['responseCode'])
        self.assertGreaterEqual(len(ret['videoEnrollments']), 0)

        print('   Test Create Voice Enrollment')
        ret = my_voiceit.create_voice_enrollment(user_id, CONTENT_LANGUAGE, PHRASE, 'test-data/enrollmentNoel1.wav')
        self.assertEqual(201, ret['status'])
        self.assertEqual('SUCC', ret['responseCode'])
        enrollment_id_to_delete = ret['id']

        print('   Test Delete Voice Enrollment')
        ret = my_voiceit.delete_voice_enrollment(user_id, enrollment_id_to_delete)
        self.assertEqual(200, ret['status'])
        self.assertEqual('SUCC', ret['responseCode'])

        print('   Test Create Voice Enrollment by URL')
        ret = my_voiceit.create_voice_enrollment_by_url(user_id, CONTENT_LANGUAGE, PHRASE, S3_URL + 'test-data/enrollmentNoel1.wav')
        self.assertEqual(201, ret['status'])
        self.assertEqual('SUCC', ret['responseCode'])

        print('   Test Create Face Enrollment')
        ret = my_voiceit.create_face_enrollment(user_id, 'test-data/faceEnrollmentArmaan1.mp4')
        self.assertEqual(201, ret['status'])
        self.assertEqual('SUCC', ret['responseCode'])
        enrollment_id_to_delete = ret['faceEnrollmentId']

        print('   Test Delete Face Enrollment')
        ret = my_voiceit.delete_face_enrollment(user_id, enrollment_id_to_delete)
        self.assertEqual(200, ret['status'])
        self.assertEqual('SUCC', ret['responseCode'])

        print('   Test Create Face Enrollment by URL')
        ret = my_voiceit.create_face_enrollment_by_url(user_id, S3_URL + 'test-data/faceEnrollmentArmaan1.mp4')
        self.assertEqual(201, ret['status'])
        self.assertEqual('SUCC', ret['responseCode'])

        print('   Test Create Video Enrollment')
        ret = my_voiceit.create_video_enrollment(user_id, CONTENT_LANGUAGE, PHRASE, 'test-data/videoEnrollmentArmaan1.mov')
        self.assertEqual(201, ret['status'])
        self.assertEqual('SUCC', ret['responseCode'])
        enrollment_id_to_delete = ret['id']

        print('   Test Delete Video Enrollment')
        ret = my_voiceit.delete_video_enrollment(user_id, enrollment_id_to_delete)
        self.assertEqual(200, ret['status'])
        self.assertEqual('SUCC', ret['responseCode'])

        print('   Test Create Video Enrollment by URL')
        ret = my_voiceit.create_video_enrollment_by_url(user_id, CONTENT_LANGUAGE, PHRASE, S3_URL + 'test-data/videoEnrollmentArmaan1.mov')
        self.assertEqual(201, ret['status'])
        self.assertEqual('SUCC', ret['responseCode'])

        print('   Test Delete All Video Enrollments')
        ret = my_voiceit.delete_all_video_enrollments(user_id)
        self.assertEqual(200, ret['status'])
        self.assertEqual('SUCC', ret['responseCode'])

        print('   Test Delete All Voice Enrollments')
        ret = my_voiceit.delete_all_voice_enrollments(user_id)
        self.assertEqual(200, ret['status'])
        self.assertEqual('SUCC', ret['responseCode'])

        print('   Test Delete All Face Enrollments')
        ret = my_voiceit.delete_all_face_enrollments(user_id)
        self.assertEqual(200, ret['status'])
        self.assertEqual('SUCC', ret['responseCode'])

        print('   Test Delete All Enrollments')
        ret = my_voiceit.delete_all_enrollments(user_id)
        self.assertEqual(200, ret['status'])
        self.assertEqual('SUCC', ret['responseCode'])

    def test_verification(self):
        my_voiceit = VoiceIt2(VI_KEY, VI_TOKEN)
        user_id = my_voiceit.create_user()['userId']
        users_to_delete.append(user_id)
        # Create 3 voice,face and video enrollments for user
        my_voiceit.create_voice_enrollment(user_id, CONTENT_LANGUAGE, PHRASE, 'test-data/enrollmentNoel1.wav')
        my_voiceit.create_voice_enrollment(user_id, CONTENT_LANGUAGE, PHRASE, 'test-data/enrollmentNoel2.wav')
        my_voiceit.create_voice_enrollment(user_id, CONTENT_LANGUAGE, PHRASE, 'test-data/enrollmentNoel3.wav')
        my_voiceit.create_face_enrollment(user_id, 'test-data/faceEnrollmentArmaan1.mp4')
        my_voiceit.create_face_enrollment(user_id, 'test-data/faceEnrollmentArmaan2.mp4')
        my_voiceit.create_face_enrollment(user_id, 'test-data/faceEnrollmentArmaan3.mp4')
        my_voiceit.create_video_enrollment(user_id, CONTENT_LANGUAGE, PHRASE, 'test-data/videoEnrollmentArmaan1.mov')
        my_voiceit.create_video_enrollment(user_id, CONTENT_LANGUAGE, PHRASE, 'test-data/videoEnrollmentArmaan2.mov')
        my_voiceit.create_video_enrollment(user_id, CONTENT_LANGUAGE, PHRASE, 'test-data/videoEnrollmentArmaan3.mov')

        print('Test Verification API Calls')

        print('   Test Voice Verification')
        ret = my_voiceit.voice_verification(user_id, CONTENT_LANGUAGE, PHRASE, 'test-data/verificationNoel1.wav')
        self.assertEqual(200, ret['status'])
        self.assertEqual('SUCC', ret['responseCode'])

        print('   Test Voice Verification by URL')
        ret = my_voiceit.voice_verification_by_url(user_id, CONTENT_LANGUAGE, PHRASE, S3_URL + 'test-data/verificationNoel1.wav')
        self.assertEqual(200, ret['status'])
        self.assertEqual('SUCC', ret['responseCode'])

        print('   Test Face Verification')
        ret = my_voiceit.face_verification(user_id, 'test-data/faceVerificationArmaan1.mp4')
        self.assertEqual(200, ret['status'])
        self.assertEqual('SUCC', ret['responseCode'])

        print('   Test Face Verification by URL')
        ret = my_voiceit.face_verification_by_url(user_id, S3_URL + 'test-data/faceVerificationArmaan1.mp4')
        self.assertEqual(200, ret['status'])
        self.assertEqual('SUCC', ret['responseCode'])

        print('   Test Video Verification')
        ret = my_voiceit.video_verification(user_id, CONTENT_LANGUAGE, PHRASE, 'test-data/videoVerificationArmaan1.mov')
        self.assertEqual(200, ret['status'])
        self.assertEqual('SUCC', ret['responseCode'])

        print('   Test Video Verification by URL')
        ret = my_voiceit.video_verification_by_url(user_id, CONTENT_LANGUAGE, PHRASE, S3_URL + 'test-data/videoVerificationArmaan1.mov')
        self.assertEqual(200, ret['status'])
        self.assertEqual('SUCC', ret['responseCode'])

    def test_identification(self):
        my_voiceit = VoiceIt2(VI_KEY, VI_TOKEN)
        global groups_to_delete,users_to_delete
        print('Start Identification Setup...')
        user_id_1 = my_voiceit.create_user()['userId']
        users_to_delete.append(user_id_1)
        user_id_2 = my_voiceit.create_user()['userId']
        users_to_delete.append(user_id_2)
        group_id = my_voiceit.create_group('Test Identification Group')['groupId']
        groups_to_delete.append(group_id)
        my_voiceit.add_user_to_group(group_id, user_id_1)
        my_voiceit.add_user_to_group(group_id, user_id_2)

        # Create 3 voice enrollments for each user
        for file in ['test-data/enrollmentNoel1.wav','test-data/enrollmentNoel2.wav','test-data/enrollmentNoel3.wav']:
            my_voiceit.create_voice_enrollment(user_id_1, CONTENT_LANGUAGE, PHRASE, file)
        for file in ['test-data/enrollmentStephen1.wav','test-data/enrollmentStephen2.wav','test-data/enrollmentStephen3.wav']:
            my_voiceit.create_voice_enrollment(user_id_2, CONTENT_LANGUAGE, PHRASE, file)
        # Create 3 video enrollments for each user
        for file in ['test-data/videoEnrollmentArmaan1.mov','test-data/videoEnrollmentArmaan2.mov','test-data/videoEnrollmentArmaan3.mov']:
            my_voiceit.create_video_enrollment(user_id_1, CONTENT_LANGUAGE, PHRASE, file)
        for file in ['test-data/videoEnrollmentStephen1.mov','test-data/videoEnrollmentStephen2.mov','test-data/videoEnrollmentStephen3.mov']:
            my_voiceit.create_video_enrollment(user_id_2, CONTENT_LANGUAGE, PHRASE, file)

        print('Test Identification API Calls')

        print('   Test Voice Identification')
        ret = my_voiceit.voice_identification(group_id, CONTENT_LANGUAGE, PHRASE, 'test-data/enrollmentNoel1.wav')
        self.assertEqual(200, ret['status'])
        self.assertEqual('SUCC', ret['responseCode'])
        self.assertEqual(user_id_1, ret['userId'])
        ret = my_voiceit.voice_identification(group_id, CONTENT_LANGUAGE, PHRASE, 'test-data/enrollmentStephen1.wav')
        self.assertEqual(200, ret['status'])
        self.assertEqual('SUCC', ret['responseCode'])
        self.assertEqual(user_id_2, ret['userId'])

        print('   Test Voice Identification by URL')
        ret = my_voiceit.voice_identification_by_url(group_id, CONTENT_LANGUAGE, PHRASE, S3_URL + 'test-data/enrollmentNoel1.wav')
        self.assertEqual(200, ret['status'])
        self.assertEqual('SUCC', ret['responseCode'])
        self.assertEqual(user_id_1, ret['userId'])
        ret = my_voiceit.voice_identification_by_url(group_id, CONTENT_LANGUAGE, PHRASE, S3_URL + 'test-data/enrollmentStephen1.wav')
        self.assertEqual(200, ret['status'])
        self.assertEqual('SUCC', ret['responseCode'])
        self.assertEqual(user_id_2, ret['userId'])

        print('   Test Face Identification')
        ret = my_voiceit.face_identification(group_id, 'test-data/faceVerificationArmaan1.mp4')
        self.assertEqual(200, ret['status'])
        self.assertEqual('SUCC', ret['responseCode'])
        self.assertEqual(user_id_1, ret['userId'])
        ret = my_voiceit.face_identification(group_id, 'test-data/faceVerificationStephen1.mp4')
        self.assertEqual(200, ret['status'])
        self.assertEqual('SUCC', ret['responseCode'])
        self.assertEqual(user_id_2, ret['userId'])

        print('   Test Face Identification by URL')
        ret = my_voiceit.face_identification_by_url(group_id, S3_URL + 'test-data/faceVerificationArmaan1.mp4')
        self.assertEqual(200, ret['status'])
        self.assertEqual('SUCC', ret['responseCode'])
        self.assertEqual(user_id_1, ret['userId'])
        ret = my_voiceit.face_identification_by_url(group_id, S3_URL + 'test-data/faceVerificationStephen1.mp4')
        self.assertEqual(200, ret['status'])
        self.assertEqual('SUCC', ret['responseCode'])
        self.assertEqual(user_id_2, ret['userId'])

        print('   Test Video Identification')
        ret = my_voiceit.video_identification(group_id, CONTENT_LANGUAGE, PHRASE, 'test-data/videoEnrollmentArmaan1.mov')
        self.assertEqual(200, ret['status'])
        self.assertEqual('SUCC', ret['responseCode'])
        self.assertEqual(user_id_1, ret['userId'])
        ret = my_voiceit.video_identification(group_id, CONTENT_LANGUAGE, PHRASE, 'test-data/videoEnrollmentStephen1.mov')
        self.assertEqual(200, ret['status'])
        self.assertEqual('SUCC', ret['responseCode'])
        self.assertEqual(user_id_2, ret['userId'])

        print('   Test Video Identification by URL')
        ret = my_voiceit.video_identification_by_url(group_id, CONTENT_LANGUAGE, PHRASE, S3_URL + 'test-data/videoEnrollmentArmaan1.mov')
        self.assertEqual(200, ret['status'])
        self.assertEqual('SUCC', ret['responseCode'])
        self.assertEqual(user_id_1, ret['userId'])
        ret = my_voiceit.video_identification_by_url(group_id, CONTENT_LANGUAGE, PHRASE, S3_URL + 'test-data/videoEnrollmentStephen1.mov')
        self.assertEqual(200, ret['status'])
        self.assertEqual('SUCC', ret['responseCode'])
        self.assertEqual(user_id_2, ret['userId'])

if __name__ == '__main__':
    unittest.main()
