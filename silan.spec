#
# spec file for package silan
#
# Copyright (c) 2017 Radio Bern RaBe
#                    http://www.rabe.ch
#
# This program is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License 
# as published  by the Free Software Foundation, version
# 2 of the License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public
# License  along with this program.
# If not, see <http://www.gnu.org/licenses/>.
#
# Please submit enhancements, bugfixes or comments via GitHub:
# https://github.com/radiorabe/centos-rpm-silan
#

Name:     silan

# v0.3.3
%define _git_commit 40d05a9a969885b44f6f94739c376370

Version:  0.3.3
Release:  1%{?dist}
Summary:  Audiofile Silence Analyzer
License:  GPLv2+
URL:      https://github.com/x42/silan
Source0:  https://github.com/x42/silan/archive/%{_git_commit}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: automake
BuildRequires: autoconf
BuildRequires: libtool
BuildRequires: make

BuildRequires: libsndfile-devel
BuildRequires: ffmpeg-devel

%description
Silan is a standalone application to analyze audio files for silence and
print ranges of detected signals.

It supports a variety of audio-formats and codecs by making use of libsndfile 
and ffmpeg/libav for reading audio-data.

Signal threshold and hold-off time can be freely configured. The output can be 
formatted with samples or seconds as unit or printed as audacity label file.

%prep
%setup -q -n %{name}-%{_git_commit}
autoreconf --force -v --install

%build
%configure
make -j2

%install
%make_install

%files
%doc AUTHORS COPYING NEWS README TODO
%doc %{_mandir}/*/silan.*.gz
%{_bindir}/silan
