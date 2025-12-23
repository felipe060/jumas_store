from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, Date, DateTime, Float, text, Boolean, sql, update, func
from sqlalchemy.orm import sessionmaker, declarative_base, relationship, query
from dotenv import find_dotenv, load_dotenv
from os import getenv, environ
from datetime import datetime as datetime_, timedelta

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

engine = create_engine("postgresql+psycopg2://", query_cache_size=0, echo=True, pool_size=5, max_overflow=10,
                       pool_timeout=30, connect_args=dict(user=environ.get("DB_USER"), password=environ.get("DB_PASSWORD"),
                                         host=environ.get("DB_HOST"), database=environ.get("DB_DATABASE"),
                                         sslmode=environ.get("DB_SSL_MODE"),
                                         channel_binding=environ.get("DB_CHANNEL_BINDING")))

Base = declarative_base()
Session = sessionmaker(bind=engine, autoflush=False, autocommit=False)


class User(Base):
    __tablename__ = "tb_users"

    user_id = Column(Integer, autoincrement=True, nullable=False, primary_key=True)
    user_email = Column(String(255), unique=True, nullable=False)
    user_senha = Column(String(255), nullable=False)
    name = Column(String(80), nullable=False, unique=False)
    surname = Column(String(80), nullable=True, unique=False)
    cpf = Column(String(20), nullable=True)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, nullable=False, default=func.now())

    user_sessioncode = relationship("SessionCode", back_populates="id_usuario")


class SessionCode(Base):
    __tablename__ = "tb_sessioncode"

    sessioncode_id = Column(Integer, autoincrement=True, nullable=False, primary_key=True)
    user_id = Column(Integer, ForeignKey("tb_users.user_id"), nullable=False)
    sessioncode = Column(String(255), nullable=False)
    created_at = Column(DateTime, nullable=False, default=str(datetime_.now())[:-7])
    expires_at = Column(DateTime, nullable=False, default=str(datetime_.now()+timedelta(minutes=10))[:-7])

    id_usuario = relationship("User", back_populates="user_sessioncode")


class Address(Base):
    __tablename__ = "tb_addresses"

    address_id = Column(Integer, autoincrement=True, nullable=False, primary_key=True)


#Base.metadata.create_all(engine)




"""with Session() as session:
    novo = SessionCode(user_id=2, sessioncode="aq_o_sessioncode")
    session.add(novo)
    session.commit()
    #sqlalchemy.exc.IntegrityError: (psycopg2.errors.ForeignKeyViolation) insert or update on table "tb_sessioncode" violates foreign key constraint "tb_sessioncode_user_id_fkey"
    """


"""with Session() as session:
    consulta = session.query(User.user_email).where(User.user_id == 2).first()
    #consulta = session.query(User).where(User.user_id == 2).first()
    print("")
    print(consulta)
    print(consulta.user_email)
    ala = consulta.user_email
    #print(consulta.is_active)"""




"""adicionar = User(user_email="sofia@hotmail.com", user_senha="senha_sofia", name="sofia")
with Session() as session:
    session.add(adicionar)
    session.commit()

    #sqlalchemy.exc.IntegrityError: (psycopg2.errors.UniqueViolation) duplicate key value violates unique constraint "tb_users_user_email_key"""








"""ola = datetime_.now()
print(ola)
oi = ola + timedelta(minutes=200)
print("--> ", oi)"""



"""class User(Base):
    __tablename__ = "tb_user"

    id_user = sql_column(sql_integer, autoincrement=True, nullable=False, primary_key=True)
    email_user = sql_column(sql_string(80), nullable=False, unique=True)
    senha_user = sql_column(sql_string(80), nullable=False, unique=False)
    active = sql_column(sql_boolean, nullable=False, default=True)
    date = sql_column(sql_datetime, nullable=False)

    sessioncode_ = relationship("SessionCode", back_populates="person_")


class SessionCode(Base):
    __tablename__ = "tb_sessioncode"

    id_sessioncode = sql_column(sql_integer, autoincrement=True, nullable=False, primary_key=True)
    sessioncode = sql_column(sql_string, nullable=False, unique=True)
    lifetime = sql_column(sql_datetime, nullable=False)
    id_user = sql_column(sql_integer, ForeignKey("tb_user.id_user"),  nullable=False)

    person_ = relationship("User", back_populates="sessioncode_")"""




"""hora_agr = datetime_.now()
futuro = hora_agr + timedelta(minutes=1)
print("hora agr--> ", hora_agr)
print("futuro --> ", futuro)

seila = "2025-12-23 13:28:16"
format_string = '%Y-%m-%d %H:%M:%S'

datetime_object = datetime_.strptime(seila, format_string)

print("--> ", datetime_object)
print("type --> ", type(datetime_object))

if futuro > hora_agr:
    print("seila")
else:
    print("oloco")"""