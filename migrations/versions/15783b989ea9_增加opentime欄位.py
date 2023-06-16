"""增加opentime欄位

Revision ID: 15783b989ea9
Revises: 24ef6679cea3
Create Date: 2021-12-12 19:27:57.394802

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '15783b989ea9'
down_revision = '24ef6679cea3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('blog', sa.Column('opentime', sa.String(length=200), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('blog', 'opentime')
    # ### end Alembic commands ###
