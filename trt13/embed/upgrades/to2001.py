
# -*- coding: utf-8 -*-

PROJECT = 'trt13.embed'


def from2000(context):
    ''' Upgrade from 2000 to version 2001'''

    from plone import api
    setup = api.portal.get_tool('portal_setup')
    profile = 'profile-{}:default'.format(PROJECT)
    setup.runImportStepFromProfile(profile, 'typeinfo')

