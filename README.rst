=====
Pansi
=====

Pansi is a clean and simple ANSI escape code library for Python.

::

    >>> from pansi import ansi
    >>> print("hello, {green}{name}{_}".format(name="world", **ansi))
    hello, world


General usage
=============

Pansi provides an object called ``ansi`` through which all escape codes can be selected.
This object exposes the codes as both attributes (e.g. ``ansi.red``) and items (e.g. ``ansi["red"]``).

This object can therefore be used in several different ways, but the simplest is through the string ``format`` method.
Here, if the object is supplied as a simple named argument, all references need to be prefixed:

::

    >>> print("hello, {ansi.green}{name}{ansi.reset}".format(name="world", ansi=ansi))
    hello, world


Alternatively, passing the object with the ``**`` operator removes the need for prefixes and thus makes the template string shorter.
However, this does introduce a greater chance of clashing with other parameters, and doesn't signal which parameters are which.

::

    >>> print("hello, {green}{name}{_}".format(name="world", **ansi))
    hello, world

Ultimately, it is a subjective choice between these two options.


Colours
=======

For foreground text, the standard set of colours can be selected using the lower case name for normal brightness
and the upper case name for high intensity.
To select as the background colour instead, simply prefix with ``bg.``, e.g. ``bg.blue``.

==============  ===========  ==============
Colour          Foreground   Background
==============  ===========  ==============
Black           ``black``    ``bg.black``
Red             ``red``      ``bg.red``
Green           ``green``    ``bg.green``
Yellow          ``yellow``   ``bg.yellow``
Blue            ``blue``     ``bg.yellow``
Magenta         ``magenta``  ``bg.magenta``
Cyan            ``cyan``     ``bg.cyan``
White           ``white``    ``bg.white``
Bright black    ``BLACK``    ``bg.BLACK``
Bright red      ``RED``      ``bg.RED``
Bright green    ``GREEN``    ``bg.GREEN``
Bright yellow   ``YELLOW``   ``bg.YELLOW``
Bright blue     ``BLUE``     ``bg.YELLOW``
Bright magenta  ``MAGENTA``  ``bg.MAGENTA``
Bright cyan     ``CYAN``     ``bg.CYAN``
Bright white    ``WHITE``    ``bg.WHITE``
==============  ===========  ==============


Full 24-bit colour support is also available (on those terminals that support it) by using the ``rgb`` selector.

::

    >>> print("A Clockwork {rgb[FF8000]}Orange{_}".format(**ansi))
    A Clockwork Orange

Reverse video

rev
_rev


Colour reset

fg.reset
bg.reset


Text Weight
===========
weight.normal
weight.bold
weight.light
b
_b


Text Style
==========
style.normal
style.italic
style.fraktur
i
_i


Text decoration
===============
u
uu
_u
o
_o
s
_s


Blinking
========
blink
BLINK
_blink


Hide & show
===========
hide
show


Font
====
font0
