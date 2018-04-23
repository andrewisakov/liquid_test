#!/usr/bin/python3

# Второй абзац статьи https://en.wikipedia.org/wiki/Isaac_Newton
text = """Newton's Principia formulated the laws of motion and universal
    gravitation that dominated scientists' view of the physical universe
    for the next three centuries. By deriving Kepler's laws of planetary
    motion from his mathematical description of gravity, and using the same
    principles to account for the trajectories of comets, the tides, the
    precession of the equinoxes, and other phenomena, Newton removed the
    last doubts about the validity of the heliocentric model of the Solar
    System and demonstrated that the motion of objects on Earth and of
    celestial bodies could be accounted for by the same principles. Newton's
    theoretical prediction that the Earth is shaped as an oblate spheroid
    was later vindicated by the geodetic measurements of Maupertuis, La
    Condamine, and others, thus convincing most Continental European
    scientists of the superiority of Newtonian mechanics over the earlier
    system of Descartes."""

vowels = set("aeiouy,\n:;\'\". ?!-")  # Гласные и пунктуация
word_set = set(text.lower())
non_volwels = list(word_set.difference(vowels))
print(sorted(non_volwels))
