FROM centos:7 as ned-rpm
LABEL maintainer="Nev Delap <nevdelap@gmail.com>"
RUN yum update -y
RUN yum install -y epel-release git man nano rpmdevtools
RUN yum install -y cargo rust
WORKDIR /root/rpmbuild/SPECS
CMD rpmbuild -ba ned.spec

FROM centos:7 as test
RUN yum install -y man
WORKDIR /root/RPMS/x86_64
