"""another test table

Revision ID: 595bcda71ae9
Revises: 0d102c68e653
Create Date: 2019-05-29 15:46:11.323978

"""
from alembic import op
import sqlalchemy as sa
import datetime


# revision identifiers, used by Alembic.
revision = '595bcda71ae9'
down_revision = '0d102c68e653'
branch_labels = None
depends_on = None


def upgrade():
		op.create_table('example_table2',
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
    op.drop_table('example_table2')