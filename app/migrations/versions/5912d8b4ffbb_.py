"""empty message

Revision ID: 5912d8b4ffbb
Revises: a12e4bac23b3
Create Date: 2020-09-05 18:26:27.048344

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5912d8b4ffbb'
down_revision = 'a12e4bac23b3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('slug', table_name='post')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index('slug', 'post', ['slug'], unique=True)
    # ### end Alembic commands ###
