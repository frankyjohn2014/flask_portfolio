"""empty message

Revision ID: 13e85e1bdaf5
Revises: af084ecc24e6
Create Date: 2020-09-05 15:19:57.893432

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '13e85e1bdaf5'
down_revision = 'af084ecc24e6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('storage_model',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.Unicode(length=64), nullable=True),
    sa.Column('path', sa.Unicode(length=128), nullable=True),
    sa.Column('type', sa.Unicode(length=3), nullable=True),
    sa.Column('create_date', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_column('category', 'img_path')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('category', sa.Column('img_path', mysql.VARCHAR(length=140), nullable=True))
    op.drop_table('storage_model')
    # ### end Alembic commands ###
