"""adding a new table

Revision ID: 527c371fefd5
Revises: 22029b334fde
Create Date: 2019-05-29 20:32:17.383634

"""
from alembic import op
import sqlalchemy as sa
import datetime

# revision identifiers, used by Alembic.
revision = '527c371fefd5'
down_revision = '22029b334fde'
branch_labels = None
depends_on = None


def upgrade():
		op.create_table('example_table',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('string', sa.String(length=255), nullable=False),
        sa.Column('db_created_at', sa.DateTime,
            default=datetime.datetime.utcnow,
            nullable=False
        ),
        sa.Column('db_modified_at', sa.DateTime,
            default=datetime.datetime.utcnow,
            nullable=False
        ),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    op.drop_table('example_table')
