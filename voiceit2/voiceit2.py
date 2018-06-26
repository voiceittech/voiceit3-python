import requests

class VoiceIt2:
    base_URL = 'https://api.voiceit.io/'
    voiceit_basic_auth_credentials = ''

    def __init__(self, key, token):
        self.voiceit_basic_auth_credentials = (key, token)

    def get_all_users(self):
        try:
            response = requests.get(self.base_URL+'users', auth=self.voiceit_basic_auth_credentials)
            return response.json()
        except requests.exceptions.HTTPError as e:
            return e.read()

    def create_user(self):
        try:
            response = requests.post(self.base_URL+'users', auth=self.voiceit_basic_auth_credentials)
            return response.json()
        except requests.exceptions.HTTPError as e:
            return e.read()

    def get_user(self, user_id):
        try:
            response = requests.get(self.base_URL+'users/'+user_id, auth=self.voiceit_basic_auth_credentials)
            return response.json()
        except  requests.exceptions.HTTPError as e:
            return e.read()

    def delete_user(self, user_id):
        try:
            response = requests.delete(self.base_URL+'users/'+user_id, auth=self.voiceit_basic_auth_credentials)
            return response.json()
        except  requests.exceptions.HTTPError as e:
            return e.read()

    def get_groups_for_user(self, user_id):
        try:
            response = requests.get(self.base_URL+'users/'+user_id + '/groups', auth=self.voiceit_basic_auth_credentials)
            return response.json()
        except  requests.exceptions.HTTPError as e:
            return e.read()

    def get_all_groups(self):
        try:
            response = requests.get(self.base_URL+'groups', auth=self.voiceit_basic_auth_credentials)
            return response.json()
        except  requests.exceptions.HTTPError as e:
            return e.read()

    def get_group(self, group_id):
        try:
            response = requests.get(self.base_URL+'groups/' + group_id, auth=self.voiceit_basic_auth_credentials)
            return response.json()
        except  requests.exceptions.HTTPError as e:
            return e.read()

    def group_exists(self, group_id):
        try:
            response = requests.get(self.base_URL+'groups/' + group_id + '/exists', auth=self.voiceit_basic_auth_credentials)
            return response.json()
        except  requests.exceptions.HTTPError as e:
            return e.read()

    def create_group(self, group_desc):
        dataObj = {}
        dataObj['description'] = group_desc
        try:
            response = requests.post(self.base_URL + 'groups', auth=self.voiceit_basic_auth_credentials, data = dataObj)
            return response.json()
        except  requests.exceptions.HTTPError as e:
            return e.read()

    def add_user_to_group(self, group_id, user_id):
        dataObj = {}
        dataObj['groupId'] = group_id
        dataObj['userId'] = user_id
        try:
            response = requests.put(self.base_URL + 'groups/addUser', auth=self.voiceit_basic_auth_credentials, data = dataObj)
            return response.json()
        except  requests.exceptions.HTTPError as e:
            return e.read()

    def remove_user_from_group(self, group_id, user_id):
        dataObj = {}
        dataObj['groupId'] = group_id
        dataObj['userId'] = user_id
        try:
            response = requests.put(self.base_URL + 'groups/removeUser', auth=self.voiceit_basic_auth_credentials, data = dataObj)
            return response.json()
        except  requests.exceptions.HTTPError as e:
            return e.read()

    def delete_group(self, group_id):
        try:
            response = requests.delete(self.base_URL + 'groups/' + group_id, auth=self.voiceit_basic_auth_credentials)
            return response.json()
        except  requests.exceptions.HTTPError as e:
            return e.read()

    def get_all_enrollments_for_user(self, user_id):
        try:
            response = requests.get(self.base_URL + 'enrollments/' + user_id, auth=self.voiceit_basic_auth_credentials)
            return response.json()
        except  requests.exceptions.HTTPError as e:
            return e.read()

    def get_face_enrollments_for_user(self, user_id):
        try:
            response = requests.get(self.base_URL + 'enrollments/face/' + user_id, auth=self.voiceit_basic_auth_credentials)
            return response.json()
        except  requests.exceptions.HTTPError as e:
            return e.read()

    def create_voice_enrollment(self, user_id, lang, file_path):
        dataObj = {}
        dataObj['userId'] = user_id
        dataObj['contentLanguage'] = lang
        filesObj = [('recording', ('enrollment.wav', open(file_path, 'rb'), 'audio/wav'))]
        try:
            response = requests.post(self.base_URL+ '/enrollments', auth=self.voiceit_basic_auth_credentials, data=dataObj, files=filesObj)
            return response.json()
        except  requests.exceptions.HTTPError as e:
            return e.read()

    def create_voice_enrollment_by_url(self, user_id, lang, file_Url):
        dataObj = {}
        dataObj['userId'] = user_id
        dataObj['fileUrl'] = file_Url
        dataObj['contentLanguage'] = lang
        try:
            response = requests.post(self.base_URL+ '/enrollments/byUrl', auth=self.voiceit_basic_auth_credentials, data=dataObj)
            return response.json()
        except  requests.exceptions.HTTPError as e:
            return e.read()

    def create_face_enrollment(self, user_id, file_path, blink_detection=False):
        dataObj = {}
        dataObj['userId'] = user_id
        dataObj['doBlinkDetection'] = blink_detection
        filesObj = [('video', ('video.mp4', open(file_path, 'rb'), 'video/mp4'))]
        try:
            response = requests.post(self.base_URL+ '/enrollments/face', auth=self.voiceit_basic_auth_credentials, data=dataObj, files=filesObj)
            return response.json()
        except  requests.exceptions.HTTPError as e:
            return e.read()

    def create_video_enrollment(self, user_id, lang, file_path, blink_detection=False):
        dataObj = {}
        dataObj['userId'] = user_id
        dataObj['doBlinkDetection'] = blink_detection
        dataObj['contentLanguage'] = lang
        filesObj = [('video', ('video.mp4', open(file_path, 'rb'), 'video/mp4'))]
        try:
            response = requests.post(self.base_URL + '/enrollments/video', auth=self.voiceit_basic_auth_credentials, data=dataObj, files=filesObj)
            return response.json()
        except requests.exceptions.HTTPError as e:
            return e.read()

    def create_video_enrollment_by_url(self, user_id, lang, file_Url, blink_detection=False):
        dataObj = {}
        dataObj['userId'] = user_id
        dataObj['contentLanguage'] = lang
        dataObj['doBlinkDetection'] = blink_detection
        dataObj['fileUrl'] = file_Url
        try:
            response = requests.post(self.base_URL + '/enrollments/video/byUrl', auth=self.voiceit_basic_auth_credentials, data=dataObj)
            return response.json()
        except requests.exceptions.HTTPError as e:
            return e.read()

    def delete_all_enrollments_for_user(self, user_id):
        try:
            response = requests.delete(self.base_URL + 'enrollments/' + user_id + '/all', auth=self.voiceit_basic_auth_credentials)
            return response.json()
        except requests.exceptions.HTTPError as e:
                return e.read()

    def delete_face_enrollment(self, user_id, face_enrollment_id):
        try:
            response = requests.delete(self.base_URL + 'enrollments/face/' + user_id + '/'+ face_enrollment_id, auth=self.voiceit_basic_auth_credentials)
            return response.json()
        except requests.exceptions.HTTPError as e:
                return e.read()

    def delete_enrollment_for_user(self, user_id, enrollment_id):
        try:
            response = requests.delete(self.base_URL + 'enrollments/' + user_id + '/'+ enrollment_id, auth=self.voiceit_basic_auth_credentials)
            return response.json()
        except requests.exceptions.HTTPError as e:
            return e.read()

    def voice_verification(self, user_id, lang, file_path):
        dataObj = {}
        dataObj['userId'] = user_id
        dataObj['contentLanguage'] = lang
        filesObj = [('recording', ('verification.wav', open(file_path, 'rb'), 'audio/wav'))]
        try:
            response = requests.post(self.base_URL+ '/verification', auth=self.voiceit_basic_auth_credentials, data=dataObj, files=filesObj)
            return response.json()
        except requests.exceptions.HTTPError as e:
            return e.read()

    def voice_verification_by_url(self, user_id, lang, file_Url):
        dataObj = {}
        dataObj['userId'] = user_id
        dataObj['contentLanguage'] = lang
        dataObj['fileUrl'] = file_Url
        try:
            response = requests.post(self.base_URL+ '/verification/byUrl', auth=self.voiceit_basic_auth_credentials, data=dataObj)
            return response.json()
        except requests.exceptions.HTTPError as e:
            return e.read()

    def face_verification(self, user_id, file_path, blink_detection = False):
        dataObj = {}
        dataObj['userId'] = user_id
        dataObj['doBlinkDetection'] = blink_detection
        filesObj = [('video', ('video.mp4', open(file_path, 'rb'), 'video/mp4'))]
        try:
            response = requests.post(self.base_URL + 'verification/face', auth=self.voiceit_basic_auth_credentials, data=dataObj, files=filesObj)
            return response.json()
        except requests.exceptions.HTTPError as e:
            return e.read()

    def video_verification(self, user_id, lang, file_path, blink_detection = False):
        dataObj = {}
        dataObj['userId'] = user_id
        dataObj['contentLanguage'] = lang
        dataObj['doBlinkDetection'] = blink_detection
        filesObj = [('video', ('video.mp4', open(file_path, 'rb'), 'video/mp4'))]
        try:
            response = requests.post(self.base_URL + 'verification/video', auth=self.voiceit_basic_auth_credentials, data=dataObj, files=filesObj)
            return response.json()
        except requests.exceptions.HTTPError as e:
            return e.read()

    def video_verification_by_url(self, user_id, lang, file_Url, blink_detection = False):
        dataObj = {}
        dataObj['userId'] = user_id
        dataObj['contentLanguage'] = lang
        dataObj['fileUrl'] = file_Url
        dataObj['doBlinkDetection'] = blink_detection
        try:
            response = requests.post(self.base_URL+ '/verification/video/byUrl', auth=self.voiceit_basic_auth_credentials, data=dataObj)
            return response.json()
        except requests.exceptions.HTTPError as e:
            return e.read()

    def voice_identification(self, group_id, lang, file_path):
        dataObj = {}
        dataObj['groupId'] = group_id
        dataObj['contentLanguage'] = lang
        filesObj = [('recording', ('identification.wav', open(file_path, 'rb'), 'audio/wav'))]
        try:
            response = requests.post(self.base_URL + 'identification', auth=self.voiceit_basic_auth_credentials, data=dataObj, files=filesObj)
            return response.json()
        except requests.exceptions.HTTPError as e:
            return e.read()

    def voice_identification_by_url(self, user_id, lang, file_Url):
        dataObj = {}
        dataObj['userId'] = user_id
        dataObj['contentLanguage'] = lang
        dataObj['fileUrl'] = file_Url
        try:
            response = requests.post(self.base_URL+ '/identification/byUrl', auth=self.voiceit_basic_auth_credentials, data=dataObj)
            return response.json()
        except requests.exceptions.HTTPError as e:
            return e.read()

    def video_identification(self, group_id, lang, file_path, blink_detection = False):
        dataObj = {}
        dataObj['groupId'] = group_id
        dataObj['contentLanguage'] = lang
        dataObj['doBlinkDetection'] = blink_detection
        filesObj = [('video', ('video.mp4', open(file_path, 'rb'), 'video/mp4'))]
        try:
            response = requests.post(self.base_URL + 'identification/video', auth=self.voiceit_basic_auth_credentials, data=dataObj, files=filesObj)
            return response.json()
        except requests.exceptions.HTTPError as e:
            return e.read()

    def video_identification_by_url(self, user_id, lang, file_Url, blink_detection = False):
        dataObj = {}
        dataObj['userId'] = user_id
        dataObj['contentLanguage'] = lang
        dataObj['fileUrl'] = file_Url
        dataObj['doBlinkDetection'] = blink_detection
        try:
            response = requests.post(self.base_URL+ '/identification/video/byUrl', auth=self.voiceit_basic_auth_credentials, data=dataObj)
            return response.json()
        except requests.exceptions.HTTPError as e:
            return e.read()
