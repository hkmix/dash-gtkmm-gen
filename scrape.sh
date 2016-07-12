#!/bin/sh

wget \
  --recursive \
  --no-clobber \
  --page-requisites \
  --html-extension \
  --convert-links \
  --domains developer.gnome.org \
  --no-parent \
  https://developer.gnome.org/gtkmm/stable/
