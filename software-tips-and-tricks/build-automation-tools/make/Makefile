# To see this work, put it somewhere and execute the following 
# at the command line:
# - `make`
# - `make clean`
# - `make double_out.txt`
# - `make test_out.txt`

# The first target is the one which is run if you execute `make`
# It is conventional to call it `all` and have it build everything
# you need. You can either leave it as is or make it a .PHONY 
# target (see below). 
all: test_out.txt double_out.txt

# The first target file can't have any dependencies as it's the
# first thing which is built
test_out.txt:
	echo "Hello" > test_out.txt

# This target file depends on test_out.xt
double_out.txt:test_out.txt
	cat test_out.txt > double_out.txt

# It is also common to have a target called `clean`, which cleans
# up your project. `clean` is almost always a phony method because
# it generally doesn't produce anything
clean:
	rm test_out.txt double_out.txt

.PHONY: clean
