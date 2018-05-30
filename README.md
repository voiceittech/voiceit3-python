## VoiceIt's API 2.0 Python Wrapper

Our official python wrapper for API 2.0

* [Getting Started](#getting-started)
* [Installation](#installation)
* [API Calls](#api-calls)
  * [Initialization](#initialization)
  * [User API Calls](#user-api-calls)
      * [Get All Users](#get-all-users)
      * [Create User](#create-user)
      * [Check User Exists](#check-if-user-exists)
      * [Get Groups for User](#get-groups-for-user)
      * [Delete User](#delete-user)
  * [Group API Calls](#group-api-calls)
      * [Get All Groups](#get-all-groups)
      * [Create Group](#create-group)
      * [Get Group](#get-group)
      * [Delete Group](#delete-group)
      * [Check Group Exists](#check-if-group-exists)
      * [Add User to Group](#add-user-to-group)
      * [Remove User from Group](#remove-user-from-group)      
  * [Enrollment API Calls](#enrollment-api-calls)
      * [Get All Enrollments for User](#get-all-enrollments-for-user)
      * [Get Face Enrollments for User](#get-face-enrollments-for-user)
      * [Delete Enrollment for User](#delete-enrollment-for-user)
      * [Delete Face Enrollment](#delete-face-enrollment)
      * [Create Voice Enrollment](#create-voice-enrollment)
      * [Create Voice Enrollment By URL](#create-voice-enrollment-by-url)
      * [Create Video Enrollment](#create-video-enrollment)
      * [Create Video Enrollment By URL](#create-video-enrollment-by-url)
      * [Create Face Enrollment](#create-face-enrollment)
  * [Verification API Calls](#verification-api-calls)
      * [Voice Verification](#voice-verification)
      * [Voice Verification By URL](#voice-verification-by-url)
      * [Video Verification](#video-verification)
      * [Video Verification By URL](#video-verification-by-url)
      * [Face Verification](#face-verification)
  * [Identification API Calls](#identification-api-calls)
      * [Voice Identification](#voice-identification)
      * [Voice Identification By URL](#voice-identification-by-url)
      * [Video Identification](#video-identification)
      * [Video Identification By URL](#video-identification-by-url)

## Getting Started

Sign up for a free Developer Account at [voiceit.io](https://voiceit.io/signup) and activate API 2.0 from the settings page. Then you should be able view the API Key and Token. You can also review the HTTP Documentation at [api.voiceit.io](https://api.voiceit.io)

## Installation
Please make sure that you have python3 installed. This wrapper uses the requests library:
```
sudo pip3 intall requests
```
The module can be installed using pip
```
sudo pip3 install voiceit2
```
### API calls

### Initialization
```
voiceitPython = VoiceIt2('YOUR_KEY','YOUR_TOKEN')
```
### User API Calls

#### Get All Users

Get all the users associated with the apiKey
```python
voiceitPython.get_all_users()
```

#### Create User

Create a new user
```python
voiceitPython.create_user()
```

#### Check if User Exists

Check whether a user exists for the given userId(begins with 'usr_')
```python
voiceitPython.get_user("USER_ID_HERE").
```

#### Delete User

Delete user with given userId(begins with 'usr_')
```python
voiceitPython.delete_user("USER_ID_HERE")
```

#### Get Groups for User

Get a list of groups that the user with given userId(begins with 'usr_') is a part of
```python
voiceitPython.get_groups_for_user("USER_ID_HERE")
```

### Group API Calls

#### Get All Groups

Get all the groups associated with the apiKey
```python
voiceitPython.get_all_groups()
```

#### Get Group

Returns a group for the given groupId(begins with 'grp_')
```python
voiceitPython.get_group("GROUP_ID_HERE")
```

#### Check if Group Exists

Checks if group with given groupId(begins with 'grp_') exists
```python
voiceitPython.group_exists("GROUP_ID_HERE")
```

#### Create Group

Create a new group with the given description
```python
voiceitPython.create_group("Sample Group Description")
```

#### Add User to Group

Adds user with given userId(begins with 'usr_') to group with given groupId(begins with 'grp_')
```python
voiceitPython.add_user_to_group("GROUP_ID_HERE", "USER_ID_HERE")
```

#### Remove User from Group

Removes user with given userId(begins with 'usr_') from group with given groupId(begins with 'grp_')

```python
voiceitPython.remove_user_from_group( "GROUP_ID_HERE", "USER_ID_HERE")
```

#### Delete Group

Delete group with given groupId(begins with 'grp_'), note: tThis call does not delete any users, but simply deletes the group and disassociates the users from the group

```python
voiceitPython.delete_group("GROUP_ID_HERE")
```

### Enrollment API Calls

#### Get All Enrollments for User

Gets all enrollment for user with given userId(begins with 'usr_')

```python
voiceitPython.get_all_enrollments_for_user("USER_ID_HERE")
```
### Get Face Enrollments For User
Get all face enrollments for the user
```
voiceitPython.get_face_enrollments_for_user("USER_ID_HERE"):
```

### Create Face Enrollment
Creates a face enrollment for user
```
voiceitPython.create_face_enrollment("USER_ID", "LANG_CODE", "FILE_PATH")
```

#### Delete Enrollment for User

Delete enrollment for user with given userId(begins with 'usr_') and enrollmentId(integer)

```python
voiceitPython.delete_enrollment_for_user( "USER_ID_HERE", "ENROLLMENT_ID_HERE")
```

### Delete Face Enrollment 
Delete a Face enrollemnt for User

```
voiceitPython.delete_face_enrollment(self, "USER_ID_HERE", "FACE_ENROLLMENT_ID_HERE")
```

#### Create Voice Enrollment

Create audio enrollment for user with given userId(begins with 'usr_') and contentLanguage('en-US','es-ES' etc.). Note: File recording need to be no less than 1.2 seconds and no more than 5 seconds

```python
voiceitPython.create_voice_enrollment("USER_ID_HERE", "CONTENT_LANGUAGE_HERE", Byte[] recording);
```

### Create Voice Enrollment By URL
Creates a voice enrollment for the user using a provided URL 

```
voiceitPython.create_voice_enrollment_by_url("USER_ID_HERE", "LANG_CODE", "URL_TO_AUDIO")
```

#### Create Video Enrollment

Create video enrollment for user with given userId(begins with 'usr_') and contentLanguage('en-US','es-ES' etc.). Note: File recording need to be no less than 1.2 seconds and no more than 5 seconds

```python
voiceitPython.create_video_enrollment("USER_ID_HERE", "CONTENT_LANGUAGE_HERE", "FILE_PATH", blink_detection=false);
```

#### Create Video Enrollment By URL

Create video enrollment for user with given userId(begins with 'usr_') and contentLanguage('en-US','es-ES' etc.) by the URL provided. Note: Recording needs to be no less than 1.2 seconds and no more than 5 seconds

```python
voiceitPython.create_video_enrollment("USER_ID_HERE", "CONTENT_LANGUAGE_HERE", "VIDEO_URL", blink_detection=false);
```

### Verification API Calls

#### Voice Verification

Verify user with the given userId(begins with 'usr_') and contentLanguage('en-US','es-ES' etc.). Note: File recording need to be no less than 1.2 seconds and no more than 5 seconds

```python
voiceitPython.voice_verification("USER_ID_HERE", "CONTENT_LANGUAGE_HERE", Byte[] recording)
```

#### Video Verification

Verify user with given userId(begins with 'usr_') and contentLanguage('en-US','es-ES' etc.). Note: File recording need to be no less than 1.2 seconds and no more than 5 seconds
```python
voiceitPython.video_verification("USER_ID_HERE", "CONTENT_LANGUAGE_HERE", Byte[] video)
```
### Face Verification 
Verify the person using a video
```
voiceitPython.face_verification("USER_ID", "FILE_PATH", bink_detection = false)
```

### Identification API Calls

#### Voice Identification

Identify user inside group with the given groupId(begins with 'grp_') and contentLanguage('en-US','es-ES' etc.). Note: File recording need to be no less than 1.2 seconds and no more than 5 seconds

```python
voiceitPython.voice_identification("GROUP_ID_HERE", "CONTENT_LANGUAGE_HERE", Byte[] recording)
```

#### Video Identification

Identify user inside group with the given groupId(begins with 'grp_') and contentLanguage('en-US','es-ES' etc.). Note: File recording need to be no less than 1.2 seconds and no more than 5 seconds

```java
voiceitPython.video_identification("GROUP_ID_HERE", "CONTENT_LANGUAGE_HERE", Byte[] video)
```

## Author

Hassan Ismaeel, hassan@voiceit.io

## License

Voiceit2_python is available under the MIT license. See the LICENSE file for more info.
