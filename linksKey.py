#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Get permission from app.

:param key: key from app
:return: keys from the apps founds.
"""
from tacyt import TacytApp
from maltego.MaltegoTransform import *
from APIManagement import Tacyt
from maltego.Entities import TacytEntities as te

api = TacytApp.TacytApp(Tacyt.APP_ID, Tacyt.SECRET_KEY)
m = MaltegoTransform()

app = sys.argv[1]


try:
    result = api.get_app_details(app)
    data = result.get_data()

    if 'result' in data and data['result'] is not None:
        details = data['result']

        if 'links' in details:
            l_links = details['links']
            for i in l_links:
                m.addEntity(te.DOMAIN,i, te.FIELD_NAME, 'permissionName')

        m.returnOutput()

    else:
        m.addException("The search returns null results")
        m.throwExceptions()

except Exception as e:
    m.addException(str(e))
    m.throwExceptions()

