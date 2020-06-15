# Tuples intro Lesson number 92
# The central ideia about tuples is analogy with list.
# Tuples are similar but, unlike lists, they are imutables.
# Lists are intended to hold homogenous items of all same type.
#
#
#
#
#
#


"""
welcome = "welcome to my nightmare", "alice cooper", 1975
bad = "bad company","bad company", 1974
budgie = "nightfly","budgie",1981
imelda = "more mayhem","imilda may", 2011
metallica = "ride the lighting","metallica", 1984

metallica2 = ["ride the lighting","metallica",1984]
print(metallica2)


metallica2.append("Rock")

title, artist, year = metallica2

print(title)
"""

imelda = (
    "more mayhem",
    "imelda may",
    2011,
    ((1, "puling hug"), (2, "pysco"), (3, "mayhem"), (4, "kentz town")),
)
print(imelda)
title, artist, year, track = imelda

print(title)
print(artist)
print(year)

for song in track:
    track, title = song
    print("\tTrack number {}, Title: {}".format(track, title))
