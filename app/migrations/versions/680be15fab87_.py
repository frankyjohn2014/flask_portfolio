"""empty message

Revision ID: 680be15fab87
Revises: 13e85e1bdaf5
Create Date: 2020-09-05 15:48:59.537639

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '680be15fab87'
down_revision = '13e85e1bdaf5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('storage_model')
    op.add_column('category', sa.Column('create_date', sa.DateTime(), nullable=True))
    op.add_column('category', sa.Column('path', sa.Unicode(length=128), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('category', 'path')
    op.drop_column('category', 'create_date')
    op.create_table('storage_model',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('name', mysql.VARCHAR(length=64), nullable=True),
    sa.Column('path', mysql.VARCHAR(length=128), nullable=True),
    sa.Column('type', mysql.VARCHAR(length=3), nullable=True),
    sa.Column('create_date', mysql.DATETIME(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='latin1',
    mysql_engine='InnoDB'
    )
    # ### end Alembic commands ###
