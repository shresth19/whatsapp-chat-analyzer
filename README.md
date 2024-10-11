"""
    # WhatsApp Chat Analyzer

    This project analyzes WhatsApp chat data using Python. It processes chat logs exported from WhatsApp, extracting meaningful insights such as the most active users, message trends, and activity patterns. The analysis includes breaking down message counts, dates, times, and more from the chat data.

    ## Table of Contents
    - [Features](#features)
    - [Requirements](#requirements)
    - [Installation](#installation)
    - [Usage](#usage)
    - [Project Structure](#project-structure)
    - [Functionality](#functionality)
    - [Contributing](#contributing)
    - [License](#license)

    ## Features
    - Extracts messages, users, and timestamps from WhatsApp chat export.
    - Supports both 12-hour (AM/PM) and 24-hour time formats.
    - Generates insights on:
      - Total messages per user
      - Active periods (hours of the day, days of the week)
      - Word cloud for most frequently used words
      - Monthly and daily activity trends
      - User-level message statistics (most messages, least messages)

    ## Requirements
    To run this project, you'll need the following:
    - Python 3.x
    - Libraries:
      - pandas
      - matplotlib
      - re
      - numpy

    ## Installation
    1. Clone the repository:
       ```bash
       git clone https://github.com/yourusername/whatsapp-chat-analyzer.git
       ```
    2. Install the required libraries:
       ```bash
       pip install pandas matplotlib numpy
       ```

    ## Usage
    1. **Export your WhatsApp chat**:
       - Open a chat in WhatsApp.
       - Go to `Options -> More -> Export Chat` and export the chat **without media**.
       - This will generate a `.txt` file of your chat history.
      
    2. **Run the Analyzer**:
       - Place the exported `.txt` file in the project directory.
       - Use the following script to start analyzing:
         ```python
         from app import preprocess

         # Open the exported chat file
         with open("whatsapp_chat.txt", "r", encoding="utf-8") as file:
             data = file.read()

         # Process and analyze
         df = preprocess(data)

         # Display basic information
         print(df.head())
         ```

    3. **View Results**:
       - The results will include a DataFrame of messages, timestamps, users, and various other extracted data.
       - You can then extend the analysis by plotting graphs or further processing the data.

    ## Project Structure
    ```bash
    whatsapp-chat-analyzer/
    │
    ├── app.py               # Main application logic and preprocessing function
    ├── requirements.txt      # Required libraries
    ├── whatsapp_chat.txt     # Example WhatsApp chat export (this file is user-provided)
    └── README.md             # Project README file (this file)
    ```

    ## Functionality
    The core of the project is the `preprocess` function, which:
    - **Parses chat data**: Uses regular expressions to extract messages, users, and timestamps from the exported chat file.
    - **Handles both 12-hour and 24-hour time formats**: Supports various timestamp formats, such as `13/07/22, 14:43` and `03/03/24, 8:23 PM`.
    - **Extracts metadata**: Converts timestamps to Pandas `datetime` objects and creates new columns such as `year`, `month`, `day`, `hour`, and more.
    - **User/message extraction**: Splits user names and messages and handles group notifications.

    
