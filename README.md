# Simple Mastodon Image Poster Bot

Posts a random picture from a folder to your mastodon account. Then, it moves the picture in another folder (so it does not get posted again).

The script checks if it already posted that image (in case it was saved twice in the same folder). In that case, the image will be moved in the "Errors" folder.

If an error occurs, it will be moved to the "Errors" folder.

A log will be created, so you know what happens each time the script is run.

## Inital Setup

Clone the repository or download all files. In the folder, open a console and do the following:

 _Create a virtual environment_
```
  python3 -m venv venv
  source venv/bin/activate
  pip install -r requirements.txt
```

_Fill out config.ini.example_

Fill it out as you need. If you want to run the script via Cron, you should specify the full path to folders. You will find the client_secret if you create a new application on your mastodon account on your instance (under "Development"). You could also rename "config.ini.example" to "config.ini"

"this_folder" should point to a folder that contains three folders: "Errors", "Files" and "UsedFiles". "Files" should contain all images you'd like to post, "UsedFiles" are images that were posted, "Errors" are images that produced an error somehow.

You may want to change the "Message_To_Post" in Poster.py and disable the "Contentwarning" (default is "True"). I did not put this in the config.ini because in your use case, the message and warning may depend on the picture chosen.

## Calling the script
```
path/to/venv/bin/python path/to/script/Poster.py path/to/config/config.ini
```
