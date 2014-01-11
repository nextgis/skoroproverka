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

    return {'id': row.id, 'name': row.name, 'orgn': row.orgn.decode('utf8'), 'inn': row.inn}


@view_config(route_name='substr', renderer='json')
def substr(request):

    dbsession = DBSession()

    substr = request.matchdict['substr'].encode('utf-8')
    print substr
    like_str = "%{0}%".format(substr)
    print like_str
    rows = dbsession.query(Genproc).filter(Genproc.name.ilike(like_str)).limit(LIMIT)
    result = []
    for row in rows:
        result.append({'id': row.id, 'name': row.name, 'orgn': row.orgn, 'inn': row.inn})

    return result
