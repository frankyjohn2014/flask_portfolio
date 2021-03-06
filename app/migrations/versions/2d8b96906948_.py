"""empty message

Revision ID: 2d8b96906948
Revises: 
Create Date: 2020-08-30 21:11:57.691807

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '2d8b96906948'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('post',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=140), nullable=True),
    sa.Column('slug', sa.String(length=140), nullable=True),
    sa.Column('url_site', sa.String(length=140), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('slug')
    )
    op.create_table('post_category',
    sa.Column('post_id', sa.Integer(), nullable=True),
    sa.Column('category_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['category_id'], ['category.id'], ),
    sa.ForeignKeyConstraint(['post_id'], ['post.id'], )
    )
    op.drop_table('test')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('test',
    sa.Column('name', mysql.VARCHAR(length=100), nullable=False),
    sa.Column('team', mysql.VARCHAR(length=100), nullable=False),
    sa.Column('G', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.Column('PA', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    mysql_default_charset='latin1',
    mysql_engine='InnoDB'
    )
    op.drop_table('post_category')
    op.drop_table('post')
    # ### end Alembic commands ###
