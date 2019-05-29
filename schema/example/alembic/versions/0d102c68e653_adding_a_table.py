"""adding a table

Revision ID: 0d102c68e653
Revises: bb72acf65773
Create Date: 2019-05-29 12:32:33.502910

"""
from alembic import op
import sqlalchemy as sa
import datetime

# revision identifiers, used by Alembic.
revision = '0d102c68e653'
down_revision = 'bb72acf65773'
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