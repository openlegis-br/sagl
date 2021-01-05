'ursa' profile
==============

This profile supplies an alternate main template to the one provided
in the 'zpt_generic' skins directory, with two optimizations:

- it uses the 'ursine_globals' view to look up its globals, rather than
  using the usual Python script implementation: that view can be (and *is*)
  tested, tweaked, and profiled as normal Python code.

- it also strips away all non-essential rendering, leaving a "pure" /
  semantic HTML interface, which should be easier to re-theme with a
  tool such as Deliverance.

Together, these two optimizations should provide about a twenty-five to
thirty percent speed boost (e.g., 23ms on the empty site root vs 33ms for
the standard view;  YMMV, of course).
