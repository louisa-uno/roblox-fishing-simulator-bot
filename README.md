# Roblox Fishing Simulator Automation Bot

This script provides automated mouse and keyboard actions to simulate fishing in the roblox game Fishing Simulator. It uses image recognition to detect fish and air bubbles on the screen and performs actions accordingly.

> **Note**: This is a project I made a while ago and just wanted to share with the community. While I don't plan on further developing it, I'll still maintain it and address any issues that may arise.

> **Disclaimer**: Using this script can theoretically get you banned from the game or Roblox platform. Use at your own risk and always respect the terms of service of the game and platform.

## Features

-   Simulates mouse clicks and movements.
-   Detects fish and air bubbles using pixel color recognition.
-   Randomized click timings to simulate human-like interactions.
-   Adjusts to the difficult of fish, making sure the fishing meter stays on center.
-   Keeps track of the number of fish caught.
-   Automatically sells if inventory is full. (Only if you bought gamepass.)

## Prerequisites

-   Python 3.8

## Installation for Windows

1. Clone the repository:

```batch
git clone https://github.com/KristianCorrea/roblox-fishing-simulator-bot
```

2. Navigate to the project directory:

```batch
cd roblox-fishing-simulator-bot
```

3. Install the required packages:

```batch
pip install -r requirements.txt
```

## Usage

1. Edit the Coordinate Variables on the bot.py to adjust to your screen/game.
1. Start the roblox game Fishing Simulator
2. Position the game window such that the script can detect the necessary pixels (Fullscreen is recommended on a 1920x1080 screen)
3. Run the script:

```batch
python bot.py
```

4. The script will start simulating fishing actions. Press 'q' to stop the script.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the AGPL-3.0 License - see the [LICENSE](LICENSE) file for details.
