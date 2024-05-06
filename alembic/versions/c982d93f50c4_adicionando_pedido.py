"""Adicionando Pedido

Revision ID: c982d93f50c4
Revises: 736dd2bd6d6f
Create Date: 2024-05-05 22:17:27.510529

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c982d93f50c4'
down_revision: Union[str, None] = '736dd2bd6d6f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pedido',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('quantidade', sa.Integer(), nullable=True),
    sa.Column('local_entrega', sa.String(), nullable=True),
    sa.Column('tipo_entrega', sa.String(), nullable=True),
    sa.Column('observacao', sa.String(), nullable=True),
    sa.Column('usuario_id', sa.Integer(), nullable=True),
    sa.Column('produto_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['produto_id'], ['produto.id'], name='fk_pedido_produto'),
    sa.ForeignKeyConstraint(['usuario_id'], ['usuario.id'], name='fk_pedido_usuario'),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('pedido', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_pedido_id'), ['id'], unique=False)

    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('pedido', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_pedido_id'))

    op.drop_table('pedido')
    # ### end Alembic commands ###
