// CGreet.cpp : Implementation of CCGreet
#include "stdafx.h"
#include "Sample1.h"
#include "CGreet.h"

/////////////////////////////////////////////////////////////////////////////
// CCGreet


STDMETHODIMP CCGreet::SayHello(BSTR name, BSTR *retstr)
{
	// TODO: Add your implementation code here
//{-----------code added by imran on 18 sept 2k------------------
	char str[20] ;
	sprintf(str,"hello "); // copy the value of hello into the string variable

    //create a new variable called temp initialized with the value of str
	CComBSTR temp(str);

	//append the input parameter value to the temp variable
	temp += name ;
	
	//send the value back to the calling function
	*retstr = temp.Detach();
//-----------code added by imran on 18 sept 2k--------------------------------}

	return S_OK;
}
