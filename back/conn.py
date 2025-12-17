from sqlalchemy import (create_engine, ForeignKey, Column as sql_column, String as sql_string,
                        Integer as sql_integer, Date as sql_date, DateTime as sql_datetime, Float as sql_float,
                        text as sql_text, Boolean as sql_boolean, sql, update)
from sqlalchemy.orm import sessionmaker, declarative_base, relationship
from dotenv import find_dotenv, load_dotenv
from os import getenv, environ

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

    person_ = relationship("User", back_populates="sessioncode_")


Base.metadata.create_all(engine)
