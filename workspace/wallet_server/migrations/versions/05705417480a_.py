"""empty message

Revision ID: 05705417480a
Revises: 
Create Date: 2025-01-02 16:22:11.509151

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '05705417480a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.String(length=100), nullable=False),
    sa.Column('password', sa.String(length=100), nullable=False),
    sa.Column('email', sa.String(length=100), nullable=False),
    sa.Column('phone_mobile', sa.String(length=20), nullable=False),
    sa.Column('name', sa.String(length=10), nullable=False),
    sa.Column('create_date', sa.DateTime(), nullable=True),
    sa.Column('update_date', sa.DateTime(), nullable=True),
    sa.Column('private_key', sa.String(length=300), nullable=True),
    sa.Column('public_key', sa.String(length=300), nullable=True),
    sa.Column('blockchain_addr', sa.String(length=300), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###
