# Polyrhythms

In music, a polyrhythm occurs when two or more repeating rhythmic patterns are
played simultaneously. Linear polyrhythms are the most simple of such
phenomena. Imagine counting the numbers 1, 2, 3, 4, and then continuing from 1
again, such that there is equal time between each number (as if counting in
seconds). Then imagine doing the same, but only going as high as 3, before
returning to 1. Now, try to imagine playing both patterns together such that
the 1s of each pattern are counted at the same instant. To do this, either the
first layer must be sped up, or the second one sped down. When this happens,
all numbers (beside the 1s) will be offset from one another, and will not
align with any other from the opposite layer. Verbally counting such rhythms
is typically not easy, so it is natural to use one hand to tap the beat of the
first rhythm, and the other hand to tap the beat of the other rhythm. If done
correctly, you will have successfully played what is usually refered to as a
'3 against 4 linear polyrhythm', or simply a 'three four polyrhythm' ('linear'
refers to the equal time between each beat within each layer). This example is
a mere scratch on the surface on the topic of polyrhythms, but will suffice
for the purposes of this project.

This algorithm returns all discrete polyrhythms up to a given limit, starting
from 3:2 (the most simple polyrhythm). 'Discrete' refers to a set of
constraints for candidate polyrhythms. First, it should be noted that a 3:4
polyrhythm is effectively identical to a 4:3 as the resolved pattern will
sound the same. Second, a 6:8 polyrhythm would also be considered identical to
a 3:4 polyrhythm, as it would sound the same as two repeats of the 3:4 when
played. We also place one additional constraint, such that any polyrhythm
containing a one (e.g. 1:4 or 3:1) is omitted, as playing such polyrhythms is
trivial.

Some polyrhythms output by the algorithm may have either 'easy' or 'hard'
written beside them. Humans have a remarkable ability to naturally subdivide
or 'feel' time, in subdivisions of two and three. However, the human brain can
also feel in compound subdivisions of these factors. For example, the number 4
is simply a 2, multiplied by another 2. The number 6 is a 2, multiplied by
a 3. 54 is the product of three 2s and two 3s, however, the number 10 for
example, has a prime factor of 5, which cannot be naturally 'felt' by humans,
without actively training to do so. When playing a polyrhythm, it is typical
for the player to 'count' one layer, and 'subdivide' the second layer, to
determine where the beats should land relative to the counted layer.
Polyrhythms marked as 'easy' are ones where both numbers of that polyrhythm
can be naturally felt, meaning they can be counted either way. Polyrhythms
without a difficulty indicator are ones where only one of the numbers can be
naturally subdivided, forcing the player to count with the other. Polyrhythms
with marked as 'hard' are ones where neither number can be naturally felt, and
thus will be difficult to pull off correctly without deliberately training for
that particular subdivision. This is generally a very hard skill to aquire,
even for advanced musicians, which speaks volumes as to the intricacy of the
human mind, and its natural capacity to divide time accurately and
comfortably in factors of two and three.
