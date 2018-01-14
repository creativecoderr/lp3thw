## More Files

from sys import argv

from os.path import exists

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

in_file = open(from_file)   # open the input file
indata = in_file.read()     # read the data of the input file and save it in memory


print(f"The input file is {len(indata)} bytes long")
print("Ready, hit RETURN to continue, CTR+C to abort.")
input()

out_file = open(to_file, "w")    # open the output file in write mode.
out_file.write(indata)

print("Alright, all done!")

out_file.close()
in_file.close()
