"""empty message

Revision ID: 56c24346a5c3
Revises: e6bca0728de6
Create Date: 2024-09-10 02:37:51.297281

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '56c24346a5c3'
down_revision = 'e6bca0728de6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('planet', schema=None) as batch_op:
        batch_op.drop_column('Orbital_period')

    with op.batch_alter_table('starships', schema=None) as batch_op:
        batch_op.alter_column('Length',
               existing_type=postgresql.DOUBLE_PRECISION(precision=53),
               type_=sa.Integer(),
               existing_nullable=True)
        batch_op.drop_column('Max_atmosphering_speed')
        batch_op.drop_column('Hyperdrive_rating')
        batch_op.drop_column('Cost_in_credits')
        batch_op.drop_column('Manufacturer')
        batch_op.drop_column('Cargo_capacity')
        batch_op.drop_column('Consumables')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('starships', schema=None) as batch_op:
        batch_op.add_column(sa.Column('Consumables', sa.VARCHAR(length=250), autoincrement=False, nullable=False))
        batch_op.add_column(sa.Column('Cargo_capacity', sa.VARCHAR(length=250), autoincrement=False, nullable=False))
        batch_op.add_column(sa.Column('Manufacturer', sa.VARCHAR(length=100), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('Cost_in_credits', sa.INTEGER(), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('Hyperdrive_rating', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('Max_atmosphering_speed', sa.INTEGER(), autoincrement=False, nullable=True))
        batch_op.alter_column('Length',
               existing_type=sa.Integer(),
               type_=postgresql.DOUBLE_PRECISION(precision=53),
               existing_nullable=True)

    with op.batch_alter_table('planet', schema=None) as batch_op:
        batch_op.add_column(sa.Column('Orbital_period', sa.INTEGER(), autoincrement=False, nullable=True))

    # ### end Alembic commands ###
