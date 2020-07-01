=====
Pansi
=====

Pansi is a clean and simple ANSI escape code library for Python.

.. image :: art/hello-world.png


General usage
=============

Pansi provides an object called ``ansi`` through which all escape codes can be selected.
This object exposes the codes as both attributes (e.g. ``ansi.red``) and items (e.g. ``ansi["red"]``).

This object can therefore be used in several different ways, but the simplest is through the string ``format`` method.
Here, if the object is supplied as a simple named argument, all references need to be prefixed:

.. image :: art/usage-long.png

Alternatively, passing the object with the ``**`` operator removes the need for prefixes and thus makes the template string shorter.
However, this does introduce a greater chance of clashing with other parameters, and doesn't signal which parameters are which.

.. image :: art/usage-short.png

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

.. image :: art/rgb-orange.png

Foreground and background colours can be inverted and then set back to normal using the ``rev`` and ``_rev`` tags respectively.

To reset foreground and background back to their defaults, use ``fg.reset`` and ``bg.reset``.


Text Weight
===========
- ``weight.normal``
- ``weight.bold``
- ``weight.light``
- ``b`` (alias for ``weight.bold``)
- ``_b`` (alias for ``weight.normal``)


Text Style
==========
- ``style.normal``
- ``style.italic``
- ``style.fraktur``
- ``i`` (alias for ``style.italic``)
- ``_i`` (alias for ``style.normal``)


Text decoration
===============
- ``u`` (underline)
- ``uu`` (double underline)
- ``_u`` (no underline)
- ``o`` (overline)
- ``_o`` (no overline)
- ``s`` (strike through)
- ``_s`` (no strike through)


Blinking
========
- ``blink`` (blink)
- ``BLINK`` (blink fast)
- ``_blink`` (no blink)


Hide & show
===========
- ``hide``
- ``show``
