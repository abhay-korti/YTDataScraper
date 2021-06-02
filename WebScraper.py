from googleapiclient.discovery import build
from googleapiclient import discovery
import csv
from Google import Create_Service
import os
import datetime


#input dev key 
dev_key=''

# Input client secret file path here
FOLDER_PATH = r''
CLIENT_SECRET_FILE = os.path.join(FOLDER_PATH, 'CLIENT_SECRET.json')
API_SERVICE_NAME = 'sheets'
API_VERSION = 'v4'

#Scope has to be declared 
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

sheets_id = Create_Service(CLIENT_SECRET_FILE, API_SERVICE_NAME, API_VERSION, SCOPES)
# The ID of the spreadsheet to retrieve data from.
spreadsheet_id = '' 
# The A1 notation of the values to retrieve.
range_ = 'Sheet1'  


video_id = []

request_sheet = sheets_id.spreadsheets().values().get(spreadsheetId=spreadsheet_id, range=range_, valueRenderOption='FORMATTED_VALUE', dateTimeRenderOption='FORMATTED_STRING')
response = request_sheet.execute()
total_list = response['values']

temp_var = 0
for i in range(len(total_list)-1):
    temp_var += 1
    video_link = total_list[temp_var][1]
    video_id.append(video_link[-11:])

print(video_id)

prefix_column = ''
difference_var = ''
rounds = 0
print(len(total_list[0]))
if len(total_list[0]) - 26 >= 0: 
    rounds = int(len(total_list[0])/26)
    prefix_column = chr(int(len(total_list[0])/26)+64)
    print(prefix_column)
    difference_var = chr((len(total_list[0])- 26 + 65))
    print(difference_var)
else:
    prefix_column = ''
    difference_var = chr(len(total_list[0])+65)

print(total_list)
list_num = 0

print(video_id)

youtube = build('youtube','v3',developerKey=dev_key)

views = []
video_title = []
date_published = []
channel_name = []

for i in video_id:
    request = youtube.videos().list(
    part='statistics,snippet',
    id = i
)
    response = request.execute() 
    #Getting View Count from All the Info
    views.append(response.get('items')[0]['statistics']['viewCount'])
    date_published.append(response.get('items')[0]['snippet']['publishedAt'])
    video_title.append(response.get('items')[0]['snippet']['title'])
    channel_name.append(response.get('items')[0]['snippet']['channelTitle'])


print(views)
print(date_published)
print(video_title)


print(f'{prefix_column}{difference_var}2')
print(f'{prefix_column}{difference_var}1')

worksheet_name = 'Sheet1!'
cell_range_insert = f'{prefix_column}{difference_var}2'

value = [tuple(views)]
date_var = [[str(datetime.date.today())]]
pub_var = [tuple(date_published)]
title_var = [tuple(video_title)]
channel_var = [tuple(channel_name)]

value_range_body_channel_name = {
    'majorDimension': 'COLUMNS',
    'values': channel_var
}


value_range_body_date = {
    'majorDimension': 'COLUMNS',
    'values': pub_var
}


value_range_body_title = {
    'majorDimension': 'COLUMNS',
    'values': title_var
}


value_range_body = {
    'majorDimension': 'COLUMNS',
    'values': date_var
}


value_range_body_views = {
    'majorDimension': 'COLUMNS',
    'values': value
}

sheets_id.spreadsheets().values().update(
    spreadsheetId=spreadsheet_id,
    range=worksheet_name + 'A2',
    valueInputOption='USER_ENTERED',
    body=value_range_body_channel_name
).execute()

sheets_id.spreadsheets().values().update(
    spreadsheetId=spreadsheet_id,
    range=worksheet_name + 'C2',
    valueInputOption='USER_ENTERED',
    body=value_range_body_title
).execute()


sheets_id.spreadsheets().values().update(
    spreadsheetId=spreadsheet_id,
    range=worksheet_name + 'D2',
    valueInputOption='USER_ENTERED',
    body=value_range_body_date
).execute()


sheets_id.spreadsheets().values().update(
    spreadsheetId=spreadsheet_id,
    range=worksheet_name + f'{prefix_column}{difference_var}1',
    valueInputOption='USER_ENTERED',
    body=value_range_body
).execute()

sheets_id.spreadsheets().values().update(
    spreadsheetId=spreadsheet_id,
    range=worksheet_name + cell_range_insert,
    valueInputOption='USER_ENTERED',
    body=value_range_body_views
).execute()
