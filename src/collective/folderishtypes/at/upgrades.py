

def import_rolemap(context):
    context.runImportStepFromProfile(
        'profile-collective.folderishtypes.at:default',
        'rolemap',
    )


def import_skins(context):
    context.runImportStepFromProfile(
        'profile-collective.folderishtypes.at:default',
        'skins',
    )


def import_browserlayer(context):
    context.runImportStepFromProfile(
        'profile-collective.folderishtypes.at:default',
        'browserlayer',
    )
