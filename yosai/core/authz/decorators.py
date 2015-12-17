import functools
from yosai.core import (
    SecurityUtils,
)


def requires_permission(permission_s, logical_operator=all):
    """
    Requires that the calling Subject be authorized to the extent that is
    required to satisfy the permission_s specified and the logical operation
    upon them.

    :param permission_s:   the permission(s) required
    :type permission_s:  a List of Strings or List of Permission instances

    :param logical_operator:  indicates whether all or at least one permission
                              is true (and, any)
    :type: and OR all (from python standard library)

    Elaborate Example:
        requires_permission(
            permission_s=['domain1:action1,action2', 'domain2:action1'],
            logical_operator=any)

    Basic Example:
        requires_permission('domain1:action1,action2')
    """
    def outer_wrap(fn):
        @functools.wraps(fn)
        def inner_wrap(*args, **kwargs):

            subject = SecurityUtils.get_subject()

            subject.check_permission(permission_s, logical_operator)

            return fn(*args, **kwargs)
        return inner_wrap
    return outer_wrap


def requires_role(roleid_s, logical_operator=all):
    """
    Requires that the calling Subject be authorized to the extent that is
    required to satisfy the roleid_s specified and the logical operation
    upon them.

    :param roleid_s:   a collection of the role(s) required, specified by
                       identifiers (such as a role name)
    :type roleid_s:  a List of Strings

    :param logical_operator:  indicates whether all or at least one permission
                              is true (and, any)
    :type: and OR all (from python standard library)

    Elaborate Example:
        requires_role(roleid_s=['sysadmin', 'developer'], logical_operator=any)

    Basic Example:
        requires_role('physician')
    """
    def outer_wrap(fn):
        @functools.wraps(fn)
        def inner_wrap(*args, **kwargs):

            subject = SecurityUtils.get_subject()

            subject.check_role(roleid_s, logical_operator)

            return fn(*args, **kwargs)
        return inner_wrap
    return outer_wrap