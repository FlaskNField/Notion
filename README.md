# Notion Members Export Script

This Python script retrieves and lists all members (users) from your Notion workspace using the Notion API.

## Features
- Connects to the Notion API using your integration token
- Fetches all users in your Notion workspace (with pagination support)
- Prints each user's name and Notion ID

## Requirements
- Python 3.7+
- [notion-client](https://github.com/ramnes/notion-sdk-py)

## Installation
1. Clone this repository or download the script.
2. Install the required package:
   ```
   pip install notion-client
   ```

## Setup
1. [Create a Notion integration](https://developers.notion.com/docs/create-a-notion-integration) and obtain your integration token.
2. Replace the placeholder `YOUR_NOTION_INTEGRATION_TOKEN` in the script with your actual integration token.

## Usage
Run the script with Python:
