N = 100
a = [110, 604, 905, 310, 659, 229, 527, 113, 645, 798, 243, 584, 904, 553, 178, 510, 184, 368, 116, 469, 955, 795, 549, 703, 32, 63, 935, 258, 732, 870, 197, 730, 128, 14, 523, 503, 531, 545, 362, 925, 488, 806, 477, 285, 39, 148, 71, 572, 713, 78, 725, 173, 894, 84, 554, 194, 890, 448, 166, 135, 783, 587, 521, 583, 36, 348, 666, 375, 615, 867, 321, 927, 778, 45, 638, 720, 512, 359, 94, 755, 832, 585, 982, 185, 857, 336, 592, 239, 320, 53, 995, 916, 390, 465, 992, 387, 325, 880, 780, 277] 
print(a) 
 
for i in range(N-1):
    for j in range(N-i-1):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
 
print(a)