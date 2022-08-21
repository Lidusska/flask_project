"""Create users table

Revision ID: 1ed84ef6b9af
Revises: 
Create Date: 2022-08-21 19:57:13.470991

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1ed84ef6b9af'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "user",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("username", sa.String),
        sa.Column("password", sa.String)
    )


def downgrade() -> None:
    op.drop_table("user")
