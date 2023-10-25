"""empty message

Revision ID: 7cad5ae57033
Revises: 0593c9cda1b8
Create Date: 2023-10-25 23:38:12.783287

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision = '7cad5ae57033'
down_revision = '0593c9cda1b8'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('super_user', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'super_user')
    # ### end Alembic commands ###
