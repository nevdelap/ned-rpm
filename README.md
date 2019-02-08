# `ned-rpm` Build

1. Install `docker`, add yourself to the `docker` group.
2. Run `docker pull centos:7`.
3. `git clone` `ned-rpm` into `~/ned-rpm`.
4. Run `./build` to build the docker images.
5. Run `./run` to run the build container to build the rpm.
6. Run `./rerun` to rebuild in the same container.
7. Run `./test` to run the vanilla test container to test installing the rpm.
8. Run `./cleanup` to remove the containers and images.
9. Release the rpm.

**NOTE:** This is brand new and in progress, the remaining things to do are:

* Figure out what is supposed to be downloading the tarball. So far I've downloaded it into the SOURCES directory myself before the build.
* Figure out what to do about rpmbuild expecting the spec file and the source tarball to be root:root.

