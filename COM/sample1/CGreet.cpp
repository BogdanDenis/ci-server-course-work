// CGreet.cpp : Implementation of CCGreet
#include "stdafx.h"
#include <cstdio>
#include <iostream>
#include <memory>
#include <stdexcept>
#include <string>
#include <array>
#include "Sample1.h"
#include "CGreet.h"

/////////////////////////////////////////////////////////////////////////////
// CCGreet

std::string bstrToString(BSTR in) {
	std::string out;
	std::wstring inWstr(in, SysStringLen(in));
	std::string inStr(inWstr.begin(), inWstr.end());
	out += inStr;

	return out;
}

std::string exec(const char* cmd, const char*cwd) {
	std::array<char, 128> buffer;
	std::string result;
	std::string command = "cd " + *cwd + *" && " + *cmd;
	system(command.c_str());
	return result;
}

STDMETHODIMP CCGreet::SayHello(BSTR name, BSTR *retstr)
{
	char str[20] ;
	sprintf(str,"hellosssasdasd"); // copy the value of hello into the string variable

	CComBSTR temp(str);

	temp += name ;
	
	*retstr = temp.Detach();

	return S_OK;
}


STDMETHODIMP CCGreet::WORKDIR(BSTR dir, BSTR cwd, BSTR *retstr)
{
	try {
		std::string cmd = "cd " + bstrToString(dir);

		std::string res = exec(cmd.c_str(), bstrToString(cwd).c_str());

		*retstr = CComBSTR(res.c_str());
	}
	catch (std::exception e) {
		*retstr = CComBSTR(e.what());
	}
	

	return S_OK;
}

STDMETHODIMP CCGreet::COPY(BSTR what, BSTR to, BSTR cwd, BSTR *retstr)
{
	try {
		std::string cmd = "xcopy /E " + bstrToString(what) + " " + bstrToString(to) + " && echo 123";

		std::string res = exec(cmd.c_str(), bstrToString(cwd).c_str());

		*retstr = CComBSTR((cmd + " " + res).c_str());
	}
	catch (std::exception e) {
		*retstr = CComBSTR(e.what());

	}
	

	return S_OK;
}

STDMETHODIMP CCGreet::RUN(BSTR _cmd, BSTR cwd, BSTR *retstr)
{
	std::string cmd = "cd " + bstrToString(_cmd);

	std::string res = exec(bstrToString(_cmd).c_str(), bstrToString(cwd).c_str());

	*retstr = CComBSTR(res.c_str());

	return S_OK;
}