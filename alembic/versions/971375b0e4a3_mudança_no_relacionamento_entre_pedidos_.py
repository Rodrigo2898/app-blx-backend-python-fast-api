"""Mudança no relacionamento entre pedidos e usuarios

Revision ID: 971375b0e4a3
Revises: 8074fadb3d03
Create Date: 2024-05-09 21:12:19.196598

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '971375b0e4a3'
down_revision: Union[str, None] = '8074fadb3d03'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
