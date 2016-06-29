#include <boost/python.hpp>
#include <boost/python/dict.hpp>
#include <boost/python/list.hpp>
#include <boost/python/numeric.hpp>
#include <boost/numpy.hpp>
#include <numpy/arrayobject.h>
#include <iostream>

using namespace std;
using namespace boost::python;

template<typename T>
object process(boost::python::numeric::array arr)
{
    int length = boost::python::len(arr);
    cout<<"[";
    for(int i = 0; i < length; i++) {
        cout<<extract<T>(arr[i]);
        if (i!=length-1)
            cout<<", ";
    }    
    cout<<"]"<<endl;
    return arr;
}

object process_int32(boost::python::numeric::array arr)
{
    return process<int32_t>(arr);
}

object process_uint32(boost::python::numeric::array arr)
{
    return process<uint32_t>(arr);
}

object process_int64(boost::python::numeric::array arr)
{
    return process<int64_t>(arr);
}

object process_uint64(boost::python::numeric::array arr)
{
    return process<uint64_t>(arr);
}
BOOST_PYTHON_MODULE(test)
{
    using namespace boost::python;
    numeric::array::set_module_and_type("numpy", "ndarray");
    _import_array();
    boost::numpy::initialize();
    def("process_int32", process_int32);
    def("process_uint32", process_uint32);
    def("process_int64", process_int64);
    def("process_uint64", process_uint64);
}
