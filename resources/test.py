# coding: utf-8

FILENAME = "Unihan_Variants.txt"

FILEOUT = "single_conversion_candidate.txt"

single_candidates = []
with open(FILENAME, "r") as f:
    for line in f:
        l = line.strip()
        if l.startswith("#"):
            continue
        if not l:
            continue
        basechar, varianttype, variant = l.split("\t")
        if varianttype == "kSimplifiedVariant":
            hexstr = basechar.replace("U+", "")
            base = chr(int(hexstr, 16))
            
            varchars = []
            for char_scalar in variant.split(" "):
                varchar = chr(int(char_scalar.replace("U+", ""), 16))
                varchars.append(varchar)
            if len(varchars)>1:
                print(base, ",".join(varchars))
            else:
                single_candidates.append("{}\t{}\n".format(base, varchars[0]))
with open(FILEOUT, "w") as w:
    w.writelines(single_candidates)
    
        
        