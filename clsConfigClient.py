################################################
#### Written By: SATYAKI DE                 ####
#### Written On:  15-May-2020               ####
#### Modified On: 14-Apr-2024               ####
####                                        ####
#### Objective: This script is a config     ####
#### file, contains all the keys for        ####
#### personal UpTrain-based LLM evaluation  ####
#### solution to fetch the KPIs to tune it. ####
####                                        ####
################################################

import os
import platform as pl

class clsConfigClient(object):
    Curr_Path = os.path.dirname(os.path.realpath(__file__))

    os_det = pl.system()
    if os_det == "Windows":
        sep = '\\'
    else:
        sep = '/'

    conf = {
        'APP_ID': 1,
        'ARCH_DIR': Curr_Path + sep + 'arch' + sep,
        'PROFILE_PATH': Curr_Path + sep + 'profile' + sep,
        'LOG_PATH': Curr_Path + sep + 'log' + sep,
        'DATA_PATH': Curr_Path + sep + 'data' + sep,
        'OUTPUT_PATH': Curr_Path + sep + 'output' + sep,
        'TEMP_PATH': Curr_Path + sep + 'temp' + sep,
        'IMAGE_PATH': Curr_Path + sep + 'Image' + sep,
        'SESSION_PATH': Curr_Path + sep + 'my-app' + sep + 'src' + sep + 'session' + sep,
        'JSONFileNameWithPath': Curr_Path + sep + 'GUI_Config' + sep + 'CircuitConfiguration.json',
        'OUTPUT_DIR': 'model',
        'APP_DESC_1': 'LLM Evaluation Demo!',
        'DEBUG_IND': 'Y',
        'INIT_PATH': Curr_Path,
        'FILE_NAME': 'input.json',
        'MODEL_NAME': "gpt-3.5-turbo",
        'API_KEY': "4zHX5D5eKnHPRLdkdii8re6jdjfdjfLP2eLHD7",
        'MODEL_NAME': 'gpt-3.5-turbo',
        'CHANNEL_NAME': 'sd_channel',
        'OPEN_AI_KEY': "sk-fz1KAVXG7Kdjr747rfjfhjfrujazuufr848jfe",
        'ABLY_ID': '4Q1j_Q.q3kHKSJfrir8r8rjhrhrUHoDvQNe3NfXE',
        'ABLY_URL': "https://realtime.ably.io/channels/sd_channel/messages?key=",
        'ABLY_READ_URL': "https://realtime.ably.io/channels/sd_channel/messages",
        "appType":"application/json",
        "conType":"keep-alive",
        "CACHE":"no-cache",
        "MAX_RETRY": 3,
        'YOUTUBE_KEY': "AIzaKdsdudr8ydhd74lFq2h-mvoiksdjdUJUOU",
        'BASE_URL': "http://127.0.0.1:5000/message",
        'TITLE': "NASA Demo!",
        'TEMP_VAL': 0.2,
        'PATH' : Curr_Path,
        'MAX_TOKEN' : 512,
        'MAX_CNT' : 5,
        'OUT_DIR': 'data',
        'OUTPUT_DIR': 'output',
        'HEADER_TOKEN': 'JSESSIONID=B278KDJDUDUD*DH8C15ED33F0; __VCAP_ID__=0fa8c599-f9d4-4763-6795-bb25',
        'MERGED_FILE': 'mergedFile.csv',
        'CLEANED_FILE': 'cleanedFile.csv',
        'CLEANED_FILE_SHORT': 'cleanedFileMod.csv',
        'SUBDIR_OUT': 'output',
        'SESSION_CACHE_FILE': 'sessionCacheCounter.csv',
        'IMAGE_FILE': 'earth.jpeg',
        'CACHE_FILE': 'data.pkl',
        'ADMIN_KEY': "Admin@23",
        'SECRET_KEY': "Adsec@23",
        "limRec": 50,
        "USER_NM": "Test",
        "USER_PWD": "Test@23",
        "DB_PATH": Curr_Path + sep + 'data' + sep,
        "DB_FILE_NM": "CustomerDetails.csv",
        "DB_FILE_LIST": ["CustomerDetails.csv","AccountAddress.csv"],
        "JOIN_CONDITION":["-- AccountAddress.user_id can be joined with CustomerDetails.user_id"],
        "INPUT_VAL": 1000000000,
        "QUERY_MODEL": "facebook/dpr-question_encoder-single-nq-base",
        "PASSAGE_MODEL": "facebook/dpr-ctx_encoder-single-nq-base",
        'YEAR_RANGE': 1,
        'MODEL_PATH': Curr_Path + sep + 'NLP_Model' + sep + 'glove.6B' + sep,
        'NO_OF_MODEL_DIM': 100,
        "FinData": "Cache.csv"
    }
