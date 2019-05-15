""" Errors used by the Discussion API. """
from __future__ import absolute_import
from django.core.exceptions import ObjectDoesNotExist


class DiscussionDisabledError(ObjectDoesNotExist):
    """ Discussion is disabled. """
    pass


class ThreadNotFoundError(ObjectDoesNotExist):
    """ Thread was not found. """
    pass


class CommentNotFoundError(ObjectDoesNotExist):
    """ Comment was not found. """
    pass
