from plone.app.content.interfaces import INameFromTitle
from zope.component import getUtility
from zope.interface import implements


class INameGenerator(INameFromTitle):
    """Behavior interface.
    """


class NameGenerator(object):
    """Customized name from title behavior."
    """

    implements(INameGenerator)


    def __init__(self, context):
        self.context = context

    @property
    def title(self):
        import pdb;pdb.set_trace()
        folder = self.context.aq_parent
        import pdb;pdb.set_trace()
        ids = [i[0] for i in 
                folder.contentItems(
                    filter={'portal_type': ('wt.testrig.foo',)})]
        ids.remove(obj.id)
        if len(ids) > 0:
            ids.sort()
            new_id = ids[-1]
            new_id = int(new_id) + 1
            new_id = '%d' % new_id
        else:
            new_id = '1'
        # YOUR IMPLEMENTATION
        title = new_id

        return title