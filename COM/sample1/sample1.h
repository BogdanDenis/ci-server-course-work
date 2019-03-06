

/* this ALWAYS GENERATED file contains the definitions for the interfaces */


 /* File created by MIDL compiler version 8.01.0622 */
/* at Tue Jan 19 05:14:07 2038
 */
/* Compiler settings for sample1.idl:
    Oicf, W1, Zp8, env=Win32 (32b run), target_arch=X86 8.01.0622 
    protocol : dce , ms_ext, c_ext, robust
    error checks: allocation ref bounds_check enum stub_data 
    VC __declspec() decoration level: 
         __declspec(uuid()), __declspec(selectany), __declspec(novtable)
         DECLSPEC_UUID(), MIDL_INTERFACE()
*/
/* @@MIDL_FILE_HEADING(  ) */



/* verify that the <rpcndr.h> version is high enough to compile this file*/
#ifndef __REQUIRED_RPCNDR_H_VERSION__
#define __REQUIRED_RPCNDR_H_VERSION__ 500
#endif

#include "rpc.h"
#include "rpcndr.h"

#ifndef __RPCNDR_H_VERSION__
#error this stub requires an updated version of <rpcndr.h>
#endif /* __RPCNDR_H_VERSION__ */

#ifndef COM_NO_WINDOWS_H
#include "windows.h"
#include "ole2.h"
#endif /*COM_NO_WINDOWS_H*/

#ifndef __sample1_h__
#define __sample1_h__

#if defined(_MSC_VER) && (_MSC_VER >= 1020)
#pragma once
#endif

/* Forward Declarations */ 

#ifndef __ICGreet_FWD_DEFINED__
#define __ICGreet_FWD_DEFINED__
typedef interface ICGreet ICGreet;

#endif 	/* __ICGreet_FWD_DEFINED__ */


#ifndef __CGreet_FWD_DEFINED__
#define __CGreet_FWD_DEFINED__

#ifdef __cplusplus
typedef class CGreet CGreet;
#else
typedef struct CGreet CGreet;
#endif /* __cplusplus */

#endif 	/* __CGreet_FWD_DEFINED__ */


/* header files for imported files */
#include "oaidl.h"
#include "ocidl.h"

#ifdef __cplusplus
extern "C"{
#endif 


#ifndef __ICGreet_INTERFACE_DEFINED__
#define __ICGreet_INTERFACE_DEFINED__

/* interface ICGreet */
/* [unique][helpstring][dual][uuid][object] */ 


EXTERN_C const IID IID_ICGreet;

#if defined(__cplusplus) && !defined(CINTERFACE)
    
    MIDL_INTERFACE("1638ED3E-43E1-11D6-89B2-00010302158B")
    ICGreet : public IDispatch
    {
    public:
        virtual /* [helpstring][id] */ HRESULT STDMETHODCALLTYPE SayHello( 
            /* [in] */ BSTR name,
            /* [retval][out] */ BSTR *retstr) = 0;
        
    };
    
    
#else 	/* C style interface */

    typedef struct ICGreetVtbl
    {
        BEGIN_INTERFACE
        
        HRESULT ( STDMETHODCALLTYPE *QueryInterface )( 
            ICGreet * This,
            /* [in] */ REFIID riid,
            /* [annotation][iid_is][out] */ 
            _COM_Outptr_  void **ppvObject);
        
        ULONG ( STDMETHODCALLTYPE *AddRef )( 
            ICGreet * This);
        
        ULONG ( STDMETHODCALLTYPE *Release )( 
            ICGreet * This);
        
        HRESULT ( STDMETHODCALLTYPE *GetTypeInfoCount )( 
            ICGreet * This,
            /* [out] */ UINT *pctinfo);
        
        HRESULT ( STDMETHODCALLTYPE *GetTypeInfo )( 
            ICGreet * This,
            /* [in] */ UINT iTInfo,
            /* [in] */ LCID lcid,
            /* [out] */ ITypeInfo **ppTInfo);
        
        HRESULT ( STDMETHODCALLTYPE *GetIDsOfNames )( 
            ICGreet * This,
            /* [in] */ REFIID riid,
            /* [size_is][in] */ LPOLESTR *rgszNames,
            /* [range][in] */ UINT cNames,
            /* [in] */ LCID lcid,
            /* [size_is][out] */ DISPID *rgDispId);
        
        /* [local] */ HRESULT ( STDMETHODCALLTYPE *Invoke )( 
            ICGreet * This,
            /* [annotation][in] */ 
            _In_  DISPID dispIdMember,
            /* [annotation][in] */ 
            _In_  REFIID riid,
            /* [annotation][in] */ 
            _In_  LCID lcid,
            /* [annotation][in] */ 
            _In_  WORD wFlags,
            /* [annotation][out][in] */ 
            _In_  DISPPARAMS *pDispParams,
            /* [annotation][out] */ 
            _Out_opt_  VARIANT *pVarResult,
            /* [annotation][out] */ 
            _Out_opt_  EXCEPINFO *pExcepInfo,
            /* [annotation][out] */ 
            _Out_opt_  UINT *puArgErr);
        
        /* [helpstring][id] */ HRESULT ( STDMETHODCALLTYPE *SayHello )( 
            ICGreet * This,
            /* [in] */ BSTR name,
            /* [retval][out] */ BSTR *retstr);
        
        END_INTERFACE
    } ICGreetVtbl;

    interface ICGreet
    {
        CONST_VTBL struct ICGreetVtbl *lpVtbl;
    };

    

#ifdef COBJMACROS


#define ICGreet_QueryInterface(This,riid,ppvObject)	\
    ( (This)->lpVtbl -> QueryInterface(This,riid,ppvObject) ) 

#define ICGreet_AddRef(This)	\
    ( (This)->lpVtbl -> AddRef(This) ) 

#define ICGreet_Release(This)	\
    ( (This)->lpVtbl -> Release(This) ) 


#define ICGreet_GetTypeInfoCount(This,pctinfo)	\
    ( (This)->lpVtbl -> GetTypeInfoCount(This,pctinfo) ) 

#define ICGreet_GetTypeInfo(This,iTInfo,lcid,ppTInfo)	\
    ( (This)->lpVtbl -> GetTypeInfo(This,iTInfo,lcid,ppTInfo) ) 

#define ICGreet_GetIDsOfNames(This,riid,rgszNames,cNames,lcid,rgDispId)	\
    ( (This)->lpVtbl -> GetIDsOfNames(This,riid,rgszNames,cNames,lcid,rgDispId) ) 

#define ICGreet_Invoke(This,dispIdMember,riid,lcid,wFlags,pDispParams,pVarResult,pExcepInfo,puArgErr)	\
    ( (This)->lpVtbl -> Invoke(This,dispIdMember,riid,lcid,wFlags,pDispParams,pVarResult,pExcepInfo,puArgErr) ) 


#define ICGreet_SayHello(This,name,retstr)	\
    ( (This)->lpVtbl -> SayHello(This,name,retstr) ) 

#endif /* COBJMACROS */


#endif 	/* C style interface */




#endif 	/* __ICGreet_INTERFACE_DEFINED__ */



#ifndef __SAMPLE1Lib_LIBRARY_DEFINED__
#define __SAMPLE1Lib_LIBRARY_DEFINED__

/* library SAMPLE1Lib */
/* [helpstring][version][uuid] */ 


EXTERN_C const IID LIBID_SAMPLE1Lib;

EXTERN_C const CLSID CLSID_CGreet;

#ifdef __cplusplus

class DECLSPEC_UUID("1638ED3F-43E1-11D6-89B2-00010302158B")
CGreet;
#endif
#endif /* __SAMPLE1Lib_LIBRARY_DEFINED__ */

/* Additional Prototypes for ALL interfaces */

unsigned long             __RPC_USER  BSTR_UserSize(     unsigned long *, unsigned long            , BSTR * ); 
unsigned char * __RPC_USER  BSTR_UserMarshal(  unsigned long *, unsigned char *, BSTR * ); 
unsigned char * __RPC_USER  BSTR_UserUnmarshal(unsigned long *, unsigned char *, BSTR * ); 
void                      __RPC_USER  BSTR_UserFree(     unsigned long *, BSTR * ); 

unsigned long             __RPC_USER  BSTR_UserSize64(     unsigned long *, unsigned long            , BSTR * ); 
unsigned char * __RPC_USER  BSTR_UserMarshal64(  unsigned long *, unsigned char *, BSTR * ); 
unsigned char * __RPC_USER  BSTR_UserUnmarshal64(unsigned long *, unsigned char *, BSTR * ); 
void                      __RPC_USER  BSTR_UserFree64(     unsigned long *, BSTR * ); 

/* end of Additional Prototypes */

#ifdef __cplusplus
}
#endif

#endif


