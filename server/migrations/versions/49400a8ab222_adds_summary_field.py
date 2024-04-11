"""Adds summary field

Revision ID: 49400a8ab222
Revises: 131085601e40
Create Date: 2024-04-11 11:09:51.699890

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '49400a8ab222'
down_revision = '131085601e40'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('categories', schema=None) as batch_op:
        batch_op.add_column(sa.Column('summary', sa.String(), nullable=True))

    with op.batch_alter_table('entries', schema=None) as batch_op:
        batch_op.alter_column('date',
               existing_type=sa.DATETIME(),
               type_=sa.Date(),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('entries', schema=None) as batch_op:
        batch_op.alter_column('date',
               existing_type=sa.Date(),
               type_=sa.DATETIME(),
               existing_nullable=True)

    with op.batch_alter_table('categories', schema=None) as batch_op:
        batch_op.drop_column('summary')

    # ### end Alembic commands ###
