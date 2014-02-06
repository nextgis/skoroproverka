# encoding: utf8

from pyramid.response import Response
from pyramid.view import view_config

from sqlalchemy.exc import DBAPIError

from .models import (
    DBSession,
    Genproc,
    )

# Максимальное количество возвращаемых записей
LIMIT = 100

@view_config(route_name='id', renderer='json')
def genpoc_by_id(request):

    dbsession = DBSession()

    id = request.matchdict['id']
    row = dbsession.query(Genproc).filter_by(id=id).one()

    result = {
        'id': row.id,
        'name': row.name,
        'ogrn': row.ogrn,
        'inn': row.inn,
         'addrloc_jur': row.addrloc_jur,
        'addrloc_ip': row.addrloc_ip,
        'addr_act': row.addr_act,
        'addr_obj': row.addr_obj,
        'goal': row.goal,
        'osn_datestart':row.osn_datestart,
        'osn_dateend': row.osn_dateend,
        'osn_datestart2': row.osn_datestart2,
        'osn_other': row.osn_other,
        'check_month': row.check_month,
        'check_days': row.check_days,
        'check_hours': row.check_hours,
        'check_form': row.check_form,
        'check_org': row.check_org
    }

    return result

@view_config(route_name='ogrn', renderer='json')
def genpoc_by_ogrn(request):

    dbsession = DBSession()

    ogrn = request.matchdict['ogrn']
    rows = dbsession.query(Genproc).filter_by(ogrn=ogrn).all()

    result = []
    for row in rows:
        data = {
            'id': row.id,
            'name': row.name,
            'ogrn': row.ogrn,
            'inn': row.inn,
             'addrloc_jur': row.addrloc_jur,
            'addrloc_ip': row.addrloc_ip,
            'addr_act': row.addr_act,
            'addr_obj': row.addr_obj,
            'goal': row.goal,
            'osn_datestart':row.osn_datestart,
            'osn_dateend': row.osn_dateend,
            'osn_datestart2': row.osn_datestart2,
            'osn_other': row.osn_other,
            'check_month': row.check_month,
            'check_days': row.check_days,
            'check_hours': row.check_hours,
            'check_form': row.check_form,
            'check_org': row.check_org
        }
        result.append(data)

    return result


@view_config(route_name='substr', renderer='json')
def substr(request):

    dbsession = DBSession()

    substr = request.matchdict['substr'].encode('utf-8')
    tmp_str = substr.strip()

    # Определяем, производить ли поиск по имени или же
    # по номеру компании или ИНН
    if tmp_str.isdigit():
        name_search = False
    else:
        name_search = True

    if name_search:
        # Поиск по подстроке в названии организации
        like_str = "%{0}%".format(substr)
        rows = dbsession.query(Genproc).filter(Genproc.name.ilike(like_str)).limit(LIMIT)
    else:
        if len(tmp_str) in [13, 15]:
            # Поиск по номеру ogrn
            print ''
            rows = dbsession.query(Genproc).filter_by(ogrn=tmp_str).all()
        elif len(tmp_str) in [10, 12]:
            # Поиск по ИНН
            rows = dbsession.query(Genproc).filter_by(inn=tmp_str).all()
        else:
            return {'error': 'Incorrect number format. '
                             'If you are searching an organization name,'
                             'use letters in the searching string.'}

    result = []
    for row in rows:
        result.append({'id': row.id, 'name': row.name, 'ogrn': row.ogrn, 'inn': row.inn})

    return result
