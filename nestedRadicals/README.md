# Nested Radicals

The python code implements a result I proved in the Nested Radicals Proof paper.  This was a collaboration with Veniamin Ilmer, who first presented me with the idea.

The user inputs a rational multiple of pi.  The python code then writes the cosine of that angle in the form +-sqrt(2 +- sqrt(2 +- ...))/2.

Note:  If the denominator is a power of two, this nesting eventually terminates.
If not, the sequence of plusses and minuses eventually repeats itself.
The output is formatted so that the non-repeating portion appears on the top line and the repeating portion appears on the bottom line.
