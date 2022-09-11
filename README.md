# Discord FAQ AI Bot
## A ShellHacks 2022 Hackathon Project Submission
### Category:  In-person
---
## Contents

- [Project Description and Overview](#project-description-and-overview)
- [Development Methodology](#development-methodology)
- [GitHub Repository](#github-repository)
- [Contact Me](#contact-me)
- [License](#license)

---

### Project Description and Overview

Quite often, in Discord servers created for events like ShellHacks or for other communities such as in the education space, questions and requests posted have previously already been asked and answered by others.  Consequently, the server's moderators and other community members end up posting redundant responses.  The Discord FAQ AI Bot was developed to address this issue and improve the overall experience for Discord community members.

The bot monitors chats 24/7 and uses a trained machine learning model to predict whether a new post is a question or request that has been routinely posted on Discord in the past.  The bot will generate a confidence score ranging from 0 to 1 (or 0% to 100%) that the post is similar to previous ones.  If the score is greater than 50%, the bot directly replies to the original poster with a statement about its prediction and directing them to a linked FAQ document.

---

<a href="https://ibb.co/gdXhXgQ"><img src="https://i.ibb.co/f9KLK0Z/Screen-Shot-2022-09-11-at-9-44-26-AM.png" alt="Screen-Shot-2022-09-11-at-9-44-26-AM" border="0"></a>

---

Since a bot must be trained on historical data for that particular server (and channel), for the purpose of this hackathon, data from the UPE Discord server #shellhacks channel for ShellHacks 2022 was used.

To test the bot, a new Discord server for _SmellHacks 2022_ (not a typo) was created for a hackathon also taking place this weekend on Earth-515 from the multiverse.  (In this parallel Earth, deodorant was never invented.)  A mock FAQ document likewise was created.

Anyone with a Discord account - even from our Earth - can join this server [here](https://discord.gg/SJAFrWYz) and test it out.

---

## Development Methodology

### Create Discord Server and Bot

- To provide a test environment for the AI Bot, a new Discord server was created.
- A developer account was used to create a bot with permissions to send messages.

### Download Historic Discord Data and Clean

- The Chrome Discordmate extension was used to download historic data from the UPE Discord server and #shellhacks channel.  (For the purpose of the training model used, 200 recent chat entries were used.)
- Extraneous columns were deleted, leaving a single column consisting of the posts's text content.
- Each of the posts were labeled either TRUE (question) or FALSE (non-question) in a second column (to the right).
- The data was cleaned using the Python file clean_data.py located in this Github repo to remove posts with newline characters, remove non-ASCII characters, URLs, and duplicate entries (e.g., "Thanks!").

### Google Cloud Vertex AI

After registering for a Google Cloud account (and applying a $25 education credit kindly provided by Google), the Google Cloud Vertex AI service was utilized to build and deploy the machine learning model and prediction endpoint for the AI Bot.  This was comprised of the following tasks performed at the console UI:

- Creating and importing a text dataset using the cleaned data.
- Training the model using AutoML and single classification.
- Creating a prediction endpoint.

### Google Cloud Compute Engine (VM Instance)

After establishing Google ADC credentials, a Python script was created locally that controls the AI Bot's behavior as follows:

- Listen for new posts.
- Call the prediction endpoint (via a Google provided prediction Python script) with the new text.
- Send a reply message if the returned confidence prediction value is greater than 0.5; otherwise, take no action.

To accomplish the above, the following dependencies were used:

- discord 2.0.0
- multidict 6.0.2
- requests 2.28.1
- A variety of Google Cloud dependencies (consult official Google Cloud documentation for the most current list)

The Python scripts were then uploaded to a VM Instance on the Google Cloud Compute Engine and persistence established by first executing a tmux library dependency.

---

## GitHub Repository

This README.md file and all other files and source code is located at the following GitHub Repository:

https://github.com/liujohnj/discord-faq-bot

---

## Contact Me

LinkedIn:  https://www.linkedin.com/in/johnjliu

---

## License

[![License](http://img.shields.io/:license-mit-blue.svg?style=flat-square)](http://badges.mit-license.org)

- **[MIT license](http://opensource.org/licenses/mit-license.php)**

- Copyright © 2022
