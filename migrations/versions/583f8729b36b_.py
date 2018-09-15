"""empty message

Revision ID: 583f8729b36b
Revises: 
Create Date: 2018-09-15 13:08:00.458982

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '583f8729b36b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('antropometrias',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('peso', sa.Float(), nullable=True),
    sa.Column('braco', sa.Float(), nullable=True),
    sa.Column('torax', sa.Float(), nullable=True),
    sa.Column('cintura', sa.Float(), nullable=True),
    sa.Column('abdomen', sa.Float(), nullable=True),
    sa.Column('quadril', sa.Float(), nullable=True),
    sa.Column('coxa', sa.Float(), nullable=True),
    sa.Column('biceps', sa.Float(), nullable=True),
    sa.Column('triceps', sa.Float(), nullable=True),
    sa.Column('peito', sa.Float(), nullable=True),
    sa.Column('subsCap', sa.Float(), nullable=True),
    sa.Column('axilar', sa.Float(), nullable=True),
    sa.Column('gorduraPerc', sa.Float(), nullable=True),
    sa.Column('aguaPerc', sa.Float(), nullable=True),
    sa.Column('pesoMagro', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tipoAtendimentos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(length=30), nullable=True),
    sa.Column('preco', sa.Float(), nullable=True),
    sa.Column('qtdRetorno', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tipoEstados',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(length=30), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('nome')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(), nullable=True),
    sa.Column('password', sa.String(), nullable=True),
    sa.Column('nome', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('celular', sa.String(length=11), nullable=True),
    sa.Column('tipo', sa.String(length=1), nullable=True),
    sa.Column('ativo', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('pacientes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('dataNascimento', sa.DateTime(), nullable=True),
    sa.Column('sexo', sa.String(length=1), nullable=True),
    sa.Column('cidade', sa.String(length=50), nullable=True),
    sa.Column('profissao', sa.String(length=50), nullable=True),
    sa.Column('objetivo', sa.String(length=50), nullable=True),
    sa.Column('altura', sa.Float(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('consultas',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('paciente_id', sa.Integer(), nullable=False),
    sa.Column('tipoAtendimento_id', sa.Integer(), nullable=False),
    sa.Column('hora', sa.TIME(), nullable=False),
    sa.Column('data', sa.Date(), nullable=False),
    sa.Column('tipoEstado_id', sa.Integer(), nullable=False),
    sa.Column('antropometria_id', sa.Integer(), nullable=True),
    sa.Column('dieta', sa.LargeBinary(), nullable=True),
    sa.Column('pagamento', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['antropometria_id'], ['tipoAtendimentos.id'], ),
    sa.ForeignKeyConstraint(['paciente_id'], ['pacientes.id'], ),
    sa.ForeignKeyConstraint(['tipoAtendimento_id'], ['tipoAtendimentos.id'], ),
    sa.ForeignKeyConstraint(['tipoEstado_id'], ['tipoEstados.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('consultas')
    op.drop_table('pacientes')
    op.drop_table('users')
    op.drop_table('tipoEstados')
    op.drop_table('tipoAtendimentos')
    op.drop_table('antropometrias')
    # ### end Alembic commands ###