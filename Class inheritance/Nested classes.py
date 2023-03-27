# You can do without nested classes, this is more for Django
# you can create an instance of a nested class,
    # self.meta = self.Meta(user + '@' + psw) # instantiate Meta
    # BUT CANNOT BE CREATED IN A NESTED INSTANCE OF THE BASE CLASS


class Women:
    title = 'title fields'
    photo = 'photo fields'
    ordering = 'ordering fields'


    def __init__(self, user, psw):
        self.user = user
        self.psw = psw
        self.meta = self.Meta(user + '@' + psw) # create Meta instance


    class Meta:
        ordering = ['id']

        def __init__(self, access): # now, when we create Meta instance we should pass 1 argument
            self.access = access


w = Women('root', '12345')
# print(w.ordering)
# print(w.Meta.ordering)
print(w.__dict__)
print(w.meta.__dict__)

