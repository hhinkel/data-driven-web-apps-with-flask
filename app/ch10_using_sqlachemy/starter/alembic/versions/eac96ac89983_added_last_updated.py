"""Added last_updated

Revision ID: eac96ac89983
Revises: 
Create Date: 2021-12-13 20:07:38.449153

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'eac96ac89983'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('packages', sa.Column('last_updated', sa.DateTime(), nullable=True))
    op.create_index(op.f('ix_packages_last_updated'), 'packages', ['last_updated'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_packages_last_updated'), table_name='packages')
    op.drop_column('packages', 'last_updated')
    # ### end Alembic commands ###
