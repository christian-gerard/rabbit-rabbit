"""add category icon

Revision ID: 4b826ee0a170
Revises: 49400a8ab222
Create Date: 2024-04-17 20:11:53.493564

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4b826ee0a170'
down_revision = '49400a8ab222'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('categories', schema=None) as batch_op:
        batch_op.add_column(sa.Column('icon', sa.String(), nullable=True))

    with op.batch_alter_table('entries', schema=None) as batch_op:
        batch_op.alter_column('body',
               existing_type=sa.VARCHAR(),
               nullable=False)
        batch_op.alter_column('date',
               existing_type=sa.DATE(),
               type_=sa.String(),
               existing_nullable=True)

    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.create_unique_constraint(None, ['username'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')

    with op.batch_alter_table('entries', schema=None) as batch_op:
        batch_op.alter_column('date',
               existing_type=sa.String(),
               type_=sa.DATE(),
               existing_nullable=True)
        batch_op.alter_column('body',
               existing_type=sa.VARCHAR(),
               nullable=True)

    with op.batch_alter_table('categories', schema=None) as batch_op:
        batch_op.drop_column('icon')

    # ### end Alembic commands ###
