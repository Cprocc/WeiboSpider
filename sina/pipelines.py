import pymongo
from pymongo.errors import DuplicateKeyError
from sina.items import RelationshipsItem, TweetsItem, FansInformationItem, CommentItem, CommentsInformationItem, \
    RepostItem, RepostInformationItem, LikeItem, LikeInformationItem
from sina.settings import LOCAL_MONGO_HOST, LOCAL_MONGO_PORT, DB_NAME


class MongoDBPipeline(object):
    def __init__(self):
        client = pymongo.MongoClient(LOCAL_MONGO_HOST, LOCAL_MONGO_PORT)
        db = client[DB_NAME]
        self.Information = db["Fans_Information"]
        self.Tweets = db["Tweets"]
        self.Comments = db["Comments"]
        self.Relationships = db["Relationships"]
        self.Comments_Information = db["Comments_Information"]
        self.Repost = db["Repost"]
        self.Repost_Informations = db["Repost_Informations"]
        self.Like = db["Like"]
        self.Like_Informations = db["Like_Informations"]

    def process_item(self, item, spider):
        """ 判断item的类型，并作相应的处理，再入数据库 """
        if isinstance(item, RelationshipsItem):
            self.insert_item(self.Relationships, item)
        # elif isinstance(item, TweetsItem):
        #     self.insert_item(self.Tweets, item)
        # elif isinstance(item, FansInformationItem):
        #     self.insert_item(self.Information, item)

        elif isinstance(item, CommentItem):
            self.insert_item(self.Comments, item)
        elif isinstance(item, CommentsInformationItem):
            self.insert_item(self.Comments_Information, item)
        elif isinstance(item, RepostItem):
            self.insert_item(self.Repost, item)
        elif isinstance(item, RepostInformationItem):
            self.insert_item(self.Repost_Informations, item)
        elif isinstance(item, LikeItem):
            self.insert_item(self.Like, item)
        elif isinstance(item, LikeInformationItem):
            self.insert_item(self.Like_Informations, item)
        return item

    @staticmethod
    def insert_item(collection, item):
        try:
            collection.insert(dict(item))
        except DuplicateKeyError:
            """
            说明有重复数据
            """
            pass