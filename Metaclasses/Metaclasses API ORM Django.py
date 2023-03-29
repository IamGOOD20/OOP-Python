class Meta(type):
    def create_local_attrs(self, *args, **kwargs):
        for key, value in self.class_attrs.items():
            self.__dict__[key] = value

    def __init__(cls, name, basses, attrs): # cls is a link on class Women
        cls.class_attrs = attrs
        cls.__init__ = Meta.create_local_attrs


class Women(metaclass=Meta):
    title = 'title'
    content = 'content'
    photo = 'path photo'


# this metaclass works like this:
# class Women:
#     class_attrs = {'title': 'title', 'content': 'content', 'photo': 'path to photo'}
#     title = 'title'
#     content = 'content'
#     photo = 'path to photo'
#
#     def __init__(self, *args, **kwargs):
#         for key, value in self.class_attrs.items():
#             self.__dict__[key] = value


w = Women()

print(w.__dict__)