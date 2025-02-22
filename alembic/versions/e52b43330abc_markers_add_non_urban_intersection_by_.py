"""markers: Add non_urban_intersection_by_junction_number

Revision ID: e52b43330abc
Revises: 9d24fbb0f1fa
Create Date: 2019-10-21 16:41:23.553994

"""

# revision identifiers, used by Alembic.
revision = 'e52b43330abc'
down_revision = '9d24fbb0f1fa'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('markers', sa.Column('non_urban_intersection_by_junction_number', sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('markers', 'non_urban_intersection_by_junction_number')
    # ### end Alembic commands ###
