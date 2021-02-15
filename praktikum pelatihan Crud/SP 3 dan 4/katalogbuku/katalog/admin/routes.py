from flask import Flask, Blueprint, render_template
from katalog import app
from katalog.models import Tjenisbuku, Tbuku

#penamabaan bluprint admin
radmin= Blueprint('radmin',__name__)

@radmin.route("/")
def home():
    return render_template ("base.html")


@radmin.route("/jenisbuku")
def jenisbuku():
    datajenisbuku=Tjenisbuku.query.all()
    return render_template ("jenisbuku.html", djenisbuku=datajenisbuku)


@radmin.route("/buku")
def buku():
    databuku=Tbuku.query.all()
    return render_template ("buku.html", dbuku=databuku)