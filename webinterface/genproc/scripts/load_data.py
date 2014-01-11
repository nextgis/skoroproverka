# -*- coding: utf-8 -*-

import csv

import transaction

from sqlalchemy import engine_from_config

from pyramid.paster import (
    get_appsettings,
    setup_logging,
    )

from ..models import (
    DBSession,
    Genproc,
    Base
)


fieldmap = (
    ("id", "genproc_id"),
    ("subid", "subid"),
    ("url", "url"),
    ("name", "name"),
    ("addrloc_jur", "addrloc_jur"),
    ("addrloc_ip", "addrloc_ip"),
    ("addr_act", "addr_act"),
    ("addr_obj", "addr_obj"),
    ("ogrn", "ogrn"),
    ("inn", "inn"),
    ("goal", "goal"),
    ("osn_datestart", "osn_datestart"),
    ("osn_dateend", "osn_dateend"),
    ("osn_datestart2", "osn_datestart2"),
    ("osn_other", "osn_other"),
    ("check_month", "check_month"),
    ("check_days", "check_days"),
    ("check_hours", "check_hours"),
    ("check_form", "check_form"),
    ("check_org", "check_org")
)

def load_data(file_name):
    print 'Importing...'
    f = csv.DictReader(open(file_name), delimiter=',', quotechar='"')
    with transaction.manager:
        for row in f:
            row = {k.lower(): v for k, v in row.iteritems()}
            line = Genproc()
            for source_name, target_name in fieldmap:
                setattr(line, target_name, None if row[source_name] == '' else row[source_name])
            DBSession.add(line)

