import re
import pandas as pd

def preprocess(data):
    # Regex to capture both 12-hour (AM/PM) and 24-hour formats
    pattern = r'\d{1,2}/\d{1,2}/\d{2,4},\s\d{1,2}:\d{2}\s(?:[apAP][mM])?\s'

    # Split the data using the pattern
    messages = re.split(pattern, data)[1:]  # Split the chat log into individual messages
    dates = re.findall(pattern, data)       # Extract the date-time entries

    # Create DataFrame
    df = pd.DataFrame({'user_message': messages, 'message_date': dates})

    # Attempt to parse dates in 24-hour format first
    df['message_date'] = pd.to_datetime(df['message_date'], errors='coerce')

    # For any rows that failed to parse (NaT), try the 12-hour format with AM/PM
    df['message_date'] = df['message_date'].fillna(
        pd.to_datetime(df['message_date'], format='%d/%m/%Y, %I:%M %p ', errors='coerce')
    )

    # Rename message_date column to 'date'
    df.rename(columns={'message_date': 'date'}, inplace=True)

    # Extract users and messages
    users = []
    messages = []
    for message in df['user_message']:
        entry = re.split('([\w\W]+?):\s', message)
        if entry[1:]:  # If the message contains a user name
            users.append(entry[1])
            messages.append(" ".join(entry[2:]))
        else:
            users.append('group_notification')
            messages.append(entry[0])

    df['user'] = users
    df['message'] = messages
    df.drop(columns=['user_message'], inplace=True)

    # Add additional time-related columns for analysis
    df['only_date'] = df['date'].dt.date
    df['year'] = df['date'].dt.year
    df['month_num'] = df['date'].dt.month
    df['month'] = df['date'].dt.month_name()
    df['day'] = df['date'].dt.day
    df['day_name'] = df['date'].dt.day_name()
    df['hour'] = df['date'].dt.hour
    df['minute'] = df['date'].dt.minute

    # Create a 'period' column to group messages by hour periods
    period = []
    for hour in df['hour']:
        if hour == 23:
            period.append(str(hour) + "-00")
        elif hour == 0:
            period.append("00-01")
        else:
            period.append(str(hour) + "-" + str(hour + 1))

    df['period'] = period

    # Return the processed DataFrame
    return df
