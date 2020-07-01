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

=======  ===========  ===========  ==============  ==============
~        Foreground                Background
-------  ------------------------  ------------------------------
Colour   Normal       Bright       Normal          Bright
=======  ===========  ===========  ==============  ==============
Black    ``black``    ``BLACK``    ``bg.black``    ``bg.BLACK``
Red      ``red``      ``RED``      ``bg.red``      ``bg.RED``
Green    ``green``    ``GREEN``    ``bg.green``    ``bg.GREEN``
Yellow   ``yellow``   ``YELLOW``   ``bg.yellow``   ``bg.YELLOW``
Blue     ``blue``     ``BLUE``     ``bg.yellow``   ``bg.YELLOW``
Magenta  ``magenta``  ``MAGENTA``  ``bg.magenta``  ``bg.MAGENTA``
Cyan     ``cyan``     ``CYAN``     ``bg.cyan``     ``bg.CYAN``
White    ``white``    ``WHITE``    ``bg.white``    ``bg.WHITE``
=======  ===========  ===========  ==============  ==============


Full 24-bit colour support is also available (on those terminals that support it) by using the ``rgb`` selector.

rgb

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
