## YouTube Video walkthough
Follow this tutorial on YouTube here: https://youtu.be/ejLQ5danlIY

## Kubernetes: What is it?
Kubernetes is a portable, extensible, open-source platform for managing containerized workloads and services that facilitates
both declarative configuration and automation.

Source: https://kubernetes.io/docs/concepts/overview/what-is-kubernetes/


## Why do I need it?
Containers are a good way to bundle and run your applications. In a production environment, you need to manage the containers
that run the applications and ensure that there is no downtime. For example, if a container goes down, another container needs
to start. Wouldn’t it be easier if this behaviour was handled by a system?

That’s how Kubernetes comes to the rescue! Kubernetes provides you with a framework to run distributed systems resiliently.
It takes care of scaling and failover for your application, provides deployment patterns, and more.


## Introduction to minikube
Minikube is a tool that makes it easy to run Kubernetes locally. Minikube runs a single-node Kubernetes cluster inside a
Virtual Machine (VM) on your laptop for users looking to try out Kubernetes or develop with it day-to-day.

In this example, we’ll use our laptop along with Minikube, VirtualBox and Kubectl to create a single node Kubernetes cluster:
(Source picture:Platform9: https://platform9.com/docs/install-kubernetes-the-ultimate-guide/)

# Overview:

I'm assuming you have Virtualbox already setup. If you need a demo on any of these tools, just let me know in the comments.

Install VirtualBox on your system:
https://www.virtualbox.org/wiki/Downloads
 
 
### Minikube install:
On windows, MAC OS or Linux, download and install minikube from the following link:
https://minikube.sigs.k8s.io/docs/start/

Follow the install procedure first and once complete, continue with these steps.

### Start minikube
Minikube gets installed in the ```C:\``` so find the location in file explorer and open up a CMD windows in that directory.

The first install takes a few minutes:

```
C:\minikube>minikube start
C:\minikube>minikube start
* minikube v1.28.0 on Microsoft Windows 11 Home 10.0.22000 Build 22000
* Automatically selected the virtualbox driver
* Downloading VM boot image ...
    > minikube-v1.28.0-amd64.iso....:  65 B / 65 B [---------] 100.00% ? p/s 0s
    > minikube-v1.28.0-amd64.iso:  274.45 MiB / 274.45 MiB  100.00% 7.62 MiB p/
* Starting control plane node minikube in cluster minikube
* Downloading Kubernetes v1.25.3 preload ...
    > preloaded-images-k8s-v18-v1...:  385.44 MiB / 385.44 MiB  100.00% 7.60 Mi
* Creating virtualbox VM (CPUs=2, Memory=6000MB, Disk=20000MB) ...
! This VM is having trouble accessing https://registry.k8s.io
* To pull new external images, you may need to configure a proxy: https://minikube.sigs.k8s.io/docs/reference/networking/proxy/
* Preparing Kubernetes v1.25.3 on Docker 20.10.20 ...
  - Generating certificates and keys ...
  - Booting up control plane ...
  - Configuring RBAC rules ...
  - Using image gcr.io/k8s-minikube/storage-provisioner:v5
* Verifying Kubernetes components...
* Enabled addons: storage-provisioner, default-storageclass
* kubectl not found. If you need it, try: 'minikube kubectl -- get pods -A'
* Done! kubectl is now configured to use "minikube" cluster and "default" namespace by default
```

### Kubectl install:
Kubectl is part of the minikube install so you can run kubectl commands just by putting minikube infront of it.

**But** we're going to install kubectl because we want full functionality.

On windows, MAC OS or Linux, download and install kubectl from the following link:
https://kubernetes.io/docs/tasks/tools/install-kubectl/

Find your OS and follow the install process. I ran this command from C:\minikube

```
C:\minikube>curl.exe -LO "https://dl.k8s.io/release/v1.25.0/bin/windows/amd64/kubectl.exe"
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   138  100   138    0     0    123      0  0:00:01  0:00:01 --:--:--   423
100 43.6M  100 43.6M    0     0  6420k      0  0:00:06  0:00:06 --:--:-- 7793k
```

### Kubernetes commands
Check kubectl commands work:

```
C:\minikube>kubectl version
WARNING: This version information is deprecated and will be replaced with the output from kubectl version --short.  Use --output=yaml|json to get the full version.
Client Version: version.Info{Major:"1", Minor:"25", GitVersion:"v1.25.0", GitCommit:"a866cbe2e5bbaa01cfd5e969aa3e033f3282a8a2", GitTreeState:"clean", BuildDate:"2022-08-23T17:44:59Z", GoVersion:"go1.19", Compiler:"gc", Platform:"windows/amd64"}
Kustomize Version: v4.5.7
Server Version: version.Info{Major:"1", Minor:"25", GitVersion:"v1.25.3", GitCommit:"434bfd82814af038ad94d62ebe59b133fcb50506", GitTreeState:"clean", BuildDate:"2022-10-12T10:49:09Z", GoVersion:"go1.19.2", Compiler:"gc", Platform:"linux/amd64"}

C:\minikube>kubectl get pods -A
NAMESPACE     NAME                               READY   STATUS    RESTARTS        AGE
kube-system   coredns-565d847f94-5zzq5           1/1     Running   0               7m2s
kube-system   etcd-minikube                      1/1     Running   0               7m15s
kube-system   kube-apiserver-minikube            1/1     Running   0               7m15s
kube-system   kube-controller-manager-minikube   1/1     Running   0               7m15s
kube-system   kube-proxy-zw9qz                   1/1     Running   0               7m2s
kube-system   kube-scheduler-minikube            1/1     Running   0               7m15s
kube-system   storage-provisioner                1/1     Running   1 (6m31s ago)   7m13s
```

The kubectl command creates a deployment and deployments create our pods and keep them up and running. Lets add the meetup-app into minukube:

```
C:\minikube>kubectl create deployment meetup-app --image=dmccuk/meetup-app:first --port=80
deployment.apps/meetup-app created
