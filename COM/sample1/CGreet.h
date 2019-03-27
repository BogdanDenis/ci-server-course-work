// CGreet.h : Declaration of the CCGreet

#ifndef __CGREET_H_
#define __CGREET_H_

#include "resource.h"       // main symbols

/////////////////////////////////////////////////////////////////////////////
// CCGreet
class ATL_NO_VTABLE CCGreet : 
	public CComObjectRootEx<CComSingleThreadModel>,
	public CComCoClass<CCGreet, &CLSID_CGreet>,
	public IDispatchImpl<ICGreet, &IID_ICGreet, &LIBID_SAMPLE1Lib>
{
public:
	CCGreet()
	{
	}

DECLARE_REGISTRY_RESOURCEID(IDR_CGREET)

DECLARE_PROTECT_FINAL_CONSTRUCT()

BEGIN_COM_MAP(CCGreet)
	COM_INTERFACE_ENTRY(ICGreet)
	COM_INTERFACE_ENTRY(IDispatch)
END_COM_MAP()

// ICGreet
public:
	STDMETHOD(SayHello)(/*[in]*/ BSTR name, /*[out,retval]*/ BSTR *retstr);
	STDMETHOD(WORKDIR)(/*[in]*/ BSTR dir, /*[in]*/ BSTR cwd, /*[out,retval]*/ BSTR *retstr);
	STDMETHOD(COPY)(/*[in]*/ BSTR what, /*[in]*/ BSTR to, /*[in]*/ BSTR cwd, /*[out,retval]*/ BSTR *retstr);
	STDMETHOD(RUN)(/*[in]*/ BSTR cmd, /*[in]*/ BSTR cwd, /*[out,retval]*/ BSTR *retstr);
};

#endif //__CGREET_H_
