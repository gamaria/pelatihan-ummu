from flask import Flask, Blueprint, render_template
from katalog import app


#penamabaan bluprint admin
radmin= Blueprint('radmin',__name__)

@radmin.route("/")
def home():
    return render_template ("base.html")


@radmin.route("/jenisbuku")
def jenisbuku():
    return render_template ("jenisbuku.html")