from flask import Flask, Blueprint, render_template, flash, url_for, redirect, request
from katalog import app, db
from katalog.models import Tjenisbuku, Tbuku
from katalog.admin.forms import jenisbuku_F, buku_F, editjenisbuku_F, editbuku_F
from PIL import Image
import os
import secrets

#penamabaan bluprint admin
radmin= Blueprint('radmin',__name__)

#simpan foto
def simpan_gambar(form_gambar):
    random_hex= secrets.token_hex(8)
    f_name, f_ext= os.path.splitext(form_gambar.filename)
    foto_fn= random_hex + f_ext
    foto_path= os.path.join(app.root_path, 'katalog/static/gambar', foto_fn)
    ubah_size=(300,300)
    j=Image.open(form_gambar)
    j.thumbnail(ubah_size)
    j.save(foto_path)
    #form_foto.save(foto_path)
    return foto_fn

@radmin.route("/")
def home():
    return render_template ("base.html")


@radmin.route("/jenisbuku", methods=['GET', 'POST'])
def jenisbuku():
    form=jenisbuku_F()
    datajenisbuku=Tjenisbuku.query.all()
    if form.validate_on_submit():
        #tambah data pengaduan
        add_jenisbuku= Tjenisbuku(jenisbuku=form.jenisbuku.data, keterangan=form.keterangan.data)
        db.session.add(add_jenisbuku)
        db.session.commit()
        flash('Data berhasil ditambahkan','warning')
        return redirect(url_for('radmin.jenisbuku'))
    return render_template ("jenisbuku.html", djenisbuku=datajenisbuku, form=form)


@radmin.route("/buku", methods=['GET', 'POST'])
def buku():
    form=buku_F()
    databuku=Tbuku.query.all()
    if form.validate_on_submit():
        file_foto=simpan_gambar(form.gambar.data)
        add_buku= Tbuku(kodebuku=form.jenisbuku.data, jenisbuku_id=form.jenisbuku.data, 
        judulbuku=form.judulbuku.data, penulis=form.penulis.data, penerbit=form.penerbit.data, 
        thnterbit=form.thnterbit.data, status=form.status.data, gambar=file_foto )
        db.session.add(add_buku)
        db.session.commit()
        flash('Data berhasil ditambahkan','warning')
        return redirect(url_for('radmin.buku'))
    return render_template ("buku.html", dbuku=databuku, form=form)


@radmin.route("/editjenis/<int:ed_id>/update", methods=['GET', 'POST'])
def update_jenis(ed_id):
    datajenis=Tjenisbuku.query.get_or_404(ed_id)
    form=editjenisbuku_F()
    if form.validate_on_submit():
        datajenis.jenisbuku=form.jenisbuku.data
        datajenis.keterangan=form.keterangan.data
        db.session.commit()
        flash('Data Berhasil Di ubah','warning')
        return redirect(url_for('radmin.jenisbuku'))
    elif request.method=="GET":
        form.jenisbuku.data=datajenis.jenisbuku
        form.keterangan.data=datajenis.keterangan
    return render_template('editjenis.html', form=form)



@radmin.route("/editbuku/<int:ed_id>/update", methods=['GET', 'POST'])
def update_buku(ed_id):
    databuku=Tbuku.query.get_or_404(ed_id)
    form=editbuku_F()
    if form.validate_on_submit():
        if form.gambar.data:
            file_foto=simpan_gambar(form.gambar.data)
            form.foto = file_foto
        databuku.kodebuku=form.kodebuku.data
        databuku.jenisbuku_id=form.jenisbuku.data
        databuku.judulbuku=form.judulbuku.data
        databuku.penulis=form.penulis.data
        databuku.penerbit=form.penerbit.data
        databuku.thnterbit=form.thnterbit.data
        databuku.status=form.status.data
        databuku.gambar=file_foto
        db.session.commit()
        flash('Data Berhasil Di ubah','warning')
        return redirect(url_for('radmin.buku'))
    elif request.method=="GET":
        form.kodebuku.data=databuku.kodebuku
        form.jenisbuku.data=databuku.jenisbuku_id
        form.judulbuku.data=databuku.judulbuku
        form.penulis.data=databuku.penulis
        form.penerbit.data=databuku.penerbit
        form.thnterbit.data=databuku.thnterbit
    return render_template('editbuku.html', form=form)

@radmin.route("/hapusjenis/<id>", methods=['GET', 'POST'])
def hapus_jenisbuku(id):
    qjenisbuku=Tjenisbuku.query.get(id)
    db.session.delete(qjenisbuku)
    db.session.commit()
    flash('Data Berhasil Di hapus','warning')
    return redirect(url_for('radmin.jenisbuku'))



@radmin.route("/hapusbuku/<id>", methods=['GET', 'POST'])
def hapus_buku(id):
    qbuku=Tbuku.query.get(id)
    db.session.delete(qbuku)
    db.session.commit()
    flash('Data Berhasil Di hapus','warning')
    return redirect(url_for('radmin.buku'))