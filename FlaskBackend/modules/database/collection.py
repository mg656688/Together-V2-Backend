from pymongo import MongoClient
from bson import ObjectId


client = MongoClient("mongodb+srv://admin:admin1234@together.cvq6ffb.mongodb.net/?retryWrites=true&w=majority")

db = client.seedlings
seedlings = db.seedlings
pollution_report = db.report
crop = db.crop
flowers = db.flower
leaves = db.leaf
paddy = db.paddy
weeds = db.weed


def addSeedlingImage(i_name, Type, time, url):
    seedlings.insert({
        "file_name": i_name,
        "prediction": Type,
        "upload_time": time,
        "url": url
    })


def addFlowerImage(i_name, Type, time, url):
    flowers.insert({
        "file_name": i_name,
        "prediction": Type,
        "upload_time": time,
        "url": url
    })


def addLeaveImage(i_name, Type, time, url):
    leaves.insert({
        "file_name": i_name,
        "prediction": Type,
        "upload_time": time,
        "url": url
    })


def addWeedImage(i_name, Type, time, url):
    weeds.insert({
        "file_name": i_name,
        "prediction": Type,
        "upload_time": time,
        "url": url
    })


def addPaddyImage(i_name, Type, time, url):
    paddy.insert({
        "file_name": i_name,
        "prediction": Type,
        "upload_time": time,
        "url": url
    })


def cropRecommendation(Type, time):
    crop.insert({
        "prediction": Type,
        "upload_time": time
    })


def pollutionReport(image, time, location):
    pollution_report.insert({
        "prediction": image,
        "upload_time": time,
        "location": location
    })
