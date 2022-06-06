import k3d

def rgba(r, g, b, t):
    return r*2**16 + g*2**8 + b

# made on coolors.co 

palette1 = [
 rgba(212, 230, 181, 1),
 rgba(156, 179, 128, 1),
 rgba(98, 148, 96, 1),
 rgba(213, 185, 66, 1),
 rgba(102, 16, 31, 1),
 rgba(210, 255, 150, 1),
 rgba(173, 226, 93, 1),
 rgba(146, 140, 111, 1),
]

# 1, 3, 3, 1 
# like in Pascal's triangle
palette = [
 0x5D576B,
 rgba(156, 179, 128, 1),
 rgba(156, 179, 128, 1),
 rgba(156, 179, 128, 1),
 rgba(213, 185, 66, 1),
 rgba(213, 185, 66, 1),
 rgba(213, 185, 66, 1),
 rgba(102, 16, 31, 1),

]
