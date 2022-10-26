"""empty message

Revision ID: dd50d0124f97
Revises: 8e544528cfd0
Create Date: 2022-10-21 21:42:23.451194

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dd50d0124f97'
down_revision = '8e544528cfd0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('actions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('function', sa.String(length=50), nullable=True),
    sa.Column('description', sa.String(length=1500), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('courses',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('dept_id', sa.String(length=50), nullable=True),
    sa.Column('course_name', sa.String(length=25), nullable=True),
    sa.Column('course_acronym', sa.String(length=10), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('departments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('dept_name', sa.String(length=50), nullable=True),
    sa.Column('dept_acronym', sa.String(length=10), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('modules',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('module', sa.String(length=50), nullable=True),
    sa.Column('description', sa.String(length=1500), nullable=True),
    sa.Column('routeUri', sa.String(length=25), nullable=True),
    sa.Column('icon', sa.String(length=50), nullable=True),
    sa.Column('default_url', sa.String(length=50), nullable=True),
    sa.Column('encryptname', sa.String(length=500), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('profiles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('firstaname', sa.String(length=20), nullable=True),
    sa.Column('middlename', sa.String(length=20), nullable=True),
    sa.Column('lastname', sa.String(length=20), nullable=True),
    sa.Column('suffix', sa.String(length=4), nullable=True),
    sa.Column('contact_no', sa.String(length=15), nullable=True),
    sa.Column('address', sa.String(length=150), nullable=True),
    sa.Column('bday', sa.DateTime(), nullable=True),
    sa.Column('gender', sa.String(length=6), nullable=True),
    sa.Column('civil', sa.String(length=15), nullable=True),
    sa.Column('link', sa.String(length=500), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('roles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('group', sa.String(length=50), nullable=True),
    sa.Column('modules', sa.String(length=300), nullable=True),
    sa.Column('action', sa.String(length=500), nullable=True),
    sa.Column('log', sa.String(length=100000), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('schedules',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('subj_id', sa.String(length=50), nullable=True),
    sa.Column('sched_json', sa.String(length=5000), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('school_records',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('usn', sa.String(length=50), nullable=True),
    sa.Column('accademic_year', sa.String(length=25), nullable=True),
    sa.Column('course', sa.String(length=50), nullable=True),
    sa.Column('year', sa.String(length=10), nullable=True),
    sa.Column('study_load', sa.String(length=10000), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('subjects',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('course_id', sa.String(length=15), nullable=True),
    sa.Column('subj_name', sa.String(length=50), nullable=True),
    sa.Column('subj_code', sa.String(length=10), nullable=True),
    sa.Column('units', sa.String(length=10), nullable=True),
    sa.Column('pre_requisite', sa.String(length=10), nullable=True),
    sa.Column('syr', sa.String(length=10), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=50), nullable=True),
    sa.Column('username', sa.String(length=25), nullable=True),
    sa.Column('password', sa.String(length=500), nullable=True),
    sa.Column('access', sa.String(length=120), nullable=True),
    sa.Column('online', sa.String(length=2), nullable=True),
    sa.Column('active', sa.String(length=2), nullable=True),
    sa.Column('role', sa.String(length=2), nullable=True),
    sa.Column('link', sa.String(length=500), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    op.drop_table('subjects')
    op.drop_table('school_records')
    op.drop_table('schedules')
    op.drop_table('roles')
    op.drop_table('profiles')
    op.drop_table('modules')
    op.drop_table('departments')
    op.drop_table('courses')
    op.drop_table('actions')
    # ### end Alembic commands ###
