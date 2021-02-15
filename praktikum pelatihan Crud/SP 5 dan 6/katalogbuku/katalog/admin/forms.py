from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Length, ValidationError
from flask_wtf.file import FileField, FileAllowed
from katalog.models import Tbuku

class jenisbuku_F(FlaskForm):
    jenisbuku= StringField('Jenis Buku', validators=[DataRequired(),Length(min=5, max=10)])
    keterangan= StringField('Keterangan')
    submit=SubmitField('Simpan')


class buku_F(FlaskForm):
    kodebuku= StringField('Kode Buku', validators=[DataRequired(),Length(min=5, max=15)])
    jenisbuku= StringField('Jenis Buku',validators=[DataRequired()])
    judulbuku= StringField('Judul Buku', validators=[DataRequired()])
    penulis= StringField('Penulis', validators=[DataRequired()])
    penerbit= StringField('Penerbit', validators=[DataRequired()])
    thnterbit= StringField('Tahun Terbit', validators=[DataRequired(), Length(max=4)])
    status= SelectField(u'Status', choices=[('ada','ada'), ('kosong','kosong')], validators=[DataRequired()] )
    gambar= FileField('Gambar', validators=[FileAllowed(['jpg','png'])])
    submit=SubmitField('Simpan')

    def validate_kodebuku(self, kodebuku):
        cekkode=Tbuku.query.filter_by(kodebuku=kodebuku.data).first()
        if cekkode:
            raise ValidationError('Kode Buku Sudah Terdaftar, Gunakan Kode Yang Lain')


class editjenisbuku_F(FlaskForm):
    jenisbuku= StringField('Jenis Buku', validators=[DataRequired(),Length(min=5, max=10)])
    keterangan= StringField('Keterangan')
    submit=SubmitField('Ubah')


class editbuku_F(FlaskForm):
    kodebuku= StringField('Kode Buku', validators=[DataRequired(),Length(min=5, max=15)])
    jenisbuku= StringField('Jenis Buku',validators=[DataRequired()])
    judulbuku= StringField('Judul Buku', validators=[DataRequired()])
    penulis= StringField('Penulis', validators=[DataRequired()])
    penerbit= StringField('Penerbit', validators=[DataRequired()])
    thnterbit= StringField('Tahun Terbit', validators=[DataRequired(), Length(max=4)])
    status= SelectField(u'Status', choices=[('ada','ada'), ('kosong','kosong')], validators=[DataRequired()] )
    gambar= FileField('Gambar', validators=[FileAllowed(['jpg','png'])])
    submit=SubmitField('Ubah')