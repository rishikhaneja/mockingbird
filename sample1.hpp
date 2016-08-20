
namespace SampleNamespace {

class SampleClass
{
public:
    SampleClass();
    ~SampleClass();
    string meth1() const;
    int meth2(int v1);
    void meth3(const string & v1, vector<string> & v2);
    unsigned int meth4();
private:
    void * meth5(){return NULL};
    /// prop1 description
    string prop1;
    //! prop5 description
    int prop5;
};

}

namespace AlphaNamespace
{
    class AlphaClass
    {
    public:
        AlphaClass();

        void alphaMethod();

        string alphaString;
    };

    namespace Omega
    {
        class OmegaClass
        {
        public:
            OmegaClass();

            string omegaString;
        };
    };
}

int sampleFreeFunction(int i)
{
	return i + 1;
}

int anotherFreeFunction(void);
}
