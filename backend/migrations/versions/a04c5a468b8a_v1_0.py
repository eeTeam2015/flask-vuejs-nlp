"""v1.0

Revision ID: a04c5a468b8a
Revises: 
Create Date: 2019-12-18 21:10:52.005843

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a04c5a468b8a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('novels',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('book_name', sa.String(length=64), nullable=True),
    sa.Column('book_url', sa.String(), nullable=True),
    sa.Column('book_img', sa.String(), nullable=True),
    sa.Column('author', sa.String(length=64), nullable=True),
    sa.Column('type', sa.String(length=64), nullable=True),
    sa.Column('last_update', sa.String(length=64), nullable=True),
    sa.Column('profile', sa.Text(), nullable=True),
    sa.Column('keyword', sa.String(), nullable=True),
    sa.Column('page', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_novels')),
    mysql_charset='utf8'
    )
    with op.batch_alter_table('novels', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_novels_book_name'), ['book_name'], unique=False)

    op.create_table('chapters',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('chapter', sa.String(length=64), nullable=True),
    sa.Column('chapter_url', sa.String(), nullable=True),
    sa.Column('book_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['book_id'], ['novels.id'], name=op.f('fk_chapters_book_id_novels')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_chapters'))
    )
    with op.batch_alter_table('chapters', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_chapters_chapter_url'), ['chapter_url'], unique=False)

    op.create_table('contents',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('content', sa.String(), nullable=True),
    sa.Column('chapter_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['chapter_id'], ['chapters.id'], name=op.f('fk_contents_chapter_id_chapters')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_contents'))
    )
    op.create_table('sentencesegs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('sentenceseg', sa.Text(), nullable=True),
    sa.Column('chapter_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['chapter_id'], ['chapters.id'], name=op.f('fk_sentencesegs_chapter_id_chapters')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_sentencesegs'))
    )
    op.create_table('postcontentsegs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('postag', sa.String(), nullable=True),
    sa.Column('chapter_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['chapter_id'], ['sentencesegs.id'], name=op.f('fk_postcontentsegs_chapter_id_sentencesegs')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_postcontentsegs'))
    )
    op.create_table('sentiContent',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('senti', sa.String(), nullable=True),
    sa.Column('degree', sa.Float(), nullable=True),
    sa.Column('sentence_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['sentence_id'], ['sentencesegs.id'], name=op.f('fk_sentiContent_sentence_id_sentencesegs')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_sentiContent'))
    )
    op.create_table('wordsegs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('wordseg', sa.String(), nullable=True),
    sa.Column('sentence_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['sentence_id'], ['sentencesegs.id'], name=op.f('fk_wordsegs_sentence_id_sentencesegs')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_wordsegs'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('wordsegs')
    op.drop_table('sentiContent')
    op.drop_table('postcontentsegs')
    op.drop_table('sentencesegs')
    op.drop_table('contents')
    with op.batch_alter_table('chapters', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_chapters_chapter_url'))

    op.drop_table('chapters')
    with op.batch_alter_table('novels', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_novels_book_name'))

    op.drop_table('novels')
    # ### end Alembic commands ###
