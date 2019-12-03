#
# note to self: Linus releases need to be named 5.x.0 not 5.x or various
# things break
# 
#

Name:           linux
Version:        5.3.14
#                   ^^^ right there it needs the .0 for 5.x releases
Release:        874
License:        GPL-2.0
Summary:        The Linux kernel
Url:            http://www.kernel.org/
Group:          kernel
Source0:        https://cdn.kernel.org/pub/linux/kernel/v5.x/linux-5.3.14.tar.xz
Source1:        config
Source2:        cmdline

%define ktarget  native
%define kversion %{version}-%{release}.%{ktarget}

BuildRequires:  buildreq-kernel

Requires: systemd-bin
Requires: init-rdahead-extras
Requires: linux-license = %{version}-%{release}

# don't strip .ko files!
%global __os_install_post %{nil}
%define debug_package %{nil}
%define __strip /bin/true

#cve.start cve patches from 0001 to 050
Patch0001: CVE-2019-12379.patch
Patch0002: CVE-2019-19043.patch
Patch0003: CVE-2019-19046.patch
Patch0004: CVE-2019-19050.patch
Patch0005: CVE-2019-19053.patch
Patch0006: CVE-2019-19054.patch
Patch0007: CVE-2019-19055.patch
Patch0008: CVE-2019-19056.patch
Patch0009: CVE-2019-19057.patch
Patch0010: CVE-2019-19058.patch
Patch0011: CVE-2019-19059.patch
Patch0012: CVE-2019-19062.patch
Patch0013: CVE-2019-19063.patch
Patch0014: CVE-2019-19064.patch
Patch0015: CVE-2019-19066.patch
Patch0016: CVE-2019-19068.patch
Patch0017: CVE-2019-19070.patch
Patch0018: CVE-2019-19071.patch
Patch0019: CVE-2019-19072.patch
Patch0020: CVE-2019-19073.patch
Patch0021: CVE-2019-19074.patch
Patch0022: CVE-2019-19077.patch
Patch0023: CVE-2019-19078.patch
Patch0024: CVE-2019-19082.patch
#cve.end

#mainline: Mainline patches, upstream backport and fixes from 0051 to 0099
Patch0051: 0051-staging-exfat-add-exfat-filesystem-code-to-staging.patch
Patch0052: 0052-fpga-altera-cvp-Fix-function-definition-argument.patch
Patch0053: 0053-fpga-altera-pr-ip-Make-alt_pr_unregister-function-vo.patch
Patch0054: 0054-fpga-dfl-use-driver-core-functions-not-sysfs-ones.patch
Patch0055: 0055-fpga-dfl-fme-add-DFL_FPGA_FME_PORT_RELEASE-ASSIGN-io.patch
Patch0056: 0056-fpga-dfl-pci-enable-SRIOV-support.patch
Patch0057: 0057-fpga-dfl-afu-add-AFU-state-related-sysfs-interfaces.patch
Patch0058: 0058-fpga-dfl-add-id_table-for-dfl-private-feature-driver.patch
Patch0059: 0059-fpga-dfl-make-uinit-callback-optional.patch
Patch0060: 0060-fpga-dfl-fme-add-capability-sysfs-interfaces.patch
Patch0061: 0061-fpga-altera-cvp-Discover-Vendor-Specific-offset.patch
Patch0062: 0062-fpga-altera-cvp-Preparation-for-V2-parts.patch
Patch0063: 0063-fpga-altera-cvp-Add-Stratix10-V2-Support.patch
Patch0064: 0064-fpga-dfl-make-init-callback-optional.patch
Patch0065: 0065-fpga-dfl-fme-convert-platform_driver-to-use-dev_grou.patch
Patch0066: 0066-fpga-dfl-afu-convert-platform_driver-to-use-dev_grou.patch
Patch0067: 0067-fpga-dfl-afu-add-userclock-sysfs-interfaces.patch
Patch0068: 0068-fpga-dfl-afu-expose-__afu_port_enable-disable-functi.patch
Patch0069: 0069-fpga-dfl-afu-add-error-reporting-support.patch
Patch0070: 0070-fpga-dfl-afu-add-STP-SignalTap-support.patch
Patch0071: 0071-fpga-dfl-fme-add-global-error-reporting-support.patch
Patch0072: 0072-driver-core-add-dev_groups-to-all-drivers.patch
Patch0073: 0073-x86-fpu-Don-t-cache-access-to-fpu_fpregs_owner_ctx.patch
#mainline.end

#Serie.clr 01XX: Clear Linux patches
Patch0101: 0101-i8042-decrease-debug-message-level-to-info.patch
Patch0102: 0102-Increase-the-ext4-default-commit-age.patch
Patch0103: 0103-silence-rapl.patch
Patch0104: 0104-pci-pme-wakeups.patch
Patch0105: 0105-ksm-wakeups.patch
Patch0106: 0106-intel_idle-tweak-cpuidle-cstates.patch
Patch0107: 0107-bootstats-add-printk-s-to-measure-boot-time-in-more-.patch
Patch0108: 0108-smpboot-reuse-timer-calibration.patch
Patch0109: 0109-raid6-add-Kconfig-option-to-skip-raid6-benchmarking.patch
Patch0110: 0110-Initialize-ata-before-graphics.patch
Patch0111: 0111-give-rdrand-some-credit.patch
Patch0112: 0112-ipv4-tcp-allow-the-memory-tuning-for-tcp-to-go-a-lit.patch
Patch0113: 0113-kernel-time-reduce-ntp-wakeups.patch
Patch0114: 0114-init-wait-for-partition-and-retry-scan.patch
Patch0115: 0115-print-fsync-count-for-bootchart.patch
Patch0116: 0116-Add-boot-option-to-allow-unsigned-modules.patch
Patch0117: 0117-Enable-stateless-firmware-loading.patch
Patch0118: 0118-Migrate-some-systemd-defaults-to-the-kernel-defaults.patch
Patch0119: 0119-xattr-allow-setting-user.-attributes-on-symlinks-by-.patch
Patch0120: 0120-add-scheduler-turbo3-patch.patch
Patch0121: 0121-use-lfence-instead-of-rep-and-nop.patch
Patch0122: 0122-do-accept-in-LIFO-order-for-cache-efficiency.patch
Patch0123: 0123-zero-extra-registers.patch
Patch0124: 0124-locking-rwsem-spin-faster.patch
Patch0125: 0125-ata-libahci-ignore-staggered-spin-up.patch
Patch0126: 0126-print-CPU-that-faults.patch
Patch0127: 0127-x86-microcode-Force-update-a-uCode-even-if-the-rev-i.patch
Patch0128: 0128-x86-microcode-echo-2-reload-to-force-load-ucode.patch
Patch0129: 0129-fix-ucode-revcheck.patch
Patch0130: 0130-add-workaround-for-binutils-optimization.patch
Patch0131: 0131-nvme-workaround.patch
#Serie.end

#Serie1.name WireGuard
#Serie1.git  https://git.zx2c4.com/WireGuard
#Serie1.cmt  7bf34f50d41e8b60e01846baa2eb304697fab89c
#Serie1.tag  0.0.20190913
Patch1001: 1001-WireGuard-fast-modern-secure-kernel-VPN-tunnel.patch
#Serie1.end

%description
The Linux kernel.

%package extra
License:        GPL-2.0
Summary:        The Linux kernel extra files
Group:          kernel
Requires:       linux-license = %{version}-%{release}

%description extra
Linux kernel extra files

%package license
Summary: license components for the linux package.
Group: Default

%description license
license components for the linux package.

%package cpio
License:        GPL-2.0
Summary:        cpio file with kenrel modules
Group:          kernel

%description cpio
Creates a cpio file with some modules

%package dev
License:        GPL-2.0
Summary:        The Linux kernel
Group:          kernel
Requires:       linux = %{version}-%{release}
Requires:       linux-extra = %{version}-%{release}
Requires:       linux-license = %{version}-%{release}

%description dev
Linux kernel build files

%prep
%setup -q -n linux-5.3.14

#cve.patch.start cve patches
%patch0001 -p1
%patch0002 -p1
%patch0003 -p1
%patch0004 -p1
%patch0005 -p1
%patch0006 -p1
%patch0007 -p1
%patch0008 -p1
%patch0009 -p1
%patch0010 -p1
%patch0011 -p1
%patch0012 -p1
%patch0013 -p1
%patch0014 -p1
%patch0015 -p1
%patch0016 -p1
%patch0017 -p1
%patch0018 -p1
%patch0019 -p1
%patch0020 -p1
%patch0021 -p1
%patch0022 -p1
%patch0023 -p1
%patch0024 -p1
#cve.patch.end

#mainline.patch.start Mainline patches, upstream backport and fixes
%patch0051 -p1
%patch0052 -p1
%patch0053 -p1
%patch0054 -p1
%patch0055 -p1
%patch0056 -p1
%patch0057 -p1
%patch0058 -p1
%patch0059 -p1
%patch0060 -p1
%patch0061 -p1
%patch0062 -p1
%patch0063 -p1
%patch0064 -p1
%patch0065 -p1
%patch0066 -p1
%patch0067 -p1
%patch0068 -p1
%patch0069 -p1
%patch0070 -p1
%patch0071 -p1
%patch0072 -p1
%patch0073 -p1
#mainline.patch.end

#Serie.patch.start Clear Linux patches
%patch0101 -p1
%patch0102 -p1
%patch0103 -p1
%patch0104 -p1
%patch0105 -p1
%patch0106 -p1
%patch0107 -p1
%patch0108 -p1
%patch0109 -p1
%patch0110 -p1
%patch0111 -p1
%patch0112 -p1
%patch0113 -p1
%patch0114 -p1
%patch0115 -p1
%patch0116 -p1
%patch0117 -p1
%patch0118 -p1
%patch0119 -p1
%patch0120 -p1
%patch0121 -p1
%patch0122 -p1
%patch0123 -p1
%patch0124 -p1
%patch0125 -p1
%patch0126 -p1
%patch0127 -p1
%patch0128 -p1
%patch0129 -p1
%patch0130 -p1
%patch0131 -p1
#Serie.patch.end

#Serie1.patch.start
%patch1001 -p1
#Serie1.patch.end

cp %{SOURCE1} .

%build
BuildKernel() {

    Target=$1
    Arch=x86_64
    ExtraVer="-%{release}.${Target}"

    perl -p -i -e "s/^EXTRAVERSION.*/EXTRAVERSION = ${ExtraVer}/" Makefile

    make O=${Target} -s mrproper
    cp config ${Target}/.config

    make O=${Target} -s ARCH=${Arch} olddefconfig
    make O=${Target} -s ARCH=${Arch} CONFIG_DEBUG_SECTION_MISMATCH=y %{?_smp_mflags} %{?sparse_mflags}
}

BuildKernel %{ktarget}

%install

InstallKernel() {

    Target=$1
    Kversion=$2
    Arch=x86_64
    KernelDir=%{buildroot}/usr/lib/kernel
    DevDir=%{buildroot}/usr/lib/modules/${Kversion}/build

    mkdir   -p ${KernelDir}
    install -m 644 ${Target}/.config    ${KernelDir}/config-${Kversion}
    install -m 644 ${Target}/System.map ${KernelDir}/System.map-${Kversion}
    install -m 644 ${Target}/vmlinux    ${KernelDir}/vmlinux-${Kversion}
    install -m 644 %{SOURCE2}           ${KernelDir}/cmdline-${Kversion}
    cp  ${Target}/arch/x86/boot/bzImage ${KernelDir}/org.clearlinux.${Target}.%{version}-%{release}
    chmod 755 ${KernelDir}/org.clearlinux.${Target}.%{version}-%{release}

    mkdir -p %{buildroot}/usr/lib/modules
    make O=${Target} -s ARCH=${Arch} INSTALL_MOD_PATH=%{buildroot}/usr modules_install

    rm -f %{buildroot}/usr/lib/modules/${Kversion}/build
    rm -f %{buildroot}/usr/lib/modules/${Kversion}/source

    mkdir -p ${DevDir}
    find . -type f -a '(' -name 'Makefile*' -o -name 'Kbuild*' -o -name 'Kconfig*' ')' -exec cp -t ${DevDir} --parents -pr {} +
    find . -type f -a '(' -name '*.sh' -o -name '*.pl' ')' -exec cp -t ${DevDir} --parents -pr {} +
    cp -t ${DevDir} -pr ${Target}/{Module.symvers,tools}
    ln -s ../../../kernel/config-${Kversion} ${DevDir}/.config
    ln -s ../../../kernel/System.map-${Kversion} ${DevDir}/System.map
    cp -t ${DevDir} --parents -pr arch/x86/include
    cp -t ${DevDir}/arch/x86/include -pr ${Target}/arch/x86/include/*
    cp -t ${DevDir}/include -pr include/*
    cp -t ${DevDir}/include -pr ${Target}/include/*
    cp -t ${DevDir} --parents -pr scripts/*
    cp -t ${DevDir}/scripts -pr ${Target}/scripts/*
    find  ${DevDir}/scripts -type f -name '*.[cho]' -exec rm -v {} +
    find  ${DevDir} -type f -name '*.cmd' -exec rm -v {} +
    # Cleanup any dangling links
    find ${DevDir} -type l -follow -exec rm -v {} +

    # Kernel default target link
    ln -s org.clearlinux.${Target}.%{version}-%{release} %{buildroot}/usr/lib/kernel/default-${Target}
}

# cpio file for keyboard drivers
createCPIO() {

    Target=$1
    Kversion=$2
    KernelDir=%{buildroot}/usr/lib/kernel
    ModDir=/usr/lib/modules/${Kversion}

    mkdir -p cpiofile${ModDir}/kernel/drivers/input/{serio,keyboard}
    mkdir -p cpiofile${ModDir}/kernel/drivers/hid
    cp %{buildroot}${ModDir}/kernel/drivers/input/serio/i8042.ko      cpiofile${ModDir}/kernel/drivers/input/serio
    cp %{buildroot}${ModDir}/kernel/drivers/input/serio/libps2.ko     cpiofile${ModDir}/kernel/drivers/input/serio
    cp %{buildroot}${ModDir}/kernel/drivers/input/keyboard/atkbd.ko   cpiofile${ModDir}/kernel/drivers/input/keyboard
    cp %{buildroot}${ModDir}/kernel/drivers/hid/hid-logitech-dj.ko    cpiofile${ModDir}/kernel/drivers/hid
    cp %{buildroot}${ModDir}/kernel/drivers/hid/hid-logitech-hidpp.ko cpiofile${ModDir}/kernel/drivers/hid
    cp %{buildroot}${ModDir}/kernel/drivers/hid/hid-apple.ko          cpiofile${ModDir}/kernel/drivers/hid
    cp %{buildroot}${ModDir}/modules.order   cpiofile${ModDir}
    cp %{buildroot}${ModDir}/modules.builtin cpiofile${ModDir}

    depmod -b cpiofile/usr ${Kversion}

    (
      cd cpiofile
      find . | cpio --create --format=newc \
        | xz --check=crc32 --lzma2=dict=512KiB > ${KernelDir}/initrd-org.clearlinux.${Target}.%{version}-%{release}
    )
}

InstallKernel %{ktarget} %{kversion}

createCPIO %{ktarget} %{kversion}

rm -rf %{buildroot}/usr/lib/firmware

mkdir -p %{buildroot}/usr/share/package-licenses/linux
cp COPYING %{buildroot}/usr/share/package-licenses/linux/COPYING
cp -a LICENSES/* %{buildroot}/usr/share/package-licenses/linux

%files
%dir /usr/lib/kernel
%dir /usr/lib/modules/%{kversion}
/usr/lib/kernel/config-%{kversion}
/usr/lib/kernel/cmdline-%{kversion}
/usr/lib/kernel/org.clearlinux.%{ktarget}.%{version}-%{release}
/usr/lib/kernel/default-%{ktarget}
/usr/lib/modules/%{kversion}/kernel
/usr/lib/modules/%{kversion}/modules.*

%files extra
%dir /usr/lib/kernel
/usr/lib/kernel/System.map-%{kversion}
/usr/lib/kernel/vmlinux-%{kversion}

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/linux

%files cpio
/usr/lib/kernel/initrd-org.clearlinux.%{ktarget}.%{version}-%{release}

%files dev
%defattr(-,root,root)
/usr/lib/modules/%{kversion}/build
