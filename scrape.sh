#!/bin/sh

rm -rf developer.gnome.org
rm -rf gtkmm.docset/Contents/Resources/Documents/*

wget \
  --recursive \
  --no-clobber \
  --page-requisites \
  --html-extension \
  --convert-links \
  --domains developer.gnome.org \
  --no-parent \
  https://developer.gnome.org/gtkmm/stable/

wget \
  --recursive \
  --no-clobber \
  --page-requisites \
  --html-extension \
  --convert-links \
  --domains developer.gnome.org \
  --no-parent \
  https://developer.gnome.org/glibmm/stable/

mv developer.gnome.org/* gtkmm.docset/Contents/Resources/Documents
rm -rf developer.gnome.org
