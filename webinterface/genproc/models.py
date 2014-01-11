# encoding: utf8

from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text
)

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import (
    scoped_session,
    sessionmaker
)

from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()


class Genproc(Base):
    __tablename__ = 'genproc'
    id = Column(Integer, primary_key=True)

    # Далее идут оригинальные поля,
    # но к полю id от генпрокуратуры добавлен
    # префикс genproc_
    genproc_id = Column(Text, nullable=False)
    subid = Column(Text)
    url = Column(Text)
    name = Column(Text, nullable=False, index=True)
    addrloc_jur = Column(Text)
    addrloc_ip = Column(Text)
    addr_act = Column(Text)
    addr_obj = Column(Text)
    ogrn = Column(Text, nullable=False, index=True)
    inn = Column(Text, nullable=False, index=True)
    goal = Column(Text)
    osn_datestart = Column(Text)
    osn_dateend = Column(Text)
    osn_datestart2 = Column(Text)
    osn_other = Column(Text)
    check_month = Column(Text)
    check_days = Column(Text)
    check_hours = Column(Text)
    check_form = Column(Text)
    check_org = Column(Text)

