PROJECTNAME = "collective.folderishtypes"


def schema_cleanup(schema):
    """ Cleanup a schema to prepare it to be merged with another one.
        ATCT Schema definitions are not simple lists or dicts, so there is
        some manual interaction neccessary.
    """
    for key in [
        'id', 'title', 'description', 'subject', 'relatedItems', 'location',
        'language', 'effectiveDate', 'expirationDate', 'creation_date',
        'modification_date', 'creators', 'contributors', 'rights',
        'allowDiscussion', 'excludeFromNav'
    ]:
        if key in schema:
            del schema[key]
    return schema
