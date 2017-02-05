# centos-rpm-silan
CentOS 7 RPM Specfile for [silan](https://github.com/x42/silan) which is part of [RaBe's audio package collection](https://build.opensuse.org/project/show/home:radiorabe:audio)

## Usage
There are pre-built binary packages for CentOS 7 available on [Radio RaBe's OBS audio package repository](https://build.opensuse.org/project/show/home:radiorabe:audio), which can be installed as follows:

```bash
curl -o /etc/yum.repos.d/home:radiorabe:audio.repo \
     http://download.opensuse.org/repositories/home:/radiorabe:/audio/CentOS_7/home:radiorabe:audio.repo
     
yum install silan
```
