CFLAGS = -O2 -g -Wextra
PREFIX ?= /usr
bindir = $(DESTDIR)/$(PREFIX)/bin

all:
	$(CC) $(CFLAGS) -o aiaiai-locker aiaiai-locker.c
	make -C external

clean:
	$(RM) aiaiai-locker
	make -C external clean

install: all
	install -d $(bindir)/{external,email}
	find . -maxdepth 1 -executable -type f -exec install '{}' $(bindir) \; ;
	install aiaiai-sh-functions $(bindir)
	find external/* -executable -type f -exec install '{}' $(bindir)/external/ \; ;
	find email/* -executable -type f -exec install '{}' $(bindir)/email/ \; ;
