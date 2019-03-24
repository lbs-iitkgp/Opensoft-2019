from dotenv import load
import os

load("../.env")
ENV = os.environ


# Use like:
#
# from env import ENV
# with open("{}/CaseDocuments/All_FT/{}".format(ENV["DATASET_PATH"], case_filename)) as f:
