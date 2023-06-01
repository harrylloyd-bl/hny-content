import os
import glob

done_zips = glob.glob("\\\\ad\\collections\\TwoCenturies\\TwoCenturies IV\\Incunabula\\split_data\\*")

for f in done_zips:
    print(f"Combining  {f}")
    txts = glob.glob(os.path.join(f, "splittextfiles\\*.txt"))
    with open(os.path.join(f, "combinedsplittext.txt"), "w") as outfile:
        for t in txts:
            with open(t) as infile:
                entry = infile.readlines()
                no_lines_entry = [x for x in entry if '------------------------' not in x]
                english_only_entry = [y for y in no_lines_entry if "NON-ENGLISH SECTION LASTING" not in y]
                out_str = ""
                for l in english_only_entry:
                    out_str += l
                outfile.write(out_str)
                outfile.write("\n\n")