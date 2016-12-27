# -*- coding: utf-8 -*-


def import_browserlayer(context):
    context.runImportStepFromProfile(
        'profile-collective.folderishtypes:default',
        'browserlayer',
    )
