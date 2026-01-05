from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, Date, DateTime, Float, text, Boolean, sql, update, func, Text, DECIMAL
from sqlalchemy.orm import sessionmaker, declarative_base, relationship, query
from dotenv import find_dotenv, load_dotenv
from os import getenv, environ
from datetime import datetime as datetime_, timedelta

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

engine = create_engine("postgresql+psycopg2://", query_cache_size=0, echo=True, pool_size=5, max_overflow=10,
                       pool_timeout=30, connect_args=dict(user=environ.get("DB_USER"), password=environ.get("DB_PASSWORD"),
                                         host=environ.get("DB_HOST"), database=environ.get("DB_DATABASE"),
                                         sslmode=environ.get("DB_SSL_MODE"), channel_binding=environ.get("DB_CHANNEL_BINDING")))

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
    phone = Column(String(20), nullable=True)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, nullable=False, default=func.now())

    user_sessioncode = relationship("SessionCode", back_populates="id_usuario")
    user_address = relationship("Address", back_populates="id_usuario")
    user_order = relationship("Order", back_populates="id_usuario")


class SessionCode(Base):
    __tablename__ = "tb_sessioncodes"

    sessioncode_id = Column(Integer, autoincrement=True, nullable=False, primary_key=True)
    user_id = Column(Integer, ForeignKey("tb_users.user_id"), nullable=False)
    sessioncode = Column(String(255), nullable=False, unique=True)
    created_at = Column(DateTime, nullable=False, default=str(datetime_.now())[:-7])
    expires_at = Column(DateTime, nullable=False, default=str(datetime_.now()+timedelta(minutes=10))[:-7])

    id_usuario = relationship("User", back_populates="user_sessioncode")


class Address(Base):
    __tablename__ = "tb_addresses"

    address_id = Column(Integer, autoincrement=True, nullable=False, primary_key=True)
    user_id = Column(Integer, ForeignKey("tb_users.user_id"), nullable=False)
    cep = Column(String(15), nullable=False)
    street = Column(String(200), nullable=False)
    number = Column(Integer, nullable=False)
    complement = Column(String(255), nullable=True)
    bairro = Column(String(100), nullable=False)
    city = Column(String(100), nullable=False)
    state = Column(String(2), nullable=False)
    reference_point = Column(Text, nullable=True)
    description = Column(String(50), nullable=True)

    id_usuario = relationship("User", back_populates="user_address")
    id_order = relationship("Order", back_populates="id_address")


class Product(Base):
    __tablename__ = "tb_products"

    product_id = Column(Integer, autoincrement=True, nullable=False, primary_key=True)
    name = Column(String(200), nullable=False, unique=False)
    description = Column(Text, nullable=True)
    material = Column(String(100), nullable=False, unique=False)
    gender = Column(String(2), nullable=False, unique=False)
    base_price = Column(DECIMAL(10, 2), nullable=False, unique=False)
    is_active = Column(Boolean, default=True, nullable=False)
    created_at = Column(DateTime, nullable=False, default=str(datetime_.now())[:-7])

    id_produto = relationship("ProductVariant", back_populates="id_produto")


class ProductVariant(Base):
    __tablename__ = "tb_product_variants"

    variant_id = Column(Integer, autoincrement=True, nullable=False, primary_key=True)
    product_id = Column(Integer, ForeignKey("tb_products.product_id"), nullable=False)
    size = Column(String(10), nullable=False)
    color = Column(String(50), nullable=False)
    qtd_stock = Column(Integer, default=0)
    code = Column(String(20), unique=True, nullable=True)

    id_produto = relationship("Product", back_populates="id_produto")
    id_variant = relationship("OrderItem", back_populates="id_variant")


class Order(Base):
    __tablename__ = "tb_orders"

    order_id = Column(Integer, autoincrement=True, nullable=False, primary_key=True)
    user_id = Column(Integer, ForeignKey("tb_users.user_id"), nullable=False)
    address_id = Column(Integer, ForeignKey("tb_addresses.address_id"), nullable=False)
    total_amount = Column(DECIMAL(10, 2), nullable=False)
    status = Column(String(50), default="pending", nullable=False)
    created_at = Column(DateTime, nullable=False, default=str(datetime_.now())[:-7])

    id_usuario = relationship("User", back_populates="user_order")
    id_address = relationship("Address", back_populates="id_order")
    id_order = relationship("OrderItem", back_populates="id_order")


class OrderItem(Base):
    __tablename__ = "tb_order_items"

    item_id = Column(Integer, autoincrement=True, nullable=False, primary_key=True)
    order_id = Column(Integer, ForeignKey("tb_orders.order_id"), nullable=False)
    variant_id = Column(Integer, ForeignKey("tb_product_variants.variant_id"), nullable=False)
    qtd = Column(Integer, nullable=False)
    unit_price = Column(DECIMAL(10, 2), nullable=False)

    id_order = relationship("Order", back_populates="id_order")
    id_variant = relationship("ProductVariant", back_populates="id_variant")


Base.metadata.create_all(engine)

