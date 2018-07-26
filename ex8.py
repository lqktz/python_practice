# -*- coding: utf-8 -*-

formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % ("One", "Two", "Three", "Four")
print formatter % (True, False, True, False)
print formatter % (formatter, formatter, formatter, formatter)

print formatter % (
        "I had this thing.",
        "That you could type up right.",
        "But it didn't sing.",
        "So I said goodnight."
        )

# 对比 r  和 s 对输出的影响
print "%r" % "这是一句中文"
print "%s" % "这是一句中文"
