print("Let's practice everythin\'")
print("You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.")

poem = """
\tBeautiful is better than ugly.
\tExplicit is better than implicit.
\tSimple is better than complex.
\tComplex is better than complicated.
\tFlat is better than nested.
\tSparse is better than dense.
\tReadability counts.
\tSpecial cases aren't special enough to break the rules.
\tAlthough practicality beats purity.
\tErrors should never pass silently.
\tUnless explicitly silenced.
\tIn the face of ambiguity, refuse the temptation to guess.
\tThere should be one-- and preferably only one --obvious way to do it.
\tAlthough that way may not be obvious at first unless you're Dutch.
\tNow is better than never.
\tAlthough never is often better than *right* now.
\tIf the implementation is hard to explain, it's a bad idea.
\tIf the implementation is easy to explain, it may be a good idea.
\tNamespaces are one honking great idea -- let's do more of those!
"""

print("\t===============================================================")
print(poem)
print("\t===============================================================")

five = 10 - 2 + 3 - 6
print("What does \'five\' hold: {}".format(five))

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100

    return jelly_beans, jars, crates

start_point = 10000
beans, jars, crates = secret_formula(start_point)

print("With a starting point of {0}, we will have {1} beans, {2} jars, {3} crates.".format(start_point, beans, jars, crates))

start_point /= 10

print("We could also do this way: %d beans, %d jars, & %d crates." % secret_formula(start_point))
