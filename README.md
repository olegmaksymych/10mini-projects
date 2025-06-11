# 10mini-projects
A showcase of 10 Python mini-projects demonstrating diverse skills: Snake Game, Pong, SMS Rain Alert App, Pomodoro Timer GUI, CLI and GUI Password Managers, Email Sender &amp; Date Manager, CSV Data Analysis, Stock Price SMS Alerts, and Flight Deal Finder. Each project highlights game development, GUI design, API integration, or data processing.

```markdown
# Mini-Projects Portfolio

Welcome to my collection of Python mini-projects! Each of these 10 projects helped me sharpen different skills—from game development and GUI design to API integration and data analysis. Feel free to explore the code and see how I tackled each challenge.

## 1. Snake Game
A modern take on the classic Snake arcade game using Pygame. Features dynamic movement, food spawning, self-collision detection, and real-time score tracking.

## 2. Pong
Recreated the timeless two-player paddle game with Python and Pygame. Implements ball physics, paddle controls, collision responses, and adjustable game speed.

## 3. SMS Rain Alert App
A command-line tool that fetches weather forecasts and uses the Twilio API to send daily SMS reminders when rain is predicted—securing API keys via environment variables.

## 4. Pomodoro Timer GUI
A desktop Pomodoro timer built in Tkinter. Includes customizable work/break intervals, start/stop controls, popup notifications, and sound alerts.

## 5. CLI Password Manager
A secure command-line credential store. Prompts for a master password, encrypts entries with AES, and saves them to a local file—no plaintext exposure.

## 6. Workout Tracking Using Google Sheets
A Python CLI tool that lets users log workouts in natural language and automatically tracks calories burned and workout details in a Google Sheet.

## 7. Email Sender & Date Manager
A script that combines Python’s `smtplib` and `datetime` modules to send templated emails with dynamic date handling and command-line scheduling options.

## 8. CSV Data Analysis
An end-to-end data cleaning and visualization pipeline using Pandas. Processes large CSV files in chunks, performs aggregation, and creates plots with Matplotlib and Seaborn.

## 9. Stock Price SMS Alerts
Monitors real-time stock prices via a financial API and sends threshold-based SMS alerts using Twilio. Logs all alerts and prevents duplicate notifications.

## 10. Flight Deal Finder
Automates flight-deal tracking by reading destinations and price thresholds from Google Sheets, querying a flight-search API daily, and alerting via SMS when low fares arise.

---
1. Snake Game
   * Rendered grid and snake via Pygame
   * Managed real-time arrow-key input for movement
   * Implemented food spawning, growth, self-collision logic
   * Tracked score and added restart functionality

 2. Pong
   * Programmed paddle and ball physics with velocity vectors
   * Detected collisions with walls/paddles and updated direction
   * Maintained player scores and serve/reset rules
   * Introduced adjustable game speed

3. SMS Rain Alert App
   * Loaded Twilio credentials securely via environment variables
   * Fetched weather forecasts from a public API
   * Scheduled daily checks and triggered SMS reminders when rain predicted

4. Pomodoro Timer GUI
   * Designed start/stop buttons and countdown display in Tkinter
   * Managed work/break intervals and state transitions
   * Implemented pop-up notifications and sounds on interval end

5. CLI Password Manager
   * Captured user input with `getpass` for master password
   * Encrypted/decrypted stored credentials using AES
   * Saved to and read from a local file, preventing plaintext exposure

6. Workout Tracking Using Google Sheets
   * A Python CLI that parses natural-language workout entries (e.g., “30 min yoga”), fetches duration and calories via Nutritionix’s Exercise API, and timestamps each session.
   * Securely manages credentials through environment variables (APP_ID, API_KEY, SHEETY_TOKEN) and sends structured workout data to a Google Sheet using the Sheety API.
   * Automates end-to-end workout logging—input, calorie computation, and cloud storage—without manual spreadsheet editing.

7. Email Sender & Date Manager
   * Sent templated emails via `smtplib`
   * Parsed and formatted dates with the `datetime` module
   * Supported command-line arguments for recipients and schedule

8. CSV Data Analysis
   * Loaded large CSVs in chunks with Pandas
   * Cleaned and transformed data (fill/NA, type casts)
   * Performed group-by aggregations and statistical summaries
   * Generated visualizations (histograms, line plots)

9. Stock Price SMS Alerts
    * Retrieved real-time quotes via a finance API
    * Detected ±5% moves and triggered Twilio SMS alerts
    * Logged alerts and ensured no duplicate notifications

10. Flight Deal Finder
    * Pulled destination lists and price thresholds from Google Sheets API
    * Queried a flight-search API daily for six-month windows
    * Compared to historical lows and SMS-alerted via Twilio when a deal appeared

---
Feel free to clone this repo and explore each project’s folder for setup instructions, dependencies, and code walkthroughs. Enjoy!  
```
