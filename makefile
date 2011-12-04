
# Harmattan IP Address "Widget" (http://thp.io/2011/ipaddr-widget/)
# Copyright (c) 2011 Thomas Perl <thp.io/about>; License: GPLv3+

WIDGET_NAME = ipaddr-widget

all:
	true

install:
	mkdir -p $(DESTDIR)/usr/share/$(WIDGET_NAME)/
	cp template.png $(DESTDIR)/usr/share/$(WIDGET_NAME)/
	mkdir -p $(DESTDIR)/usr/bin/
	cp $(WIDGET_NAME).py $(DESTDIR)/usr/bin/
	mkdir -p $(DESTDIR)/usr/share/applications/
	cp $(WIDGET_NAME).desktop $(DESTDIR)/usr/share/applications/

.PHONY: all install

