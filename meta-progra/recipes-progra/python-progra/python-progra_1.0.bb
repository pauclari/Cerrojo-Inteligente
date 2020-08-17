DESCRIPTION = "Programa implementado para reconocimiento facial"
SECTION = "examples"
LICENSE = "MIT"
LIC_FILES_CHKSUM = "file://${COMMON_LICENSE_DIR}/MIT;md5=0835ade698e0bcf8506ecda2f7b4f302"

SRC_URI = "file://setup.py \
           file://python-progra.py \
           file://progra/__init__.py \
           file://progra/main.py \
           file://haarcascade_frontalface_default.xml \
           file://modeloEigenFace_Sofia.xml \

S = "${WORKDIR}"

inherit setuptools

do_install_append () {
    install -d ${D}${bindir}
    install -m 0755 python-progra.py ${D}${bindir}
    install -m 0755 haarcascade_frontalface_default.xml ${D}${bindir}  
    install -m 0755 modeloEigenFace_Sofia.xml ${D}${bindir} 
}
