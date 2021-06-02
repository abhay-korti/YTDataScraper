# YouTube DataScraper

Purpose: 

The purpose of this WebScraper is to gather the following information from a given YouTube link in any given sheet.
- Channel Name 
- Video Title 
- Views of the video
- Date Published 


# Usage 

Go to https://console.developers.google.com and enable two of the services in APIs 
- YouTube Data v3 - Public data only
- Sheets v4  - Private Data access request and enable the Google Spreadsheet scope to edit and create spreadsheets




Download the scripts and change the following variables - 
- dev_key - API Developer Key that needs to be generated with a Google Account from - https://console.developers.google.com
- Client Secret JSON - Download it from the Credentials Generation screen from you Google Account.
- Sheets ID - Copy it from the link of a Google Sheet from a URL - (docs.google.com/spreadsheets/d/ *spreadsheetId*/)

Running WebScraper.py with the inserted info will read the sheet and the B2 column for any YouTube Video links and then Return the follwing 
- Channel Name - A2 
- Video Title - C2 
- Date Published - D2 
- Views of the video - E2 Onwards 


# Credit 

Google.py is a modified version of (https://developers.google.com/sheets/api/quickstart/python) https://learndataanalysis.org/google-py-file-source-code/ - by Jie Jenn. 
