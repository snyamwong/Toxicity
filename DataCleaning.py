import json


output = []
#files = ["RC_2016-01", "RC_2016-02", "RC_2016-03", "RC_2016-04",
#         "RC_2016-05", "RC_2016-06", "RC_2016-07", "RC_2016-08",
#         "RC_2016-09", "RC_2016-10", "RC_2016-11", "RC_2016-12"]

files = ["RC_2016-09", "RC_2016-10", "RC_2016-11", "RC_2016-12"]
# for rerunning b/c "ups" field was depreciated for the "score" field

target_subreddits = ["the_donald", "hillaryclinton", "sandersforpresident", "politics", "rarepuppers"]

TD = 0
HC = 0
BS = 0
POLITIC = 0
PUPPERS = 0

for file in files:
    print("File: {}".format(file))
    with open('../Reddit-Comments/{}'.format(file), 'r') as test:
        for _ in range(0, 5):
            for obj in test:
                x = json.loads(obj)
                if x["subreddit"].lower() in target_subreddits and x["body"].lower() != "[deleted]":
                    outputDict = {}
                    try:
                        outputDict.update([("subreddit", x["subreddit"].lower()), ("author", x["author"].lower()),
                                           ("body", x["body"].lower()), ("gilded", x["gilded"]),
                                           ("controversiality", x["controversiality"]), ("ups", x["ups"])])
                        output.append(outputDict)
                        if outputDict["subreddit"] == "the_donald":
                            TD += 1
                        elif outputDict["subreddit"] == "hillaryclinton":
                            HC += 1
                        elif outputDict["subreddit"] == "sandersforpresident":
                            BS += 1
                        elif outputDict["subreddit"] == "politics":
                            POLITIC += 1
                        elif outputDict["subreddit"] == "rarepuppers":
                            PUPPERS += 1
                        else:
                            print("Unexpected subreddit, Subreddit = {}".format(outputDict["subreddit"]))
                            print(outputDict)
                    except:
                        try:
                            outputDict.update([("subreddit", x["subreddit"].lower()), ("author", x["author"].lower()),
                                               ("body", x["body"].lower()), ("gilded", x["gilded"]),
                                               ("controversiality", x["controversiality"]), ("ups", x["score"])])
                            output.append(outputDict)
                            if outputDict["subreddit"] == "the_donald":
                                TD += 1
                            elif outputDict["subreddit"] == "hillaryclinton":
                                HC += 1
                            elif outputDict["subreddit"] == "sandersforpresident":
                                BS += 1
                            elif outputDict["subreddit"] == "politics":
                                POLITIC += 1
                            elif outputDict["subreddit"] == "rarepuppers":
                                PUPPERS += 1
                            else:
                                print("Unexpected subreddit, Subreddit = {}".format(outputDict["subreddit"]))
                                print(outputDict)
                        except:
                            print("Something else is f*cked...")
                            pass

    out_file = "../Clean-Reddit-Comments/clean{}".format(file)
    with open(out_file, 'a') as f:
        for data in output:
            f.write(json.dumps(data))
            f.write("\n")

    with open("../Clean-Reddit-Comments/{}stats".format(file), "w") as f:
        f.write("The_Donald Comments: {}\n".format(TD))
        f.write("HillaryClinton Comments: {}\n".format(HC))
        f.write("SandersForPresident Comments: {}\n".format(BS))
        f.write("Politics Comments: {}\n".format(POLITIC))
        f.write("RarePuppers Comments: {}\n".format(PUPPERS))
