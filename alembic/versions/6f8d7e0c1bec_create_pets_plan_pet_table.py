"""merge heads

Revision ID: 6f8d7e0c1bec
Revises: 27b2c8fde1c3, 55e798c542d1
Create Date: 2024-09-06 17:13:42.789531

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6f8d7e0c1bec'
down_revision: Union[str, None] = ('27b2c8fde1c3', '55e798c542d1')
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'pet_plan_pet',
        sa.Column('id', sa.String, primary_key=True),
        sa.Column('pet_id', sa.String, sa.ForeignKey('pets.id')),
        sa.Column('plan_id', sa.String, sa.ForeignKey('pets_plan.id'))
    )


def downgrade() -> None:
    op.drop_table('pet_plan_pet')
