LIBDIR = $(DESTDIR)/usr/share/pyshared/shadow-tools
BINDIR = $(DESTDIR)/usr/bin
APPDIR = $(DESTDIR)/usr/share/applications
ICONDIR = $(DESTDIR)/usr/share/icons
clean:
	rm -f *.py[co] */*.py[co]
install:
	mkdir -p $(LIBDIR)
	mkdir -p $(BINDIR)
	mkdir -p $(APPDIR)
	mkdir -p $(ICONDIR)
	cp shadow-tools/shadow_tools.py $(BINDIR)/shadow-tools
	cp shadow-tools/shadow_tools_ui.py $(LIBDIR)/
	cp -r shadow-tools/images $(LIBDIR)/
	cp shadow-tools.desktop $(APPDIR)/
	cp shadow-tools.png $(ICONDIR)/

uninstall:
	rm -rf $(LIBDIR)
	rm -f $(BINDIR)/shadow-tools
	rm -f $(APPDIR)/shadow-tools.desktop
	rm -f $(ICONDIR)/shadow-tools.png

