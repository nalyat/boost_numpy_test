OS=$(shell uname)


PYTHON=/opt/anaconda/bin/python

deps: boost_numpy/lib

boost_numpy:
	git clone https://github.com/ndarray/Boost.NumPy.git boost_numpy

boost_numpy/CMakeCache.txt: boost_numpy
	cd boost_numpy && cmake .

boost_numpy/lib: boost_numpy/CMakeCache.txt
	cd boost_numpy && make
ifeq (${OS},Darwin)
	cd boost_numpy && ${SUDO} install_name_tool -change  libpython2.7.dylib /opt/anaconda/lib/libpython2.7.dylib lib/libboost_numpy.dylib
endif

all: deps
	${PYTHON} setup.py build_ext -i
test: all
	${PYTHON} test.py

install:
	rm -rf build
	${PYTHON} setup.py install
ifeq (${OS},Darwin)
	echo "Fixing the shared library to use libstdc++ from gcc 5.3.0"
	install_name_tool -change /usr/local/opt/gcc5/lib/gcc/5/libstdc++.6.dylib /usr/local/Cellar/gcc5/5.3.0/lib/gcc/5/libstdc++.6.dylib /opt/anaconda/lib/python2.7/site-packages/imc/eagle/Strategy/LeadLag.so
endif

clean:
	rm -rf boost_numpy/CMakeCache.txt
	rm -rf build
	rm imc/eagle/Algo/AlgoBindings_wrap.cpp imc/eagle/Algo/AlgoBindings.py imc/eagle/Algo/_AlgoBindings.so
	rm imc/eagle/Strategy/LeadLag.so
