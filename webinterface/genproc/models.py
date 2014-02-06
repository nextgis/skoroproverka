# encoding: utf8

from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
    event,
    DDL
)

from sqlalchemy.types import UserDefinedType

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import (
    scoped_session,
    sessionmaker
)

from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()

###########################################################################################
# Поддержка полнотекстового поиска.
# В основе реализации лежит статья:
#   http://nibrahim.net.in/2013/11/29/sqlalchemy_and_full_text_searching_in_postgresql.html
###########################################################################################

class TsVector(UserDefinedType):
    "Holds a TsVector column"

    name = "TSVECTOR"

    def get_col_spec(self):
        return self.name



###########################################################################################
# Описание основной базы:
###########################################################################################

class Genproc(Base):
    __tablename__ = 'genproc'
    __table_args__ = (Index('details_tsvector_idx', 'details_tsvector', postgresql_using = 'gin'),)

    id = Column(Integer, primary_key=True)

    # Далее идут оригинальные поля,
    # но к полю id от генпрокуратуры добавлен
    # префикс genproc_
    genproc_id = Column(Text)
    subid = Column(Text)
    url = Column(Text)
    name = Column(Text, nullable=False, index=True)
    addrloc_jur = Column(Text)
    addrloc_ip = Column(Text)
    addr_act = Column(Text)
    addr_obj = Column(Text)
    orgn = Column(Text, index=True)
    inn = Column(Text, index=True)
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

    details_tsvector = Column(TsVector)

# Триггер на таблицу genproc
trigger_snippet = DDL("""
    CREATE TRIGGER details_tsvector_update BEFORE INSERT OR UPDATE
    ON genproc
    FOR EACH ROW EXECUTE PROCEDURE
    tsvector_update_trigger(details_tsvector,'pg_catalog.russian', 'name')
""")

event.listen(Genproc.__table__, 'after_create', trigger_snippet.execute_if(dialect = 'postgresql'))

