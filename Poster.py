from mastodon import Mastodon
import random
from configparser import ConfigParser
import os
import sys
from datetime import datetime

conf = sys.argv[1]

CP = ConfigParser()
CP.read(conf)
abu = CP["mastodon"]["api_base_url"]
mcs = CP["mastodon"]["client_secret"]
login =  CP["mastodon"]["login"]
password = CP["mastodon"]["password"]

SourceFolder = CP["folders"]["this_folder"]

now = datetime.now()
current_time = now.strftime("%Y-%m-%d %H:%M:%S")

SF = SourceFolder + "Files/"
EF = SourceFolder + "Errors/"
TF = SourceFolder + "UsedFiles/"

Toot_Message = "Your toot message here"

try:
    if len(os.listdir(SF))>=1:
        FN = random.choice(os.listdir(SF))
        Filename = SF + FN


        Mastodon.create_app("Poster", api_base_url=abu, to_file=mcs)   
        Mastodon = Mastodon(client_id = mcs, api_base_url=abu)

        Mastodon.log_in(login, password, to_file = mcs)
        try:
            pic = Mastodon.media_post(Filename)

            with open(SourceFolder + "/Log.txt", "r") as file:
                NotHashes = file.read().splitlines()
            Hashes = []
            for Line in NotHashes:
                Hashes.append(Line.split(" - ")[-1])
            if pic["blurhash"] not in Hashes:
                result = ""
                result = Mastodon.status_post(Toot_Message, sensitive=True, media_ids=pic)
                with open(SourceFolder + "/Log.txt", "a") as file:
                    file.write(str(current_time) + " - " + str(FN) + " - " + str(len(os.listdir(SF))-1) + " - " + result["url"] + " - " + str(pic["blurhash"]))
                    file.write("\n")
                os.rename(Filename, TF + FN)
            else:
                with open(SourceFolder + "/Log.txt", "a") as file:
                    file.write(str(current_time) + " - " + str(FN) + " - Blurhash " + str(pic["blurhash"]) + " already posted.")
                    file.write("\n")
                os.rename(Filename, EF + FN)
        except Exception as er:
            try:
                os.rename(Filename, EF + FN)
                with open(SourceFolder + "/Log.txt", "a") as file:
                    file.write(str(current_time) + " - " + str(FN) + " - " + result["url"] + " - " + str(er))
                    file.write("\n")
            except Exception as err:
                with open(SourceFolder + "/Log.txt", "a") as file:
                    file.write(str(current_time) + " - " + str(FN) + " - " + str(err) + " - " + str(er))
                    file.write("\n")
             
        
    else:
        with open(SourceFolder + "/Log.txt", "a") as file:
            file.write(str(current_time) + " - Folder empty.")
            file.write("\n")
except Exception as e:
        with open(SourceFolder + "/Log.txt", "a") as file:
            file.write(str(current_time) + " - " + str(e))
            file.write("\n")





