from django.http import Http404

class Post():
    
    POSTS = [
            {'id':1,'title':'first article','body':'This is my first article'},
            {'id':2,'title':'second article','body':'This is my second article'},
            {'id':3,'title':'third article','body':'This is my third article'}
        ]

    @classmethod
    def all(cls):
        return cls.POSTS

    
    @classmethod
    def find(cls, id):
        try:
            return cls.POSTS[int(id) - 1]
        except:
            raise Http404("Oups ! pas de post #{} retouvé".format(id))




