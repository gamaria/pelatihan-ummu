from katalog import db


class Tjenisbuku(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    jenisbuku = db.Column(db.String(15), unique=True, nullable=False)
    keterangan = db.Column(db.String(100), nullable=True)
    book = db.relationship('Tbuku', backref='books',lazy=True)
    
    def __repr__(self):
        return f"Tjenisbuku('{self.jenisbuku}','{self.keterangan}')"

class Tbuku(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    kodebuku = db.Column(db.String(100), nullable=False)
    jenisbuku_id = db.Column (db.Integer, db.ForeignKey('tjenisbuku.id'))
    judulbuku= db.Column(db.String(100), nullable=False)
    penulis= db.Column(db.String(60), nullable=False)
    penerbit= db.Column(db.String(60), nullable=False)
    thnterbit= db.Column(db.String(60), nullable=True)
    status= db.Column(db.String(60), nullable=True)
    gambar = db.Column(db.String(30), nullable=False)
    def __repr__(self):
        return f"Tbuku('{self.kodebuku}','{self.jenisbuku_id}','{self.judulbuku}','{self.penulis}', '{self.penerbit}','{self.thnterbit}', '{self.status}', '{self.gambar}')"