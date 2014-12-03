from five import grok

from z3c.form import group, field
from zope import schema
from zope.interface import invariant, Invalid
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm

from plone.dexterity.content import Container

from plone.directives import dexterity, form
from plone.app.textfield import RichText
from plone.namedfile.field import NamedImage, NamedFile
from plone.namedfile.field import NamedBlobImage, NamedBlobFile
from plone.namedfile.interfaces import IImageScaleTraversable

from z3c.relationfield.schema import RelationList, RelationChoice
from plone.formwidget.contenttree import ObjPathSourceBinder
from zope.lifecycleevent.interfaces import IObjectAddedEvent
from plone import api


from wt.testrig import MessageFactory as _


# Interface class; used to define content-type schema.

class IFoo(form.Schema, IImageScaleTraversable):
    """
    Description of the Example Type
    """

    # If you want a schema-defined interface, delete the model.load
    # line below and delete the matching file in the models sub-directory.
    # If you want a model-based interface, edit
    # models/foo.xml to define the content type.

    form.model("models/foo.xml")


#
#@grok.subscribe(IFoo, IObjectAddedEvent)
#def renameId(obj, event):
#    folder = obj.aq_parent
#    ids = [i[0] for i in 
#            folder.contentItems(
#                filter={'portal_type': ('wt.testrig.foo',)})]
#    ids.remove(obj.id)
#    if len(ids) > 0:
#        ids.sort()
#        new_id = ids[-1]
#        new_id = int(new_id) + 1
#        new_id = '%d' % new_id
#    else:
#        new_id = '1'
#    obj.jobNumber = new_id
#    api.content.rename(obj, new_id)

# Custom content-type class; objects created for this content type will
# be instances of this class. Use this class to add content-type specific
# methods and properties. Put methods that are mainly useful for rendering
# in separate view classes.

class Foo(Container):
    grok.implements(IFoo)

    # Add your class methods and properties here
    pass


# View class
# The view will automatically use a similarly named template in
# foo_templates.
# Template filenames should be all lower case.
# The view will render when you request a content object with this
# interface with "/@@sampleview" appended.
# You may make this the default view for content objects
# of this type by uncommenting the grok.name line below or by
# changing the view class name and template filename to View / view.pt.

class SampleView(grok.View):
    """ sample view class """

    grok.context(IFoo)
    grok.require('zope2.View')

    # grok.name('view')

    # Add view methods here
