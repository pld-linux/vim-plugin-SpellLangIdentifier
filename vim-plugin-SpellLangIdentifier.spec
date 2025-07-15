%define		plugin	SpellLangIdentifier
Summary:	Vim plugin: Automatically identify buffer's language and set the spell lang
Name:		vim-plugin-%{plugin}
Version:	1.0.0
Release:	1
License:	GPL v3+
Group:		Applications/Editors/Vim
Source0:	https://github.com/daaugusto/spelllangidentifier/archive/v%{version}/sli-%{version}.tar.gz
# Source0-md5:	615deaac501adf1ff8194688c3c0bdad
Patch0:		sh.patch
Patch1:		maps_path.patch
URL:		https://www.vim.org/scripts/script.php?script_id=4988
Requires:	mguesser
Requires:	vim-rt >= 4:7.4.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_vimdatadir	%{_datadir}/vim

%description
SpellLangIdentifier detects the language based on the buffer contents
through 'mguesser' (http://www.mnogosearch.org/guesser/), which in
turn uses "N-Gram-Based Text Categorization".

%prep
%setup -qn spelllangidentifier-%{version}
%patch -P0 -p1
%patch -P1 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_vimdatadir}/plugin
cp -pr LanguageIdentifier.sh SpellLangIdentifier.vim $RPM_BUILD_ROOT%{_vimdatadir}/plugin

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README.md vimrc.sample
%attr(755,root,root) %{_vimdatadir}/plugin/LanguageIdentifier.sh
%{_vimdatadir}/plugin/SpellLangIdentifier.vim
