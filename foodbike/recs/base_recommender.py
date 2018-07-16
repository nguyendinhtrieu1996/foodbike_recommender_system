# from abc import ABCMeta, abstractmethod
import abc
ABC = abc.ABCMeta('ABC', (object,), {'__slots__': ()})

class base_recommender(ABC):
    @abc.abstractmethod
    def predict_score(self, user_id, item_id):
        pass

    @abc.abstractmethod
    def recommend_items(self, user_id, num=6):
        pass
